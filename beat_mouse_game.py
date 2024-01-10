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
for hole in holes:
    hole[0] += 55
    hole[1] += 55
    
hole_list = []
for hole in holes:
    top, down, left, right = hole[1] - 55, hole[1] + 55, hole[0] - 55, hole[0] + 55 
    hole_list.append([top,down,left,right])

list_mouse_appear = []

for hole in holes:
    # print(i)
    random_mouse = mouse.get_rect(center = (hole[0],hole[1]))
    list_mouse_appear.append(random_mouse)
# print(hole_list)


#Hammer
hammer = pygame.image.load(r'Image\Hammer.png')
hammer = pygame.transform.scale(hammer,(90,90))
hammer_rect = hammer.get_rect(center=(x_screen/2,y_screen/2))

#sound Hammer
click_sound = pygame.mixer.Sound(r'D:\HK232\Game\LTGame\Assignment_1\Sound\sfx_wing.wav') 
hit_sound = pygame.mixer.Sound(r'D:\HK232\Game\LTGame\Assignment_1\Sound\sfx_hit.wav') 
#Score
score = 0
score_font = pygame.font.Font(None,72)
def display_score():
    text_score = score_font.render(str(score),True,(255,255,255))
    screen.blit(text_score,(800,10))


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
            list_mouse_appear.append(hole_list[counter])
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Xử lý khi có click chuột
            click_sound.play()
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for hole in hole_list:
                #xử lí khi đập trúng chuột
                if (mouse_x >= hole[2] and mouse_x <= hole[3]) and (mouse_y >= hole[0] and mouse_y <= hole[1]):
                    score += 1
                    print(f'Score: {score}')
                    hit_sound.play()
            
            
    #draw background     
    screen.blit(bg,(0,0))
    screen.blit(bg2,(0,0))
    
    #randon draw mouse
    if(counter != -1):
        mouse_rect = list_mouse_appear[counter]
        screen.blit(mouse,mouse_rect)
    
    
    #dwaw hammer
    hammer_rect.center = pygame.mouse.get_pos()
    screen.blit(hammer,hammer_rect)
    display_score()
    
    pygame.display.update()