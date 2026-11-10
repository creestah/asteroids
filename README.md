# Asteroids - in development

A Python implementation of Asteroids built with [Pygame](https://www.pygame.org/). The current program opens a game window with the player's ship at the center and asteroids spawning from the edges. Move and rotate the ship to avoid them. A collision ends the game.

## Controls

- **W** — move forward
- **S** — move backward
- **A** — rotate left
- **D** — rotate right

## Requirements

- Python 3.13 or newer
- [uv](https://docs.astral.sh/uv/) for dependency and environment management

## Setup and run

From the project directory, install the locked dependencies and run the program:

```sh
uv sync
uv run python main.py
```

Use the window's close button to exit. Game state snapshots and events are written to `game_state.jsonl` and `game_events.jsonl` in the project directory; these generated files are ignored by Git.

## Project files

- `main.py` — application entry point
- `player.py` — player ship shape, drawing, and controls
- `asteroid.py` — asteroid movement and drawing
- `asteroidfield.py` — asteroid spawning
- `circleshape.py` — shared base class for game objects
- `constants.py` — screen dimensions and player movement settings
- `logger.py` — game state and event logging
- `pyproject.toml` — project metadata and dependencies
- `uv.lock` — locked dependency versions
- `.python-version` — preferred Python version for uv (3.13)
