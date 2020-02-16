import pygame
import sys
# Player class
class Player:
    GoingLeft = 0
    GoingRight = 0

    def __init__(self, screen_width, screen_height, icon_name):

        # The starship is 64x64 pixels
        self.playerImg = pygame.image.load(icon_name)
        self.playerY = screen_height - self.playerImg.get_width()
        self.playerX = (screen_width / 2) - (self.playerImg.get_width() / 2)

    # Drawing the player
    def draw(self):
        screen.blit(self.playerImg, (player.playerX, player.playerY))

    def go_left(self):
        self.GoingLeft = 1

    def go_right(self):
        self.GoingRight = 1

    def stop_left(self):
        self.GoingLeft = 0

    def stop_right(self):
        self.GoingRight = 0

    def move(self):
        if self.GoingLeft == 1:
            self.playerX -= 1
        if self.GoingRight == 1:
            self.playerX += 1



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

player = Player(width, height, "main_starship.png")

# Main Game Loop
while running:
    # Adding color fill for bc
    screen.fill((20, 30, 68))
    # Checking for even: closing game window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        # If a key is pressed check if right or left
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_LEFT) or (event.key == pygame.K_a):
                # Start going left
                player.go_left()
            if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
                # Start going right
                player.go_right()
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_LEFT) or (event.key == pygame.K_a):
                # Stop going left
                player.stop_left()
            if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
                # Stop going right
                player.stop_right()
    player.move()
    player.draw()
    pygame.display.update()




# Main starship author: https://www.flaticon.com/authors/nhor-phai