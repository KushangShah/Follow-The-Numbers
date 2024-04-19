import pygame
import pyzero 
import pgzrun 
from random import randint

# pgzrun /Users/bina/Code?/Exercise/Game?/Follow-The-Numbers/FollowTheNum.py

WIDTH = 600
HEIGHT = 550

sqrs = []
lines = []
next_sqrs = 0

for sqr in range(0, 11):
    actor = Actor("sqr")
    actor.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
    sqrs.append(actor)

def draw():
    screen.fill("black")
    num = 1
    for sqr in sqrs:
        screen.draw.text(str(num), (sqr.pos[0] - 10, sqr.pos[1] + 20))
        sqr.draw()
        num += 1
    
    for line in lines:
        screen.draw.line(line[0], line[1], (100, 5, 5))

def on_mouse_down(pos):
    global next_sqrs
    global lines

    if sqrs[next_sqrs].collidepoint(pos):
        if next_sqrs:
            lines.append((sqrs[next_sqrs - 1].pos, sqrs[next_sqrs].pos))
        next_sqrs += 1
    else:
        lines = []
        next_sqrs = 0

sqr = Actor("sqr")

def on_mouse_down(pos):
    if sqr.collidepoint(pos):
        print("Ouch")
    else:
        pass

