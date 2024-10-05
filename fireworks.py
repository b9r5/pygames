import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Fireworks Animation")

# Define colors
black = (0, 0, 0)

# Particle class for fireworks
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(2, 4)
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        self.speed_x = random.uniform(-2, 2)
        self.speed_y = random.uniform(-2, 2)
        self.lifetime = random.randint(50, 100)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.lifetime -= 1

    def draw(self, screen):
        if self.lifetime > 0:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

# Main loop
running = True
clock = pygame.time.Clock()
particles = []

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with black
    screen.fill(black)

    # Create a new burst of particles occasionally
    if random.randint(0, 30) == 0:
        burst_x = random.randint(100, 500)
        burst_y = random.randint(50, 300)
        for _ in range(50):
            particles.append(Particle(burst_x, burst_y))

    # Update and draw all particles
    for particle in particles[:]:
        particle.move()
        particle.draw(screen)
        if particle.lifetime <= 0:
            particles.remove(particle)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
