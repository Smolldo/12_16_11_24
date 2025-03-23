import pygame

pygame.init()

screen = pygame.display.set_mode((900, 900))
original_image = pygame.image.load('84-847110_solid-snake-png-file-metal-gear-solid-4.png')

sprite_image = pygame.transform.scale(original_image, (100,100))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = sprite_image
        self.rect = self.image.get_rect()
        self.rect.center = (450,450)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x  -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x  += 5
        if keys[pygame.K_UP]:
            self.rect.y  -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y  += 5


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

running = True

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    all_sprites.update()

    screen.fill((255,255,255))

    all_sprites.draw(screen)

    pygame.draw.line(screen, (55,55,55), (50,50), (100,100), x)

    # pygame.draw.rect(screen, (255,0,0), (50, 50, 100,150))
    # pygame.draw.rect(screen, (0,255,0), (200, 100, 150,100))

    pygame.display.flip()


pygame.quit()