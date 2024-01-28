import pygame
import sys
import random

### START
pygame.init ()
pygame.mixer.init()
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

############## UI staer game ############################### -*- coding=utf-8 -*-
start_game = pygame.image.load(r'Image\start_game_1.png')
start_game_rect = start_game.get_rect(center=(x_screen/2,600))
start_game = pygame.transform.scale(start_game,(210,91))

start_game2 = pygame.image.load(r'Image\start_game_2.png')
start_game2_rect = start_game2.get_rect(center=(x_screen/2,600))
start_game2 = pygame.transform.scale(start_game2,(215,91))

UI_start_game = pygame.image.load(r'Image\UI_start_game.jpg')
UI_start_game = pygame.transform.scale(UI_start_game,(900,507))


############# set mouse and hole ###########################
# Mouse
mouse = pygame.image.load(r'Image\Mouse.png')
mouse = pygame.transform.scale(mouse,(110,110))
stunned_mouse = pygame.image.load(r'Image\mouse stunned.jpg')
stunned_mouse = pygame.transform.scale(stunned_mouse,(110,110))
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
    
def display_stunned_mouse():
    for mouse_appear in list_mouse_appear:
        screen.blit(stunned_mouse,mouse_appear)
################## end set mouse and hole ############################

#Hammer
hammer = pygame.image.load(r'Image\Hammer.png')
hammer = pygame.transform.scale(hammer,(90,90))
hammer_rect = hammer.get_rect(center=(x_screen/2,y_screen/2))

#sound Hammer
click_sound = pygame.mixer.Sound(r'Sound\sfx_wing.wav') 
hit_sound = pygame.mixer.Sound(r'Sound\sfx_hit.wav') 
back_ground_sound = pygame.mixer.Sound(r'Sound\01-FAIRY-TAIL-Main-Theme-Takanashi-Yasuharu.mp3') 
back_ground_sound.set_volume(0.01)
#hammer animation
original_hammer_frames  = [pygame.image.load(r'Animation\hammer_ani\0001.png'), pygame.image.load(r'Animation\hammer_ani\0002.png'), pygame.image.load(r'Animation\hammer_ani\0003.png'), pygame.image.load(r'Animation\hammer_ani\0004.png'),pygame.image.load(r'Animation\hammer_ani\0005.png')]
hammer_frames = [pygame.transform.scale(frame, (90, 90)) for frame in original_hammer_frames]
current_hammer_frame = 0
frame_counter = 0
frame_threshold = 10
# Flag to control animation
play_animation = False
show_static_hammer = True
pygame.mouse.set_visible(False)
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

start_time = pygame.time.get_ticks()

flag_appear = 0
flag_disappear = 0

clock = pygame.image.load(r'Image\clock.png')
clock = pygame.transform.scale(clock,(50,50))

timer_countdown = 60
timer_countdown_font = pygame.font.Font(None,72)
def display_timer_countdown():
    if(timer_countdown >= 60):  
        text_timer_countdown = timer_countdown_font.render("01:00",True,(255,255,0))
    elif(timer_countdown < 10):
        text_timer_countdown = timer_countdown_font.render("00:0" + str(timer_countdown),True,(255,255,0))
    else:
        text_timer_countdown = timer_countdown_font.render("00:" + str(timer_countdown),True,(255,255,0))
    screen.blit(text_timer_countdown,(300,12))

start_game_display = True
game_play = True



######################### game loop ###########################
counter_list = []
run = True
while run:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            run = False
            
            
        if(event.type == timer_interrup and game_play and start_game_display == False):    
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
            if(start_game_display == False):
                if game_play and not play_animation:
                    play_animation = True
                    show_static_hammer = False
                    click_sound.play()
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    frame_counter = 0
                    current_hammer_frame = 1
                    
                    # print(f'mouse: x {mouse_x}, y {mouse_y}')
                    for hole in hole_have_mouse:
                        #xử lí khi đập trúng chuột
                        if (mouse_x >= hole[2] and mouse_x <= hole[3]) and (mouse_y >= hole[0] and mouse_y <= hole[1]):
                            first_time = pygame.time.get_ticks()
                            
                            second_time = pygame.time.get_ticks()
                            while second_time-first_time<300:
                                display_stunned_mouse()
                                pygame.display.update()                 
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
                        start_game_display = True
                    # print(f'mouse: x {mouse_x}, y {mouse_y}')
            
            else:
                
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if (mouse_x >= 343 and mouse_x <= 557) and (mouse_y >= 555 and mouse_y <= 646):
                    start_game_display = False
                    game_play = True
                    score = 0
                    timer_countdown = 60
                         

    #343 -> 557; 555 # y: 555 -> 646
    #draw background
    if(start_game_display):
        pygame.mouse.set_visible(True)
        back_ground_sound.play()   
        white = (255, 255, 255)
        screen.fill(white)
        screen.blit(UI_start_game,(0,40))
        screen.blit(start_game,start_game_rect)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if(mouse_x >= 343 and mouse_x <= 557) and (mouse_y >= 555 and mouse_y <= 646):
            screen.blit(start_game2,start_game2_rect)
        
    else:
        pygame.mouse.set_visible(False)
        back_ground_sound.stop()
        screen.blit(bg,(0,0))
        screen.blit(bg2,(0,0))
        
        screen.blit(clock,(235,10))
        display_score()
        display_timer_countdown()
        if(game_play):
            
            #randon draw mouse
            display_mouse()
            
            
            #dwaw hammer
            hammer_rect.center = pygame.mouse.get_pos()
            if show_static_hammer:
                screen.blit(hammer,hammer_rect)
            if play_animation:
                # Draw the hammer with animation
                screen.blit(hammer_frames[current_hammer_frame], hammer_rect)

                # Update hammer animation frames
                frame_counter += 1
                if frame_counter >= frame_threshold:
                    current_hammer_frame = (current_hammer_frame + 1) % len(hammer_frames)
                    frame_counter = 0

                # Stop the animation after playing once
                if current_hammer_frame == 0:
                    play_animation = False
                    show_static_hammer = True
            
            
            if(timer_countdown <= 0):
                game_play = False
                
        
        else:
            play_animation = False
            pygame.mouse.set_visible(True)
            screen.blit(gameOver,gameOver_rect)
            hole_have_mouse.clear()
            list_mouse_appear.clear()
    
    pygame.display.update()
pygame.mouse.set_visible(True)