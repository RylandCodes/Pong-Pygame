import pygame as py

class HighScore:
    def __init__(self, font_name="Arial", font_size=30, color=(255, 255, 255)):
        py.font.init()
        self.score = 0
        self.font = py.font.SysFont(font_name, font_size)
        self.color = color
        self.position = (10, 60)

    def load(self, screen):
        score_text = self.font.render(f"High Score {self.score}", True, self.color)
        screen.blit(score_text, self.position)

    def set(self,amount):
        self.score = amount

    def add(self):
        self.score += 1