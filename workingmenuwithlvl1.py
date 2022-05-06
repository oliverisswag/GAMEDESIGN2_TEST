#MAria I SUarez
#learning how to draw circles and rectangles
#use keys to move objects
#Using Dictionaries

#Objective of the game is for the rect to run away fom the circle, if they collide the circle etas the square, 
#circle will  get larger, and a new rect should appear somewhere on the screen
# K_UP                  up circle
# K_DOWN                down circle
# K_RIGHT               right circle
# K_LEFT                left circle
# K_a                   left square
# K_d                   right square
# K_w                   up square
# K_s                   down square
# K_SPACE               jump
#initialize pygame
import os, random, time, pygame, math, datetime
from turtle import screensize
os.system('cls')
name=input("What is your name? ")
#initialize pygame
pygame.init()

#Declare constants, variables, list, dictionaries, any object
#scree size
WIDTH=400
HEIGHT=600
xMs=50
yMs=250
wb=30
hb=30
MAIN=True
INST=False
SETT=False
LEV_I=False
LEV_II=False
LEV_III=False
SCORE=False
#List f messages
MenuList=['Instructions','Settings', "Level I","Level II",'Level III','Scoreboard','Exit']
SettingList=['Screen Size','Backgrnd Color','Icon','']
sizeList=['1000 x 1000','800 x 800','600 x 600']
check=True #for the while loop

#create screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Circle eats Square')

#define colors
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],
'orange':[255,85,0],'purple':[48,25,52],'navy':[5,31,64],'pink':[200,3,75]}
#Get colors
background= colors.get('white')
randColor=''
cr_color=colors.get('aqua')
sqM_color=colors.get('pink')
BLACK=(0,0,0)
#create fifferent type 
TITLE_FNT=pygame.font.SysFont('comicsans', 80)
MENU_FNT=pygame.font.SysFont('comicsans', 40)
INST_FNT=pygame.font.SysFont('comicsans', 30)
#Create square fr menu

squareM=pygame.Rect(xMs,yMs,wb,hb)
#Create Title
def TitleMenu(Message):
    text=TITLE_FNT.render(Message, 1, (255,0,0))
    screen.fill((255,255,255))
    #get the width  the text 
    #x value = WIDTH/2 - wText/2
    xt=WIDTH/2-text.get_width()/2
    screen.blit(text,(xt,50))
#This is a function uses a parameter
def MainMenu(Mlist):
    txty=243
    squareM.y=250
    for i in range(len(Mlist)):
        message=Mlist[i]
        text=INST_FNT.render(message,1,(51,131,51))
        screen.blit(text,(90,txty))
        pygame.draw.rect(screen,sqM_color, squareM )
        squareM.y +=50
        txty+=50
    pygame.display.update()
    pygame.time.delay(10)
def changeColor():
    global randColor
    colorCheck=True
    while colorCheck:
        randColor=random.choice(list(colors))
        if colors.get(randColor)==background:
            print(randColor)
            print(background)
            randColor=random.choice(list(colors))
        else:
            colorCheck=False
def instr():
    print("in instr")
    myFile=open('ClassStuff\CircleEatsSquare\instructions.txt', 'r')
    yi=150
    stuff= myFile.readlines()


    print(stuff)
    for line in stuff:
        print(line)
        text=INST_FNT.render(line, 1, BLACK)
        screen.blit(text, (40,yi))
        pygame.display.update()
        pygame.time.delay(50)
        yi+=50
    myFile.close()
def keepScore(score):
    date=datetime.datetime.now()
    print(date.strftime('%m/%d/%Y'))
    scoreLine=str(score)+"\t"+name+"\t"+date.strftime('%m/%d/%Y'+'\n')
 
    #open a file and write in it 
    # when y write it erases the prev 
    myFile=open('ClassStuff\sce.txt','a') 
    myFile.write(scoreLine)
    myFile.close()
def scoreBoard():
    myFile=open('ClassStuff\CircleEatsSquare\sce.txt', 'r')
    yi=150
    stuff= myFile.readlines()
    myFile.close()
    stuff.sort()
    N=len(stuff)-1
    temp=[]
    j=0
    for i in range(N, -1, -1):
        print(i,stuff[i])
        # temp[j]=stuff[i]
        #     j +=1
        # print(temp)
        # for i in range(N):
        #     text=INST_FNT.render(temp[i], 1, BLACK)
        #     screen.blit(text, (40,yi))
        #     pygame.display.update()
        #     pygame.time.delay(50)
        #     yi+=50
    
def keepScore(score):
    date=datetime.datetime.now()
    print(date.strftime('%m/%d/%Y'))
    scoreLine='\n'+str(score)+"\t"+name+"\t"+date.strftime('%m/%d/%Y'+'\n')
 
    #open a file and write in it 
    # when y write it erases the prev 
    myFile=open('ClassStuff\CircleEatsSquare\sce.txt','a') 
    myFile.write(scoreLine)
    myFile.close()
