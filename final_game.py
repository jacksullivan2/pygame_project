import pygame as pg
import sys
from random import randrange
from start_page import MainMenu

# Initilise pygame's settings
pg.init()

# GLOBAL VARIABLES #
screen_width = 950
screen_height = 700
game_screen = pg.display.set_mode((screen_width, screen_height))
game_screen_rect = game_screen.get_rect()
# The speed at which the prisoner moves (in pixels)
speed = 1
# Width and Height of the Prisoner and Guard images (in pixels)
width = 90
height = 72

# Starting coordinates for guard 1 (that moves)
startx_guard1 = 200
starty_guard1 = 10

# Starting coordinates for guard 2 (that moves)
startx_guard2 = 15
starty_guard2 = 295

# Load the background music into the game
pg.mixer.init()
pg.mixer.music.load("background_music.mp3")
# Set the volume of the music
pg.mixer.music.play()
pg.mixer.music.set_volume(0.5)


####### WALLS #########
class Wall(pg.sprite.Sprite):
    """Model the walls"""

    def __init__(self, image, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# Creating the walls objectsfor the prison map
hor_bor_1 = Wall("up_bord.png", 0, 0)
hor_bor_2 = Wall("up_bord.png", 0, 490)
ver_bor_1 = Wall("down_bord.png", 0, 0)
ver_bor_2 = Wall("down_bord.png", 490, 0)

# cells
int_wall_1 = Wall("up_bord_mini.png", 0, 380)
int_wall_2 = Wall("up_bord_mini.png", 125, 380)
int_wall_3 = Wall("up_bord_mini.png", 175, 380)
int_wall_4 = Wall("up_bord_mini.png", 300, 380)

int_wall_6 = Wall("down_bord_mini.png", 170, 390)
int_wall_8 = Wall("down_bord_mini.png", 170, 440)
int_wall_7 = Wall("down_bord_mini.png", 345, 390)
int_wall_9 = Wall("down_bord_mini.png", 345, 440)

# office
int_wall_5 = Wall("up_bord_mini.png", 350, 380)
# foyer upper
int_wall_14 = Wall("up_bord_mini.png", 345, 200)
int_wall_15 = Wall("up_bord_mini.png", 395, 200)
int_wall_16 = Wall("up_bord_mini.png", 445, 200)

# room 2 east
int_wall_10 = Wall("down_bord_mini.png", 345, 10)
int_wall_11 = Wall("down_bord_mini.png", 345, 160)
int_wall_12 = Wall("down_bord_mini.png", 345, 210)
int_wall_13 = Wall("down_bord_mini.png", 345, 250)
# room 2 west
int_wall_20 = Wall("down_bord_mini.png", 180, 10)
int_wall_21 = Wall("down_bord_mini.png", 180, 60)
int_wall_22 = Wall("down_bord_mini.png", 180, 210)

# corridor north
int_wall_17 = Wall("up_bord_mini.png", 10, 260)
int_wall_18 = Wall("up_bord_mini.png", 300, 260)
int_wall_19 = Wall("up_bord_mini.png", 160, 260)

# Placing the wall objects into a list
wall_list = [hor_bor_1, hor_bor_2, ver_bor_1, ver_bor_2, int_wall_1, int_wall_2, int_wall_3, int_wall_4, int_wall_5,
             int_wall_6, int_wall_7, int_wall_8, int_wall_9
    , int_wall_10, int_wall_11, int_wall_12, int_wall_13, int_wall_14, int_wall_15, int_wall_16, int_wall_17,
             int_wall_18, int_wall_19, int_wall_20, int_wall_21, int_wall_22]

# Creating a group of sprites from this list
walls = pg.sprite.Group()
for wall in wall_list:
    walls.add(wall)


##### GUARDS #######

class Guard(pg.sprite.Sprite):
    """Model the guard"""

    def __init__(self, image, x, y, vx, vy, startx, starty):
        """Initilise the attributes of the guard"""
        super().__init__()
        self.image = pg.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vx = vx
        self.vy = vy
        self.startx = startx
        self.starty = starty

    def move(self, room_xcoord, room_ycoord):
        startx = self.startx
        starty = self.starty
        down_right = True
        if (self.rect.x == startx) and (self.rect.y < room_ycoord) and down_right:
            self.rect.y += self.vy
            print(f'{self.rect.x},{self.rect.y}')
        elif self.rect.x < room_xcoord and self.rect.y == room_ycoord and down_right:
            self.rect.x += self.vx
            print(f'{self.rect.x},{self.rect.y}')
        elif self.rect.x == room_xcoord and self.rect.y > starty:
            down_right = False
            self.rect.y -= self.vy
            print(f'{self.rect.x},{self.rect.y}')
        elif self.rect.x > startx and self.rect.y == starty:
            self.rect.x -= self.vx
            print(f'{self.rect.x},{self.rect.y}')
        else:
            down_right = True

    def move_down_right(self, room_xcoord, room_ycoord):
        move_down_right = True
        while move_down_right:
            if self.rect.x == self.startx and self.rect.y < room_ycoord:
                self.rect.y += self.vy
                print(f"{self.rect.x}, {self.rect.y}")
            elif self.rect.x < room_xcoord and self.rect.y == room_ycoord:
                self.rect.x += self.vx
                print(f"{self.rect.x}, {self.rect.y}")
            else:
                move_down_right = False
                self.move_up_left(room_xcoord, room_ycoord)

    def move_up_left(self, room_xcoord, room_ycoord):
        move_up_left = True
        while move_up_left:
            if self.rect.x == room_xcoord and self.rect.y > self.starty:
                self.rect.y -= self.vy
                print(f"{self.rect.x}, {self.rect.y}")
            elif self.rect.x > self.startx and self.rect.y == self.starty:
                self.rect.x -= self.vx
                print(f"{self.rect.x}, {self.rect.y}")
            else:
                move_up_left = False
                self.move_down_right(room_xcoord, room_ycoord)


guard1 = Guard('guard_image.jpg', 200, 20, 1, 1, startx_guard1, starty_guard1)
guard2 = Guard('guard_image.jpg', 15, 295, 1, 1, startx_guard2, starty_guard2)
guard3 = Guard('guard_image.jpg', 440, 120, 1, 1, 440, 120)
# guard4 = Guard('guard_image.jpg', 435, 215, 1, 1, 435, 215)

guards_list = [guard1, guard2, guard3]

guards = pg.sprite.Group()
for guard in guards_list:
    guards.add(guard)


######## PRISONER ##########


class Prisoner(pg.sprite.Sprite):
    """Model the prisoner"""

    def __init__(self, image_path):
        self.image = pg.image.load(image_path)
        self.prisoner_image_left = pg.image.load(image_path)  # added this line
        self.prisoner_image_right = pg.transform.flip(self.prisoner_image_left, True,
                                                      False)  # added this line - create a flipped image
        self.rect = self.image.get_rect()

        # Set the initial starting location of the prisoner, via the x and y attributes of the prisoners rect
        self.rect.x = 100
        self.rect.y = 420

        # BOUNTY ATTRIBUTE
        self.bounty = 0

        # KEY COUNT
        self.cle_count = 0
        self.last_move = "right"

        # Lives
        self.lives = 3

    def move_prisoner(self, keys=[]):
        # First, check if the prisoner has collided with a wall rect. If so, move them in the opposite direction by 5 pixels
        collision_tolerance = 10
        ###### NEED TO REFERENCE THIS CODE #######
        for wall in wall_list:
            if pg.sprite.collide_rect(prisoner, wall):
                if abs(wall.rect.top - self.rect.bottom) < collision_tolerance:
                    self.rect.y -= 5
                if abs(wall.rect.bottom - self.rect.top) < collision_tolerance:
                    self.rect.y += 5
                if abs(wall.rect.right - self.rect.left) < collision_tolerance:
                    self.rect.x += 5
                if abs(wall.rect.left - self.rect.right) < collision_tolerance:
                    self.rect.x -= 5

        # Respond to different key press events by the user
        if keys[pg.K_LEFT] and self.rect.x > speed:
            self.rect.x -= speed
            self.image = self.prisoner_image_left  # added this line - have left image when moving left
            self.last_move == "left"
        if keys[pg.K_RIGHT] and self.rect.x < (screen_width - width):
            self.rect.x += speed
            self.image = self.prisoner_image_right  # added this line - have right image when moving right
            self.last_move == "right"
        if keys[pg.K_DOWN] and self.rect.y < (screen_height - height):
            self.rect.y += speed
            self.last_move == "down"
        if keys[pg.K_UP] and self.rect.y > speed:
            self.rect.y -= speed
            self.last_move == "up"


prisoner = Prisoner('prisoner.jpg')


##### COINS #######


class Coins(pg.sprite.Sprite):
    """Model the coins"""
    add_coins = True

    def __init__(self, image, x, y):
        """Initilise the attributes of the key"""
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


coin1 = Coins("coin.jpeg", 15, 15)
coin2 = Coins("coin.jpeg", 325, 240)
coin3 = Coins("coin.jpeg", 180, 390)
coin4 = Coins("coin.jpeg", 355, 180)

coins_list = [coin1, coin2, coin3, coin4]
coins = pg.sprite.Group()
for coin in coins_list:
    coins.add(coin)


##### KEY ##########

class Cle(pg.sprite.Sprite):
    add_cle = True
    """Model the key"""

    def __init__(self, image, x, y):
        """Initilise the attributes of the key"""
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


cle1 = Cle('key.jpeg', 355, 390)
cles_list = [cle1]
cles = pg.sprite.Group()
for cle in cles_list:
    cles.add(cle)


####### DOOR ############

class Door(pg.sprite.Sprite):
    """Model the door"""

    def __init__(self, image, x, y):
        """Initilise the door attributes"""
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


door = Door('door.jpeg', 430, 25)
doorgroup = pg.sprite.Group(door)


######### HUD ###########
class Hud:
    """Hud display"""

    def __init__(self):
        """Initilise the attributes of the score"""
        # The font object
        self.font = pg.font.SysFont('verdana', 50, bold=True)
        # Access the information regarding the prisoner and the screen
        # self.keys = prisoner.cle_count
        self.x_location_coins = 10
        self.y_location_coins = 520
        self.x_location_keys = 10
        self.y_location_keys = 580
        self.x_location_lives = 555
        self.y_location_lives = 30

    def display_hud(self):
        """Display the Heads-up Display (HUD) to the screen"""
        display1 = self.font.render(f"Coins: " + str(prisoner.bounty), 1, 'white')
        display2 = self.font.render(f"Keys: " + str(prisoner.cle_count), 1, 'white')
        display3 = self.font.render(f"Lives: " + str(prisoner.lives), 1, "red")
        game_screen.blit(display1, (self.x_location_coins, self.y_location_coins))
        game_screen.blit(display2, (self.x_location_keys, self.y_location_keys))
        game_screen.blit(display3, (self.x_location_lives, self.y_location_lives))


# Create the hud object
hud = Hud()


############# MAIN GAME LOOP ################

# Start the game, using a while loop

def game():
    """Function that plays the game"""
    game_active = True

    while game_active:
        # Loop through all of the events (occurences in the game)
        # Allow the user to quit by pressing on the exit button
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_active = False

        # Get a list of all of the keys that have been pressed by the user
        keys = pg.key.get_pressed()

        # Using this returned list, allow the player to move the prisoner
        prisoner.move_prisoner(keys)
        # Allow the user to quit the game by pressing q
        if keys[pg.K_q]:
            sys.exit()
        # Allow the user to quit the game window via the escape key
        if keys[pg.K_ESCAPE]:
            sys.exit()
        # Allow the user to pause the game
        if keys[pg.K_x]:
            m.mainScreen()
        # Fill the screen with a background colour of black
        game_screen.fill("black")
        # Draw the prisoner and their latest move onto the screen
        game_screen.blit(prisoner.image, (prisoner.rect.x, prisoner.rect.y))
        # Draw the guard sprites onto the game window
        guards.draw(game_screen)
        # Draw the wall sprites onto the game window
        walls.draw(game_screen)
        # Continuosly play the background music
        pg.mixer.music.play()

        # Draw the coins, keys, and door sprites onto the game window
        coins.draw(game_screen)
        cles.draw(game_screen)
        doorgroup.draw(game_screen)

        # Display the HUD on the game window
        hud.display_hud()

        # Display the changes made onto the screen
        pg.display.flip()

        # Move the guards within the room they are placed (box like motion within a range of coordinates)
        guard1.move(290, 190)
        guard2.move(450, 300)
        # Draw the guard sprites to the screen
        guards.draw(game_screen)

        #### GUARD COLLISION #####
        # The code for guard collision
        for guard in guards_list:
            if pg.sprite.collide_rect(prisoner, guard):
                prisoner.lives -= 1
                # Need to reset the prisoners bounty and the position of the coins
                prisoner.bounty = 0
                # create_coins()

                if prisoner.lives < 1:
                    # Print the message onto the screen #
                    loser = hud.font.render("GAME OVER!", True, "red")
                    # Fill the background colour of the screen for the loser message
                    game_screen.fill('black')
                    game_screen.blit(loser, (150, 270))
                    pg.display.flip()
                    # Allow the user to see the congratulations message
                    pg.time.delay(3000)

                    sys.exit()
                else:
                    lives_message = hud.font.render(f"YOU HAVE {prisoner.lives} LIVES REMAINING", True, "red")
                    game_screen.fill("black")
                    game_screen.blit(lives_message, (150, 270))
                    pg.display.flip()
                    pg.time.delay(2000)
                    # Move the prisoner back to their starting location (their) to avoid them continuosly colliding with the prisoner which will cause their
                    # lives to fall below zero causing the game to end
                    prisoner.rect.x = 100
                    prisoner.rect.y = 420
                    continue

        # Code for coin collision
        for coin in coins_list:
            if pg.sprite.collide_rect(prisoner, coin):
                pg.mixer.init()

                Coins_sound = pg.mixer.Sound("coin_sound.mp3")
                Coins_sound.play(0)
                # coin sounds retrived from https://www.fesliyanstudios.com/royalty-free-sound-effects-download/coin-272
                # the sound is called "Bag Of Coins A Sound Effect"

                if coin.add_coins:
                    Coins_sound = pg.mixer.Sound("coin_sound.mp3")
                    prisoner.bounty += 1
                    print(f'Coins = {prisoner.bounty}')
                    coin.add_coins = False
                pg.sprite.Sprite.remove(coin, coins)
                Coins_sound.stop()

        # Code for key collision
        for cle in cles_list:
            if pg.sprite.collide_rect(prisoner, cle):
                pg.mixer.init()
                # load sound effect for keys
                # retrieved from https://mixkit.co/free-sound-effects/key/
                # the sound is called "magic keys"
                key_sound = pg.mixer.Sound("key_sound.wav")
                key_sound.play(0)
                if cle.add_cle:
                    key_sound = pg.mixer.Sound("key_sound.wav")
                    prisoner.cle_count += 1
                    print(f'Keys = {prisoner.cle_count}')
                    cle.add_cle = False
                pg.sprite.Sprite.remove(cle, cles)
                key_sound.stop()

        # Code for door collision
        if pg.sprite.collide_rect(prisoner, door):
            if prisoner.cle_count == len(cles_list):
                print('You win!')
                # Print the message onto the screen #

                congrats = hud.font.render(f"Congratulations! Score: {prisoner.bounty}", True, "red")
                # Fill the background colour of the screen for the congratulations message
                game_screen.fill('black')
                game_screen.blit(congrats, (100, 270))
                pg.display.flip()
                # Allow the user to see the congratulations message
                pg.time.delay(3000)
                sys.exit()
            else:
                prisoner.rect.x -= 20
                keep_going = hud.font.render(f"You still need the key!", True, "red")
                game_screen.blit(keep_going, (150, 270))
                pg.display.flip()
                pg.time.delay(3000)
                sys.exit()


# Running the game #

if __name__ == "__main__":
    import pygame as pg

    m = MainMenu()
    m.mainScreen()
    # Run the game function
    game()