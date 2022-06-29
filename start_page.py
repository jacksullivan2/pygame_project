# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 16:04:39 2021

@author: sophie
"""

import pygame as pg


class MainMenu:
    def instructionScreen(self):
        """
        Created on Sun Dec 12 15:43:57 2021

        @author: akosuabrobbey
        """
        # VARIABLES
        screen_width = 860
        screen_height = 620
        font_type = "ZilapGamePunkDemoMod1-JRZVE.ttf"
        title_size = 140
        font_colour = pg.Color("white")
        bg_colour = (74, 74, 74)
        body_size = 40

        """ The program"""
        # Initialise pygame
        pg.init()

        # Defining a font object
        title_font = pg.font.Font(font_type, title_size)
        body_font = pg.font.Font(font_type, body_size)

        text = title_font.render("INSTRUCTIONS", True, font_colour, bg_colour)

        bodyline1 = body_font.render("Use arrow keys to move prisoner.", True, font_colour, bg_colour)
        bodyline2 = body_font.render("Avoid the prison guards.", True, font_colour, bg_colour)
        bodyline3 = body_font.render("Find the key to open the door.", True, font_colour, bg_colour)
        bodyline4 = body_font.render("Collect the coins.", True, font_colour, bg_colour)
        bodyline5 = body_font.render("Press X to pause", True, font_colour, bg_colour)
        buttonText = body_font.render("BACK", True, font_colour)

        """body = ["Use arrow keys to move prisoner.", "Avoid the prison guards.", "Find the key to open the door.", "Collect the coins.", "Press X to pause"]
        for line in body:
            body_font.render(line, True,font_colour, bg_colour )
        """

        # displaying the screen on pygame
        screen = pg.display.set_mode((screen_width, screen_height))

        # Displays the name of the game at top of window
        pg.display.set_caption("Prison Break")

        # filling screen with background colour
        screen.fill(bg_colour)

        # displaying the 'Game Over' text
        screen.blit(text, (0, 0))

        # displaying the instructions

        screen.blit(bodyline1, (0, 150))
        screen.blit(bodyline2, (0, 250))
        screen.blit(bodyline3, (0, 350))
        screen.blit(bodyline4, (0, 450))
        screen.blit(bodyline5, (0, 550))

        # Game loop
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()

                # Adding return button

                # stores the (x,y) coordinates of the mouse into the variable as a tuple
                mouse = pg.mouse.get_pos()

                # Return Button

                # button colours
                color_light = (41, 82, 11)
                color_dark = (32, 54, 16)

                # if the mouse hovers over the button it changes to lighter shade
                if (screen_width * 7 / 8) <= mouse[0] <= (screen_width * 7 / 8) - 140 and ((screen_height * 7 / 8)) <= \
                        mouse[1] <= (screen_height * 7 / 8) + 40:
                    pg.draw.rect(screen, color_light, [(screen_width * 7 / 8), ((screen_height * 7 / 8)), 140, 40])

                else:
                    pg.draw.rect(screen, color_dark, [screen_width * 7 / 8, ((screen_height * 7 / 8)), 140, 40])

                # superimposing the text onto the button
                screen.blit(buttonText, (screen_width * 7 / 8 + 10, ((screen_height * 7 / 8))))

                # checks if a mouse is clicked
                if event.type == pg.MOUSEBUTTONDOWN:

                    # if the mouse is clicked on the button the game starts
                    if (screen_width * 7 / 8) <= mouse[0] <= screen_width * 7 / 8 + 140 and ((screen_height * 7 / 8)) <= \
                            mouse[1] <= (screen_height * 7 / 8) + 40:
                        return self.mainScreen()

                # updates the frames of the game
                pg.display.update()

    def mainScreen(self):
        # Variable to keep our game loop running
        running = True

        # Making pygame screen
        pg.init()

        # Setting the backgroundcolour
        background_colour = (74, 74, 74)

        # Define the dimensions of window
        x = 18 * 70
        y = 9 * 75
        screen = pg.display.set_mode((x, y))

        # Naming the window
        pg.display.set_caption('Prison Break')
        # setting screen colour
        screen.fill(background_colour)

        # Adding the brickwall image (from the internet) and scaling
        brickwall = pg.image.load('./brickwall.jpg').convert_alpha()
        brickwall = pg.transform.scale(brickwall, (18 * 70, 9 * 75))

        # Update the display
        pg.display.flip()

        # Adding title

        # Define colours
        white = (255, 255, 255)
        black = (0, 0, 0)

        # Setting font and size of title
        font = pg.font.Font('./mainMenuFont.ttf', 100)

        text = font.render('PRISON BREAK', True, white)

        # create a rectangular object for the text
        textRect = text.get_rect()

        # set the center of the rectangle.
        textRect.center = (x // 2, (y // 2) - 50)
        screen.blit(text, textRect)

        # Adding start button and instruction button

        # button colours
        color_light = (41, 82, 11)
        color_dark = (32, 54, 16)

        # Getting the width and height of the screen
        width = screen.get_width()
        height = screen.get_height()

        # defining a font
        startFont = pg.font.Font('./mainMenuFont.ttf', 40)

        startText = startFont.render('START', True, white)
        instructionsText = startFont.render('INSTRUCTIONS', True, white)

        # Loop for whilst the window is running
        while True:
            for event in pg.event.get():

                # Drawing the brickwall
                brickwall.set_colorkey(black)
                screen.blit(brickwall, (-20, 0))

                # stores the (x,y) coordinates of the mouse into the variable as a tuple
                mouse = pg.mouse.get_pos()

                # Start Button

                # if the mouse hovers over the button it changes to lighter shade
                if (width / 2 - 70) <= mouse[0] <= width / 2 + 70 and ((height / 2) + 10) <= mouse[1] <= (
                        height / 2) + 50:
                    pg.draw.rect(screen, color_light, [width / 2 - 70, ((height / 2) + 10), 140, 40])

                else:
                    pg.draw.rect(screen, color_dark, [width / 2 - 70, ((height / 2) + 10), 140, 40])

                # superimposing the text onto the button
                screen.blit(startText, (width / 2 - 50, ((height / 2) + 10)))

                if event.type == pg.QUIT:
                    pg.quit()

                # checks if a mouse is clicked
                elif event.type == pg.MOUSEBUTTONDOWN:

                    # if the mouse is clicked on the button the game starts
                    if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and ((height / 2) + 10) <= mouse[1] <= (
                            height / 2) + 50:
                        return "start"

                # Instruction Button

                # changes to lighter shade
                if (width / 2 - 130) <= mouse[0] <= width / 2 + 130 and ((height / 2) + 70) <= mouse[1] <= (
                        height / 2) + 110:
                    pg.draw.rect(screen, color_light, [width / 2 - 130, ((height / 2) + 70), 260, 40])

                else:
                    pg.draw.rect(screen, color_dark, [width / 2 - 130, ((height / 2) + 70), 260, 40])

                # superimposing the text onto the button
                screen.blit(instructionsText, (width / 2 - 120, ((height / 2) + 70)))

                if event.type == pg.QUIT:
                    pg.quit()

                # checks if a mouse is clicked
                elif event.type == pg.MOUSEBUTTONDOWN:

                    # if the mouse is clicked on the button, open instructions page
                    if width / 2 - 130 <= mouse[0] <= width / 2 + 130 and ((height / 2) + 70) <= mouse[1] <= (
                            height / 2) + 110:
                        ret = self.instructionScreen()
                        if ret == "start":
                            return "start"

            # updates the frames of the game
            pg.display.update()


if __name__ == "__main__":
    import pygame as pg

    m = MainMenu()
    m.mainScreen()