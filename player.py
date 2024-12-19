import pygame as py

class Player:
     def __init__(self):
          self.x = 70
          self.y = 300
          self.width = 20
          self.height = 120
          self.speed = 6
          self.sprite_color = (255,255,255) # white
     def load(self,screen):
          py.draw.rect(screen, self.sprite_color, (self.x, self.y , self.width , self.height))

     def move(self):
          keys = py.key.get_pressed()

          if keys[py.K_UP]:
               self.y -= self.speed
          elif keys[py.K_DOWN]:
               self.y += self.speed
          
          