def changeScreenSize(xm,ym):
    global HEIGHT, WIDTH, screen
    if ((xm >20 and xm <80) and (ym >250 and ym <290)):
        HEIGHT=1000
        WIDTH=1000

    if ((xm >20 and xm <80) and (ym >300 and ym <330)):
        HEIGHT=800
        WIDTH=800
        
    if ((xm >20 and xm <80) and (ym >350 and ym <380)):
        HEIGHT=600
        WIDTH=600
    screen=pygame.display.set_mode((WIDTH,HEIGHT))
 
def playGame():
    pygame.display.set_caption('Jumpy')

    #set frame rate
    clock = pygame.time.Clock()
    FPS = 60

    #game variables
    SCROLL_THRESH = 200
    GRAVITY = 1
    MAX_PLATFORMS = 10
    scroll = 0
    bg_scroll = 0
    game_over = False
    score = 0
    fade_counter = 0

    #define colours
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    #define font
    font_small = pygame.font.SysFont('Lucida Sans', 20)
    font_big = pygame.font.SysFont('Lucida Sans', 24)

    #load images
    jumpy_image = pygame.image.load('jump.png').convert_alpha()
    bg_image = pygame.image.load('bg.png').convert_alpha()
    platform_image = pygame.image.load('wood.png').convert_alpha()

    #function for outputting text onto the screen
    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    #function for drawing the background
    def draw_bg(bg_scroll):
        screen.blit(bg_image, (0, 0 + bg_scroll))
        screen.blit(bg_image, (0, -600 + bg_scroll))

    #player class
    class Player():
        def __init__(self, x, y):
            self.image = pygame.transform.scale(jumpy_image, (45, 45))
            self.width = 25
            self.height = 40
            self.rect = pygame.Rect(0, 0, self.width, self.height)
            self.rect.center = (x, y)
            self.vel_y = 0
            self.flip = False

        def move(self):
            #reset variables
            scroll = 0
            dx = 0
            dy = 0

            #process keypresses
            key = pygame.key.get_pressed()
            if key[pygame.K_a]:
                dx = -10
                self.flip = True
            if key[pygame.K_d]:
                dx = 10
                self.flip = False

            #gravity
            self.vel_y += GRAVITY
            dy += self.vel_y

            #ensure player doesn't go off the edge of the screen
            if self.rect.left + dx < 0:
                dx = -self.rect.left
            if self.rect.right + dx > WIDTH:
                dx = WIDTH - self.rect.right


            #check collision with platforms
            for platform in platform_group:
                #collision in the y direction
                if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    #check if above the platform
                    if self.rect.bottom < platform.rect.centery:
                        if self.vel_y > 0:
                            self.rect.bottom = platform.rect.top
                            dy = 0
                            self.vel_y = -20

            #check if the player has bounced to the top of the screen
            if self.rect.top <= SCROLL_THRESH:
                #if player is jumping
                if self.vel_y < 0:
                    scroll = -dy

            #update rectangle position
            self.rect.x += dx
            self.rect.y += dy + scroll

            return scroll

        def draw(self):
            screen.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x - 12, self.rect.y - 5))
            pygame.draw.rect(screen, WHITE, self.rect, 2)



    #platform class
    class Platform(pygame.sprite.Sprite):
        def __init__(self, x, y, width):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(platform_image, (width, 10))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

        def update(self, scroll):

            #update platform's vertical position
            self.rect.y += scroll

            #check if platform has gone off the screen
            if self.rect.top > HEIGHT:
                self.kill()

    #player instance
    jumpy = Player(WIDTH // 2, HEIGHT - 150)

    #create sprite groups
    platform_group = pygame.sprite.Group()

    #create starting platform
    platform = Platform(WIDTH // 2 - 50, HEIGHT - 50, 100)
    platform_group.add(platform)

    #game loop
    run = True
    while run:

        clock.tick(FPS)

        if game_over == False:
            scroll = jumpy.move()

            #draw background
            bg_scroll += scroll
            if bg_scroll >= 600:
                bg_scroll = 0
            draw_bg(bg_scroll)

            #generate platforms
            if len(platform_group) < MAX_PLATFORMS:
                p_w = random.randint(40, 60)
                p_x = random.randint(0, WIDTH - p_w)
                p_y = platform.rect.y - random.randint(80, 120)
                platform = Platform(p_x, p_y, p_w)
                platform_group.add(platform)

            #update platforms
            platform_group.update(scroll)

            #draw sprites
            platform_group.draw(screen)
            jumpy.draw()

            #check game over
            if jumpy.rect.top > HEIGHT:
                game_over = True
        else:
            if fade_counter < WIDTH:
                fade_counter += 5
                for y in range(0, 6, 2):
                    pygame.draw.rect(screen, BLACK, (0, y * 100, fade_counter, 100))
                    pygame.draw.rect(screen, BLACK, (WIDTH - fade_counter, (y + 1) * 100, WIDTH, 100))
            draw_text('GAME OVER!', font_big, WHITE, 130, 200)
            draw_text('SCORE: ' + str(score), font_big, WHITE, 130, 250)
            draw_text('PRESS SPACE TO PLAY AGAIN', font_big, WHITE, 40, 300)
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                #reset variables
                game_over = False
                score = 0
                scroll = 0
                fade_counter = 0
                #reposition jumpy
                jumpy.rect.center = (WIDTH // 2, HEIGHT - 150)
                #reset platforms
                platform_group.empty()
                #create starting platform
                platform = Platform(WIDTH // 2 - 50, HEIGHT - 50, 100)
                platform_group.add(platform)


        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        #update display window
        pygame.display.update()





#sq_color=colors.get('navy')
#Making a rand c f the square
changeColor()

#==============================================
#
#Beginning  main prram
sq_color=colors.get(randColor)
keys=pygame.key.get_pressed()
mouse_pos=(0,0)
screCk=True
first=True
xm=0 
ym=0
f_SEET=True
sc_size=False
set_first=True
c_first=True
while check:
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            check=False
        if case.type ==pygame.MOUSEBUTTONDOWN:
            mouse_pos=pygame.mouse.get_pos()
            xm= mouse_pos[0]
            ym= mouse_pos[1]
        # print(mouse_pos)
    keys=pygame.key.get_pressed() #this returns a list
    if MAIN:
        screen.fill(background)
        TitleMenu("MENU")
        MainMenu(MenuList)
    if INST and first:
        screen.fill(background)
        TitleMenu("INSTRUCTIONS")
        instr()
        first=False
    if INST:
        if keys[pygame.K_ESCAPE]:
            INST=False
            MAIN=True
            first=True
    if SETT and f_SEET:
        screen.fill(background)
        TitleMenu("SETTINGS")
        MainMenu(SettingList)
        f_SEET=False
    if SETT:
        if keys[pygame.K_ESCAPE]:
            SETT=False
            MAIN=True
            f_SEET=True
    if LEV_I:
        screen.fill(background)
        playGame()
        LEV_I=False
        MAIN=True
        xm=0
        ym=0
    if LEV_II:
        screen.fill(background)
        TitleMenu("LEVEL II")
        if keys[pygame.K_ESCAPE]:
            LEV_II=False
            MAIN=True
    if LEV_III:
        screen.fill(background)
        TitleMenu("LEVEL III")
        if keys[pygame.K_ESCAPE]:
            LEV_III=False
            MAIN=True
    if SCORE and screCk:
        screen.fill(background)
        TitleMenu("SCOREBOARD")
        scoreBoard()
        #call funct t print scres
        screCk=False
    if SCORE:
        if keys[pygame.K_ESCAPE]:
            SCORE=False
            MAIN=True
            screCk=True
    if ((xm >20 and xm <80) and (ym >250 and ym <290)) and MAIN:
        MAIN=False
        INST=True
    if ((xm >20 and xm <80) and (ym >300 and ym <330))and MAIN:
        MAIN=False
        SETT=True  
    if ((xm >20 and xm <80) and (ym >350 and ym <380))and MAIN :
        MAIN=False
        LEV_I=True   
    if ((xm >20 and xm <80) and (ym >400 and ym <430))and MAIN :
        MAIN=False
        LEV_II=True   
    if ((xm >20 and xm <80) and (ym >450 and ym <480))and MAIN:
        MAIN=False
        LEV_III=True   
    if ((xm >20 and xm <80) and (ym >500 and ym <530))and MAIN:
        MAIN=False
        SCORE=True 
    if ((xm >20 and xm <80) and (ym >250 and ym <290)) and SETT and set_first:  
        screen.fill(background)
        TitleMenu("Screen Size")
        MainMenu(sizeList )
        sc_size=True
        set_first=False
        f_SEET=True
        if keys[pygame.K_ESCAPE]:
            sc_size=False
            set_first=True
    if sc_size and xm >0:
        changeScreenSize(xm,ym)
        screen.fill(background)
        TitleMenu("Screen Size")
        MainMenu(sizeList )
        if keys[pygame.K_ESCAPE]:
            sc_size=False
            set_first=True
    if ((xm >20 and xm <80) and (ym >300 and ym <330))and SETT and c_first:
        screen.fill(background)
        TitleMenu("Background Color")
        c_first=False
        if keys[pygame.K_ESCAPE]:
            c_first=True
            set_first=True
    if ((xm >20 and xm <80) and (ym >550 and ym <580)) :
        screen.fill(background)
        keepScore(121)
        text=INST_FNT.render("Make sure you update the score file", 1, BLACK)
        screen.blit(text, (40,200))
        text=INST_FNT.render("before you exit", 1, BLACK)
        screen.blit(text, (40,300))
        text=INST_FNT.render("Thank you for playing", 1, BLACK)
        screen.blit(text, (40,400))
        pygame.display.update()
        pygame.time.delay(50)
        MAIN=False
        SCORE=False 
        pygame.time.delay(3000)
        check=False
    pygame.display.update()
    pygame.time.delay(10)

os.system('cls')
pygame.quit()
