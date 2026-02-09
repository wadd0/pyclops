## petcam

## Quick Start

1. **Install [`uv`](https://github.com/astral-sh/uv) for dependency and environment management:**
    ```bash
    pip intall uv
    ```

2. **Sync all dependencies (including optional extras):**
    ```bash
    uv sync --all-extras
    ```

3. **Activate the Virtual Environment:**

    ```bash
    source .venv/bin/activate
    ```

4. **Install the project in editable mode:**

    ```bash
    uv pip install -e .
    ```

## Code Quality & Automation

1. **Initialise Git repo:**

    ```bash
    git init
    ```

2. **Set up pre-commit hooks:**

    ```bash
    uv run pre-commit install
    ```

3. **Run pre-commit checks on all files:**

    ```bash
    uv run pre-commit run --all-files
    ```

4. **Run a specific nox session (e.g. lint, format):**

    ```bash
    uv run nox --session lint
    ```