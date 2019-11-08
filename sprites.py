import pygame
import random
import math

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

class Block (pygame.sprite.Sprite):
    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.OG_image = pygame.Surface([width,height])
        self.center = self.OG_image.get_rect().center
        self.rect = self.OG_image.get_rect(center = self.center)
        self.image_angle = 0#random.randrange(0,360)
        self.image = pygame.transform.rotate(self.OG_image, self.image_angle)
    def spin(self):
        self.image_angle += 10
        self.image = pygame.transform.rotate(self.OG_image, self.image_angle)
        self.rect = self.image.get_rect(center = self.center)
    def move(self):
        rad = math.radians(self.image_angle)
        self.rect.x += math.sin(rad)*speed*-1
        self.rect.y += math.cos(rad)*speed*-1
        self.center = (self.center[0] + math.sin(rad)*speed*-1, self.center[1] + math.cos(rad)*speed*-1)

pygame.init()

speed = 10
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width,screen_height])

blocks = pygame.sprite.Group()
block_list = []
cblock_hit_list = []
all_sprites_list = pygame.sprite.Group()

for i in range(4):
    block = Block(20,15)
    block.rect.x = random.randrange(0,650)
    block.rect.y = (i*200) - 400
    block.OG_image = pygame.transform.scale(pygame.image.load("wood.jpg"), (20, 15))
    blocks.add(block)
    block_list.append(block)
    all_sprites_list.add(block)

target = 3
player = Block(20, 20)
player.rect.x = 325
player.rect.y = 300
player.center = (325,300)
player.OG_image = pygame.transform.scale(pygame.image.load("harpoongun.png"), (50,50))
all_sprites_list.add(player)

all_sprites_list.draw(screen)
spin = False
move = False
done = False
start = True
clock = pygame.time.Clock()
score = 0

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and start == True:
        player.spin()
        spin = True
    elif (spin == True and event.type != pygame.KEYDOWN) or (move == True):
        spin = False
        move = True
        player.move()

    screen.fill(white)
    
    blocks_hit = pygame.sprite.spritecollide(player,blocks,False)
        
    if len(blocks_hit) > 0:
        if blocks_hit[-1] == block_list[target]:
            block_list[target].rect.x = random.randrange(0, 650)
            block_list[target].rect.y -= 800
            target -= 1
            if target == -1:
                target = 3
            score += 1
            print(score)
        else:
            done = True

    for sprite in all_sprites_list:
        sprite.rect.y += 2
    
    all_sprites_list.draw(screen)
    
    clock.tick(20)
    
    pygame.display.flip()

pygame.quit()
    
