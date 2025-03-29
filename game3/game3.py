import pygame

pygame.init()

screen = pygame.display.set_mode((800,800))


x, y = 400, 300
speed = 20


running = True

while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print('натиснута ЛКМ')
            elif event.button == 2:
                print('СКМ натиснута')
        elif event.type == pygame.MOUSEMOTION:
            mouse_position = event.pos
            if mouse_position[0] % 10 == 0 and mouse_position[1] % 10 == 0:
                print(f'Координати курсора: {mouse_position}')
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         x -= speed
        #     elif event.key == pygame.K_RIGHT:
        #         x += speed
        #     elif event.key == pygame.K_UP:
        #         y -= speed
        #     elif event.key == pygame.K_DOWN:
        #         y += speed
        if keys[pygame.K_RCTRL] or keys[pygame.K_LCTRL]:
            if keys[pygame.K_c]:
                print('натиснуто CTRL + C')
        

    
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,0,0), (x, y, 50, 50))
    pygame.display.flip()




pygame.quit()