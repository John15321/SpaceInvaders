import pygame
import sys

# Game Over Function
def GameOver():
    print("GAME OVER")
    pygame.event.wait()
    running = 0
    pygame.quit()
    sys.exit()



# Bullet
class Bullet:
    status = 0

    def __init__(self, icon_name):
        self.bulletImg = pygame.image.load(icon_name)

    def start(self, X, Y):
        self.bulletY = Y
        self.bulletX = X
        status = 0

    # Drawing the bullet


    def move(self):
        self.bulletY += 1
        if self.bulletY < 0:
            status = 0

    def CheckHit(self):
        pass


# Player class
class Player:
    GoingLeft = 0
    GoingRight = 0
    status = 1
    def __init__(self, screen_width, screen_height, icon_name):

        # The starship is 64x64 pixels
        self.playerImg = pygame.image.load(icon_name)
        self.playerY = screen_height - self.playerImg.get_width()
        self.playerX = (screen_width / 2) - (self.playerImg.get_width() / 2)

        # The Bullet
        self.bullet = Bullet("bullet.png")

    # Drawing the player
    def draw(self):
        screen.blit(self.playerImg, (player.playerX, player.playerY))
        if self.bullet.status == 1:
            screen.blit(self.bullet.bulletImg, (self.bullet.bulletX, self.bullet.bulletY))
            self.bullet.move()

    def go_left(self):
        self.GoingLeft = 1

    def go_right(self):
        self.GoingRight = 1

    def stop_left(self):
        self.GoingLeft = 0

    def stop_right(self):
        self.GoingRight = 0

    def move(self):
        if (self.GoingLeft == 1) and (self.playerX >= 0):
            self.playerX -= 1
        if (self.GoingRight == 1) and (self.playerX <= width - self.playerImg.get_width()):
            self.playerX += 1
        if (self.bullet.status == 1):
            self.bullet.move()

    def shoot(self):
        self.bullet.start(self.playerX, self.playerY)

# -------------------------------------------------------------------------------------------------------

# Enemy Class
class Enemy:
    GoingLeft = 0
    GoingRight = 0
    def __init__(self, screen_width, screen_height, icon_name, x0, y0):

        # The starship is 64x64 pixels
        self.enemyImg = pygame.image.load(icon_name)
        self.enemyY = y0
        self.enemyX = x0
        self.dead_or_alive = 1
        self.GoingRight = 1



    # Drawing the player
    def draw(self):
        screen.blit(self.enemyImg, (self.enemyX, self.enemyY))

    def go_left(self):
        self.GoingLeft = 1

    def go_right(self):
        self.GoingRight = 1

    def stop_left(self):
        self.GoingLeft = 0

    def stop_right(self):
        self.GoingRight = 0

    def move(self):
        if (self.enemyX == (width - self.enemyImg.get_width())):
            self.enemyX = 0
            self.enemyY += 64
            if self.enemyY == 448:
                GameOver()
        if (self.GoingLeft == 1) and (self.enemyX >= 0):
            self.enemyX -= 0.25
        if (self.GoingRight == 1) and (self.enemyX <= width - self.enemyImg.get_width()):
            self.enemyX += 0.25



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

# Our list of enemies (we will have only six)
enemy_list = []
# Enemy(width, height, "main_enemy.png", 0, 0)
# enemy_list = list(enemy_list)
# Adding 6 enemies (6 so they fit nicely)
for i in range(0, 8):
    enemy = Enemy(width, height, "main_enemy.png", i*64+32*i+20*(i+1), 0)
    enemy_list.append(enemy)


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
                print("go_left()")
            if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
                # Start going right
                player.go_right()
                print("go_right()")
            if event.type == pygame.KEYUP:
                if (event.key == pygame.K_LEFT) or (event.key == pygame.K_a):
                    # Stop going left
                    player.stop_left()
                    print("stop_left()")
                if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
                    # Stop going right
                    player.stop_right()
                    print("stop_right()")
            if event.type == pygame.K_SPACE:
                player.shoot()
                print("shoot()")
    player.move()
    player.draw()

    # Going thru all enemies and drawing them
    for i in enemy_list:
        i.draw()
        i.move()
    pygame.display.update()




# Main starship author: https://www.flaticon.com/authors/nhor-phai