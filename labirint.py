from pygame import *
window = display.set_mode((1020, 640))
background = transform.scale(image.load('1.jpg'), (1020, 640))
game = True
win = transform.scale(image.load('thumb_1.jpg'), (1020,640))
lose = transform.scale(image.load('game-over-3.jpg'), (1020, 640))
class GameSprite(sprite.Sprite):
    def __init__(self, picture, w, h, x, y):
        super().__init__()
        self.image = transform.scale(image.load(picture), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Wall(GameSprite):
    def stk(self):
        a = True

class player(GameSprite):
    def __init__(self, picture, w, h, x, y,  vx, vy):
        super().__init__(picture, w, h, x, y)
        self.vx=vx
        self.vy=vy
    def moveup(self):
        if (self.rect.y - self.vy >= 0):
            self.rect.y -= self.vy
    def movedown(self):
        if self.rect.y + self.vy + 50<= 640:
            self.rect.y += self.vy
    def moveleft(self):
        if self.rect.x - self.vx >= 0:
            self.rect.x -= self.vx
    def moveright(self):
        if self.rect.x + self.vx + 50 <= 1020:
            self.rect.x += self.vx

        

wall1 = Wall('wall.png', 20, 440, 300, 0)

wall2 = Wall('wall.png', 20, 460, 450, 200)

wall3 = Wall('wall.png', 20, 440, 600, 0)

walls = sprite.Group()

walls.add(wall1)
walls.add(wall2)
walls.add(wall3)

trophy = GameSprite('final.png', 50, 50, 970, 0)

cat = player('cat.png', 50, 50, 0, 0, 10, 10 )
cat.reset()

enemy = player('alien_1.png', 75, 75, 810, 320, 5, 5)
enemy.reset()
window.blit(background, (0, 0))
wall1.reset()
wall2.reset()
wall3.reset()
trophy.reset()
finish = False
n = 1
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if key.get_pressed()[K_w]:
            cat.moveup()
    if key.get_pressed()[K_s]:
       cat.movedown()
    if key.get_pressed()[K_a]:
        cat.moveleft()
    if key.get_pressed()[K_d]:
        cat.moveright()
    if (not finish):
        window.blit(background, (0,0))
        wall1.reset()
        wall2.reset()
        wall3.reset()
        enemy.reset()
        trophy.reset()
        cat.reset()
        if ((sprite.collide_rect(wall1,cat)) or (sprite.collide_rect(wall2,cat)) or (sprite.collide_rect(wall3,cat)) or (sprite.collide_rect(enemy,cat))):
            finish = True
            window.blit(lose, (0, 0))
        if (sprite.collide_rect(trophy,cat)):
            finish = True
            window.blit(win, (0, 0))
        if enemy.rect.x >= 955 or enemy.rect.x <= 620:
            enemy.vx = enemy.vx*(-1)
        enemy.moveright()
        time.delay(1)
        display.update()