from imp import reload
import os
import pygame, sys, random, math
from button import Button

pygame.init()

gamewindow = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Menu")

BG = pygame.image.load("A:\Hackathon_Python_game\menu\_assets\Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("A:\Hackathon_Python_game\menu\_assets\_font.ttf", size)


controls= ["# Arrow keys controls :-","# < or A move left", "# > or D move right", "# Space bar to Attack", "Note :- use mouse to navigate"]


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        gamewindow.fill("black")

        OPTIONS_TEXT = get_font(25).render(controls[0], True, "white")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(400, 120))
        gamewindow.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_TEXT1 = get_font(18).render(controls[1], True, "white")
        OPTIONS_RECT1 = OPTIONS_TEXT.get_rect(center=(430, 180))
        gamewindow.blit(OPTIONS_TEXT1, OPTIONS_RECT1)

        OPTIONS_TEXT2 = get_font(18).render(controls[2], True, "white")
        OPTIONS_RECT2 = OPTIONS_TEXT.get_rect(center=(430, 210))
        gamewindow.blit(OPTIONS_TEXT2, OPTIONS_RECT2)

        OPTIONS_TEXT3 = get_font(18).render(controls[3], True, "white")
        OPTIONS_RECT3 = OPTIONS_TEXT.get_rect(center=(430, 240))
        gamewindow.blit(OPTIONS_TEXT3, OPTIONS_RECT3)

        OPTIONS_TEXT4 = get_font(22).render(controls[4], True, "white")
        OPTIONS_RECT4 = OPTIONS_TEXT.get_rect(center=(400, 300))
        gamewindow.blit(OPTIONS_TEXT4, OPTIONS_RECT4)

        OPTIONS_BACK = Button(image=None, pos=(400, 460), 
                            text_input="BACK", font=get_font(75), base_color="white", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(gamewindow)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    return main_menu(), reload

        pygame.display.update()

credit_D=["Credits/Licence Details :-","# Develper : Dhanush H", "# status : In Development","# Genre : Space", "# Language : English"]
def credit():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        gamewindow.fill("black")

        OPTIONS_TEXT = get_font(25).render(credit_D[0], True, "white")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(400, 120))
        gamewindow.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_TEXT1 = get_font(22).render(credit_D[1], True, "white")
        OPTIONS_RECT1 = OPTIONS_TEXT.get_rect(center=(430, 180))
        gamewindow.blit(OPTIONS_TEXT1, OPTIONS_RECT1)

        OPTIONS_TEXT2 = get_font(22).render(credit_D[2], True, "white")
        OPTIONS_RECT2 = OPTIONS_TEXT.get_rect(center=(430, 220))
        gamewindow.blit(OPTIONS_TEXT2, OPTIONS_RECT2)

        OPTIONS_TEXT3 = get_font(22).render(credit_D[3], True, "white")
        OPTIONS_RECT3 = OPTIONS_TEXT.get_rect(center=(430, 260))
        gamewindow.blit(OPTIONS_TEXT3, OPTIONS_RECT3)

        OPTIONS_TEXT4 = get_font(22).render(credit_D[4], True, "white")
        OPTIONS_RECT4 = OPTIONS_TEXT.get_rect(center=(430, 300))
        gamewindow.blit(OPTIONS_TEXT4, OPTIONS_RECT4)

        OPTIONS_BACK = Button(image=None, pos=(400, 460), 
                            text_input="BACK", font=get_font(75), base_color="white", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(gamewindow)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    return main_menu(),reload

        pygame.display.update()

def main_menu():
    while True:
        gamewindow.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(75).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("A:\Hackathon_Python_game\menu\_assets\Play Rect.png"), pos=(400, 230), 
                            text_input="PLAY", font=get_font(60), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("A:\Hackathon_Python_game\menu\_assets\Options Rect.png"), pos=(400, 380), 
                            text_input="CONTROLS", font=get_font(60), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("A:\Hackathon_Python_game\menu\_assets\Quit Rect.png"), pos=(400, 530), 
                            text_input="CREDIT", font=get_font(50), base_color="#d7fcd4", hovering_color="White")

        gamewindow.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(gamewindow)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    return reload
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    credit()

        pygame.display.update()

main_menu()




