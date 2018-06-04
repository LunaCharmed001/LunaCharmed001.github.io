import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
grey = (100, 104, 109)

display_width = 800
display_height  = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slither')

img = pygame.image.load('snakehead2.png')


clock = pygame.time.Clock()

block_size = 20
FPS = 15

direction = "right"

#Used to define the text styles in-game
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

#creates a very basic score counter
def scoreCount(score): #created a score counter
    text = smallfont.render('SCORE: '+ str(score), True, white)
    gameDisplay.blit(text, [0,0])




def game_intro():

    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
   
		#Title screen and directions
        gameDisplay.fill(white)
        message_to_screen("Welcome to Slither",
                          green,
                          -100,
                          "large")
        message_to_screen("The objective of the game is to eat red apples",
                          black,
                          -30)

        message_to_screen("The more apples you eat, the longer you get",
                          black,
                          10)

        message_to_screen("If you run into yourself, crash into a rock, or hit the edges, you die!",
                          black,
                          50)

        message_to_screen("Press C to play or Q to quit.",
                          black,
                          180)
    
        pygame.display.update()
        clock.tick(15)
        
        

#moves the head.
def snake(block_size, snakelist):

    if direction == "right":
        head = pygame.transform.rotate(img, 270)

    if direction == "left":
        head = pygame.transform.rotate(img, 90)

    if direction == "up":
        head = img

    if direction == "down":
        head = pygame.transform.rotate(img, 180)
        
    
    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1],block_size,block_size])

def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)

    
    return textSurface, textSurface.get_rect()
    
#Defines how text will be displayed onscreen
def message_to_screen(msg,color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = (display_width / 2), (display_height / 2)+y_displace
    gameDisplay.blit(textSurf, textRect)

#basically the game loop + the end-game.
def gameLoop():
    global direction
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

	#defines the location of the items with the random import.
    randAppleX = round(random.randrange(0, display_width-block_size))#/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height-block_size))#/10.0)*10.0
    #this adds obstacles in the form of rocks
    rock1X = round(random.randrange(0, display_width-block_size))
    rock1Y = round(random.randrange(0, display_height-block_size))
    
    rock2X = round(random.randrange(0, display_width-block_size))
    rock2Y = round(random.randrange(0, display_height-block_size))

    rock3X = round(random.randrange(0, display_width-block_size))
    rock3Y = round(random.randrange(0, display_height-block_size))
    
	#Basically the game.
    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over",
                              red,
                              y_displace=-50,
                              size="large")
            
            message_to_screen("Press C to play again or Q to quit",
                              black,
                              50,
                              size="medium")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        #keylayout
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0

		#boundries which set the limit at the total height/width of the display.
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True
      

        lead_x += lead_x_change
        lead_y += lead_y_change
        
        gameDisplay.fill(black)

		#Creates the apples and obstacles as well as defining their color, location, and size.
        AppleThickness = 30
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness, AppleThickness])

        RockThickness = 40
        pygame.draw.rect(gameDisplay, grey, [rock1X, rock1Y, RockThickness, RockThickness])
        
        RockThickness2 = 25
        pygame.draw.rect(gameDisplay, grey, [rock2X, rock2Y, RockThickness2, RockThickness2])

        RockThickness3 = 35
        pygame.draw.rect(gameDisplay, grey, [rock3X, rock3Y, RockThickness3, RockThickness3])
        
        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

		#deletes the snakes "trail" so that a body may be added as it grows longer.
        if len(snakeList) > snakeLength:
            del snakeList[0]

        

#        for eachSegment in snakeList[:-1]:
#            if eachSegment == snakeHead:
#                gameOver = True

        #this changes collision detection for more precision, now running into oneself ONLY WHEN VISIBLE will end the game 
        if any(segment == snakeHead for segment in snakeList[:-1]):
            gameOver = True

        
        snake(block_size, snakeList)
		scoreCount(snakeLength - 1) #tells the counter to use the snakes length (which will be equal to the # of apples it eats) minus 1 (1 being the starting length)
        
        pygame.display.update()
        
        

        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:

            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:

                randAppleX = round(random.randrange(0, display_width-block_size))#/10.0)*10.0
                randAppleY = round(random.randrange(0, display_height-block_size))#/10.0)*10.0
                snakeLength += 1
                

            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:

                randAppleX = round(random.randrange(0, display_width-block_size))
                randAppleY = round(random.randrange(0, display_height-block_size))
                snakeLength += 1

        #this is collision detection for rocks (One tedious rock at a time)       
        if lead_x > rock1X and lead_x < rock1X + RockThickness or lead_x + block_size > rock1X and lead_x + block_size < rock1X + RockThickness:

            if lead_y > rock1Y and lead_y < rock1Y + RockThickness:
                gameOver = True

            elif lead_y + block_size > rock1Y and lead_y + block_size < rock1Y + RockThickness:
                gameOver = True
        
        if lead_x > rock2X and lead_x < rock2X + RockThickness2 or lead_x + block_size > rock2X and lead_x + block_size < rock2X + RockThickness2:
            
            if lead_y > rock2Y and lead_y < rock2Y + RockThickness2:
                gameOver = True

            elif lead_y + block_size > rock2Y and lead_y + block_size < rock2Y + RockThickness2:
                gameOver = True

        
        if lead_x > rock3X and lead_x < rock3X + RockThickness3 or lead_x + block_size > rock3X and lead_x + block_size < rock3X + RockThickness3:
                
            if lead_y > rock3Y and lead_y < rock3Y + RockThickness3:
                gameOver = True

            elif lead_y + block_size > rock3Y and lead_y + block_size < rock3Y + RockThickness3:
                gameOver = True

        #Here snakeLength is used to increase FPS by adding a multiple of the snakes overall length, which gets bigger as it eats more apples
        clock.tick(FPS + (snakeLength*2))
        
    pygame.quit()
    quit()

game_intro()
gameLoop()