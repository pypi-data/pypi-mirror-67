import pytest

import numpy as np
import fannypack


@pytest.fixture
def wrapper():
    """Creates a SliceWrapper around a dictionary
    """
    raw = {"a": [1, 2, 3, 4], "b": [5, 6, 7, 8]}
    wrapper = fannypack.utils.SliceWrapper(raw)
    return wrapper


@pytest.fixture
def wrapper_complex():
    """Creates a SliceWrapper around a more complex dictionary
    """
    raw = {
        "a": np.random.randint(10, size=(10, 5, 31)),
        "b": np.random.randint(10, size=(10, 5, 3)),
    }
    wrapper = fannypack.utils.SliceWrapper(raw)
    return wrapper


@pytest.fixture
def wrapper_thin():
    """Creates a SliceWrapper around a Python list.
    """
    raw = [1, 2, 3, 4]
    wrapper = fannypack.utils.SliceWrapper(raw)
    return wrapper


def test_fixture(wrapper):
    """Fixture sanity check.
    """
    assert type(wrapper.data["a"]) == list
    wrapper.convert_to_numpy()
    assert type(wrapper.data["a"]) == np.ndarray


def test_fixture_thin(wrapper_thin):
    """Fixture sanity check.
    """
    assert type(wrapper_thin.data) == list
    wrapper_thin.convert_to_numpy()
    assert type(wrapper_thin.data) == np.ndarray


def test_append(wrapper):
    """Checks append interface
    """
    new = {
        "a": 5,
        "b": 3,
    }
    wrapper.append(new)
    assert wrapper[-1] == new


def test_extend(wrapper):
    """Checks extend interface
    """
    new = {
        "a": [5],
        "b": [3],
    }
    wrapper.extend(new)
    assert wrapper[-1:] == new


def test_append_thin(wrapper_thin):
    """Checks append interface (thin)
    """
    new = 5
    wrapper_thin.append(new)
    assert wrapper_thin[-1] == new


def test_extend_thin(wrapper_thin):
    """Checks extend interface (thin)
    """
    new = [5]
    wrapper_thin.extend(new)
    assert wrapper_thin[-1:] == new


def test_append_numpy(wrapper):
    """Checks append interface (numpy)
    """
    new = {
        "a": 5,
        "b": 3,
    }
    wrapper.convert_to_numpy()
    wrapper.append(new)
    assert wrapper[-1] == new


def test_extend_numpy(wrapper):
    """Checks extend interface (numpy)
    """
    new = {
        "a": [5],
        "b": [3],
    }
    wrapper.convert_to_numpy()
    wrapper.extend(new)
    assert wrapper[-1:] == new


def test_iterator(wrapper):
    """Check iterator interface.
    """
    counter = 0
    for x in wrapper:
        assert type(x) == dict
        assert type(x["a"]) == int
        counter += 1
    assert counter == len(wrapper)


def test_iterator_numpy(wrapper):
    """Check iterator interface. (numpy)
    """
    wrapper.convert_to_numpy()
    counter = 0
    for x in wrapper:
        assert type(x) == dict
        assert type(x["a"]) == np.int64
        counter += 1
    assert counter == len(wrapper)


def test_iterator_thin(wrapper_thin):
    """Check iterator interface.
    """
    counter = 0
    for x in wrapper_thin:
        assert type(x) == int
        counter += 1
    assert counter == len(wrapper_thin)


def test_iterator_numpy_thin(wrapper_thin):
    """Check iterator interface. (numpy)
    """
    wrapper_thin.convert_to_numpy()
    counter = 0
    for x in wrapper_thin:
        assert type(x) == np.int64
        counter += 1
    assert counter == len(wrapper_thin)


def test_len(wrapper):
    """Check `len()` output.
    """
    assert len(wrapper) == 4
    wrapper.convert_to_numpy()
    assert len(wrapper) == 4


def test_shape(wrapper):
    """Check `shape` property.
    """
    assert wrapper.shape == (4,)
    wrapper.convert_to_numpy()
    assert wrapper.shape == (4,)


def test_shape_complex(wrapper_complex):
    """Check `shape` property.
    """
    assert wrapper_complex.shape == (10, 5)


def test_read_slice(wrapper):
    """Check that we can read slices of wrappers.
    """
    assert wrapper[::1]["a"] == [1, 2, 3, 4]
    assert wrapper[::1]["b"] == [5, 6, 7, 8]

    assert wrapper[::2]["a"] == [1, 3]
    assert wrapper[::2]["b"] == [5, 7]

    assert wrapper[:2:]["a"] == [1, 2]
    assert wrapper[1:3:]["b"] == [6, 7]


def test_read_slice_numpy(wrapper):
    """Check that we can read slices of our wrappers (numpy).
    """
    wrapper.convert_to_numpy()

    assert np.allclose(wrapper[::1]["a"], [1, 2, 3, 4])
    assert np.allclose(wrapper[::1]["b"], [5, 6, 7, 8])

    assert np.allclose(wrapper[::2]["a"], [1, 3])
    assert np.allclose(wrapper[::2]["b"], [5, 7])

    assert np.allclose(wrapper[:2:]["a"], [1, 2])
    assert np.allclose(wrapper[1:3:]["b"], [6, 7])


def test_write_slice(wrapper):
    """Check that writing does nothing for wrappers containing raw lists.
    """
    wrapper[::1]["a"][0] = 1000
    test_read_slice(wrapper)


def test_write_slice_numpy(wrapper):
    """Check that we can write to slices for wrappers containing numpy arrays.
    """
    wrapper.convert_to_numpy()

    wrapper[::1]["a"][::2] = 0

    assert np.allclose(wrapper[::1]["a"], [0, 2, 0, 4])
    assert np.allclose(wrapper[::1]["b"], [5, 6, 7, 8])

    assert np.allclose(wrapper[::2]["a"], [0, 0])
    assert np.allclose(wrapper[::2]["b"], [5, 7])

    assert np.allclose(wrapper[:2:]["a"], [0, 2])
    assert np.allclose(wrapper[1:3:]["b"], [6, 7])
