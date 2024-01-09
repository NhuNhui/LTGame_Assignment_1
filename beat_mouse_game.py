import pygame
import sys
import random

### START
pygame.init ()

pygame.display.set_caption("Game Đập chuột")
screen = pygame.display.set_mode((900,768))
x_screen = 900
y_screen = 768
#icon game
icon = pygame.image.load(r'Image\icon.jpeg')
pygame.display.set_icon(icon)

#create background
bg = pygame.image.load(r'Image\UI_down.png')
bg = pygame.transform.scale(bg,(x_screen,768))
bg2 = pygame.image.load(r'Image\UI_up.png')
bg2 = pygame.transform.scale(bg2,(x_screen,230))

# Mouse
mouse = pygame.image.load(r'Image\Mouse.png')
mouse = pygame.transform.scale(mouse,(110,110))
#hole position
holes = [[75,180],[470,180],[740,180],[250,240],[430,300],[670,270]
         ,[40,300],[210,420],[720,390],[90,540],[350,620],[690,570],[470,470]]
hole_list = []

for i in holes:
    print(i)
    random_mouse = mouse.get_rect(center = (i[0]+55,i[1]+55))
    hole_list.append(random_mouse)
print(hole_list)

random_counter = [0,1,2,3,4,5,6,7,8,9,10,11,12]

hammer = pygame.image.load(r'D:\HK232\Game\LTGame\Assignment_1\Image\Hammer.png')
hammer = pygame.transform.scale(hammer,(90,90))
hammer.set_colorkey((0, 0, 0))
hammer_rect = hammer.get_rect(center=(x_screen/2,y_screen/2))

#set timer
timer = pygame.USEREVENT
pygame.time.set_timer(timer,1000)
#game loop
counter = -1
run = True
while run:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            run = False
            
        if(event.type == timer):      
            counter = random.randint(0,12)
            
            
            
    screen.blit(bg,(0,0))
    screen.blit(bg2,(0,0))
    
    #randon draw mouse
    if(counter != -1):
        mouse_rect = hole_list[counter]
        screen.blit(mouse,mouse_rect)
    
    
    #dwaw hammer
    hammer_rect.center = pygame.mouse.get_pos()
    screen.blit(hammer,hammer_rect)
    
    
    pygame.display.update()