name_game = "Space king Dhanush"
pygame.init()                                                          #initialize all imported pygame modules (function ) to work. to initialize you just call it
screen_width = 800
screen_height = 600
gamewindow = pygame.display.set_mode((screen_width,screen_height))        #method we passing tuple having value of width and height
pygame.display.set_caption(name_game)
icon = pygame.image.load("A:\Hackathon_Python_game\launch_logo.png")
pygame.display.set_icon(icon)
# pygame.display.update() 
#                                                 #only this window open and close so we do infinit loop here

#background
background = pygame.image.load("A:\Hackathon_Python_game\_background.png")

# player
playerImg = pygame.image.load("A:\Hackathon_Python_game\spaceship.png")
playerX=370                   #position of player_image in x and y quadrant
playerY=480
def player(x,y):
    gamewindow.blit(playerImg,(x,y))                      #blit used to draw player in window (player_Image, Tuple form x and y quadrant) 

# Enemy (code same as player)
# enemyImg = pygame.image.load("A:\Hackathon_Python_game\enemy_1.png")
"""enemyX=370                   #position of player_image in x and y quadrant
enemyY=50                    #position of enemy should be in up of window so 50"""#no use of it because enemy position is fixed here i want enemy position should be random
"""enemyX = random.randint(0,736)               #because position of enemy = 800 (window) - 64 (enemy size) = 736 now enemy move in window screen only
enemyY = random.randint(50, 150)            # positon of enemy change in Y up to down
enemyX_change = 4
enemyY_change =40"""
#abow is only for one enemy below is for multiple enemy, after this multiple enemy code now we need to change every enemy code in list [i]
enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change = []
enemyY_change =[]
no_of_enemy=20
for i in range(no_of_enemy):
    enemyImg.append(pygame.image.load("A:\Hackathon_Python_game\enemy_1.png"))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)
def enemy(x,y,i):
    gamewindow.blit(enemyImg[i],(x,y))                   #i because here i taking image from list

#Bullet 
bulletImg = pygame.image.load("A:\Hackathon_Python_game\_bullet_fire.png")
bulletX=0                   
bulletY= 480
bulletX_change = 0                                    #it is not needed because bullet only move in y direction in upword
bulletY_change = 10                                     #bullet speed can control
bullet_states = "ready"                               #i can't fire bullet multiple times so it means ready to fire
def fire_bullet(x,y):
    global bullet_states 
    bullet_states = "fire"                                                                     #it means bullet already fired
    gamewindow.blit(bulletImg,(x+16,y+12))

# collission will happen when the coordinate of bullet and enemy will match maths formula = distance between two points d =  √[(x2 − x1)2 + (y2 − y1)2 + (z2 − z1)2]
def testCollision(enemyX,enemyY, bulletX, bulletY):                                  
    distance=math.sqrt(math.pow(enemyX-bulletX,2)+math.pow(enemyY-bulletY,2))         #d =  √[(x2 − x1)2 + (y2 − y1)2 + (z2 − z1)2]
    if distance<27:
        return True
    else:
        return False

score = 0
level=1
font = pygame.font.Font('freesansbold.ttf',32)       # font names
textX=590                                              #position of our score
textY=15
def show_score(x,y):
    score1 = get_font(25).render('score:'+str(score),True,(255,255,255))
    level1 = get_font(25).render('LEVEL: '+str(level),True,(255,255,255))
    gamewindow.blit(score1,(x,y))
    gamewindow.blit(level1,(300,15))

text = pygame.font.Font('freesansbold.ttf',72)
def game_over(text_end,color):
    text = get_font(30).render(text_end,True,color)
    text1 = get_font(30).render(text_end,True,(255,255,255))
    gamewindow.blit(text1,(116,270))                                  #position of text is imaginally taking to print in center
    gamewindow.blit(text,(120,270))                                  #position of text is imaginally taking to print in center
    score1 = get_font(30).render('score :'+str(score),True,color)
    score2 = get_font(30).render('score :'+str(score),True,(255,255,255))
    gamewindow.blit(score2,(286,310)) 
    gamewindow.blit(score1,(290,310))                                 
                                

