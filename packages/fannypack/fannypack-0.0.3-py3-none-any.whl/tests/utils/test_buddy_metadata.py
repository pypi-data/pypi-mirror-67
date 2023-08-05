import pytest
import fannypack
import numpy as np
import os
import torch
import torch.nn.functional as F

from ..fixtures import simple_buddy, resblock_buddy_temporary_data


def test_buddy_metadata(resblock_buddy_temporary_data):
    """Do some checks on rapid continuous checkpointing.
    """
    model, buddy, data, labels = resblock_buddy_temporary_data

    # Check initial metadata state
    assert buddy.metadata == {}

    buddy.add_metadata({"number": 5})
    buddy.add_metadata({"string": "words words"})

    # Load from file that was saved
    buddy.load_metadata()

    # Check that contents are valid
    assert len(buddy.metadata) == 2
    assert buddy.metadata["number"] == 5

    # Load from file that was saved
    buddy.load_metadata(path=buddy.metadata_path)

    # Check that contents are valid
    assert len(buddy.metadata) == 2
    assert buddy.metadata["number"] == 5
