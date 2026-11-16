# .✦ ݁˖ Asteroids .✦ ݁˖

An Asteroids arcade game built with Python and [Pygame](https://www.pygame.org/). Pilot your ship, shoot incoming asteroids, and survive as long as you can. Large asteroids split into smaller ones when hit, and destroying a small asteroid adds to your score. Colliding with an asteroid ends the game.

[Play Asteroids in your browser](https://creestah.itch.io/asteroids)

## Controls

| Key | Action |
| --- | --- |
| W | Move forward |
| S | Move backward |
| A | Rotate left |
| D | Rotate right |
| Space | Fire shots (hold to fire repeatedly) |
| P | Pause or resume |

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
- `asteroid.py` — asteroid movement, drawing, and splitting when hit
- `asteroidfield.py` — spawns asteroids at the window edges
- `shot.py` — shot movement and drawing
- `circleshape.py` — shared base class and circle collision checks
- `constants.py` — window dimensions and gameplay settings
- `logger.py` — game state and event logging
- `assets/SpaceMono-Regular.ttf` — display font
- `pyproject.toml` and `uv.lock` — project metadata and locked dependencies
- `.python-version` — preferred Python version for uv
