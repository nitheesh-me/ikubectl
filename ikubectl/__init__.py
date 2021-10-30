import os
import toml


def get_version():
    """Function to get the version of the ikubectl package."""
    pyproject_path = os.path.join(os.path.dirname(__file__), "../pyproject.toml")
    with open(pyproject_path) as f:
        pyproject = toml.load(f)
    return pyproject["tool"]["poetry"]["version"]


__version__ = get_version()
