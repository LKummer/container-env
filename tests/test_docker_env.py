"""Module test to make sure the tests work
"""

from docker_env import __version__


def test_version():
    """Test the module version
    """
    assert __version__ == "0.1.0"
