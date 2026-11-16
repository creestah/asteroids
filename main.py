import pygame, sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot
from pathlib import Path


def main():
    pygame.init()
    font_path = Path(__file__).parent / "assets" / "SpaceMono-Regular.ttf"
    font = pygame.font.Font(str(font_path), 24)
    explosion_font = pygame.font.Font(str(font_path), 16)
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    
    Player.containers = (updatable, drawable)

    explosions = []
    explosion_art = (
        "\\|/",
        "-*-",
        "/|\\",
    )
    line_height = explosion_font.get_linesize()

    # Initiate player triangle
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    score = 0

    while running:
        log_state()

        explosions = [
        (position, time_left - dt)
        for position, time_left in explosions
        if time_left - dt > 0
        ]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            collision_check = asteroid.collides_with(player)
            if collision_check:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                collision_check = asteroid.collides_with(shot)
                if collision_check:
                    log_event("asteroid_shot")
                    if asteroid.split():
                        score += 1
                        explosions.append((asteroid.position.copy(), 0.35))
                    shot.kill()
        score_text = font.render(f"Asteroids destroyed: {score}", True, "white")
        screen.blit(score_text, (10, 10))
        for position, _ in explosions:
            top = position.y - len(explosion_art) * line_height / 2
            for index, line in enumerate(explosion_art):
                image = explosion_font.render(line, True, "orange")
                rect = image.get_rect(
                    center=(position.x, top + (index + 0.5) * line_height)
                )
                screen.blit(image, rect)
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()
