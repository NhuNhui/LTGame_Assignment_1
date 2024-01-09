import pygame
pygame.init ()

pygame.display.set_caption("Đập chuột")
screen = pygame.display.set_mode((900,768))

#icon game
icon = pygame.image.load(r'Image\icon.jpeg')
pygame.display.set_icon(icon)

#create background
bg = pygame.image.load(r'Image\UI_down.png')
bg = pygame.transform.scale(bg,(900,768))

bg2 = pygame.image.load(r'Image\UI_up.png')
bg2 = pygame.transform.scale(bg2,(900,230))


mouse = pygame.image.load(r'Image\Mouse.png')
mouse = pygame.transform.scale(mouse,(110,110))


#game loop
run = True
while run:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            run = False
            
    screen.blit(bg,(0,0))
    screen.blit(bg2,(0,0))
    screen.blit(mouse,(100,100))
    pygame.display.update()