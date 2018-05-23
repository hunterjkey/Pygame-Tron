import pygame
import time
import random
 
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
trailX = [46]
trailY = [50]
robotrailX = [454]
robotrailY = [450]
playerX = 50
playerY = 50
roboY = 450
roboX = 450
playerX_speed = 1
playerY_speed = 0
roboX_speed = -1
roboY_speed = 0
death = False
win = False
speed = 2
imposibru = False #this variable decides whether the AI is almost impossible to beat
donesetup = False
Continue = False

#game setup loop
while not donesetup and not Continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            donesetup = True
            done = True

    #logic
    pos = pygame.mouse.get_pos()
    mouseX = pos[0]
    mouseY = pos[1]
    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
    if pressed1 and (mouseX <=250):
        mode = "human"
        Continue = True
    elif pressed1 and (mouseX > 250):
        mode = "computer"
        Continue = True
    #display
    screen.fill(BLACK)
    pygame.draw.rect(screen,GREEN,[0,0,250,500])
    pygame.draw.rect(screen,RED,[250,0,250,500])
    pygame.draw.rect(screen,BLACK,[0,0,500,500], 10)
    startfont = pygame.font.SysFont('Calibri', 25, True, False)
    humantext = startfont.render("Human v.s. Human",True,WHITE)
    screen.blit(humantext, [25, 240])
    robotext = startfont.render("Human v.s. Computer",True,WHITE)
    screen.blit(robotext, [260, 240])
    pygame.draw.rect(screen,BLACK,[190,60,120,40])
    robotext = startfont.render("Click one",True,WHITE)
    screen.blit(robotext, [205, 70])
    
    #display to screen
    pygame.display.flip()

pygame.mouse.set_visible(False)

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
                playerX_speed = -1
                playerY_speed = 0
            elif event.key == pygame.K_RIGHT:
                playerX_speed = 1
                playerY_speed = 0
            elif event.key == pygame.K_UP:
                playerY_speed = -1
                playerX_speed = 0
            elif event.key == pygame.K_DOWN:
                playerY_speed = 1
                playerX_speed = 0

            if (mode == "human"):
                if event.key == pygame.K_w:
                    roboY_speed = -1
                    roboX_speed = 0
                elif event.key == pygame.K_s:
                    roboY_speed = 1
                    roboX_speed = 0
                elif event.key == pygame.K_d:
                    roboX_speed = 1
                    roboY_speed = 0
                elif event.key == pygame.K_a:
                    roboX_speed = -1
                    roboY_speed = 0
    # --- Game logic should go here
    """collision with line check(it happens before I add to the line because otherwise people wouild just run into the lines they make"""
    for i in range(len(trailX)):
        if (abs(playerX-trailX[i])<speed) and (abs(playerY-trailY[i])<speed):
            death = True
        elif (abs(playerX-robotrailX[i])<speed) and (abs(playerY-robotrailY[i])<speed):
            death = True
        """elif (abs(roboX-robotrailX[i])<2) and (abs(roboY-robotrailY[i])<2):
            win = True
        elif (abs(roboX-trailX[i])<2) and (abs(roboY-trailY[i])<2):
            win = True"""

    """line drawing algorithm for both players"""
    trailX.append(playerX)
    trailY.append(playerY)
    robotrailX.append(roboX)
    robotrailY.append(roboY)

    """robot decision"""
    if (mode == "computer"):
        if (imposibru == False):
            roboaction = random.randint(1,25)
            if (roboX > 480) or (roboX < 10) or (roboY > 480) or (roboY < 10):
                move = random.randint(1,2)
                if (roboX > 480) or (roboX < 10):
                    if (roboX > 480):
                        roboX -= 4
                    elif (roboX < 10):
                        roboX += 4
                    roboX_speed = 0
                    if (roboY > 470):
                        roboY_speed = -1
                        roboY -= 4
                    elif (roboY < 20):
                        roboY_speed = 1
                        roboY += 4
                    else:
                        if (move == 1):
                           roboY_speed = -1
                           roboY -= 4
                        if (move == 2):
                           roboY_speed = 1
                           roboY += 4
                if (roboY > 480) or (roboY < 10):
                    if (roboY > 480):
                        roboY -= 1
                    elif (roboY < 10):
                        roboY += 1
                    roboY_speed = 0
                    if (roboX > 470):
                        roboX_speed = -1
                    elif (roboX < 20):
                        roboX_speed = 1
                    else:
                        if (move == 1):
                           roboX_speed = -1
            
                        if (move == 2):
                           roboX_speed = 1

            #this code doesn't work
            """if (roboaction == 1):
                if (roboX_speed == 1) or (roboX_speed == -1):
                    roboY_speed = 0
                    roboX_speed = 1
                if (roboY_speed == 1) or (roboY_speed == -1):
                    roboX_speed = 1
                    roboY_speed = 0
            if (roboaction == 2):
                if (roboX_speed == 1) or (roboX_speed == -1):
                    roboY_speed = 0
                    roboX_speed = -1
                if (roboY_speed == 1) or (roboY_speed == -1):
                    roboX_speed = -1
                    roboY_speed = 0"""
    
    """general movement"""
    playerX += playerX_speed*speed
    playerY += playerY_speed*speed
    roboX += roboX_speed*speed
    roboY += roboY_speed*speed
    
    if (playerX > 490) or (playerX < 5) or (playerY > 490) or (playerY < 5):
        death = True
    if (roboX > 490) or (roboX < 5) or (roboY > 490) or (roboY < 5):
        win = True

    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    for i in range(len(trailX)):
        pygame.draw.rect(screen, GREEN, [trailX[i], trailY[i], 4, 4])
    for i in range(len(robotrailX)):
        pygame.draw.rect(screen, RED, [robotrailX[i], robotrailY[i], 4, 4])
    pygame.draw.rect(screen, GREEN, [playerX, playerY, 4, 4])
    pygame.draw.rect(screen, WHITE, [roboX, roboY, 4, 4])
    pygame.draw.rect(screen, RED, [0, 0, 500, 500], 5)
    font = pygame.font.SysFont('Calibri', 25, True, False)
    roboposition = font.render(str(roboX_speed)+", "+str(roboY_speed),True,WHITE)
    screen.blit(roboposition, [40, 20])
    roboposition = font.render(str(roboX)+", "+str(roboY),True,WHITE)
    screen.blit(roboposition, [40, 40])
    if (death == True):
        text = font.render("You have lost",True,WHITE)
        screen.blit(text, [180, 220])
    if (win == True):
        text = font.render("You have WON!",True,WHITE)
        screen.blit(text, [180, 220])
        
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    #check death
    if (death == True) or (win == True):
        time.sleep(2)
        done = True
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()

