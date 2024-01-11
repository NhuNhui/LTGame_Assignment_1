import pygame
import sys
import random

### START
pygame.init ()

############## set background game ####################
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

############## end set background ######################

############# set mouse and hole ###########################
# Mouse
mouse = pygame.image.load(r'Image\Mouse.png')
mouse = pygame.transform.scale(mouse,(110,110))
#hole position
holes = [[75,180],[470,180],[740,180],[250,240],[430,300],[670,270]
         ,[40,300],[210,420],[720,390],[90,540],[350,620],[690,570],[470,470]]
for hole in holes:
    hole[0] += 55
    hole[1] += 55
    
hole_mouse = []
for hole in holes:
    hole_mouse.append(mouse.get_rect(center = (hole[0],hole[1])))
    
hole_list = []
for hole in holes:
    top, down, left, right = hole[1] - 55, hole[1] + 55, hole[0] - 55, hole[0] + 55 
    hole_list.append([top,down,left,right])

list_mouse_appear = []
hole_have_mouse = []
# for hole in holes:
#     # print(i)
#     random_mouse = mouse.get_rect(center = (hole[0],hole[1]))
#     list_mouse_appear.append(random_mouse)
# print(hole_list)

def display_mouse():
    for mouse_appear in list_mouse_appear:
        screen.blit(mouse,mouse_appear)

################## end set mouse and hole ############################

#Hammer
hammer = pygame.image.load(r'Image\Hammer.png')
hammer = pygame.transform.scale(hammer,(90,90))
hammer_rect = hammer.get_rect(center=(x_screen/2,y_screen/2))

#sound Hammer
click_sound = pygame.mixer.Sound(r'Sound\sfx_wing.wav') 
hit_sound = pygame.mixer.Sound(r'Sound\sfx_hit.wav') 
#Score
score = 0
score_font = pygame.font.Font(None,72)
def display_score():
    text_score = score_font.render(str(score),True,(255,255,255))
    screen.blit(text_score,(800,10))
    
################# set game over ###################################
gameOver = pygame.image.load(r'Image\game_over.png')
gameOver = pygame.transform.scale(gameOver,(500,400))
gameOver_rect = gameOver.get_rect(center=(x_screen/2,y_screen/2))
#set timer
timer_interrup = pygame.USEREVENT
pygame.time.set_timer(timer_interrup,100)

flag_appear = 0
flag_disappear = 0


timer_countdown = 60
timer_countdown_font = pygame.font.Font(None,72)
def display_timer_countdown():
    text_timer_countdown = timer_countdown_font.render(str(timer_countdown),True,(0,0,0))
    screen.blit(text_timer_countdown,(500,10))
    
game_play = True

######################### game loop ###########################
counter_list = []
run = True
while run:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            run = False
            
        if(event.type == timer_interrup and game_play):    
            flag_appear += 1
            flag_disappear += 1
            if(flag_appear >= 10): #mỗi 1s sẽ xuất hiện con chuột
                timer_countdown -= 1
                flag_appear = 0
                #todo
                counter = random.randint(0,12)
                counter_list.append(counter)
                
                list_mouse_appear.append(hole_mouse[counter])
                hole_have_mouse.append(hole_list[counter])
            
            if(flag_disappear >= 20): #con chuột xuất hiện mỗi 2s r biến mất  
                flag_disappear = 0
                if(len(list_mouse_appear) > 0):
                    list_mouse_appear.pop(0)
                if(len(hole_have_mouse) > 0):
                    hole_have_mouse.pop(0)
        
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Xử lý khi có click chuột
            
            if(game_play):
                click_sound.play()
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # print(f'mouse: x {mouse_x}, y {mouse_y}')
                for hole in hole_have_mouse:
                    #xử lí khi đập trúng chuột
                    if (mouse_x >= hole[2] and mouse_x <= hole[3]) and (mouse_y >= hole[0] and mouse_y <= hole[1]):
                        score += 1
                        print(f'Score: {score}')
                        hit_sound.play()
                        # xử lí sau khi đập
                        index_delete = hole_list.index(hole)
                        hole_have_mouse.remove(hole)
                        list_mouse_appear.remove(hole_mouse[index_delete])
                        break
            else:
                
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if(mouse_x > 317 and mouse_x < 400) and (mouse_y > 544 and mouse_y < 576):
                    game_play = True
                    score = 0
                if((mouse_x > 524 and mouse_x < 588) and (mouse_y > 543 and mouse_y < 577)):
                    run = False
                # print(f'mouse: x {mouse_x}, y {mouse_y}')
            
            
    #draw background     
    screen.blit(bg,(0,0))
    screen.blit(bg2,(0,0))
    if(game_play):
        
        #randon draw mouse
        display_mouse()
        
        
        #dwaw hammer
        hammer_rect.center = pygame.mouse.get_pos()
        screen.blit(hammer,hammer_rect)
        display_score()
        display_timer_countdown()
        if(timer_countdown <= 0):
            game_play = False
            timer_countdown = 60
    
    else:
        screen.blit(gameOver,gameOver_rect)
    
    pygame.display.update()