import random

import pygame
#initialize the game
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))
#background
background = pygame.image.load('background.png')


#title
pygame.display.set_caption("DONALD")
icon =pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('player.png')
playerX =370
playerY =480
playerX_change =0
playerY_change =0
def player(X,Y):
    screen.blit(playerImg,(X, Y))
#Enemy(amina)
enemyImg = pygame.image.load('001-ufo.png')
enemyX = random.randint(0,800)
enemyY = random.randint(150,200 )
enemyX_change =0.3
enemyY_change=.04
def enemy(X,Y):
    screen.blit(enemyImg,(X,Y))

    #laser

laserImg = pygame.image.load('laser.png')
laserX = 0
laserY = 480
laserX_change = 0
laserY_change = 10
laser_state ="ready"
def fire_laser(X,Y):
    global laser_state
    laser_state ="fire"
    screen.blit(laserImg,(X+16,Y+10))

#game loop
running = True
while running:
    screen.fill((0 , 0, 0))
    #background image
    screen.blit(background,(0,0))
    playerX += playerX_change
    playerY += playerY_change
    enemyX  += enemyX_change
    enemyY  += enemyY_change
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =  False
#Keypress id
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
           playerX_change =-4
        if event.key ==pygame.K_RIGHT:
           playerX_change = 4
        if event.key == pygame.K_UP:
           playerY_change = -4

        if event.key ==pygame.K_DOWN:
            playerY_change =4
        if event.key == pygame.K_LALT:
            fire_laser(playerX,laserY)

    if event.type ==pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key ==pygame.K_RIGHT:
         playerX_change =0
         playerY_change =0
         print(enemyX)
        if event.key == pygame.K_LALT:
            laser_state == "fire"
    playerX += playerX_change
    if playerX <=0:
      playerX = 0
    elif playerX>= 736:
      playerX=736

    playerY += playerY_change
    if playerY <= 0:
      playerY = 0
    elif playerY >= 536:
      playerY = 536

      playerX += playerX_change
    if enemyX <= 0:
     enemyX_change = 0.3
     enemyY  +=enemyY_change
    elif enemyX >=736:
     enemyX_change = -0.3
     enemyY += enemyY_change
     print ("enemyX")
    enemyY += enemyY_change
    if enemyY <= 0:
        enemyY = 0
    elif enemyY >= 536:
        enemyY = 0

    #bullet mvt
    if laser_state =="fire":
      fire_laser(playerX,laserY)
      laserY -=laserY_change

    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()
