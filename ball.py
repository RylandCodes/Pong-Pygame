import pygame as py

import math

class Ball:
     def __init__(self):
          self.x = 400
          self.y = 300
          self.width = 30
          self.height = 30
          self.speed = 6
          self.direction = 45
          self.bounce_angle = 90
          self.color = (255,255,255) # WHite

     def load(self,screen):
          py.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height))

     def move(self,screen_width,screen_height,player_paddle,enemy_paddle,score,highscore):
        radian_angle = math.radians(self.direction)
        self.x += self.speed * math.cos(radian_angle)
        self.y -= self.speed * math.sin(radian_angle)

        if self.y <= 0 or self.y + self.height >= screen_height:
            self.direction = -self.direction

        if self.x <= 0 or self.x + self.width >= screen_width:
            self.reset(screen_width,screen_height,enemy_paddle,player_paddle,score)
        
        if (
            self.x <= player_paddle.x + player_paddle.width
            and self.x + self.width >= player_paddle.x and player_paddle.y
            <= self.y + self.height and self.y <= player_paddle.y + player_paddle.height
        ):
            self.direction = 180 - self.direction
            score.add()
            if score.score > highscore.score:
                highscore.add()

        if (
            self.x + self.width >= enemy_paddle.x
            and self.x <= enemy_paddle.x + enemy_paddle.width
            and enemy_paddle.y <= self.y + self.height
            and self.y <= enemy_paddle.y + enemy_paddle.height
        ):
            self.direction = 180 - self.direction
            self.speed += 1
            player_paddle.speed += 1
            enemy_paddle.speed += 1
            

     def reset(self,screen_width,screen_height,enemy_paddle,player_paddle,score):
         self.x = screen_width // 2
         self.y = screen_height // 2
         self.speed = 6
         self.direction = 45 if self.x < screen_width // 2 else 135
         player_paddle.speed = 6
         enemy_paddle.speed = 6
         score.reset()
