"""Nox sessions for automating tasks."""

import sys

import nox

PYTHON_VERSIONS = ["3.10"]

# Default sessions to run when executing `nox` without arguments.
nox.options.sessions = [
    "dev_setup",
    "format",
    "lint",
    "typecheck",
    "tests",
]

# Do not reuse existing virtual environments.
nox.options.reuse_existing_virtualenvs = False
# Use uv as the default virtual environment manager.
nox.options.default_venv_backend = "uv"


@nox.session(python=PYTHON_VERSIONS)
def dev_setup(session: nox.Session) -> None:
    """Install development dependencies."""
    session.install("-e", ".[dev]")


@nox.session(python=PYTHON_VERSIONS)
def format(session: nox.Session) -> None:
    """Format the code using Ruff."""
    session.install("ruff")
    session.run("ruff", "format")


@nox.session(python=PYTHON_VERSIONS)
def lint(session: nox.Session) -> None:
    """Lint the code using Ruff."""
    session.install("ruff")
    session.run("ruff", "check", "--fix")


@nox.session(python=PYTHON_VERSIONS)
def typecheck(session: nox.Session) -> None:
    """Run type checks using ty."""
    session.install("ty")
    session.run("ty", "check")


@nox.session(python=PYTHON_VERSIONS)
def tests(session: nox.Session) -> None:
    """Run tests using pytest."""
    session.install(".[dev]")
    session.run(
        "pytest",
        "--cov=src",
        "--cov-report=term-missing",
        "--cov-fail-under=80",
        *session.posargs,
    )


@nox.session(python=PYTHON_VERSIONS)
def build_docs(session: nox.Session) -> None:
    """Build the documentation using MkDocs."""
    session.install(".[docs]")
    session.run("mkdocs", "build", "--strict")


@nox.session(python=PYTHON_VERSIONS)
def deploy_docs(session: nox.Session) -> None:
    """Deploy the documentation using Mike."""
    try:
        version_tag = session.posargs[0]
    except IndexError:
        sys.exit("Expercted a version tag as the first argument e.g. '0.1.0'.")

    session.install(".[docs]")
    session.run(
        "mike",
        "deploy",
        f"{version_tag}",
        "latest",
        "--push",
        "--update-aliases",
    )


@nox.session(python=PYTHON_VERSIONS)
def pre_commit_tasks(session: nox.Session) -> None:
    """Run pre-commit tasks."""
    session.notify("lint")
    session.notify("format")
    session.notify("typecheck")
    session.notify("tests")
