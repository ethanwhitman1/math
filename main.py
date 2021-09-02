import pygame
import time
import random
import os
pygame.init()
base_path = os.path.dirname(__file__)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
cyan = (10,210,248)
win_width = 1200
win_height = 900
win = pygame.display.set_mode((win_width, win_height))
mis_step = 20
pygame.display.set_caption("JET Game")
class jet(pygame.sprite.Sprite):
    file_path = os.path.join(base_path, 'jet.png')
    img = pygame.image.load(file_path).convert_alpha()
    def __init__(self,x,y):
        super().__init__()
        self.step = 8
        self.image = jet.img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mis = pygame.sprite.Group()
    def move_left(self):
        if self.rect.x > self.step: 
            self.rect.x -= self.step       
    def move_right(self):
        if self.rect.x < 1000:
            self.rect.x +=self.step
    def move_up(self):
        if self.rect.y > win_height//2: 
            self.rect.y -= self.step       
    def move_down(self):
        if self.rect.y < win_height-200-self.step:
            self.rect.y +=self.step
    def load(self):
        if len(self.mis)<=3:
            self.mis.add(missile(self.rect.x+20,self.rect.y-30))
    def update(self):
        for i in self.mis:
            if i.rect.y>-50:
                i.rect.y-=mis_step
            else:
                self.mis.remove(i)
        self.mis.draw(win)
# class attacker(pygame.sprite.Sprite):
#     file_path = os.path.join(base_path,'ball.png')
#     img = pygame.image.load(file_path).convert_alpha()
#     def __init(self,x,y):
#         super().__init__()
#         self.image = attacker.img
#         self.step = 26
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y
#         self.rok = pygame.sprite.Group()
#         self.left_right = True
#     def load(self):
#         if len(self.rok)<2:
#             self.rock.add(rock(self.rect.x,self.rect.y))
#     def update(self):
#         if self.rect.x<=0:
#             self.left_right = False
#         if self.rect.x>=win_width:
#             self.left_right = True
#         if self.left_right:
#             self.rect.x-=self.step
#         else:
#             self.rect.x+=self.step
        
class missile(pygame.sprite.Sprite):
    file_path = os.path.join(base_path,'ball.png')
    img = pygame.image.load(file_path).convert_alpha()
    def __init__(self,x,y):
        super().__init__()
        self.image = missile.img
        self.step = 20
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class rock(pygame.sprite.Sprite):
    file_path = os.path.join(base_path,'rock.png')
    img = pygame.image.load(file_path).convert_alpha()
    def __init__(self,x,y):
        super().__init__()
        self.image = rock.img
        self.step = 30
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rok = pygame.sprite.Group()
    def load(self):
        self.rok.add(rock(random.randint(0,win_width),-200))
    def update(self):
        for i in self.rok:
            if i.rect.y<win_height:
                i.rect.y+=1
            else:
                self.rok.remove(i)
jt = jet(win_width//2-50,win_height-200)
rk = rock(random.randint(0,win_width),-200)
objects = pygame.sprite.Group()
objects.add(jt)
objects.add(rk)
rock_now = 1000
run = True
correct = False
need_problem = False
num=[]
while run:
    pygame.time.delay(20)
    win.fill(cyan)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        jt.move_left()
    if keys[pygame.K_RIGHT]:
        jt.move_right()
    if keys[pygame.K_UP]:
        jt.move_up()
    if keys[pygame.K_DOWN]:
        jt.move_down()
    if keys[pygame.K_SPACE]:
        jt.load()
    # if need_problem:
    #     if keys[pygame.K_0]:
    #         num.append(0)
    #     if keys[pygame.K_1]:
    #         num.append(1)
    #     if keys[pygame.K_2]:
    #         num.append(2)
    #     if keys[pygame.K_3]:
    #         num.append(3)
    #     if keys[pygame.K_4]:
    #         num.append(4)
    #     if keys[pygame.K_5]:
    #         num.append(5)
    #     if keys[pygame.K_6]:
    #         num.append(6)
    #     if keys[pygame.K_7]:
    #         num.append(7)
    #     if keys[pygame.K_8]:
    #         num.append(8)
    #     if keys[pygame.K_9]:
    #         num.append(9)
    #     if keys[pygame.K_RETURN]:
    #         if num==c_ans:

    objects.update()
    objects.draw(win)
    pygame.display.update()