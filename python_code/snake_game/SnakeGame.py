#Snake Tutorial Python
 
import math
import random
import pygame
import time
import sys
import tkinter as tk
from tkinter import messagebox
pygame.init() 

DELAY = 10
white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128)

start_menu = True



class cube(object):
    rows = 20
    w = 500
    def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color
 
       
    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)
 
    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]
 
        pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1, dis-2, dis-2))
        if eyes:
            centre = dis//2
            radius = 3
            circleMiddle = (i*dis+centre-radius,j*dis+8)
            circleMiddle2 = (i*dis + dis -radius*2, j*dis+8)
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)


class snake(object):
    body = []
    turns = {}
    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def reset(self, pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1



    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                #left
                if keys[pygame.K_LEFT]:
                    
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_a]:
                    
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                # right
                elif keys[pygame.K_RIGHT]:
                    
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_d]:
                    
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                # up 
                elif keys[pygame.K_UP ]:
                    
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_w]:
                    
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                #down
                elif keys[pygame.K_DOWN ]:
                    
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_s]:
                    
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0],turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                if c.dirnx == -1 and c.pos[0] <= 0:
                    s.reset((10,10))
                    end_screen()
                    
                elif c.dirnx == 1 and c.pos[0] >= c.rows-1: 
                    s.reset((10,10))
                    end_screen()
                    
                elif c.dirny == 1 and c.pos[1] >= c.rows-1: 
                    s.reset((10,10))
                    end_screen()
                    
                elif c.dirny == -1 and c.pos[1] <= 0: 
                    s.reset((10,10))
                    end_screen()
                    
                else: c.move(c.dirnx,c.dirny)
      




    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0]-1,tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0]+1,tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0],tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0],tail.pos[1]+1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy
      

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i ==0:
                c.draw(surface, True)
            else:
                c.draw(surface)


def drawGrid(w, rows, surface):
    sizeBtwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255,255,255), (x,0),(x,w))
        pygame.draw.line(surface, (255,255,255), (0,y),(w,y))
      

def redrawWindow(surface, text3):
    global rows, width, s, snack
    surface.fill((0,0,0))
    s.draw(surface)
    snack.draw(surface)
    drawGrid(width,rows, surface)
    
    
    white = (255, 255, 255) 
    green = (0, 255, 0) 
    blue = (0, 0, 128) 

    font = pygame.font.Font('freesansbold.ttf', 32) 
    text = font.render(text3, True, white)
    textRect = text.get_rect()
    textRect.center = (250, 13)
    surface.blit(text, textRect)

    pygame.display.update()


def randomSnack(rows, item):

    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
            continue
        else:
            break
      
    return (x,y)


def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass



def main(DELAY):   
    
    global width, rows, s, snack   
    white = (255,255,255)   
    DELAY = 10    
    width = 500
    win = pygame.display.set_mode((width, width))    
    rows = 20
    s = snake((255,0,0), (10,10))
    s.reset((10, 10))
    pygame.display.update()
    snack = cube(randomSnack(rows, s), color=(0,255,0))
    clock = pygame.time.Clock()    
    flag = True
 
    white = (255, 255, 255) 
    green = (0, 255, 0) 
    blue = (0, 0, 128) 

    font = pygame.font.Font('freesansbold.ttf', 32) 
    text = font.render('GeeksForGeeks', True, white, blue)
    textRect = text.get_rect()
    textRect.center = (250, 250)

    while flag:
        
        pygame.time.delay(1)
        clock.tick(DELAY)
        s.move()
        
        if s.body[0].pos == snack.pos:
            
            s.addCube()
            snack = cube(randomSnack(rows, s), color=(0, 255, 0))
            DELAY += 1

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z:z.pos, s.body[x+1:])):
                
                #print("Score: ", len(s.body))
                score = str(("Score: ", len(s.body)))
                #message_box("You Lost!", 'Play again...')
                DELAY = 10
                s.reset((10, 10))
                end_screen()
                
                break
        score = ("Score: " + str(len(s.body)))       
        pygame.display.update()        
        redrawWindow(win,score)
    pass

