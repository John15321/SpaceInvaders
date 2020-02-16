import pygame
# Initializing the pygame module
pygame.init()


# Creating a window
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

running = True

# Title and Icon
pygame.display.set_caption("Space Invaders")

icon = pygame.image.load("main_icon.png")
pygame.display.set_icon(icon)
# Icon author:
# Icons made by https://www.flaticon.com/authors/itim2101" title="itim2101">itim2101</a> from <a href="https://www.flaticon.com/
# Enemy icon by Icons made by <a href="https://www.flaticon.com/authors/smashicons" title="Smashicons">Smashicons</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>


# Player
# The starship is 64x64 pixels
playerImg = pygame.image.load("main_starship.png")
playerX=(width/2)-(64/2)
playerY=height-64

# Drawing the player
def player(x, y):
    screen.blit(playerImg, (x, y))




GoingLeft=0
GoingRight=0


# Main Game Loop
while running:
    # Adding color fill for bc
    screen.fill((20, 30, 68))
    # Checking for even: closing game window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # If a key is pressed check if right or left
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_LEFT) or (event.key == pygame.K_a):
                # Start going left
                # print("Left key DOWN")
                GoingLeft = 1
            if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
                # Start going right
                # print("Right key DOWN")
                GoingRight = 1
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_LEFT) or (event.key == pygame.K_a):
                # Stop going left
                # print("Left key UP")
                GoingLeft = 0
            if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
                # Stop going right
                # print("Right key UP")
                GoingRight = 0

    if (GoingLeft == 1) and (playerX >= 0):
        playerX -= 1
    elif (GoingRight == 1) and (playerX < width-62):
        playerX += 1
    player(playerX, playerY)

    pygame.display.update()




# Main starship author: https://www.flaticon.com/authors/nhor-phai