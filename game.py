from pygame import *
window = display.set_mode((700, 500))
display.set_caption('pинг понг')

background = transform.scale(image.load('фон.jpg'), (700, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):  
        sprite.Sprite.__init__(self)  
        self.image = transform.scale(image.load(player_image), (size_x, size_y))  
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
        if keys_pressed[K_DOWN] and self.rect.y < 340:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 340:
            self.rect.y += self.speed

            
font.init()
font1 = font.Font(None, 40)
lose1 = font1.render('pl1 lose', True, (180, 0, 0))     
lose2 = font1.render('pl2 lose', True, (180, 0, 0))    
racket1 = Player('ракетка.jpg', 20, 200, 30, 150, 7)
racket2 = Player('ракетка.jpg', 660, 200, 30, 150, 7)
ball = GameSprite('мяч.jpg', 325, 225, 80, 80, 50)
game = True
finish = False
speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
           game = False
           
    if ball.rect.x < 0:
        window.blit(lose1, (310,225))
        finish = True 
    if ball.rect.x > 700:
        window.blit(lose2, (310,225))
        finish = True 

    if finish != True:
        window.blit(background,(0, 0))
        ball.update()
        racket1.update_r()
        racket2.update_l()
        ball.reset()      
        racket1.reset()
        racket2.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if ball.rect.y > 400 or ball.rect.y < 10:
        speed_y *= -1
    if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
        speed_x *= -1
    
    display.update()
    time.delay(30)
