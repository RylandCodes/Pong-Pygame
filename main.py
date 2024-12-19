import pygame as py
from player import Player
from enemy import Enemy
from ball import Ball
from score import Score
from highscore import HighScore
import pathlib

py.init()

screen_width = 900
screen_height = 600
screen = py.display.set_mode((screen_width, screen_height))

py.display.set_caption('Pong Game')

player = Player()
ball = Ball()
enemy = Enemy()
clock = py.time.Clock()
score = Score()
highscore = HighScore()
running = True

if pathlib.Path("./scores.txt").exists():
    with open("scores.txt", "r") as f:
        content = f.read().strip()
        try:
            highscore.score = int(content)
        except:
            pass

while running:
    screen.fill((0,0,0))
    player.load(screen)
    player.move()
    
    ball.load(screen)
    ball.move(screen_width,screen_height,player,enemy,score,highscore)

    enemy.load(screen)
    enemy.ai_move(ball,screen_height)

    score.load(screen)
    highscore.load(screen)
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    py.display.flip()
    clock.tick(90)
with open("scores.txt","w") as f:
    f.write(str(highscore.score) )
py.quit()