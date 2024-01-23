import sys
import pygame
import random

pygame.init()

# dimensions
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Coin Flip Animation")

black = (0, 0, 0)

# load images
coin_faces = [pygame.image.load("heads_coin.png"), pygame.image.load("tails_coin.png")]

coin_rect = coin_faces[0].get_rect()
coin_rect.center = (width // 2, height // 2)

clock = pygame.time.Clock()

run = True

flip_duration = 1000  # Time (in milliseconds) for one complete flip
current_face = 0  # 0 for heads, 1 for tails

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()

    screen.fill(black)

    # Calculate rotation angle and scaling factor based on time
    elapsed_time = pygame.time.get_ticks() % flip_duration
    progress = elapsed_time / flip_duration
    rotation_angle = 360 * progress
    scaling_factor = abs(2 * progress - 1)  # Scale from 0 to 1 and back to 0

    # Rotate and scale the coin
    rotated_coin = pygame.transform.rotozoom(coin_faces[current_face], rotation_angle, scaling_factor)
    rotated_rect = rotated_coin.get_rect(center=coin_rect.center)

    # Draw the rotated coin
    screen.blit(rotated_coin, rotated_rect)

    pygame.display.flip()
    clock.tick(30)  # Adjust the frame rate as needed

    # Switch to the other face after a complete flip
    if elapsed_time >= flip_duration:
        current_face = 1 - current_face  # Switch between 0 and 1
