# .✦ ݁˖ Asteroids .✦ ݁˖ 

A work-in-progress Asteroids game built with Python and [Pygame](https://www.pygame.org/). The player steers a ship, asteroids spawn from the edges of the window, and colliding with an asteroid ends the game. Fire shots to destroy asteroids. Scoring is not implemented yet.

## Controls

| Key | Action |
| --- | --- |
| W | Move forward |
| S | Move backward |
| A | Rotate left |
| D | Rotate right |
| Space | Fire shots |

## Requirements

- Python 3.13 or newer
- [uv](https://docs.astral.sh/uv/) for dependency and environment management

## Setup and run

From the project directory, install the locked dependencies and start the game:

```sh
uv sync
uv run python main.py
```

Close the game window to exit. Game state snapshots and events are written to `game_state.jsonl` and `game_events.jsonl` in the project directory. These generated files are ignored by Git.

## Project files

- `main.py` — initializes Pygame and runs the game loop
- `player.py` — player ship movement, rotation, and shooting
- `asteroid.py` — asteroid movement, drawing, and collision shape
- `asteroidfield.py` — spawns asteroids at the window edges
- `shot.py` — shot movement and drawing
- `circleshape.py` — shared base class and circle collision checks
- `constants.py` — window dimensions and gameplay settings
- `logger.py` — game state and event logging
- `pyproject.toml` and `uv.lock` — project metadata and locked dependencies
- `.python-version` — preferred Python version for uv