def open_menu():
    image = pygame.image.load(r'C:\Users\User\Documents\techtorium\python_code\snake.png')
    start_menu = True
    s = snake((255,0,0), (10,10))
    s.reset((10,10))
                    
    
    white = (255,255,255)
    black = (0,0,0)
    blue = (60, 106, 207)
    width = 500
    menu = pygame.display.set_mode((width, width))
    menu.fill(black)
    
    font = pygame.font.Font('freesansbold.ttf', 32) 
    text = font.render("levi's snake game", True, black)
    text2 = font.render('play', True, black)
    text3 = font.render('qwit', True, black)

    button1 = pygame.Rect(80, 25, 350, 50)
    button2 = pygame.Rect(80, 100, 350, 50)
    button3 = pygame.Rect(80, 175, 350, 50) 

    pygame.draw.rect(menu, white, button3)

    while start_menu == True:
        pressed = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        
        if 430 > mouse[0] > 80 and 150 > mouse[1] > 100:
            pygame.draw.rect(menu, blue, button2)
            for event in pygame.event.get():                
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:                    
                    print("returned")
                    return                                        
                    break
        else:
            pygame.draw.rect(menu, white, button2)

        if 430 > mouse[0] > 80 and 225 > mouse[1] > 175:
            pygame.draw.rect(menu, blue, button3)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("closing")
                quit()
        else:
            pygame.draw.rect(menu, white, button3)
            
        pygame.draw.rect(menu, white, button1)

        textRect = text.get_rect()
        textRect2 = text2.get_rect()
        textRect3 = text3.get_rect() 

        textRect.center = (500// 2, 50)
        textRect2.center = (250, 125)
        textRect3.center = (250, 200)

        menu.blit(image, (200, 300))
        menu.blit(text, textRect)
        menu.blit(text2, textRect2)
        menu.blit(text3, textRect3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
                
        pygame.display.update()

def end_screen():
    print("show end screen")
    start_menu = True
    s = snake((255,0,0), (10,10))
    s.reset((10,10))
                      
    white = (255,255,255)
    black = (0,0,0)
    blue = (60, 106, 207)
    width = 500
    menu = pygame.display.set_mode((width, width))
    menu.fill(black)
    
    font = pygame.font.Font('freesansbold.ttf', 32) 
    text = font.render("game over", True, black)
    text2 = font.render('play again?', True, black)
    text3 = font.render('qwit', True, black)

    button1 = pygame.Rect(80, 25, 350, 50)

    button2 = pygame.Rect(80, 100, 350, 50)
    button3 = pygame.Rect(80, 175, 350, 50)

    
    pygame.draw.rect(menu, white, button3)
       
    while start_menu == True:
        pressed = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        
        if 430 > mouse[0] > 80 and 150 > mouse[1] > 100:
            pygame.draw.rect(menu, blue, button2)
            for event in pygame.event.get():                
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:                    
                    print("returned")
                    return                                        
                    break
        else:
            pygame.draw.rect(menu, white, button2)

        if 430 > mouse[0] > 80 and 225 > mouse[1] > 175:
            pygame.draw.rect(menu, blue, button3)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("closing")
                quit()
        else:
            pygame.draw.rect(menu, white, button3)
            
        pygame.draw.rect(menu, white, button1)

        textRect = text.get_rect()
        textRect2 = text2.get_rect()
        textRect3 = text3.get_rect() 

        textRect.center = (500// 2, 50)
        textRect2.center = (250, 125)
        textRect3.center = (250, 200)
        
        menu.blit(text, textRect)
        menu.blit(text2, textRect2)
        menu.blit(text3, textRect3)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
                
        pygame.display.update()


open_menu()
main(DELAY)
end_screen()