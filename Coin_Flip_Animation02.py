import pygame
import random

pygame.init()

#dimensions
width, height = 100, 180
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Coin Flip")

#image files
heads_image = pygame.image.load("heads_coin.png")
tails_image = pygame.image.load("tails_coin.png")
coin_sides = heads_image, tails_image
image_width, image_height = 100, 100
heads_image = pygame.transform.scale(heads_image, (image_width, image_height))
tails_image = pygame.transform.scale(tails_image, (image_width, image_height))

def init_pygame():
    pygame.init()
    clock = pygame.time.Clock()
    return clock

def draw_coin_flip(win, width, height, heads_image, tails_image):
    coin_x, coin_y = (width//2) - 65, height//2
    coin_velocity = 0
    gravity = 1
    jump_strength = -20
    coin_image = heads_image
    clock = pygame.time.Clock()

    frames = 100
    show_result = False

    # Function to render result text and image
    def render_result():
        global coin_image
        win.fill((0, 0, 0))
        
        coin_y_position = height // 2 - image_height // 2
        win.blit(coin_image, (width // 2 - image_width // 2, coin_y_position))
        

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        if frames > 1:
            win.fill((255, 255, 255))
            coin_velocity += gravity
            coin_y += coin_velocity
            
            if coin_y>=height - heads_image.get_height():
                coin_y = height - heads_image.get_height()
                coin_velocity = jump_strength
                
                result = random.choice(["HEADS", "TAIL"])
                if coin_image == heads_image:
                    coin_image = tails_image
                else:
                    coin_image = heads_image
        
        else:
            if not show_result:
                render_result()   
                # Add this line 
        
        win.blit(coin_image, (coin_x, coin_y))
        frames -= 1
            
        pygame.display.flip()
        clock.tick(30)
        
    pygame.quit()