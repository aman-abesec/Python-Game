#*******************************************************************************************************************************************
#                                                 ---->This Program Developed My Aman Singh Using Phthon<-----------                                    #
#                                                                 ------>TRUE FRIEND<----------                                                         #
#*******************************************************************************************************************************************
#Importing pygame,random,time module
import pygame
import random
import time
pygame.init()

#DEfining and aloting Value of Sound
background_sound=pygame.mixer.Sound("background.wav")
catch_sound=pygame.mixer.Sound("drop.wav")
drop_sound=pygame.mixer.Sound("catch.wav")

#Window setting SIZE
screen_size=[350,600]
screen=pygame.display.set_mode(screen_size)

#title page
pygame.display.set_caption("True Friend")
pygame.display.update()

#Variable decleration
fps=30
start=False
user_x=100
score=0
level=0
background=pygame.image.load('background.png').convert_alpha()
background_image=pygame.image.load('user.png').convert_alpha()
user=pygame.transform.scale(background_image,(130,130))
user_image=pygame.image.load('friend.png').convert_alpha()
chicken=pygame.transform.scale(user_image,(130,130))
chicken_y=[-1*random.randint(100,1800),-1*random.randint(100,1500),-1*random.randint(150,1700)]
clock=pygame.time.Clock()

#friend moving and sound and negative scoreing
def move(i):
  global score
  chicken_y[i]=chicken_y[i]+5
  if chicken_y[i]>600:
      pygame.mixer.Sound.stop(background_sound)
      pygame.mixer.Sound.play(drop_sound)
      score=score-20
      score_fn(score,level)
      chicken_y[i]=-1*random.randint(100,1500)

#score add by 5 and play music function
def score_sound(n):
    global score
    pygame.mixer.Sound.stop(background_sound)
    pygame.mixer.Sound.play(catch_sound)
    chicken_y[n]=-1*random.randint(100,1500)
    score+=5

#Score Update function
def score_fn(score,level):
    pygame.draw.rect(screen,(180,225,55),[0,0,350,42])
    font=pygame.font.SysFont('Conic Sans MS',30)
    font_s=pygame.font.SysFont('Conic Sans MS',14)
    score_text="Score : "+str(score)
    level_text="Level : "+str(level)
    developer_text="Developed By-Aman Singh"
    text_image=font.render(score_text,True,(51,102,255))
    level_image=font.render(level_text,True,(51,102,255))
    developer_image=font_s.render(developer_text,True,(51,126,255))
    screen.blit(text_image,[15,7])
    screen.blit(level_image,[215,7])
    screen.blit(developer_image,[10,30])

# screen.blit(background,[0,0])
# mouse=pygame.mouse.get_pos()
# pygame.draw.rect(background,(0,255,255),[60,320,70,35])#START
# pygame.draw.rect(background,(0,255,255),[240,320,70,35])#EXIT
# pygame.display.update()
# if 60+70>mouse[0]>60 and 320+35>mouse[1]>320:
#     pygame.draw.rect(background,(0,5,5),[60,320,70,35])
#     pygame.display.update()
# time.sleep(5)
#Game loop or Main loop
while not start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = True
            # pygame.quit()
            # quit()
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_RIGHT  and user_x<=253:
            user_x=user_x+5
        if event.key==pygame.K_LEFT and user_x>-25:
            user_x=user_x-5
    move(0)
    move(1)
    move(2)
    screen.blit(background,[0,0])
    screen.blit(user,[user_x,505])
    screen.blit(chicken,[-10,chicken_y[0]])
    screen.blit(chicken,[140,chicken_y[1]])
    screen.blit(chicken,[253,chicken_y[2]])
    if chicken_y[0]>450 and user_x<80:
        score_sound(0)
    if chicken_y[1]>450 and (user_x<200 and user_x>86):
        score_sound(1)
    if chicken_y[2]>450 and user_x>200:
        score_sound(2)
#Score and level fps
    if score<300:
        fps=30
        leve=0
    elif score>=500 and score<700:
        fps=35
        level=1
    elif score>=700 and score<1700:
        fps=45
        level=2
    elif score>=1700 and score<4000:
        fps=50
        level=3
    elif score>=4000 and score<5000:
        fps=60
        level=4
    elif score>=5000 and score<6000 :
        fps=55
        level=5
    elif score>=6000 and score<7000:
        fps=70
        level=6
    elif score>=7000 and score<10000:
        fps=80
        level=7
    elif score>=10000:
        fps=90
        level=8
    elif score<=-500:
        font=pygame.font.SysFont('Conic Sans MS',80)
        lose_text="You Lose"
        lose_image=font.render(lose_text,True,(225,50,0))
        screen.blit(lose_image,[50,300])
        pygame.display.update()
        time.sleep(15)
        pygame.quit()
        quit()
    pygame.mixer.Sound.play(background_sound)
    score_fn(score,level)
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
quit()
