# Asteroids

A Python project built with [Pygame](https://www.pygame.org/). In development; the game itself is not implemented yet.

## Requirements

- Python 3.13 or newer
- [uv](https://docs.astral.sh/uv/) for dependency and environment management

## Setup and run

From the project directory, install the locked dependencies and run the program:

```sh
uv sync
uv run python main.py
```

You should see the Pygame version printed in the terminal.

## Project files

- `main.py` — application entry point
- `pyproject.toml` — project metadata and dependencies
- `uv.lock` — locked dependency versions
- `.python-version` — preferred Python version for uv (3.13)