block_update=4                                                                  #spaceship speed can control
playerX_change = 0
closewindow = False
white=(255,255,255)                                                        #rgb value is 255,255,255 gives white
while not closewindow:
    gamewindow.fill(white)
    gamewindow.blit(background,(0,0))                                  #it should after fill(white) and our entire program will slow because image size is more
    PLAY_MOUSE_POS = pygame.mouse.get_pos()
    back_B = Button(image=None, pos=(90,30), text_input="BACK", font=get_font(35), base_color="White", hovering_color="Green")
    back_B.changeColor(PLAY_MOUSE_POS)
    back_B.update(gamewindow)                                 #it should after fill(white) and our entire program will slow because image size is more
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                                        #if user press quit button (event) then the program will end
            closewindow=True
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if back_B.checkForInput(PLAY_MOUSE_POS):
                main_menu()

        if event.type == pygame.KEYDOWN:                                         #when we press any key in window it is event called "Key Down"      #when we release that key in window it is enent called "key up"
            if event.key == pygame.K_LEFT or event.key==pygame.K_a:
                playerX_change =-block_update                                    #only change in playerX position because we want to move spaceship horizontally
            if event.key == pygame.K_SPACE:                                                                      # when space button key down it should fire bullet
                if bullet_states== "ready":                                                                         #bullet fire if state is ready
                    bulletX=playerX                                                                                  # bullet should be fire from spaceship
                    fire_bullet(bulletX,bulletY)
            if event.key == pygame.K_RIGHT or event.key==pygame.K_d:
                playerX_change =block_update
        if event.type == pygame.KEYUP:                                      #we use keyup because after key down our space ship keep moving even if we not press key SO.
             if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key==pygame.K_a or event.key==pygame.K_d:   #afte keydown when we keyup of any key (right or left) the position change add 0 to playerX
                 playerX_change = 0
    playerX+=playerX_change                                                         #by pressing arrow the change will be add to current position of playerX
        
    if playerX <= 0: #player position in boundary                                 # spaceship is going out side the boundary condition (0) than playerX position fixed to 0 not to go position to -ve
        playerX=0
    elif playerX>= 736:                                                        # 736 but i took screen size is 800. because 800(window) - spaceship(64) = 736.
        playerX = 736

    for i in range(no_of_enemy):                                                 #here we declaring for every loop movement of every enemy is written in list 
        #when the game will over
        if enemyY[i]>440:
            for j in range(no_of_enemy):
                enemyY[j]=20000
            game_over("Game Over ! YOU LOSE",(255,0,0))
            break
        
        enemyX[i] += enemyX_change[i]   #enemy movement
        if enemyX[i] <= 0: #enemy position in boundary                                 # spaceship is going out side the boundary condition (0) than playerX position fixed to 0 not to go position to -ve
            enemyX_change[i]=3.5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i]>= 736:                                                        # 736 but i took screen size is 800. because 800(window) - spaceship(64) = 736.
            enemyX_change[i]= -3.5
            enemyY[i] += enemyY_change[i]
        collision = testCollision(enemyX[i],enemyY[i],bulletX,bulletY)                 #here checking collision for every single enemy. this collision call need to write in loop 
        if collision == True:                                                   
            bulletY=480                                                         #after collision position reach to spaceship
            bullet_states = "ready"
            score = score + 1
            enemyX[i]=random.randint(0,736)
            enemyY[i]=random.randint(50,150)
        enemy(enemyX[i],enemyY[i],i)                                                      #i am calling enemy here means when program enemy function call

    #bullet movement
    if bulletY <=0 :
        bulletY=480                                                           #after fire bullet reach boundary it should return to spaceship position 480
        bullet_states = "ready"                                                #now again ready to fire
    if bullet_states=="fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletY_change                                                #here - because we need to move our bullet in up direction


    if score==10:
        level=2
        no_of_enemy=10
    if score==20:
        level=3
        no_of_enemy=5
    if score==30:
        level=3
        no_of_enemy=0
        color=(50,205,50)
        game_over("Game Over ! You Win",color)
        """need to write code to restart game again !"""



    show_score(textX,textY)
    player(playerX,playerY)                                                  #i am calling spacship here means when program spaceship function call
    pygame.display.update()                                                   #while close window by click we doesnot get error because closewindow=True will end loop so program ends








