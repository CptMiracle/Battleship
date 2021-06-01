# Author: Aidan Huang
# Date: April 20, 2021
# Battleship


import random
import time

import pygame
import sys


pygame.init()

# set the size for the surface (screen)
# MUST BE PLAYED ON 1000 x 800
screen = pygame.display.set_mode((1000, 800), 0)
# set the caption for the screen
pygame.display.set_caption("BATTLESHIP")

# define colours you will be using
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (153, 204, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Sound enabled
sound = True

# set images
battleship_intro = pygame.image.load("../FinalProject/images/battleship-intro-background.jpg")
playerImage_battleship = pygame.image.load("../FinalProject/images/battleship.png").convert()
playerImage_battleship.set_colorkey(BLACK)
playerImage_aircraft_carrier = pygame.image.load("../FinalProject/images/aircraft carrier.png").convert()
playerImage_aircraft_carrier.set_colorkey(BLACK)
playerImage_destroyer = pygame.image.load("../FinalProject/images/destroyer.png").convert()
playerImage_destroyer.set_colorkey(BLACK)
playerImage_submarine = pygame.image.load("../FinalProject/images/submarine.png").convert()
playerImage_submarine.set_colorkey(BLACK)
playerImage_small_ship = pygame.image.load("../FinalProject/images/small ship.png").convert()
playerImage_small_ship.set_colorkey(BLACK)
plane = pygame.image.load("../FinalProject/images/Fighter-jet.png").convert()
plane.set_colorkey(BLACK)
plane_2 = pygame.image.load("../FinalProject/images/Fighter-jet2.png").convert()
plane_2.set_colorkey(BLACK)
clock = pygame.time.Clock()

#set sounds

explosion_sound = pygame.mixer.Sound("../FinalProject/sounds/battleship-explosion.wav")
splash_sound = pygame.mixer.Sound("../FinalProject/sounds/battleship-splash.wav")
button_sound = pygame.mixer.Sound("../FinalProject/sounds/button-click.wav")
plane_sound = pygame.mixer.Sound("../FinalProject/sounds/fighter-jet-flyover.wav")


# set main loop to True so it will run
main = True
intro = True
rules = False
leaderboard = False
settings = False
play_menu = False
instructions1 = False
instructions2 = False
instructions2_difficulty = False
game_setup = False
game_setup2 = False
game_AI = False
game_AI_p1 = False
game_AI_p2 = False
player1_scene = False
player2_scene = False
game_PVP = False
game_PVP_p1 = False
game_PVP_p2 = False
final = False

# main loop
while main:
    pygame.mouse.set_cursor(pygame.cursors.tri_left)

    # initialize arrays
    battleship_player1 = []
    aircraft_carrier_player1 = []
    destroyer_player1 = []
    submarine_player1 = []
    small_ship_player1 = []
    battleship_player2 = []
    aircraft_carrier_player2 = []
    destroyer_player2 = []
    submarine_player2 = []
    small_ship_player2 = []

    all_player1_ships = []
    all_player2_ships = []

    player1_clicked_grids = []
    player2_clicked_grids = []

    # variables
    clock = pygame.time.Clock()
    screen_W = screen.get_width()
    screen_H = screen.get_height()
    FPS = 60
    game_type = 1
    clock.tick(FPS)

    winner = -1  # 0 for player1, 1 for player2, 2 for computer

    while intro:
        pos = pygame.mouse.get_pos()
        screen.fill(LIGHT_BLUE)
        font_title = pygame.font.SysFont("arial bold", 100)
        font_playmenu = pygame.font.SysFont("arial bold", 50)
        title_text = font_title.render("BATTLESHIP", True, WHITE)
        play_text = font_playmenu.render("Play", True, WHITE)
        rules_text = font_playmenu.render("Rules", True, WHITE)
        leaderboard_text = font_playmenu.render("Leaderboard", True, BLACK)
        settings_text = font_playmenu.render("Settings", True, WHITE)
        #Display text to screen
        background_image = battleship_intro.get_rect()
        background_image.center = (screen_W / 2, screen_H / 2)
        screen.blit(battleship_intro, background_image)

        # Battleship
        textRect1 = title_text.get_rect()
        textRect1.center = (screen_W / 2, screen_H - screen_H / 1.2)
        screen.blit(title_text, textRect1)

        # Play
        textRect2 = play_text.get_rect()
        textRect2.center = (screen_W / 2, screen_H - screen_H / 1.4)
        screen.blit(play_text, textRect2)

        # Rules
        textRect3 = rules_text.get_rect()
        textRect3.center = (screen_W / 2, screen_H - screen_H / 1.8)
        screen.blit(rules_text, textRect3)

        # Leaderboard
        textRect4 = leaderboard_text.get_rect()
        textRect4.center = (screen_W / 2, screen_H - screen_H / 2.5)
        screen.blit(leaderboard_text, textRect4)

        #Settings
        textRect5 = settings_text.get_rect()
        textRect5.center = (screen_W / 2, screen_H - screen_H / 4)
        screen.blit(settings_text, textRect5)



        pygame.display.flip()
        for event in pygame.event.get():
            #If player decides to exit the game, quit
            if event.type == pygame.QUIT:
                main = False
                intro = False
                rules = False
                leaderboard = False
                settings = False
                play_menu = False
                instructions1 = False
                instructions2 = False
                instructions2_difficulty = False
                game_setup = False
                game_setup2 = False
                game_AI = False
                game_AI_p1 = False
                game_AI_p2 = False
                game_PVP = False
                game_PVP_p1 = False
                game_PVP_p2 = False
                final = False
            #If player clicks a button, go to another scene
            if event.type == pygame.MOUSEBUTTONUP:
                if textRect2.collidepoint(pos):
                    play_menu = True
                    intro = False
                    button_sound.play()
                elif textRect3.collidepoint(pos):
                    rules = True
                    intro = False
                    button_sound.play()

                elif textRect4.collidepoint(pos):
                    leaderboard = True
                    intro = False
                    button_sound.play()
                elif textRect5.collidepoint(pos):
                    settings = True
                    intro = False
                    button_sound.play()

    #intro -> play
    while play_menu:

        pos = pygame.mouse.get_pos()
        screen.fill(LIGHT_BLUE)
        font_title = pygame.font.SysFont("arial bold", 100)
        font_playmenu = pygame.font.SysFont("arial bold", 60)
        title_text = font_title.render("BATTLESHIP", True, BLUE)
        play_text = font_playmenu.render("Play PvP or Play PvAI", True, RED)
        PvP_text = font_playmenu.render("Player vs Player", True, BLACK)
        PvAI_text = font_playmenu.render("Player vs AI", True, BLACK)

        textRect1 = title_text.get_rect()
        textRect1.center = (screen_W / 2, screen_H - screen_H / 1.2)
        screen.blit(title_text, textRect1)

        textRect2 = play_text.get_rect()
        textRect2.center = (screen_W / 2, screen_H - screen_H / 1.4)
        screen.blit(play_text, textRect2)

        textRect3 = PvP_text.get_rect()
        textRect3.center = (screen_W / 3.5, screen_H - screen_H / 2)
        screen.blit(PvP_text, textRect3)

        textRect4 = PvAI_text.get_rect()
        textRect4.center = (screen_W / 1.5, screen_H - screen_H / 2)
        screen.blit(PvAI_text, textRect4)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False
                intro = False
                rules = False
                leaderboard = False
                settings = False
                play_menu = False
                instructions1 = False
                instructions2 = False
                instructions2_difficulty = False
                game_setup = False
                game_setup2 = False
                game_AI = False
                game_AI_p1 = False
                game_AI_p2 = False
                game_PVP = False
                game_PVP_p1 = False
                game_PVP_p2 = False
                final = False

            #PvP
            if event.type == pygame.MOUSEBUTTONUP:
                if textRect3.collidepoint(pos):
                    game_setup = True
                    play_menu = False
                    game_type = 1
                    gamePVP = True
                    button_sound.play()

                #PvAI
                elif textRect4.collidepoint(pos):
                    game_setup = True
                    play_menu = False
                    game_type = 2
                    game_AI = True
                    button_sound.play()

    #Game rules
    while rules:
        pos = pygame.mouse.get_pos()
        screen.fill(LIGHT_BLUE)
        font_instructions1 = pygame.font.SysFont("arial", 23)
        font_instructions2 = pygame.font.SysFont("arial", 18)
        instructs11 = font_instructions1.render("You can choose to play PvP or PvAI", True, BLACK)
        instructs12 = font_instructions1.render(
            "In setup mode, all players have 5 ships to place onto a 10x10 array", True, BLACK)
        instructs13 = font_instructions1.render(
            "First player to sink all enemy ship wins", True, BLACK)
        instructs14 = font_instructions2.render(
            "White grids = clickable, Green grids = No enemy ship, Red grids = Enemy ship hit, Black grids = Enemy ship destroyed", True, BLACK)
        instructs15 = font_instructions1.render("All ships do not change position after the game starts", True, BLACK)
        instructs16 = font_instructions1.render("Have fun!", True, BLACK)
        goback_text = font_instructions1.render("Go Back", True, BLACK)

        textRect1 = instructs11.get_rect()
        textRect1.center = (screen_W / 2, screen_H - screen_H / 1.1)
        screen.blit(instructs11, textRect1)

        textRect2 = instructs12.get_rect()
        textRect2.center = (screen_W / 2, screen_H - screen_H / 1.3)
        screen.blit(instructs12, textRect2)

        textRect3 = instructs13.get_rect()
        textRect3.center = (screen_W / 2, screen_H - screen_H / 1.5)
        screen.blit(instructs13, textRect3)

        textRect4 = instructs14.get_rect()
        textRect4.center = (screen_W / 2, screen_H - screen_H / 1.8)
        screen.blit(instructs14, textRect4)

        textRect5 = instructs15.get_rect()
        textRect5.center = (screen_W / 2, screen_H - screen_H / 2.2)
        screen.blit(instructs15, textRect5)

        textRect6 = instructs16.get_rect()
        textRect6.center = (screen_W / 2, screen_H - screen_H / 2.7)
        screen.blit(instructs16, textRect6)

        textRect_goback = goback_text.get_rect()
        textRect_goback.center = (screen_W / 2, screen_H - screen_H / 4)
        screen.blit(goback_text, textRect_goback)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False
                intro = False
                rules = False
                leaderboard = False
                settings = False
                play_menu = False
                instructions1 = False
                instructions2 = False
                instructions2_difficulty = False
                game_setup = False
                game_setup2 = False
                game_AI = False
                game_AI_p1 = False
                game_AI_p2 = False
                game_PVP = False
                game_PVP_p1 = False
                game_PVP_p2 = False
                final = False

            if event.type == pygame.MOUSEBUTTONUP:
                if textRect_goback.collidepoint(pos):
                    intro = True
                    rules = False
                    leaderboard = False
                    settings = False
                    play_menu = False
                    instructions1 = False
                    instructions2 = False
                    instructions2_difficulty = False
                    game_setup = False
                    game_setup2 = False
                    game_AI = False
                    game_AI_p1 = False
                    game_AI_p2 = False
                    game_PVP = False
                    game_PVP_p1 = False
                    game_PVP_p2 = False
                    final = False

    textRect2_startingy = 100

    #Leaderboard
    #Scroll down if the leaderboard is too long
    while leaderboard:
        screen.fill(LIGHT_BLUE)
        pos = pygame.mouse.get_pos()
        font_leaderboard = pygame.font.SysFont("arial", 40)
        font_goback = pygame.font.SysFont("arial", 30)
        goback_text = font_goback.render("Go Back", True, BLACK)
        leaderboard_window = ''
        textRect2 = ''

        #Read leaderboard info
        readBoard = open('../FinalProject/FinalProjectLeaderboard.txt', 'r')
        #left column
        board_names = []
        #right column
        board_score = []
        for line in readBoard:
            board_names.append(line.split(' = ')[0])
            board_score.append(line.split(' = ')[1].replace('\n', ''))

        #Display player name and scores
        for i in range(len(board_names)):
            leaderboard_window_name = font_leaderboard.render(board_names[i], True, BLACK)
            leaderboard_window_score = font_leaderboard.render(board_score[i], True, BLACK)
            textRect2 = leaderboard_window_name.get_rect()
            textRect3 = leaderboard_window_score.get_rect()
            textRect2.center = (screen_W / 3, (textRect2_startingy + (50 * i)))
            textRect3.center = (screen_W / 1.5, (textRect2_startingy + (50 * i)))
            screen.blit(leaderboard_window_name, textRect2)
            screen.blit(leaderboard_window_score, textRect3)

        textRect1 = goback_text.get_rect()
        textRect1.center = (screen_W / 2, textRect2.y + 100)
        screen.blit(goback_text, textRect1)

        readBoard.close()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False
                intro = False
                rules = False
                leaderboard = False
                settings = False
                play_menu = False
                instructions1 = False
                instructions2 = False
                instructions2_difficulty = False
                game_setup = False
                game_setup2 = False
                game_AI = False
                game_AI_p1 = False
                game_AI_p2 = False
                game_PVP = False
                game_PVP_p1 = False
                game_PVP_p2 = False
                final = False
            textRect2_dy = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # scroll up
                    textRect2_dy += 10

                if event.button == 5:  # scroll down
                    textRect2_dy -= 10

            #if leaderboard goes beyond the top of the window
            if textRect2.y < 100:
                if textRect2_dy < 0:
                    textRect2_dy = 0

            #add change in y to position y
            textRect2_startingy += textRect2_dy

            if event.type == pygame.MOUSEBUTTONUP:
                if textRect1.collidepoint(pos):
                    intro = True
                    rules = False
                    leaderboard = False
                    settings = False
                    play_menu = False
                    instructions1 = False
                    instructions2 = False
                    instructions2_difficulty = False
                    game_setup = False
                    game_setup2 = False
                    game_AI = False
                    game_AI_p1 = False
                    game_AI_p2 = False
                    game_PVP = False
                    game_PVP_p1 = False
                    game_PVP_p2 = False
                    final = False

    #Turn sound on or off
    while settings:

        pos = pygame.mouse.get_pos()
        screen.fill(LIGHT_BLUE)
        font_playmenu = pygame.font.SysFont("arial", 50)
        font_goback = pygame.font.SysFont("arial", 30)

        title_text = font_playmenu.render("Sound: ", True, BLACK)
        sound_on = font_playmenu.render("On", True, BLACK)
        sound_off = font_playmenu.render("Off", True, BLACK)
        goback_text = font_goback.render("Go Back", True, BLACK)

        textRect1 = title_text.get_rect()
        textRect1.center = (screen_W / 2.1, screen_H - screen_H / 1.2)
        screen.blit(title_text, textRect1)

        textRect3 = sound_on.get_rect()
        textRect3.center = (screen_W / 1.7, screen_H - screen_H / 1.2)
        if sound:
            screen.blit(sound_on, textRect3)

        textRect4 = sound_off.get_rect()
        textRect4.center = (screen_W / 1.7, screen_H - screen_H / 1.2)
        if sound is False:
            screen.blit(sound_off, textRect4)

        textRect2 = goback_text.get_rect()
        textRect2.center = (screen_W / 2, screen_H - screen_H / 2)
        screen.blit(goback_text, textRect2)


        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False
                intro = False
                rules = False
                leaderboard = False
                settings = False
                play_menu = False
                instructions1 = False
                instructions2 = False
                instructions2_difficulty = False
                game_setup = False
                game_setup2 = False
                game_AI = False
                game_AI_p1 = False
                game_AI_p2 = False
                game_PVP = False
                game_PVP_p1 = False
                game_PVP_p2 = False
                final = False

            if event.type == pygame.MOUSEBUTTONUP:
                if textRect1.collidepoint(pos):
                    if sound:
                        sound = False
                        #Set sound volumes to 0
                        pygame.mixer.Sound.set_volume(button_sound, 0)
                        pygame.mixer.Sound.set_volume(explosion_sound, 0)
                        pygame.mixer.Sound.set_volume(splash_sound, 0)
                        pygame.mixer.Sound.set_volume(plane_sound, 0)
                    elif sound is False:
                        sound = True
                        #Set sound volumes to initial values (100)
                        pygame.mixer.Sound.set_volume(button_sound, 100)
                        pygame.mixer.Sound.set_volume(explosion_sound, 100)
                        pygame.mixer.Sound.set_volume(splash_sound, 100)
                        pygame.mixer.Sound.set_volume(plane_sound, 100)
                        button_sound.play()
                #go back
                elif textRect2.collidepoint(pos):
                    intro = True
                    rules = False
                    leaderboard = False
                    settings = False
                    play_menu = False
                    instructions1 = False
                    instructions2 = False
                    instructions2_difficulty = False
                    game_setup = False
                    game_setup2 = False
                    game_AI = False
                    game_AI_p1 = False
                    game_AI_p2 = False
                    game_PVP = False
                    game_PVP_p1 = False
                    game_PVP_p2 = False
                    final = False

    # Player sets up their ships
    rect_dragging = False
    battleship_rect = playerImage_battleship.get_rect()
    battleship_rect.center = (100, 250)

    aircraft_carrier_rect = playerImage_aircraft_carrier.get_rect()
    aircraft_carrier_rect.center = (100, 350)

    destroyer_rect = playerImage_destroyer.get_rect()
    destroyer_rect.center = (100, 450)

    submarine_rect = playerImage_submarine.get_rect()
    submarine_rect.center = (100, 550)

    small_ship_rect = playerImage_small_ship.get_rect()
    small_ship_rect.center = (100, 650)

    offset_x = 0
    offset_y = 0

    battleship_on_grid = False
    aircraft_carrier_on_grid = False
    destroyer_on_grid = False
    submarine_on_grid = False
    small_ship_on_grid = False

    #Row and Column grid values for ship snapping to the grids
    nearest_row = [250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750]
    nearest_col = [200, 252, 304, 356, 408, 460, 512, 564, 616, 668, 720]


    # Ship setup for computer AI
    def computer_setup(ship):
        temp = []
        # initalize
        #Using random to place AI ships
        random_col = random.randint(0, 9)
        if ship == battleship_player2:
            random_row = random.randint(0, 6)
            for i in range(random_row, random_row + 4):
                temp.append([i, random_col])
        elif ship == aircraft_carrier_player2:
            random_row = random.randint(0, 5)
            for i in range(random_row, random_row + 5):
                temp.append([i, random_col])
        elif ship == destroyer_player2:
            random_row = random.randint(0, 7)
            for i in range(random_row, random_row + 3):
                temp.append([i, random_col])
        elif ship == submarine_player2:
            random_row = random.randint(0, 8)
            for i in range(random_row, random_row + 2):
                temp.append([i, random_col])
        elif ship == small_ship_player2:
            random_row = random.randint(0, 9)
            for i in range(random_row, random_row + 1):
                temp.append([i, random_col])
        #If AI ship overlaps another ship, move to another position
        for i in temp:
            for j in range(len(all_player2_ships)):
                if i == all_player2_ships[j]:
                    temp = computer_setup(ship)
        return temp


    while game_setup:
        #get mouse position
        pos = pygame.mouse.get_pos()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        screen.fill(LIGHT_BLUE)
        font_player2 = pygame.font.SysFont("arial", 50)
        font_done = pygame.font.SysFont("arial", 50)
        font_gamesetup_header = pygame.font.SysFont("arial", 15)
        done_text = font_done.render("DONE", True, BLACK)
        header1_text = font_gamesetup_header.render("Drag and drop ships onto the grids.", True, BLACK)
        header2_text = font_gamesetup_header.render(
            "Make sure all ships are placed onto the grids and do not overlap one another.", True, BLACK)
        player1_text = font_player2.render("Player 1's turn", True, BLACK)

        textRect1 = done_text.get_rect()
        textRect1.center = (screen_W / 1.15, screen_H / 2)
        screen.blit(done_text, textRect1)

        textRect2 = header1_text.get_rect()
        textRect2.center = (screen_W / 2, screen_H / 6)
        screen.blit(header1_text, textRect2)

        textRect2 = header2_text.get_rect()
        textRect2.center = (screen_W / 2, screen_H / 5)
        screen.blit(header2_text, textRect2)

        textRect3 = player1_text.get_rect()
        textRect3.center = (screen_W / 2, screen_H / 9)
        screen.blit(player1_text, textRect3)

        # Individual grids
        grid = []

        #Display white grids
        for r in range(10):
            row = []
            for c in range(10):
                row.append(pygame.Rect(250 + (50 * r), 200 + (52 * c), 50, 50))
                pygame.draw.rect(screen, WHITE, (250 + (50 * r), 200 + (52 * c), 50, 50))
            grid.append(row)

        # Vertical and Horizontal lines
        for i in range(11):
            pygame.draw.line(screen, BLACK, (250, 200 + (i * 52)), (screen_W - 250, 200 + (i * 52)), 5)
            pygame.draw.line(screen, BLACK, (250 + (i * 50), 200), (250 + (i * 50), screen_H - 80), 5)


        #Display player ships
        screen.blit(playerImage_battleship, battleship_rect)

        screen.blit(playerImage_aircraft_carrier, aircraft_carrier_rect)

        screen.blit(playerImage_destroyer, destroyer_rect)

        screen.blit(playerImage_submarine, submarine_rect)

        screen.blit(playerImage_small_ship, small_ship_rect)

        for event in pygame.event.get():  # check for any events (i.e key press, mouse click etc.)
            if event.type == pygame.QUIT:
                main = False
                intro = False
                rules = False
                leaderboard = False
                settings = False
                play_menu = False
                instructions1 = False
                instructions2 = False
                instructions2_difficulty = False
                game_setup = False
                game_setup2 = False
                game_AI = False
                game_AI_p1 = False
                game_AI_p2 = False
                game_PVP = False
                game_PVP_p1 = False
                game_PVP_p2 = False
                final = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    # Battleship
                    if battleship_rect.collidepoint(pos):
                        #True if the rect is being dragged by mouse
                        #offset_x and offset_y lets ship rects be dragged at any point of the rect without moving it to
                        #the top left corner everytime.
                        #offset contains the distance between the ship rect and the mouse position
                        #in the end, the position of the ship is the mouse position and the offset value
                        rect_dragging = True
                        offset_x = battleship_rect.x - mouse_x
                        offset_y = battleship_rect.y - mouse_y
                    # Aircraft Carrier
                    elif aircraft_carrier_rect.collidepoint(pos):
                        rect_dragging = True
                        offset_x = aircraft_carrier_rect.x - mouse_x
                        offset_y = aircraft_carrier_rect.y - mouse_y
                    # Destroyer
                    elif destroyer_rect.collidepoint(pos):
                        rect_dragging = True
                        offset_x = destroyer_rect.x - mouse_x
                        offset_y = destroyer_rect.y - mouse_y
                    # Submarine
                    elif submarine_rect.collidepoint(pos):
                        rect_dragging = True
                        offset_x = submarine_rect.x - mouse_x
                        offset_y = submarine_rect.y - mouse_y
                    # Small ship
                    elif small_ship_rect.collidepoint(pos):
                        rect_dragging = True
                        offset_x = small_ship_rect.x - mouse_x
                        offset_y = small_ship_rect.y - mouse_y

            elif event.type == pygame.MOUSEBUTTONUP:
                if textRect1.collidepoint(pos):
                    if game_type == 1:
                        game_setup = False
                        game_setup2 = True
                        button_sound.play()

                    #AI
                    elif game_type == 2:

                        game_setup = False
                        game_setup2 = False
                        game_AI = True
                        game_AI_p1 = True
                        button_sound.play()

                        #Take all AI ships and place them into a total ships array
                        def totalships_player2(ships):
                            if len(ships) != 0:
                                for x in ships:
                                    all_player2_ships.append(x)


                        # Computer setup
                        battleship_player2 = computer_setup(battleship_player2)
                        totalships_player2(battleship_player2)
                        aircraft_carrier_player2 = computer_setup(aircraft_carrier_player2)
                        totalships_player2(aircraft_carrier_player2)
                        destroyer_player2 = computer_setup(destroyer_player2)
                        totalships_player2(destroyer_player2)
                        submarine_player2 = computer_setup(submarine_player2)
                        totalships_player2(submarine_player2)
                        small_ship_player2 = computer_setup(small_ship_player2)
                        totalships_player2(small_ship_player2)

                #If player drags ship to grids, snap the ship rect
                if event.button == 1:
                    if 250 <= battleship_rect.x <= 600 and 200 <= battleship_rect.y <= 700:
                        battleship_on_grid = True
                    else:
                        battleship_on_grid = False

                    if 250 <= aircraft_carrier_rect.x <= 550 and 200 <= aircraft_carrier_rect.y <= 700:
                        aircraft_carrier_on_grid = True
                    else:
                        aircraft_carrier_on_grid = False

                    if 250 <= destroyer_rect.x <= 650 and 200 <= destroyer_rect.y <= 700:
                        destroyer_on_grid = True
                    else:
                        destroyer_on_grid = False

                    if 250 <= submarine_rect.x <= 700 and 200 <= submarine_rect.y <= 700:
                        submarine_on_grid = True
                    else:
                        submarine_on_grid = False

                    if 250 <= small_ship_rect.x <= 750 and 200 <= small_ship_rect.y <= 700:
                        small_ship_on_grid = True
                    else:
                        small_ship_on_grid = False

                    rect_dragging = False


                    # to find the closest but smallest row
                    def find_nearest_row(ship_rect_x):
                        for i in nearest_row:
                            if i <= ship_rect_x < i + 50:
                                return i
                            else:
                                i += 50


                    # to find the closest but smallest column
                    def find_nearest_col(ship_rect_y):
                        for i in nearest_col:
                            if i <= ship_rect_y < i + 52:
                                return i
                            else:
                                i += 52


                    # use rect collision and put ships into array
                    def check_for_ship(ship_rect):
                        ship_coordinates = []
                        for row in range(10):
                            for col in range(10):
                                if pygame.Rect.colliderect(grid[row][col], ship_rect):
                                    ship_coordinates.append([row, col])
                        return ship_coordinates


                    # this is to snap the ships to the grid
                    if battleship_on_grid:
                        battleship_rect.x = find_nearest_row(battleship_rect.x)
                        battleship_rect.y = find_nearest_col(battleship_rect.y)
                        battleship_player1 = check_for_ship(battleship_rect)
                        battleship_on_grid = False

                    if aircraft_carrier_on_grid:
                        aircraft_carrier_rect.x = find_nearest_row(aircraft_carrier_rect.x)
                        aircraft_carrier_rect.y = find_nearest_col(aircraft_carrier_rect.y)
                        aircraft_carrier_player1 = check_for_ship(aircraft_carrier_rect)
                        aircraft_carrier_on_grid = False

                    if destroyer_on_grid:
                        destroyer_rect.x = find_nearest_row(destroyer_rect.x)
                        destroyer_rect.y = find_nearest_col(destroyer_rect.y)
                        destroyer_player1 = check_for_ship(destroyer_rect)
                        destroyer_on_grid = False

                    if submarine_on_grid:
                        submarine_rect.x = find_nearest_row(submarine_rect.x)
                        submarine_rect.y = find_nearest_col(submarine_rect.y)
                        submarine_player1 = check_for_ship(submarine_rect)
                        submarine_on_grid = False

                    if small_ship_on_grid:
                        small_ship_rect.x = find_nearest_row(small_ship_rect.x)
                        small_ship_rect.y = find_nearest_col(small_ship_rect.y)
                        small_ship_player1 = check_for_ship(small_ship_rect)
                        small_ship_on_grid = False


            #if ship rect is being dragged, offset keeps the rect from moving to the mouse and instead is able to be clicked on
            #at any point
            elif event.type == pygame.MOUSEMOTION and rect_dragging:
                def ship_mouse_motion(ship_rect):
                    ship_rect.x = mouse_x + offset_x
                    ship_rect.y = mouse_y + offset_y


                # Battleship
                if battleship_rect.collidepoint(pos):
                    ship_mouse_motion(battleship_rect)
                # Aircraft Carrier
                elif aircraft_carrier_rect.collidepoint(pos):
                    ship_mouse_motion(aircraft_carrier_rect)
                # Destroyer
                elif destroyer_rect.collidepoint(pos):
                    ship_mouse_motion(destroyer_rect)
                # Submarine
                elif submarine_rect.collidepoint(pos):
                    ship_mouse_motion(submarine_rect)
                # Small ship
                elif small_ship_rect.collidepoint(pos):
                    ship_mouse_motion(small_ship_rect)

        #keeps ships within the window
        def ship_borders(ship_rect):
            if ship_rect.x < 0:
                ship_rect.x = 0
            elif ship_rect.x >= screen_W - 200:
                ship_rect.x = screen_W - 200
            elif ship_rect.y < 0:
                ship_rect.y = 0
            elif ship_rect.y >= screen_H - 50:
                ship_rect.y = screen_H - 50


        ship_borders(battleship_rect)
        ship_borders(aircraft_carrier_rect)
        ship_borders(destroyer_rect)
        ship_borders(submarine_rect)
        ship_borders(small_ship_rect)

        pygame.display.flip()

    #Go to gamesetup1 for reference
    rect_dragging = False
    battleship_rect = playerImage_battleship.get_rect()
    battleship_rect.center = (100, 250)

    aircraft_carrier_rect = playerImage_aircraft_carrier.get_rect()
    aircraft_carrier_rect.center = (100, 350)

    destroyer_rect = playerImage_destroyer.get_rect()
    destroyer_rect.center = (100, 450)

    submarine_rect = playerImage_submarine.get_rect()
    submarine_rect.center = (100, 550)

    small_ship_rect = playerImage_small_ship.get_rect()
    small_ship_rect.center = (100, 650)

    offset_x = 0
    offset_y = 0

    battleship_on_grid = False
    aircraft_carrier_on_grid = False
    destroyer_on_grid = False
    submarine_on_grid = False
    small_ship_on_grid = False

    nearest_row = [250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750]
    nearest_col = [200, 252, 304, 356, 408, 460, 512, 564, 616, 668, 720]

    # game setup for player 2
    while game_setup2:

        pos = pygame.mouse.get_pos()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        screen.fill(LIGHT_BLUE)
        font_player2 = pygame.font.SysFont("arial", 50)
        font_done = pygame.font.SysFont("arial", 50)
        font_gamesetup_header = pygame.font.SysFont("arial", 15)
        player2_text = font_player2.render("Player 2's turn", True, BLACK)
        done_text = font_done.render("DONE", True, BLACK)
        header1_text = font_gamesetup_header.render("Drag and drop ships onto the grids.", True, BLACK)
        header2_text = font_gamesetup_header.render(
            "Make sure all ships are placed onto the grids and do not overlap one another.", True, BLACK)

        textRect1 = done_text.get_rect()
        textRect1.center = (screen_W / 1.15, screen_H / 2)
        screen.blit(done_text, textRect1)

        textRect2 = header1_text.get_rect()
        textRect2.center = (screen_W / 2, screen_H / 6)
        screen.blit(header1_text, textRect2)

        textRect2 = header2_text.get_rect()
        textRect2.center = (screen_W / 2, screen_H / 5)
        screen.blit(header2_text, textRect2)

        textRect3 = player2_text.get_rect()
        textRect3.center = (screen_W / 2, screen_H / 9)
        screen.blit(player2_text, textRect3)

        # Individual grids
        grid = []

        for r in range(10):
            row = []
            for c in range(10):
                row.append(pygame.Rect(250 + (50 * r), 200 + (52 * c), 50, 50))
                pygame.draw.rect(screen, WHITE, (250 + (50 * r), 200 + (52 * c), 50, 50))
            grid.append(row)

        # Vertical and Horizontal lines
        for i in range(11):
            pygame.draw.line(screen, BLACK, (250, 200 + (i * 52)), (screen_W - 250, 200 + (i * 52)), 5)
            pygame.draw.line(screen, BLACK, (250 + (i * 50), 200), (250 + (i * 50), screen_H - 80), 5)

        screen.blit(playerImage_battleship, battleship_rect)

        screen.blit(playerImage_aircraft_carrier, aircraft_carrier_rect)

        screen.blit(playerImage_destroyer, destroyer_rect)

        screen.blit(playerImage_submarine, submarine_rect)

        screen.blit(playerImage_small_ship, small_ship_rect)

        for event in pygame.event.get():  # check for any events (i.e key press, mouse click etc.)
            if event.type == pygame.QUIT:  # check to see if it was "x" at top right of screen
                main = False
                intro = False
                rules = False
                leaderboard = False
                settings = False
                play_menu = False
                instructions1 = False
                instructions2 = False
                instructions2_difficulty = False
                game_setup = False
                game_setup2 = False
                game_AI = False
                game_AI_p1 = False
                game_AI_p2 = False
                game_PVP = False
                game_PVP_p1 = False
                game_PVP_p2 = False
                final = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    # Battleship
                    if battleship_rect.collidepoint(pos):
                        rect_dragging = True
                        offset_x = battleship_rect.x - mouse_x
                        offset_y = battleship_rect.y - mouse_y
                    # Aircraft Carrier
                    elif aircraft_carrier_rect.collidepoint(pos):
                        rect_dragging = True
                        offset_x = aircraft_carrier_rect.x - mouse_x
                        offset_y = aircraft_carrier_rect.y - mouse_y
                    # Destroyer
                    elif destroyer_rect.collidepoint(pos):
                        rect_dragging = True
                        offset_x = destroyer_rect.x - mouse_x
                        offset_y = destroyer_rect.y - mouse_y
                    # Submarine
                    elif submarine_rect.collidepoint(pos):
                        rect_dragging = True
                        offset_x = submarine_rect.x - mouse_x
                        offset_y = submarine_rect.y - mouse_y
                    # Small ship
                    elif small_ship_rect.collidepoint(pos):
                        rect_dragging = True
                        offset_x = small_ship_rect.x - mouse_x
                        offset_y = small_ship_rect.y - mouse_y
            elif event.type == pygame.MOUSEBUTTONUP:
                if textRect1.collidepoint(pos):
                    game_setup2 = False
                    game_PVP = True
                    game_PVP_p1 = True
                    game_PVP_p2 = True
                if event.button == 1:
                    if 250 <= battleship_rect.x <= 600 and 200 <= battleship_rect.y <= 700:
                        battleship_on_grid = True
                    else:
                        battleship_on_grid = False

                    if 250 <= aircraft_carrier_rect.x <= 550 and 200 <= aircraft_carrier_rect.y <= 700:
                        aircraft_carrier_on_grid = True
                    else:
                        aircraft_carrier_on_grid = False

                    if 250 <= destroyer_rect.x <= 650 and 200 <= destroyer_rect.y <= 700:
                        destroyer_on_grid = True
                    else:
                        destroyer_on_grid = False

                    if 250 <= submarine_rect.x <= 700 and 200 <= submarine_rect.y <= 700:
                        submarine_on_grid = True
                    else:
                        submarine_on_grid = False

                    if 250 <= small_ship_rect.x <= 750 and 200 <= small_ship_rect.y <= 700:
                        small_ship_on_grid = True
                    else:
                        small_ship_on_grid = False

                    rect_dragging = False


                    # to find the closest but smallest row
                    def find_nearest_row(ship_rect_x):
                        for i in nearest_row:
                            if i <= ship_rect_x < i + 50:
                                return i
                            else:
                                i += 50


                    # to find the closest but smallest col
                    def find_nearest_col(ship_rect_y):

                        for i in nearest_col:
                            if i <= ship_rect_y < i + 52:
                                return i
                            else:
                                i += 52


                    # if it in on the grids, use rect collision and put ship locations into array
                    def check_for_ship(ship_rect):
                        ship_coordinates = []
                        for row in range(10):
                            for col in range(10):
                                if pygame.Rect.colliderect(grid[row][col], ship_rect):
                                    ship_coordinates.append([row, col])
                        return ship_coordinates


                    # this is to snap the ships to the grid
                    if battleship_on_grid:
                        battleship_rect.x = find_nearest_row(battleship_rect.x)
                        battleship_rect.y = find_nearest_col(battleship_rect.y)
                        battleship_player2 = check_for_ship(battleship_rect)
                        battleship_on_grid = False

                    if aircraft_carrier_on_grid:
                        aircraft_carrier_rect.x = find_nearest_row(aircraft_carrier_rect.x)
                        aircraft_carrier_rect.y = find_nearest_col(aircraft_carrier_rect.y)
                        aircraft_carrier_player2 = check_for_ship(aircraft_carrier_rect)
                        aircraft_carrier_on_grid = False

                    if destroyer_on_grid:
                        destroyer_rect.x = find_nearest_row(destroyer_rect.x)
                        destroyer_rect.y = find_nearest_col(destroyer_rect.y)
                        destroyer_player2 = check_for_ship(destroyer_rect)
                        destroyer_on_grid = False

                    if submarine_on_grid:
                        submarine_rect.x = find_nearest_row(submarine_rect.x)
                        submarine_rect.y = find_nearest_col(submarine_rect.y)
                        submarine_player2 = check_for_ship(submarine_rect)
                        submarine_on_grid = False

                    if small_ship_on_grid:
                        small_ship_rect.x = find_nearest_row(small_ship_rect.x)
                        small_ship_rect.y = find_nearest_col(small_ship_rect.y)
                        small_ship_player2 = check_for_ship(small_ship_rect)
                        small_ship_on_grid = False





            elif event.type == pygame.MOUSEMOTION and rect_dragging:
                def ship_mouse_motion(ship_rect):
                    ship_rect.x = mouse_x + offset_x
                    ship_rect.y = mouse_y + offset_y


                # Battleship
                if battleship_rect.collidepoint(pos):
                    ship_mouse_motion(battleship_rect)
                # Aircraft Carrier
                elif aircraft_carrier_rect.collidepoint(pos):
                    ship_mouse_motion(aircraft_carrier_rect)
                # Destroyer
                elif destroyer_rect.collidepoint(pos):
                    ship_mouse_motion(destroyer_rect)
                # Submarine
                elif submarine_rect.collidepoint(pos):
                    ship_mouse_motion(submarine_rect)
                # Small ship
                elif small_ship_rect.collidepoint(pos):
                    ship_mouse_motion(small_ship_rect)


        def ship_borders(ship_rect):
            if ship_rect.x < 0:
                ship_rect.x = 0
            elif ship_rect.x >= screen_W - 200:
                ship_rect.x = screen_W - 200
            elif ship_rect.y < 0:
                ship_rect.y = 0
            elif ship_rect.y >= screen_H - 50:
                ship_rect.y = screen_H - 50


        ship_borders(battleship_rect)
        ship_borders(aircraft_carrier_rect)
        ship_borders(destroyer_rect)
        ship_borders(submarine_rect)
        ship_borders(small_ship_rect)

        pygame.display.flip()

    plane_rect = plane.get_rect()
    plane_pos = 0

    shooting = False
    shooting_grid = 0
    shooting_circle_size = 10


    # Puts all player 1 ships and player 2 ships in 2 arrays
    def totalships_player1(ships):
        if len(ships) != 0:
            for x in ships:
                all_player1_ships.append(x)


    totalships_player1(battleship_player1)
    totalships_player1(aircraft_carrier_player1)
    totalships_player1(destroyer_player1)
    totalships_player1(submarine_player1)
    totalships_player1(small_ship_player1)


    def totalships_player2(ships):
        if len(ships) != 0:
            for x in ships:
                all_player2_ships.append(x)


    totalships_player2(battleship_player2)
    totalships_player2(aircraft_carrier_player2)
    totalships_player2(destroyer_player2)
    totalships_player2(submarine_player2)
    totalships_player2(small_ship_player2)

    ship_hit = False
    ship_miss = False
    start = 0
    player1_scene = True
    while game_PVP:
        pygame.mouse.set_cursor(pygame.cursors.broken_x)
        #To indicate that it is player 1's turn
        while player1_scene:
            pos = pygame.mouse.get_pos()
            screen.fill(LIGHT_BLUE)
            font_title = pygame.font.SysFont("arial", 60)
            font_playmenu = pygame.font.SysFont("arial", 40)
            title_text = font_title.render("Player 1's turn", True, BLACK)
            play_text = font_playmenu.render("Ok", True, BLACK)


            textRect1 = title_text.get_rect()
            textRect1.center = (screen_W / 2, screen_H - screen_H / 1.5)
            screen.blit(title_text, textRect1)

            textRect2 = play_text.get_rect()
            textRect2.center = (screen_W / 2, screen_H - screen_H / 2)
            screen.blit(play_text, textRect2)


            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    main = False
                    intro = False
                    rules = False
                    leaderboard = False
                    settings = False
                    play_menu = False
                    player1_scene = False
                    instructions1 = False
                    instructions2 = False
                    instructions2_difficulty = False
                    game_setup = False
                    game_setup2 = False
                    game_AI = False
                    game_AI_p1 = False
                    game_AI_p2 = False
                    game_PVP = False
                    game_PVP_p1 = False
                    game_PVP_p2 = False
                    final = False

                if event.type == pygame.MOUSEBUTTONUP:
                    if textRect2.collidepoint(pos):
                        player1_scene = False
                        game_PVP_p1 = True
                        button_sound.play()

        while game_PVP_p1:
            screen.fill(LIGHT_BLUE)
            pos = pygame.mouse.get_pos()
            font_score = pygame.font.SysFont("arial", 50)
            font_level = pygame.font.SysFont("arial", 25)
            font_pause = pygame.font.SysFont("arial", 30)
            font_hit_or_miss = pygame.font.SysFont("arial", 40)
            pause = font_pause.render("Game Paused", True, BLACK)
            player1_turn = font_score.render("Player 1's turn", True, BLACK)

            your_ships = font_level.render("Your Ships", True, BLACK)
            enemy_ships = font_level.render("Enemy Ships", True, BLACK)

            miss = font_hit_or_miss.render("MISS!", True, BLACK)
            hit = font_hit_or_miss.render("HIT!", True, BLACK)

            textRect1 = your_ships.get_rect()
            textRect1.center = (screen_W / 4, screen_H / 5)
            screen.blit(your_ships, textRect1)

            textRect2 = your_ships.get_rect()
            textRect2.center = (screen_W / 1.35, screen_H / 5)
            screen.blit(enemy_ships, textRect2)

            textRect3 = your_ships.get_rect()
            textRect3.center = (screen_W / 1.95, screen_H / 6)

            textRect4 = your_ships.get_rect()
            textRect4.center = (screen_W / 1.9, screen_H / 6)

            textRect5 = player1_turn.get_rect()
            textRect5.center = (screen_W / 2, screen_H / 10)
            screen.blit(player1_turn, textRect5)

            destroyed_ships_p1 = 0

            # Left side

            for row in range(10):
                for col in range(10):
                    # pygame.draw.rect(screen, WHITE, (50 + (40 * row), 200 + (42 * col), 50, 50))
                    pygame.draw.rect(screen, WHITE, (52 + (40 * row), 198 + (40 * col), 45, 45))


            # check to see if all the grids of a ship are hit
            def check_ship_destroyed(player_ship):
                grids_hit_player1 = 0
                for rect in player1_clicked_grids:
                    for x in range(len(player_ship)):
                        if rect.x == 552 + (40 * player_ship[x][0]) and rect.y == 198 + (40 * player_ship[x][1]):
                            grids_hit_player1 += 1
                #if grids hit = the number of grids that ship has, return true
                if player_ship == battleship_player2 and grids_hit_player1 == 4:
                    return True
                elif player_ship == aircraft_carrier_player2 and grids_hit_player1 == 5:
                    return True
                elif player_ship == destroyer_player2 and grids_hit_player1 == 3:
                    return True
                elif player_ship == submarine_player2 and grids_hit_player1 == 2:
                    return True
                elif player_ship == small_ship_player2 and grids_hit_player1 == 1:
                    return True
                return False


            def display_ship_destroyed(player_ship):
                global destroyed_ships_p1
                if check_ship_destroyed(player_ship):
                    #if true, ship destroyed
                    destroyed_ships_p1 += 1
                    #display black for grids of that ship
                    for row1 in range(len(player_ship)):
                        pygame.draw.rect(screen, BLACK, (
                            552 + (40 * player_ship[row1][0]), 198 + (40 * player_ship[row1][1]), 45, 45))


            # Right side

            right_side_rects = []
            grids_hit_player1 = 0
            for row in range(10):
                for col in range(10):
                    already_clicked = False
                    #creates white grids
                    new_rect = pygame.draw.rect(screen, WHITE, (552 + (40 * row), 198 + (40 * col), 45, 45))
                    for rect in player1_clicked_grids:
                        if rect.x == 552 + (40 * row) and rect.y == 198 + (40 * col):
                            #if clicked, color them green
                            pygame.draw.rect(screen, GREEN, (552 + (40 * row), 198 + (40 * col), 45, 45))
                            already_clicked = True
                            for row1 in range(len(all_player2_ships)):
                                #if clicked and hits a ship, color them red
                                if rect.x == 552 + (40 * all_player2_ships[row1][0]) and rect.y == 198 + (
                                        40 * all_player2_ships[row1][1]):
                                    grids_hit_player1 += 1
                                    pygame.draw.rect(screen, RED, (552 + (40 * row), 198 + (40 * col), 45, 45))
                    display_ship_destroyed(
                        battleship_player2)  # checks to see if a ship is destroyed, if so, color in black
                    display_ship_destroyed(aircraft_carrier_player2)
                    display_ship_destroyed(destroyer_player2)
                    display_ship_destroyed(submarine_player2)
                    display_ship_destroyed(small_ship_player2)

                    if not already_clicked:
                        right_side_rects.append(new_rect)

            if grids_hit_player1 >= len(all_player2_ships):  # Player 1 wins
                winner = 0
                game_PVP_p1 = False
                player2_scene = False
                game_PVP_p2 = False
                game_PVP = False
                final = True


            #If player hits a ship, he/she get another shot
            #if player misses a ship, it becomes the other player's turn
            if ship_hit:
                screen.blit(hit, textRect4)
                elapsedTime = int(time.perf_counter() - start)
                if elapsedTime >= 1:
                    screen.fill(LIGHT_BLUE, (screen_W / 2, screen_H / 6, 50, 50))
                    ship_hit = False
                    ship_miss = False

            elif ship_miss:
                screen.blit(miss, textRect3)
                elapsedTime = int(time.perf_counter() - start)
                if elapsedTime >= 1:
                    screen.fill(LIGHT_BLUE, (screen_W / 2, screen_H / 6, 50, 50))
                    ship_miss = False
                    # Now we go over to the second player because the player missed
                    game_PVP_p1 = False
                    game_PVP_p2 = True
                    player2_scene = True


            # Display ships
            def display_ship_1(player_ship):
                for ship in player_ship:
                    pygame.draw.rect(screen, BLUE, (52 + (40 * ship[0]), 198 + (40 * ship[1]), 44, 45))
                for rect in player2_clicked_grids:
                    pygame.draw.rect(screen, GREEN,
                                     (52 + (40 * ((rect.x - 552) / 40)), 198 + (40 * ((rect.y - 198) / 40)), 45, 45))
                    for x in range(len(all_player1_ships)):
                        if (rect.x - 552) / 40 == all_player1_ships[x][0] and (rect.y - 198) / 40 == \
                                all_player1_ships[x][1]:
                            pygame.draw.rect(screen, RED, (
                                52 + (40 * ((rect.x - 552) / 40)), 198 + (40 * ((rect.y - 198) / 40)), 45, 45))


            display_ship_1(battleship_player1)
            display_ship_1(aircraft_carrier_player1)
            display_ship_1(destroyer_player1)
            display_ship_1(submarine_player1)
            display_ship_1(small_ship_player1)

            #if player cursor hovers over a rect, color it yellow
            for rect in right_side_rects:
                if rect.collidepoint(pos):
                    pygame.draw.rect(screen, YELLOW, (rect.x, rect.y, 45, 45))

            # Vertical and Horizontal lines
            for i in range(11):
                pygame.draw.line(screen, BLACK, (50, 200 + (i * 40)), (screen_W - 540, 200 + (i * 40)),
                                 5)  # horizontal lines
                pygame.draw.line(screen, BLACK, (50 + (i * 40.8), 200), (50 + (i * 40.8), screen_H - 200),
                                 5)  # vertical

            #Vertical and Horizontal lines for the right side
            for i in range(11):
                pygame.draw.line(screen, BLACK, (550, 200 + (i * 40)), (screen_W - 40, 200 + (i * 40)),
                                 5)  # horizontal lines
                pygame.draw.line(screen, BLACK, (550 + (i * 40.8), 200), (550 + (i * 40.8), screen_H - 200),
                                 5)  # vertical
            # print(destroyed_ships_p1)
            if shooting:
                #checks to see how many ships destroyed and speeds up the plane accordingly
                for i in range(1, 6):
                    if i == destroyed_ships_p1 / 100:
                        plane_pos += 5 + (2 * i)
                else:
                    plane_pos += 5
                plane_rect.center = (plane_pos, shooting_grid.y + 15)
                screen.blit(plane, plane_rect)
                #If plane has reached the selected grid, drop a "bomb"
                if plane_pos >= shooting_grid.x:
                    pygame.draw.circle(screen, BLACK, (shooting_grid.x + 23, shooting_grid.y + 23),
                                       shooting_circle_size, 0)
                    shooting_circle_size -= 0.1

                #If plane is out of view, depending on if it is a hit or miss, play an explosion or a splash
                if plane_pos > 1500:

                    plane_pos = 0
                    shooting_circle_size = 10
                    shooting = False
                    player1_clicked_grids.append(shooting_grid)
                    ship_hit = False
                    for row in range(len(all_player2_ships)):
                        if shooting_grid.x == 552 + (40 * all_player2_ships[row][0]) and shooting_grid.y == 198 + (
                                40 * all_player2_ships[row][1]):
                            ship_hit = True
                            explosion_sound.play()
                            start = time.perf_counter()
                    if ship_hit is False:
                        ship_miss = True
                        splash_sound.play()
                        start = time.perf_counter()

                # pygame.time.delay()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    main = False
                    intro = False
                    rules = False
                    leaderboard = False
                    settings = False
                    play_menu = False
                    instructions1 = False
                    instructions2 = False
                    instructions2_difficulty = False
                    game_setup = False
                    game_setup2 = False
                    game_AI = False
                    game_AI_p1 = False
                    game_AI_p2 = False
                    game_PVP = False
                    game_PVP_p1 = False
                    game_PVP_p2 = False
                    final = False

                #If mouse clicks on a grid
                if event.type == pygame.MOUSEBUTTONUP:
                    for rect in right_side_rects:
                        if rect.collidepoint(pos):
                            shooting = True
                            shooting_grid = rect
                            plane_sound.play()

        while player2_scene:
            #To indicate it is player 2's turn
            pos = pygame.mouse.get_pos()
            screen.fill(LIGHT_BLUE)
            font_title = pygame.font.SysFont("arial", 60)
            font_playmenu = pygame.font.SysFont("arial", 40)
            title_text = font_title.render("Player 2's turn", True, BLACK)
            play_text = font_playmenu.render("Ok", True, BLACK)


            textRect1 = title_text.get_rect()
            textRect1.center = (screen_W / 2, screen_H - screen_H / 1.5)
            screen.blit(title_text, textRect1)

            textRect2 = play_text.get_rect()
            textRect2.center = (screen_W / 2, screen_H - screen_H / 2)
            screen.blit(play_text, textRect2)


            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    main = False
                    intro = False
                    rules = False
                    leaderboard = False
                    settings = False
                    play_menu = False
                    player2_scene = False
                    instructions1 = False
                    instructions2 = False
                    instructions2_difficulty = False
                    game_setup = False
                    game_setup2 = False
                    game_AI = False
                    game_AI_p1 = False
                    game_AI_p2 = False
                    game_PVP = False
                    game_PVP_p1 = False
                    game_PVP_p2 = False
                    final = False

                if event.type == pygame.MOUSEBUTTONUP:
                    if textRect2.collidepoint(pos):
                        player2_scene = False
                        game_PVP_p2 = True
                        button_sound.play()

        ship_hit = False
        ship_miss = False
        start = 0
        #Reference to comments above
        while game_PVP_p2:
            screen.fill(LIGHT_BLUE)
            pos = pygame.mouse.get_pos()
            font_score = pygame.font.SysFont("arial", 50)
            font_level = pygame.font.SysFont("arial", 25)
            font_pause = pygame.font.SysFont("arial", 30)
            font_hit_or_miss = pygame.font.SysFont("arial", 40)
            pause = font_pause.render("Game Paused", True, BLACK)
            player2_turn = font_score.render("Player 2's turn", True, BLACK)

            your_ships = font_level.render("Your Ships", True, BLACK)
            enemy_ships = font_level.render("Enemy Ships", True, BLACK)

            miss = font_hit_or_miss.render("MISS!", True, BLACK)
            hit = font_hit_or_miss.render("HIT!", True, BLACK)

            textRect1 = your_ships.get_rect()
            textRect1.center = (screen_W / 4, screen_H / 5)
            screen.blit(your_ships, textRect1)

            textRect2 = your_ships.get_rect()
            textRect2.center = (screen_W / 1.35, screen_H / 5)
            screen.blit(enemy_ships, textRect2)

            textRect3 = your_ships.get_rect()
            textRect3.center = (screen_W / 1.95, screen_H / 6)

            textRect4 = your_ships.get_rect()
            textRect4.center = (screen_W / 1.9, screen_H / 6)

            textRect5 = player2_turn.get_rect()
            textRect5.center = (screen_W / 2, screen_H / 10)
            screen.blit(player2_turn, textRect5)

            # Left side

            for row in range(10):
                for col in range(10):
                    pygame.draw.rect(screen, WHITE, (52 + (40 * row), 198 + (40 * col), 45, 45))


            def check_ship_destroyed(player_ship):
                grids_hit_player2 = 0
                for rect in player2_clicked_grids:
                    for x in range(len(player_ship)):
                        if rect.x == 552 + (40 * player_ship[x][0]) and rect.y == 198 + (40 * player_ship[x][1]):
                            grids_hit_player2 += 1
                if player_ship == battleship_player1 and grids_hit_player2 == 4:
                    return True
                elif player_ship == aircraft_carrier_player1 and grids_hit_player2 == 5:
                    return True
                elif player_ship == destroyer_player1 and grids_hit_player2 == 3:
                    return True
                elif player_ship == submarine_player1 and grids_hit_player2 == 2:
                    return True
                elif player_ship == small_ship_player1 and grids_hit_player2 == 1:
                    return True
                return False


            destroyed_ships_p2 = 0


            def display_ship_destroyed(player_ship):
                global destroyed_ships_p2
                if check_ship_destroyed(player_ship):
                    destroyed_ships_p2 += 1
                    for row1 in range(len(player_ship)):
                        pygame.draw.rect(screen, BLACK, (
                            552 + (40 * player_ship[row1][0]), 198 + (40 * player_ship[row1][1]), 45, 45))


            # Right side

            right_side_rects = []
            grids_hit_player2 = 0
            for row in range(10):
                for col in range(10):
                    already_clicked = False
                    new_rect = pygame.draw.rect(screen, WHITE, (552 + (40 * row), 198 + (40 * col), 45, 45))
                    for rect in player2_clicked_grids:
                        if rect.x == 552 + (40 * row) and rect.y == 198 + (40 * col):
                            pygame.draw.rect(screen, GREEN, (552 + (40 * row), 198 + (40 * col), 45, 45))
                            already_clicked = True
                            for row1 in range(len(all_player1_ships)):
                                if rect.x == 552 + (40 * all_player1_ships[row1][0]) and rect.y == 198 + (
                                        40 * all_player1_ships[row1][1]):
                                    grids_hit_player2 += 1
                                    pygame.draw.rect(screen, RED, (552 + (40 * row), 198 + (40 * col), 45, 45))
                    display_ship_destroyed(
                        battleship_player1)  # checks to see if a ship is destroyed, if so, color in black
                    display_ship_destroyed(aircraft_carrier_player1)
                    display_ship_destroyed(destroyer_player1)
                    display_ship_destroyed(submarine_player1)
                    display_ship_destroyed(small_ship_player1)
                    if not already_clicked:
                        right_side_rects.append(new_rect)

            if grids_hit_player2 >= len(all_player1_ships):  # Player 2 wins
                winner = 1
                game_PVP_p1 = False
                game_PVP_p2 = False
                game_PVP = False
                player1_scene = False
                final = True

            if ship_hit: #Ship hit
                screen.blit(hit, textRect4)
                elapsedTime = int(time.perf_counter() - start)
                if elapsedTime >= 1:
                    screen.fill(LIGHT_BLUE, (screen_W / 2, screen_H / 6, 50, 50))
                    ship_hit = False
                    ship_miss = False


            elif ship_miss:# Ship missed
                screen.blit(miss, textRect3)
                elapsedTime = int(time.perf_counter() - start)
                if elapsedTime >= 1:
                    screen.fill(LIGHT_BLUE, (screen_W / 2, screen_H / 6, 50, 50))
                    ship_miss = False
                    # Now we go over to the first player because the player missed
                    game_PVP_p2 = False
                    player1_scene = True
                    game_PVP_p1 = True


            # Display ships for the left side
            def display_ship_2(player_ship):
                for ship in player_ship:
                    pygame.draw.rect(screen, BLUE, (52 + (40 * ship[0]), 198 + (40 * ship[1]), 44, 45))
                for rect in player1_clicked_grids: #If player2 fires at a grid, color it green
                    pygame.draw.rect(screen, GREEN,
                                     (52 + (40 * ((rect.x - 552) / 40)), 198 + (40 * ((rect.y - 198) / 40)), 45, 45))
                    for x in range(len(all_player2_ships)):
                        #if player2 fires and hits a ship at a grid, color it red
                        if (rect.x - 552) / 40 == all_player2_ships[x][0] and (rect.y - 198) / 40 == \
                                all_player2_ships[x][1]:
                            pygame.draw.rect(screen, RED, (
                            52 + (40 * ((rect.x - 552) / 40)), 198 + (40 * ((rect.y - 198) / 40)), 45, 45))


            display_ship_2(battleship_player2)
            display_ship_2(aircraft_carrier_player2)
            display_ship_2(destroyer_player2)
            display_ship_2(submarine_player2)
            display_ship_2(small_ship_player2)

            #if cursor is on a rect, color it yellow
            for rect in right_side_rects:
                if rect.collidepoint(pos):
                    pygame.draw.rect(screen, YELLOW, (rect.x, rect.y, 45, 45))

            # Vertical and Horizontal lines
            for i in range(11):
                pygame.draw.line(screen, BLACK, (50, 200 + (i * 40)), (screen_W - 540, 200 + (i * 40)),
                                 5)  # horizontal lines
                pygame.draw.line(screen, BLACK, (50 + (i * 40.8), 200), (50 + (i * 40.8), screen_H - 200),
                                 5)  # vertical
            # Vertical and Horizontal lines for the right grids
            for i in range(11):
                pygame.draw.line(screen, BLACK, (550, 200 + (i * 40)), (screen_W - 40, 200 + (i * 40)),
                                 5)  # horizontal lines
                pygame.draw.line(screen, BLACK, (550 + (i * 40.8), 200), (550 + (i * 40.8), screen_H - 200),
                                 5)  # vertical

            #If need be, reference from the earlier comments above
            if shooting:
                for i in range(1, 6):
                    if i == destroyed_ships_p2 / 100:
                        plane_pos += 5 + (2 * i)
                else:
                    plane_pos += 5
                plane_rect.center = (plane_pos, shooting_grid.y + 15)
                screen.blit(plane, plane_rect)
                if plane_pos >= shooting_grid.x:
                    pygame.draw.circle(screen, BLACK, (shooting_grid.x + 23, shooting_grid.y + 23),
                                       shooting_circle_size, 0)
                    shooting_circle_size -= 0.1
                if plane_pos > 1500:

                    plane_pos = 0
                    shooting_circle_size = 10
                    shooting = False
                    player2_clicked_grids.append(shooting_grid)
                    ship_hit = False
                    for row in range(len(all_player1_ships)):
                        if shooting_grid.x == 552 + (40 * all_player1_ships[row][0]) and shooting_grid.y == 198 + (
                                40 * all_player1_ships[row][1]):
                            ship_hit = True
                            explosion_sound.play()
                            start = time.perf_counter()
                    if ship_hit is False:
                        ship_miss = True
                        splash_sound.play()
                        start = time.perf_counter()

                # pygame.time.delay()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    main = False
                    intro = False
                    rules = False
                    leaderboard = False
                    settings = False
                    play_menu = False
                    instructions1 = False
                    instructions2 = False
                    instructions2_difficulty = False
                    game_setup = False
                    game_setup2 = False
                    game_AI = False
                    game_AI_p1 = False
                    game_AI_p2 = False
                    game_PVP = False
                    game_PVP_p1 = False
                    game_PVP_p2 = False
                    final = False

                if event.type == pygame.MOUSEBUTTONUP:
                    for rect in right_side_rects:
                        if rect.collidepoint(pos):
                            shooting = True
                            shooting_grid = rect
                            plane_sound.play()

    #Reference to comments above
    #PvAI
    while game_AI:
        pygame.mouse.set_cursor(pygame.cursors.broken_x)
        ship_hit = False
        ship_miss = False
        start = 0
        #Player 1
        while game_AI_p1:
            screen.fill(LIGHT_BLUE)
            pos = pygame.mouse.get_pos()
            font_score = pygame.font.SysFont("arial", 50)
            font_level = pygame.font.SysFont("arial", 25)
            font_pause = pygame.font.SysFont("arial", 30)
            font_hit_or_miss = pygame.font.SysFont("arial", 40)
            pause = font_pause.render("Game Paused", True, BLACK)
            player1_turn = font_score.render("Player 1's turn", True, BLACK)

            your_ships = font_level.render("Player 1's Ships", True, BLACK)
            enemy_ships = font_level.render("Computer's Ships", True, BLACK)

            miss = font_hit_or_miss.render("MISS!", True, BLACK)
            hit = font_hit_or_miss.render("HIT!", True, BLACK)

            textRect1 = your_ships.get_rect()
            textRect1.center = (screen_W / 4, screen_H / 5)
            screen.blit(your_ships, textRect1)

            textRect2 = your_ships.get_rect()
            textRect2.center = (screen_W / 1.35, screen_H / 5)
            screen.blit(enemy_ships, textRect2)

            textRect3 = your_ships.get_rect()
            textRect3.center = (screen_W / 1.85, screen_H / 6)

            textRect4 = your_ships.get_rect()
            textRect4.center = (screen_W / 1.8, screen_H / 6)

            textRect5 = player1_turn.get_rect()
            textRect5.center = (screen_W / 2, screen_H / 10)
            screen.blit(player1_turn, textRect5)



            # check to see if all the grids of a ship are hit
            def check_ship_destroyed(player_ship):
                grids_hit = 0
                for rect in player1_clicked_grids:
                    for x in range(len(player_ship)):
                        if rect.x == 552 + (40 * player_ship[x][0]) and rect.y == 198 + (40 * player_ship[x][1]):
                            grids_hit += 1

                if player_ship == battleship_player2 and grids_hit == 4:
                    return True
                elif player_ship == aircraft_carrier_player2 and grids_hit == 5:
                    return True
                elif player_ship == destroyer_player2 and grids_hit == 3:
                    return True
                elif player_ship == submarine_player2 and grids_hit == 2:
                    return True
                elif player_ship == small_ship_player2 and grids_hit == 1:
                    return True
                return False


            destroyed_ships_p1 = 0
            def display_ship_destroyed(player_ship):
                global destroyed_ships_p1
                if check_ship_destroyed(player_ship):
                    destroyed_ships_p1 += 1
                    for row1 in range(len(player_ship)):
                        pygame.draw.rect(screen, BLACK, (
                            552 + (40 * player_ship[row1][0]), 198 + (40 * player_ship[row1][1]), 45, 45))

            # Right side

            right_side_rects = []
            grids_hit_player1 = 0
            for row in range(10):
                for col in range(10):
                    already_clicked = False
                    new_rect = pygame.draw.rect(screen, WHITE, (552 + (40 * row), 198 + (40 * col), 45, 45))
                    for rect in player1_clicked_grids:
                        if rect.x == 552 + (40 * row) and rect.y == 198 + (40 * col):
                            pygame.draw.rect(screen, GREEN, (552 + (40 * row), 198 + (40 * col), 45, 45))
                            already_clicked = True
                            for row1 in range(len(all_player2_ships)):
                                if rect.x == 552 + (40 * all_player2_ships[row1][0]) and rect.y == 198 + (
                                        40 * all_player2_ships[row1][1]):
                                    grids_hit_player1 += 1
                                    pygame.draw.rect(screen, RED, (552 + (40 * row), 198 + (40 * col), 45, 45))
                    display_ship_destroyed(
                        battleship_player2)  # checks to see if a ship is destroyed, if so, color in black
                    display_ship_destroyed(aircraft_carrier_player2)
                    display_ship_destroyed(destroyer_player2)
                    display_ship_destroyed(submarine_player2)
                    display_ship_destroyed(small_ship_player2)

                    if not already_clicked:
                        right_side_rects.append(new_rect)

            # Left side
            for row in range(10):
                for col in range(10):

                    already_clicked = False
                    new_rect = pygame.draw.rect(screen, WHITE, (50 + (40 * row), 198 + (40 * col), 45, 45))
                    for rect in player2_clicked_grids:
                        if rect.x == (50 + (40 * row)) and rect.y == (198 + (40 * col)):
                            pygame.draw.rect(screen, GREEN, (rect.x, rect.y, 45, 45))
                            already_clicked = True
                            for x in range(len(all_player1_ships)):
                                if rect.x == 50 + (40 * all_player1_ships[x][0]) and rect.y == 198 + (
                                        40 * all_player1_ships[x][1]):
                                    pygame.draw.rect(screen, RED, (rect.x, rect.y, 45, 45))


            if grids_hit_player1 >= len(all_player2_ships):  # Player 1 wins
                winner = 0
                game_AI_p1 = False
                game_AI_p2 = False
                game_AI = False
                final = True

            if ship_hit: #ship hit
                screen.blit(hit, textRect4)
                elapsedTime = int(time.perf_counter() - start)
                if elapsedTime >= 1:
                    screen.fill(LIGHT_BLUE, (screen_W / 2, screen_H / 6, 50, 50))
                    ship_hit = False
                    ship_miss = False

            elif ship_miss: #ship miss
                screen.blit(miss, textRect3)
                elapsedTime = int(time.perf_counter() - start)
                if elapsedTime >= 1:
                    screen.fill(LIGHT_BLUE, (screen_W / 2, screen_H / 6, 50, 50))
                    ship_miss = False
                    # Now we go over to the second player because the player missed
                    game_AI_p1 = False
                    game_AI_p2 = True
                    plane_pos = 1000
                    plane_rect = plane_2.get_rect()

            # Display ships
            def display_ship_1(player_ship):
                for ship in player_ship:
                    #If there is a ship, color the grids blue
                    pygame.draw.rect(screen, BLUE, (52 + (40 * ship[0]), 198 + (40 * ship[1]), 45, 45))
                for rect in player2_clicked_grids:
                    #If enemy fires at a grid, color it green
                    pygame.draw.rect(screen, GREEN, (rect.x, rect.y, 45, 45))
                    for x in range(len(all_player1_ships)):
                        #If it hits a ship, color it red
                        if rect.x == 50 + (40 * all_player1_ships[x][0]) and rect.y == 198 + (
                                40 * all_player1_ships[x][1]):
                            pygame.draw.rect(screen, RED, (rect.x, rect.y, 45, 45))


            display_ship_1(battleship_player1)
            display_ship_1(aircraft_carrier_player1)
            display_ship_1(destroyer_player1)
            display_ship_1(submarine_player1)
            display_ship_1(small_ship_player1)

            #For player 1 only, if cursor is on a rect, color it yellow
            for rect in right_side_rects:
                if rect.collidepoint(pos):
                    pygame.draw.rect(screen, YELLOW, (rect.x, rect.y, 45, 45))

            # Vertical and Horizontal lines
            for i in range(11):
                pygame.draw.line(screen, BLACK, (50, 200 + (i * 40)), (screen_W - 540, 200 + (i * 40)),
                                 5)  # horizontal lines
                pygame.draw.line(screen, BLACK, (50 + (i * 40.8), 200), (50 + (i * 40.8), screen_H - 200),
                                 5)  # vertical

            #For right side
            for i in range(11):
                pygame.draw.line(screen, BLACK, (550, 200 + (i * 40)), (screen_W - 40, 200 + (i * 40)),
                                 5)  # horizontal lines
                pygame.draw.line(screen, BLACK, (550 + (i * 40.8), 200), (550 + (i * 40.8), screen_H - 200),
                                 5)  # vertical

            #Reference code above if need be
            if shooting:
                for i in range(1, 6):
                    if i <= destroyed_ships_p1 / 100 or i <= len(player1_clicked_grids)/10:
                        plane_pos += 5 + (2 * i)
                else:
                    plane_pos += 5
                plane_rect.center = (plane_pos, shooting_grid.y + 15)
                screen.blit(plane, plane_rect)
                if plane_pos >= shooting_grid.x:
                    pygame.draw.circle(screen, BLACK, (shooting_grid.x + 23, shooting_grid.y + 23),
                                       shooting_circle_size, 0)
                    shooting_circle_size -= 0.1
                if plane_pos > 1500:

                    plane_pos = 0
                    shooting_circle_size = 10
                    shooting = False
                    player1_clicked_grids.append(shooting_grid)
                    ship_hit = False
                    for row in range(len(all_player2_ships)):
                        if shooting_grid.x == 552 + (40 * all_player2_ships[row][0]) and shooting_grid.y == 198 + (
                                40 * all_player2_ships[row][1]):
                            ship_hit = True
                            start = time.perf_counter()
                            explosion_sound.play()
                    if ship_hit is False:
                        ship_miss = True
                        splash_sound.play()
                        start = time.perf_counter()

                # pygame.time.delay()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    main = False
                    intro = False
                    rules = False
                    leaderboard = False
                    settings = False
                    play_menu = False
                    instructions1 = False
                    instructions2 = False
                    instructions2_difficulty = False
                    game_setup = False
                    game_setup2 = False
                    game_AI = False
                    game_AI_p1 = False
                    game_AI_p2 = False
                    game_PVP = False
                    game_PVP_p1 = False
                    game_PVP_p2 = False
                    final = False

                if event.type == pygame.MOUSEBUTTONUP:
                    for rect in right_side_rects:
                        if rect.collidepoint(pos):
                            shooting = True
                            shooting_grid = rect
                            plane_sound.play()


        ship_hit = False
        ship_miss = False
        start = 0
        selecting_grid = True
        plane_sound_play = True
        #Computer plays
        while game_AI_p2:
            screen.fill(LIGHT_BLUE)
            pos = pygame.mouse.get_pos()
            font_score = pygame.font.SysFont("arial", 50)
            font_level = pygame.font.SysFont("arial", 25)
            font_pause = pygame.font.SysFont("arial", 30)
            font_hit_or_miss = pygame.font.SysFont("arial", 40)
            pause = font_pause.render("Game Paused", True, BLACK)
            player2_turn = font_score.render("Computer's turn", True, BLACK)

            your_ships = font_level.render("Player 1's Ships", True, BLACK)
            enemy_ships = font_level.render("Computer's Ships", True, BLACK)

            miss = font_hit_or_miss.render("MISS!", True, BLACK)
            hit = font_hit_or_miss.render("HIT!", True, BLACK)

            textRect1 = your_ships.get_rect()
            textRect1.center = (screen_W / 4, screen_H / 5)
            screen.blit(your_ships, textRect1)

            textRect2 = your_ships.get_rect()
            textRect2.center = (screen_W / 1.35, screen_H / 5)
            screen.blit(enemy_ships, textRect2)

            textRect3 = your_ships.get_rect()
            textRect3.center = (screen_W / 1.85, screen_H / 6)

            textRect4 = your_ships.get_rect()
            textRect4.center = (screen_W / 1.8, screen_H / 6)

            textRect5 = player2_turn.get_rect()
            textRect5.center = (screen_W / 2, screen_H / 10)
            screen.blit(player2_turn, textRect5)




            def check_ship_destroyed(player_ship):
                grids_hit = 0
                for rect in player1_clicked_grids:
                    for x in range(len(player_ship)):
                        if rect.x == 552 + (40 * player_ship[x][0]) and rect.y == 198 + (40 * player_ship[x][1]):
                            grids_hit += 1
                if player_ship == battleship_player2 and grids_hit == 4:
                    return True
                elif player_ship == aircraft_carrier_player2 and grids_hit == 5:
                    return True
                elif player_ship == destroyer_player2 and grids_hit == 3:
                    return True
                elif player_ship == submarine_player2 and grids_hit == 2:
                    return True
                elif player_ship == small_ship_player2 and grids_hit == 1:
                    return True
                return False


            destroyed_ships_p1 = 0


            def display_ship_destroyed(player_ship):
                global destroyed_ships_p1
                if check_ship_destroyed(player_ship):
                    destroyed_ships_p1 += 1
                    for row1 in range(len(player_ship)):
                        pygame.draw.rect(screen, BLACK, (
                            552 + (40 * player_ship[row1][0]), 198 + (40 * player_ship[row1][1]), 45, 45))


            # Right side
            right_side_rects = []

            for row in range(10):
                for col in range(10):
                    already_clicked = False
                    new_rect = pygame.draw.rect(screen, WHITE, (552 + (40 * row), 198 + (40 * col), 45, 45))
                    for rect in player1_clicked_grids:
                        if rect.x == 552 + (40 * row) and rect.y == 198 + (40 * col):
                            pygame.draw.rect(screen, GREEN, (552 + (40 * row), 198 + (40 * col), 45, 45))
                            already_clicked = True
                            for row1 in range(len(all_player2_ships)):
                                if rect.x == 552 + (40 * all_player2_ships[row1][0]) and rect.y == 198 + (
                                        40 * all_player2_ships[row1][1]):

                                    pygame.draw.rect(screen, RED, (552 + (40 * row), 198 + (40 * col), 45, 45))
                    display_ship_destroyed(
                        battleship_player2)  # checks to see if a ship is destroyed, if so, color in black
                    display_ship_destroyed(aircraft_carrier_player2)
                    display_ship_destroyed(destroyer_player2)
                    display_ship_destroyed(submarine_player2)
                    display_ship_destroyed(small_ship_player2)


            # Left side
            left_side_rects = []
            grids_hit_player2 = 0
            for row in range(10):
                for col in range(10):

                    already_clicked = False
                    new_rect = pygame.draw.rect(screen, WHITE, (50 + (40 * row), 198 + (40 * col), 45, 45))
                    for rect in player2_clicked_grids:
                        if rect.x == (50 + (40 * row)) and rect.y == (198 + (40 * col)):
                            pygame.draw.rect(screen, GREEN, (rect.x, rect.y, 45, 45))
                            already_clicked = True
                            for x in range(len(all_player1_ships)):
                                if rect.x == 50 + (40 * all_player1_ships[x][0]) and rect.y == 198 + (
                                        40 * all_player1_ships[x][1]):
                                    grids_hit_player2 += 1
                                    pygame.draw.rect(screen, RED, (rect.x, rect.y, 45, 45))
                    if not already_clicked:
                        left_side_rects.append(new_rect)

            #Counts how many grids hit and see if the player wins
            if grids_hit_player2 >= (len(all_player1_ships)):  # Player 2 wins
                winner = 2  # computer wins
                game_AI_p1 = False
                game_AI_p2 = False
                game_AI = False
                final = True

            if ship_hit:
                screen.blit(hit, textRect4)
                elapsedTime = int(time.perf_counter() - start)
                if elapsedTime >= 1:
                    screen.fill(LIGHT_BLUE, (screen_W / 2, screen_H / 6, 50, 50))
                    ship_hit = False
                    ship_miss = False
                    selecting_grid = True



            elif ship_miss:
                screen.blit(miss, textRect3)
                elapsedTime = int(time.perf_counter() - start)
                if elapsedTime >= 1:
                    screen.fill(LIGHT_BLUE, (screen_W / 2, screen_H / 6, 50, 50))
                    ship_miss = False
                    # Now we go over to the first player because the player missed
                    game_AI_p2 = False
                    game_AI_p1 = True
                    plane_rect = plane.get_rect()
                    plane_pos = 0

            #display ships
            def display_ship_1(player_ship):
                for ship in player_ship:
                    pygame.draw.rect(screen, BLUE, (52 + (40 * ship[0]), 198 + (40 * ship[1]), 45, 45))
                for rect in player2_clicked_grids:
                    pygame.draw.rect(screen, GREEN, (rect.x, rect.y, 45, 45))
                    for x in range(len(all_player1_ships)):
                        if rect.x == 50 + (40 * all_player1_ships[x][0]) and rect.y == 198 + (
                                40 * all_player1_ships[x][1]):
                            pygame.draw.rect(screen, RED, (rect.x, rect.y, 45, 45))


            display_ship_1(battleship_player1)
            display_ship_1(aircraft_carrier_player1)
            display_ship_1(destroyer_player1)
            display_ship_1(submarine_player1)
            display_ship_1(small_ship_player1)




            # Vertical and Horizontal lines
            for i in range(11):
                pygame.draw.line(screen, BLACK, (50, 200 + (i * 40)), (screen_W - 540, 200 + (i * 40)),
                                 5)  # horizontal lines
                pygame.draw.line(screen, BLACK, (50 + (i * 40.8), 200), (50 + (i * 40.8), screen_H - 200),
                                 5)  # vertical

            for i in range(11):
                pygame.draw.line(screen, BLACK, (550, 200 + (i * 40)), (screen_W - 40, 200 + (i * 40)),
                                 5)  # horizontal lines
                pygame.draw.line(screen, BLACK, (550 + (i * 40.8), 200), (550 + (i * 40.8), screen_H - 200),
                                 5)  # vertical

            #Computer randomly decides where to fire
            if selecting_grid:
                shooting_grid = random.choice(left_side_rects)
                shooting = True
                selecting_grid = False
            if shooting:
                for i in range(1, 6):
                    if i <= destroyed_ships_p1 / 100 or i <= len(player1_clicked_grids)/10:
                        plane_pos -= 5 + (2 * i)
                else:
                    #Plane flies from the opposite (right) direction
                    plane_pos -= 5
                if plane_sound_play:
                    plane_sound.play()
                    plane_sound_play = False
                plane_rect.center = (plane_pos, shooting_grid.y + 15)
                screen.blit(plane_2, plane_rect)
                if plane_pos <= shooting_grid.x:
                    pygame.draw.circle(screen, BLACK, (shooting_grid.x + 23, shooting_grid.y + 23),
                                       shooting_circle_size, 0)
                    shooting_circle_size -= 0.1
                #reset
                if plane_pos < -500:
                    plane_pos = 1000
                    shooting_circle_size = 10
                    shooting = False
                    ship_hit = False
                    player2_clicked_grids.append(shooting_grid)
                    for row in range(len(all_player1_ships)):
                        if shooting_grid.x == 50 + (40 * all_player1_ships[row][0]) and shooting_grid.y == 198 + (
                                40 * all_player1_ships[row][1]):
                            ship_hit = True
                            start = time.perf_counter()
                            explosion_sound.play()
                    if ship_hit is False:
                        ship_miss = True
                        splash_sound.play()
                        start = time.perf_counter()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    main = False
                    intro = False
                    rules = False
                    leaderboard = False
                    settings = False
                    play_menu = False
                    instructions1 = False
                    instructions2 = False
                    instructions2_difficulty = False
                    game_setup = False
                    game_setup2 = False
                    game_AI = False
                    game_AI_p1 = False
                    game_AI_p2 = False
                    game_PVP = False
                    game_PVP_p1 = False
                    game_PVP_p2 = False
                    final = False


    #Checking for input
    def checkString(name):
        while True:
            try:
                user_name = input(name)
                break
            except TypeError:
                print("Please enter a valid String")
        print("Thank you %s, your score is on the leaderboard when you run the game again." % user_name)
        return user_name


    global writeBoard
    pygame.mouse.set_cursor(pygame.cursors.tri_left)
    #Final screen
    while final:
        pos = pygame.mouse.get_pos()
        screen.fill(LIGHT_BLUE)
        font_final = pygame.font.SysFont("arial", 50)
        secondary = pygame.font.SysFont("arial", 30)
        winner1_text = font_final.render("Player 1 wins!", True, BLACK)
        winner2_text = font_final.render("Player 2 wins!", True, BLACK)
        winner3_text = font_final.render("Computer wins!", True, BLACK)
        play_again = secondary.render("Play again?", True, BLACK)
        yes_text = secondary.render("Yes!", True, BLACK)
        exit_text = secondary.render("Exit", True, BLACK)
        leaderboard_name = secondary.render("Type your name into the console to add your score onto the leaderboard",
                                            True, BLACK)
        leaderboard_message = secondary.render("Click here ", True, BLACK)

        textRect1 = winner1_text.get_rect()
        textRect1.center = (screen_W / 2, screen_H - screen_H / 1.2)

        textRect2 = winner2_text.get_rect()
        textRect2.center = (screen_W / 2, screen_H - screen_H / 1.2)

        textRect3 = play_again.get_rect()
        textRect3.center = (screen_W / 3, screen_H - screen_H / 4)
        screen.blit(play_again, textRect3)

        textRect4 = yes_text.get_rect()
        textRect4.center = (screen_W / 3, screen_H - screen_H / 4)

        textRect5 = exit_text.get_rect()
        textRect5.center = (screen_W / 1.5, screen_H - screen_H / 4)
        screen.blit(exit_text, textRect5)

        textRect6 = winner3_text.get_rect()
        textRect6.center = (screen_W / 2, screen_H - screen_H / 1.2)

        textRect7 = leaderboard_name.get_rect()
        textRect7.center = (screen_W / 2, screen_H - screen_H / 1.5)
        screen.blit(leaderboard_name, textRect7)

        textRect8 = leaderboard_message.get_rect()
        textRect8.center = (screen_W / 2, screen_H - screen_H / 1.7)

        if textRect3.collidepoint(pos):
            screen.fill(LIGHT_BLUE, (screen_W / 4.5, screen_H - screen_H / 3, 200, 150))
            screen.blit(yes_text, textRect4)

        #Display winner
        if winner == 0:
            screen.blit(winner1_text, textRect1)
            screen.blit(leaderboard_message, textRect8)
        elif winner == 1:
            screen.blit(winner2_text, textRect2)
            screen.blit(leaderboard_message, textRect8)
        elif winner == 2:
            screen.blit(winner3_text, textRect6)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False
                intro = False
                rules = False
                leaderboard = False
                settings = False
                play_menu = False
                instructions1 = False
                instructions2 = False
                instructions2_difficulty = False
                game_setup = False
                game_setup2 = False
                game_AI = False
                game_AI_p1 = False
                game_AI_p2 = False
                game_PVP = False
                game_PVP_p1 = False
                game_PVP_p2 = False
                final = False

            if event.type == pygame.MOUSEBUTTONUP:

                if textRect3.collidepoint(pos):
                    play_menu = True
                    final = False

                elif textRect5.collidepoint(pos):
                    main = False
                    intro = False
                    rules = False
                    leaderboard = False
                    settings = False
                    play_menu = False
                    instructions1 = False
                    instructions2 = False
                    instructions2_difficulty = False
                    game_setup = False
                    game_setup2 = False
                    game_AI = False
                    game_AI_p1 = False
                    game_AI_p2 = False
                    game_PVP = False
                    game_PVP_p1 = False
                    game_PVP_p2 = False
                    final = False
                #Open up leaderboard if Player1 or Player 2 wins
                elif textRect8.collidepoint(pos):
                    if winner == 0 or winner == 1:
                        #open file, a+ means to append to the current file
                        writeBoard = open('../FinalProject/FinalProjectLeaderboard.txt', 'a+')
                        main = False
                        intro = False
                        rules = False
                        leaderboard = False
                        settings = False
                        play_menu = False
                        instructions1 = False
                        instructions2 = False
                        instructions2_difficulty = False
                        game_setup = False
                        game_setup2 = False
                        game_AI = False
                        game_AI_p1 = False
                        game_AI_p2 = False
                        game_PVP = False
                        game_PVP_p1 = False
                        game_PVP_p2 = False
                        final = False
                        pygame.quit()
                        print("<-------------------------------------------------------->")
                        name = checkString("Type your name here: ")

                        if winner == 0:
                            writeBoard.write(name + " = " + str(len(player1_clicked_grids)) + "\n")
                        elif winner == 1:
                            writeBoard.write(name + " = " + str(len(player2_clicked_grids)) + "\n")
                        #close file
                        writeBoard.close()
# quit pygame and exit the program (i.e. close everything down)

pygame.quit()
sys.exit()
