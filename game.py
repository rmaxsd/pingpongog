from pygame import *
window = display.set_mode((700, 500))
display.set_caption('pинг понг')

background = transform.scale(image.load('фон.jpg'), (700, 500))
ball =  transform.scale(image.load('мяч.jpg'), (50, 50))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (20, 120))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 420:
            self.rect.y += self.speed
        
racket1 = Player('ракетка.jpg', 20, 200, 4)
racket2 = Player('ракетка.jpg', 660, 200, 4)
game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
           game = False
           
    if finish != True:
        window.blit(background,(0, 0))
        racket1.update_r()
        racket2.update_l()      
        racket1.reset()
        racket2.reset()
    display.update()
    time.delay(50)