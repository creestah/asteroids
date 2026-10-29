# Asteroids

A Python implementation of Asteroids built with [Pygame](https://www.pygame.org/). The project is in development; the current program opens a game window and draws the player's ship at the center of the screen.
The player can rotate the ship using A and D.

## Requirements

- Python 3.13 or newer
- [uv](https://docs.astral.sh/uv/) for dependency and environment management

## Setup and run

From the project directory, install the locked dependencies and run the program:

```sh
uv sync
uv run python main.py
```

Use the window's close button to exit.

## Project files

- `main.py` — application entry point
- `player.py` — player ship shape, drawing, and controls
- `circleshape.py` — shared base class for game objects
- `constants.py` — screen and player dimensions
- `logger.py` — logging helper
- `pyproject.toml` — project metadata and dependencies
- `uv.lock` — locked dependency versions
- `.python-version` — preferred Python version for uv (3.13)
