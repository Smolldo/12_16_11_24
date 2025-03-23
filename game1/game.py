import pygame
import time

pygame.init()

pygame.display.set_caption('Моя перша гра')
screen = pygame.display.set_mode((1280, 720))

screen.fill((0,23,171))
pygame.display.flip()

# font = pygame.font.Font(None, 36)
# text = font.render('Привіт, геймери!', True, (0, 255, 0))
# screen.blit(text, (50, 50))
# pygame.display.flip()


# pygame.draw.line(screen, (255, 0, 0), (100, 50), (500, 650), 15)
# pygame.draw.circle(screen, (0,0,0), (640, 360), 40, 5)
pygame.draw.rect(screen, (255,0,0), (50,50, 300,300), 5, 50)

pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    

    
pygame.quit()