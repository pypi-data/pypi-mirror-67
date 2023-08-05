import time

import torch

from .._forward_declarations import _BuddyForwardDeclarations


class _BuddyOptimizer(_BuddyForwardDeclarations):
    """Buddy's optimization interface.
    """

    # Supported optimizer types
    # Note that torch (as of 1.5) has a stub issue with optim.Adadelta
    _OPTIMIZER_TYPES = {
        "adam": torch.optim.Adam,
        "adadelta": torch.optim.Adadelta,  # type: ignore
    }

    # Default learning rates
    _OPTIMIZER_DEFAULT_LEARNING_RATES = {
        "adam": 1e-4,
        "adadelta": 1,
    }

    def __init__(self, optimizer_type, optimizer_checkpoint_interval):
        """Optimizer-specific setup.
        """
        # Assign our training configuration.
        self._optimizer_config = {
            "global_steps": 0,
            "optimizer_type": optimizer_type,
            "learning_rate_schedulers": {},
        }

        # Map from optimizer name to optimizers
        # These are constructed lazily!
        self._optimizer_dict = {}

        # Autocheckpoint variables
        self._optimizer_checkpoint_interval = optimizer_checkpoint_interval
        self._optimizer_last_checkpoint_time = None

    def minimize(
        self,
        loss,
        optimizer_name="primary",
        *,
        retain_graph=False,
        checkpoint_interval=None,
    ):
        """Compute gradients and use them to minimize a loss function.
        """

        self._instantiate_optimizer(optimizer_name)

        # Update learning rate using scheduler if possible
        schedulers = self._optimizer_config["learning_rate_schedulers"]
        if optimizer_name in schedulers:
            self._set_learning_rate(
                schedulers[optimizer_name](self._optimizer_config["global_steps"]),
                optimizer_name,
            )

        # Take gradient step
        self._optimizer_dict[optimizer_name].zero_grad()
        loss.backward(retain_graph=retain_graph)
        self._optimizer_dict[optimizer_name].step()

        # Update global step count
        self._optimizer_config["global_steps"] += 1

        # Autocheckpoint procedure
        if checkpoint_interval == None:
            checkpoint_interval = self._optimizer_checkpoint_interval

        if checkpoint_interval == 0:
            # Disabled if 0
            return

        if self._optimizer_last_checkpoint_time == None:
            # First iteration
            self._optimizer_last_checkpoint_time = time.time()
        elif (
            time.time() - self._optimizer_last_checkpoint_time
            > self._optimizer_checkpoint_interval
        ):
            # Checkpoint!
            self.save_checkpoint()
            self._optimizer_last_checkpoint_time = time.time()

    def get_learning_rate(self, optimizer_name="primary"):
        """Gets an optimizer learning rate.
        """
        assert optimizer_name in self._optimizer_dict

        # Return scheduled learning rate
        schedulers = self._optimizer_config["learning_rate_schedulers"]
        if optimizer_name in schedulers:
            return schedulers[optimizer_name](self.optimizer_steps)

        # Return raw learning rate
        # Currently, only one parameter group is supported
        optimizer = self._optimizer_dict[optimizer_name]
        assert len(optimizer.param_groups) == 1
        return optimizer.param_groups[0]["lr"]

    def set_learning_rate(self, value, optimizer_name="primary"):
        """Sets an optimizer learning rate. Accepts either a floating point
        learning rate or a schedule function (int steps -> float LR).
        """

        schedulers = self._optimizer_config["learning_rate_schedulers"]
        if callable(value):
            # Store a scheduler
            assert type(value(0)) == float
            schedulers[optimizer_name] = value
        else:
            # Set learning rate to a float
            assert type(value) == float
            # Delete scheduler
            if optimizer_name in schedulers:
                schedulers.pop(optimizer_name)

            # Set scalar learning rate
            self._set_learning_rate(value, optimizer_name)

    @property
    def optimizer_steps(self):
        """Read-only interface for # of steps taken by optimizer.
        """
        return self._optimizer_config["global_steps"]

    def _set_learning_rate(self, value, optimizer_name):
        """(Private) Sets an optimizer's learning rate.
        """

        self._instantiate_optimizer(optimizer_name)

        # Currently, only one parameter group is supported
        optimizer = self._optimizer_dict[optimizer_name]
        assert len(optimizer.param_groups) == 1
        optimizer.param_groups[0]["lr"] = value

    def _instantiate_optimizer(self, optimizer_name):
        """(Private) Instantiates an optimizer. Returns immediately if
        optimizer already exists.
        """
        if optimizer_name in self._optimizer_dict.keys():
            # Optimizer already exists: do nothing!
            return

        self._print("Instantiating optimizer: ", optimizer_name)

        # Make sure we're creating a valid optimizer
        optimizer_type = self._optimizer_config["optimizer_type"]
        assert optimizer_type in self._OPTIMIZER_TYPES

        # Parameters
        Optimizer = self._OPTIMIZER_TYPES[optimizer_type]
        initial_learning_rate = self._OPTIMIZER_DEFAULT_LEARNING_RATES[optimizer_type]

        # Construct optimizer
        self._optimizer_dict[optimizer_name] = Optimizer(
            self._model.parameters(), lr=initial_learning_rate
        )
