from pygame import *
window =display.set_mode((1020,640))
display.set_caption('УльтраСуперМегаКрутаяИгра')
color_back = (200, 0, 200)
window.fill(color_back)
picture = transform.scale(image.load('fonstola.ru_389333.jpg'), (1020,640))
game = True
Biruza = (0, 200, 200)

class Card(sprite.Sprite):
    def __init__(self, width, height, x, y, color):
        super().__init__()
        self.rect = Rect(x, y, width, height)
        self.fill_color = color
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color
    def draw(self):
        draw.rect(window, self.fill_color, self.rect)

player1 = Card(100,100, 50, 50, Biruza)
class Pic(sprite.Sprite):
    def __init__(self, picture, w, h, x, y):
        super().__init__()
        self.image = transform.scale(image.load(picture), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
window.blit(picture, (0,0))
player2 = Pic('hero.png', 100, 100, 50, 50)
player1.draw()
player2.reset()

while game:
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    display.update()