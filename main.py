import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))


#название окна приложения
pygame.display.set_caption('score and multiplication table')

#координаты игрока, которые можно регулировать
x = 50
y = 50
whdht = 40
height = 60
speed = 5

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    win.fill((0,0,0))
    pygame.draw.rect(win, (255,255,0), (x, y, whdht, height))
    pygame.display.update()

pygame.quit()