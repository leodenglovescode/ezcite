import pygame
from pygame.locals import *
from pygame import mixer
import os




def credsmusic():
    pygame.init()
    screen=pygame.display.set_mode([900,600])
    cwd_font = os.getcwd() + r'\assets\fonts\Ubuntu-Regular.ttf'
    cwd_music = os.getcwd() + r'\assets\sound\swmt.mp3'

    yellow = (255,255,0)
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    darkBlue = (0,0,128)
    white = (255,255,255)
    black = (0,0,0)
    pink = (255,200,200)



    mixer.init()
    mixer.music.load(cwd_music)
    mixer.music.set_volume(0.2)
    mixer.music.play()



    #closing credits or end credits are a list of the movie cast or crew
    movie_credits = '''

























    Credits:










    Programmers:

    Leodeng

    Allen Wang








    Sound Effects:
    BFXR - Sound effects for 8 bit games 
    https://www.bfxr.net/










    Code:
    GFG - Geeks For Geeks
    https://www.geeksforgeeks.org/
    how-to-make-rounded-buttons-in-tkinter/

    https://www.geeksforgeeks.org/
    open-a-new-window-with-a-button-in-python-tkinter/










    Texture(Buttons):
    ClickMind Button Generator 
    https://www.clickminded.com/button-generator/











    Scrolling text: 
    HAPPY CHUCK PROGRAMMING Youtube Channel 
    https://www.youtube.com/watch?v=Vbj-CtchRSI













    Music:
    Star Wars (Main Theme) - John Williams 
    https://www.youtube.com/watch?v=MNMSAIG0dfQ

























































    u still here?
    well thats fun! :3
    happy easteregg day! 
    :D :3 :>
    '''


    centerx, centery = screen.get_rect().centerx, screen.get_rect().centery
    deltaY = centery + 50  # adjust so it goes below screen start


    running =True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        screen.fill(0)
        deltaY-= 1
        i=0
        msg_list=[]
        pos_list=[]
        
        font = pygame.font.Font(cwd_font, 29)

        #msg = font.render('Hello there, how are you?', True, red)
        for line in movie_credits.split('\n'):
            msg=font.render(line, True, yellow)
            msg_list.append(msg)
            pos= msg.get_rect(center=(centerx, centery+deltaY+30*i))
            pos_list.append(pos)
            i=i+1
    
        #pos = msg.get_rect(center=(centerx, centery+deltaY))
        

        #if (centery + deltaY < 0):
        #   running = False         # no repetition - once text scrolls up past screen, over 
            
        #screen.blit(msg, pos)
        for j in range(i):
            screen.blit(msg_list[j], pos_list[j])
            
        pygame.display.update()


    pygame.quit()
credsmusic()
        
        