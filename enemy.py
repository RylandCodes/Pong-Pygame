import pygame as py

class Enemy:
     def __init__(self):
          self.x = 800
          self.y = 300
          self.width = 20
          self.height = 120
          self.speed = 6
          self.sprite_color = (255,255,255) # white
     def load(self,screen):
          py.draw.rect(screen, self.sprite_color, (self.x, self.y , self.width , self.height))

     def move(self,direction,screen_height):
          if direction == "u" and self.y > 0:
               self.y -= self.speed
          elif direction == "d" and self.y + self.height < screen_height:
               self.y += self.speed

     def ai_move(self,ball,screen_height):
          if ball.y + ball.height // 2 > self.y + self.height // 2:
               self.move("d",screen_height)
          elif ball.y + ball.height // 2 < self.y + self.height // 2:
               self.move("u",screen_height)
          

          
          
