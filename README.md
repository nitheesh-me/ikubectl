# ikubectl
interactive mode for kubectl

## Dev Setup

Following are the steps to setup ikubectl for development:

1. Install [Pyenv](https://realpython.com/lessons/installing-pyenv/) or any pthon version management and set to Python version `^3.8`.
2. Install [poetry](https://python-poetry.org/docs/)
3. Install Dependencies and activate env
    ```bash
    # Venv as local files
    poetry config virtualenvs.in-project true

    # Install without project
    poetry install --no-root

    # Activate venv
    source ./.venv/bin/activate
    # or similarin Windows
    ```
4. Setup Pre-commit hook
    ```bash
    pre-commit install
    ```

## TODOs:

???
