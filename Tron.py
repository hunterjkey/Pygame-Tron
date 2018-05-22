import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (500, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Tron")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#setup
trailX = [50]
trailY = [50]
robotrailX = [450]
robotrailY = [450]
playerX = 50
playerY = 50
roboY = 450
roboX = 450
playerX_speed = 3
playerY_speed = 0
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # User pressed down on a key
        elif event.type == pygame.KEYDOWN:
        # Figure out if it was an arrow key. If so
        # adjust speed.
            if event.key == pygame.K_LEFT:
                playerX_speed = -3
                playerY_speed = 0
            elif event.key == pygame.K_RIGHT:
                playerX_speed = 3
                playerY_speed = 0
            elif event.key == pygame.K_UP:
                playerY_speed = -3
                playerX_speed = 0
            elif event.key == pygame.K_DOWN:
                playerY_speed = 3
                playerX_speed = 0
    # --- Game logic should go here
    playerX += playerX_speed
    playerY += playerY_speed
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    pygame.draw.rect(screen, GREEN, [playerX, playerY, 4, 4])
    pygame.draw.rect(screen, RED, [roboX, roboY, 4, 4])
    pygame.draw.rect(screen, RED, [0, 0, 500, 500], 5)
    for i in range(len(trailX)):
        pygame.draw.rect(screen, GREEN, [trailX[i], trailY[i], 4, 4])
    for i in range(len(robotrailX)):
        pygame.draw.rect(screen, RED, [robotrailX[i], robotrailY[i], 4, 4])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
