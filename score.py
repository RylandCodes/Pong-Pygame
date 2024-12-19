import pygame as py

class Score:
    def __init__(self, font_name="Arial", font_size=30, color=(255, 255, 255)):
        py.font.init()
        self.score = 0
        self.font = py.font.SysFont(font_name, font_size)
        self.color = color
        self.position = (10, 10)

    def load(self, screen):
        score_text = self.font.render(f"Score {self.score}", True, self.color)
        screen.blit(score_text, self.position)

    def add(self):
        self.score += 1

    def reset(self):
        self.score = 0
     