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
class shark(pygame.sprite.Sprite):
    file_path = os.path.join(base_path,'shark.png')
    img = pygame.image.load(file_path).convert_alpha()
    def __init__(self,x,y):
        super().__init__()
        self.image = shark.img
        self.step = 5
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.x = y
        self.check = True
        self.balls = pygame.sprite.Group()
    def load(self):
        print(len(self.balls))
        if len(self.balls)<=1:
            self.balls.add(black_ball(self.rect.x,self.rect.y))
    def update(self):
        if self.rect.x>=win_width-200:
            self.check = False
        if self.rect.x<=self.step:
            self.check = True
        if self.check:
            self.rect.x+=self.step
        else:
            self.rect.x-=self.step
        shark.load(self)
        for f in self.balls:
            if f.rect.y<win_height:
                f.rect.y+=f.step
            else:
                self.balls.remove(f)
        self.balls.draw(win)
class black_ball(pygame.sprite.Sprite):
    file_path = os.path.join(base_path,'black_ball.png')
    img = pygame.image.load(file_path).convert_alpha()
    def __init__(self,x,y):
        super().__init__()
        self.image = black_ball.img
        self.step = 20
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
jt = jet(win_width//2-50,win_height-200)
sk = shark(win_width//2-50,200)
objects = pygame.sprite.Group()
objects.add(jt)
objects.add(sk)
rock_now = 1000
run = True
correct = False
need_problem = False
num=[]
score = 0
enemy = 0
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

    #collision
    for i in jt.mis:
        ball_crash = pygame.sprite.spritecollide(i,sk.balls,True)
        if ball_crash:
            jt.mis.remove(i)
        collide = pygame.sprite.collide_rect(i,sk)
        if collide:
            score+=1
            objects.remove(sk)
    for j in sk.balls:
        crash = pygame.sprite.collide_rect(j,jt)
        if crash:
            enemy+=1
            objects.remove(jt)
    objects.update()
    objects.draw(win)
    pygame.display.update()
