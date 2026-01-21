import pygame
import random
from sys import exit

pygame.init() #starts pygame
pygame.mixer.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('W.H.A.T')
clock = pygame.time.Clock()

# fonts
font = pygame.font.Font('JMH Typewriter.ttf', 40)
font2 = pygame.font.Font('JMH Typewriter.ttf', 20)

title_img = pygame.image.load('W_H_A_T.png').convert_alpha()
title_img = pygame.transform.scale(title_img, (500,500))

text_title = "Walker Harold Agency Test"
text_title_displayed = ""
text_title_index = 0

typing_speed = 3
frame_count = 0

txt_tit_pos = 0
txt_tit_pos_speed = 0.2

ti_img_x_pos = 0
img_speed = 0.1

game_state = "menu"
text_start = font.render('START', True, 'White')
txt_start_rect = text_start.get_rect(midtop = (1075, 300))

#game
info = [
    "Your a test subject from W.H.A.T. Your goal today is answer their following assessments.",
    "Obey the Law and you will be fine, disobey them will lead to consequences.",
    "Good luck... Test Subject #6..."
]

current_text = 0
displayed_text = ""
char_index = 0
shown_lines = []


text_exit = font.render('EXIT', True, 'White')
txt_exit_rect = text_exit.get_rect(midbottom = (1075, 500))

#next scene inputs or test qustions
#q1
q1_input = ""

#audio
menu_music = False

#sound effect
typewriter_sound = pygame.mixer.Sound("sounds/Typewriting-seconds.MP3")
typewriter_sound.set_volume(0.5)

#q3 sfx
whisper_sound = pygame.mixer.Sound("sounds/whispers.MP3")
whisper_sound.set_volume(0.7)

whisper_played = False
whisper_time = 0

heard_something = None

#q4
glitch_timer = 0
glitch_text = "[REDACTED]"

glitched_q5 = False
glitch_name = q1_input
glitch5_timer = 0

#6 question

eerie_sound = pygame.mixer.Sound("sounds/eerie-atmosphere-ambience-372558.mp3")
eerie_sound.set_volume(0.5)

cat_img = pygame.image.load("cat.jpg").convert_alpha()
cat_img = pygame.transform.scale(cat_img, (450, 350))
cat_img_rect = cat_img.get_rect(center=(690,510))

anomaly_img = pygame.image.load("home.png").convert_alpha()
anomaly_img = pygame.transform.scale(anomaly_img, (400, 300))
anomaly_img_rect = anomaly_img.get_rect(center=(880, 500))

glitch6_timer = 0
base_img_text = "image?"
glitch_img = base_img_text

glitched_6 = False

post_end_timer = 0
post_end_stage = 0

while True:
    frame_count += 1
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()   
            exit()

        # ===> MAIN MENU LOGICS
        if game_state == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if txt_exit_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    exit()

                if txt_start_rect.collidepoint(mouse_pos):
                    game_state = "game"

                    pygame.mixer.music.fadeout(1000)

                    #reset
                    frame_count = 0
                    current_text = 0
                    displayed_text = ""
                    menu_music = False
                    char_index = 0

        elif game_state == "game":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if char_index < len(info[current_text]):
                    displayed_text = info[current_text]
                    char_index = len(info[current_text])
                    typewriter_sound.stop()
                else:
                    shown_lines.append(displayed_text)
                    displayed_text = ""
                    char_index = 0
                    if current_text < len(info) - 1:
                        current_text += 1
                    else:
                        game_state = "next_scene"

        #next sequence / q1
        elif game_state == "next_scene":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    q1_input = q1_input[:-1]
                elif event.key == pygame.K_RETURN:
                    glitch_name = q1_input
                    game_state = "question2"
                else:
                    q1_input += event.unicode

        #2nd 
        elif game_state == "question2":
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if yes_btn.collidepoint(mouse_pos) or no_btn.collidepoint(mouse_pos):
                    game_state = "question3"
                    whisper_time = pygame.time.get_ticks()
                    whisper_played = False

        #3rd
        elif game_state == "question3":
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if yes3_btn.collidepoint(mouse_pos):
                    heard_something = True
                    game_state = "question4"

                elif no3_btn.collidepoint(mouse_pos):
                    heard_something = False
                    game_state = "question4"

        elif game_state == "question4" and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if yes4_btn.collidepoint(mouse_pos):
                if heard_something:
                    print("Answer4: GLTICHED")
                    game_state = "question5"
                    glitched_q5 = True
                else:
                    glitched_q5 = False
                game_state = "question5"
                
            elif no4_btn.collidepoint(mouse_pos):
                glitched_q5 = False
                game_state = "question5"

        elif game_state == "question5" and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if yes5_btn.collidepoint(mouse_pos):
                game_state = "question6"
            
            
            elif no5_btn.collidepoint(mouse_pos):
                glitched_q5 = False
                game_state = "question6"

        #game last
        elif game_state == "question6" and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if yes6_btn.collidepoint(mouse_pos):
                glitched_6 = True
                game_state = "post_end"
                
            elif no6_btn.collidepoint(mouse_pos):
                glitched_6 = False
                game_state = "post_end"


    # ====> DRAWINGS AND ANIMATION ==> MENU
    if game_state == "menu":
        screen.fill((0,0,0))
        screen.blit(text_start,txt_start_rect)
        screen.blit(text_exit, txt_exit_rect)

        #Menu music
        if not menu_music: 
            pygame.mixer.music.load("music/old-nuclear-factory-atmo-drone-thriller-9358.mp3")
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1, fade_ms=2000)
            menu_music = True

        if ti_img_x_pos < 100:
            ti_img_x_pos += (100 - ti_img_x_pos) * img_speed

        if txt_tit_pos < 100:
            txt_tit_pos += (100 - txt_tit_pos) * txt_tit_pos_speed

        if frame_count % typing_speed == 0 and text_title_index < len(text_title):
            text_title_displayed += text_title[text_title_index]
            text_title_index += 1

        text_title_surface = font.render(text_title_displayed, True, 'White')
        screen.blit(text_title_surface, (txt_tit_pos, 160))
        screen.blit(title_img,(ti_img_x_pos,-50)) #x and y cartesian plane
    
    # ====> DRAWINGS AND ANIMATION ==> GAMEPLAY 
    elif game_state == "game":
        screen.fill((0,0,0))
        frame_count += 1
        y = 180

        for line in shown_lines:
            surf = font2.render(line, True, 'White')
            rect = surf.get_rect(center=(640, y))
            screen.blit(surf, rect)
            y += 30
        
        typing_surface = font2.render(displayed_text, True, 'White')
        typing_rect = typing_surface.get_rect(center=(640, y))
        screen.blit(typing_surface, typing_rect)
        
        if frame_count % typing_speed == 0 and char_index < len(info[current_text]):
                char = info[current_text][char_index]
                displayed_text += info[current_text][char_index]
                char_index += 1
                
                if char != " " and not typewriter_sound.get_num_channels():
                    typewriter_sound.play()

        if char_index >= len(info[current_text]):
            hint_surface = font2.render("Click to continue...", True, 'White')
            hint_rect = hint_surface.get_rect(center=(640, 680))
            screen.blit(hint_surface, hint_rect)
    
    elif game_state == "next_scene":
        screen.fill((0,0,0))

        question1 = font2.render("What is your name? Test Subject #6?", True, 'White')
        question1_rect = question1.get_rect(center=(640, 100))
        screen.blit(question1, question1_rect)

        input_box = pygame.Rect(440, 200, 400, 50)
        pygame.draw.rect(screen, (255,255,255), input_box, 2)

        input_text = font2.render(q1_input, True, 'White')
        screen.blit(input_text, (input_box.x + 5, input_box.y + 10))

    elif game_state == "question2":
        screen.fill((0,0,0))

        question2_text = font2.render(f"Okay {q1_input}. Have you heard any weird phenomena?", True, 'White')
        question2_rect = question2_text.get_rect(center=(640, 100))
        screen.blit(question2_text, question2_rect)

        yes_btn = pygame.Rect((440, 250, 150, 50))
        no_btn = pygame.Rect((690, 250, 150, 50))

        pygame.draw.rect(screen, (0,200,0), yes_btn)
        yes_text = font2.render("YES", True, 'White')
        yes_rect = yes_text.get_rect(center=yes_btn.center)
        screen.blit(yes_text, yes_rect)

        pygame.draw.rect(screen, (0,200,0), no_btn)
        no_text = font2.render("NO", True, 'White')
        no_rect = no_text.get_rect(center=no_btn.center)
        screen.blit(no_text, no_rect)

    elif game_state == "question3":
        screen.fill((0,0,0))

        current_time = pygame.time.get_ticks()

        if not whisper_played and current_time - whisper_time > 1500:
            whisper_sound.play()
            whisper_played = True

        question3_text = font2.render(f"Fair enough {q1_input}... Do you hear something strange?", True, 'White')
        question3_rect = question3_text.get_rect(center=(640, 100))
        screen.blit(question3_text, question3_rect)

        yes3_btn =pygame.Rect((440, 250, 150, 50))
        no3_btn = pygame.Rect((690, 250, 150, 50))

        pygame.draw.rect(screen, (0,0, 30), yes3_btn)
        yes3_text = font2.render("YES", True, 'White')
        yes3_rect = yes3_text.get_rect(center=yes3_btn.center)
        screen.blit(yes3_text, yes3_rect)

        pygame.draw.rect(screen, (0,0, 30), no3_btn)
        no3_text = font2.render("NO", True, 'White')
        no3_rect = no3_text.get_rect(center=no3_btn.center)
        screen.blit(no3_text, no3_rect)

    elif game_state == "question4":
        screen.fill((0,0,0))

        question4_text = "Okay? Have you ever felt something weird in your "

        if heard_something:
            glitch_timer += 1

            if glitch_timer % 20 == 0:
                glitch_text = "".join(random.choice("234%$#%@#$%#W$%$#") for _ in range(len("[REDACTED]")))
            life_text = glitch_text
            life_color = (200,0,0)
            yes4_btn =pygame.Rect((500, 250, 150, 50))
            no4_btn = pygame.Rect((750, 400, 150, 50))
        else:
            life_text ="life?"
            life_color = (255, 255, 255)
            yes4_btn =pygame.Rect((440, 250, 150, 50))
            no4_btn = pygame.Rect((690, 250, 150, 50))
        
        text1 = font2.render(question4_text, True, (255, 255, 255))
        text2 = font2.render(life_text, True, life_color)
        text1_rect = text1.get_rect(center=(640 - text2.get_width()//2, 200))
        text2_rect = text2.get_rect(midleft=(text1_rect.right, text1_rect.centery))
        screen.blit(text1, text1_rect)
        screen.blit(text2, text2_rect)
        

        pygame.draw.rect(screen, (0,0,30), yes4_btn)
        yes4_text = font2.render("YES", True, "White")
        yes4_rect = yes4_text.get_rect(center=yes4_btn.center)
        screen.blit(yes4_text, yes4_rect)

        pygame.draw.rect(screen, (0,0, 30), no4_btn)
        no4_text = font2.render("NO", True, "White")
        no4_rect = no4_text.get_rect(center=no4_btn.center)
        screen.blit(no4_text, no4_rect)
        
    elif game_state == "question5":
        screen.fill((0,0,0))

        question5_text = "Final question Test subject #6 are you ready? "

        if glitched_q5:
            glitch5_timer += 1

            if glitch5_timer % 10 == 0:
                glitch_name = "".join(random.choice("123456789") for _ in range(len(f"{q1_input}")))
            name_text = glitch_name
            name_color = (255, 0, 255)
            yes5_btn = pygame.Rect((500, 250, 150, 50))
            no5_btn = pygame.Rect((703, 99, 100, 500))
        else:
            name_text = q1_input
            name_color = (255, 255, 255)
            yes5_btn = pygame.Rect((440, 250, 150, 50))
            no5_btn = pygame.Rect((690, 250, 150, 50))

        text1 = font2.render(question5_text, True, (255, 255, 255))
        text2 = font2.render(name_text, True, name_color)
        text1_rect = text1.get_rect(center=(640 - text2.get_width()//2, 200))
        text2_rect = text2.get_rect(midleft=(text1_rect.right, text1_rect.centery))
        screen.blit(text1, text1_rect)
        screen.blit(text2, text2_rect)

        pygame.draw.rect(screen, (0,0,30), yes5_btn)
        yes5_text = font2.render("Yes...", True, "White")
        yes5_rect = yes5_text.get_rect(center=yes5_btn.center)
        screen.blit(yes5_text, yes5_rect)

        pygame.draw.rect(screen, (0,0,30), no5_btn)
        no5_text = font2.render("No", True, "White")
        no5_rect = no5_text.get_rect(center=no5_btn.center)
        screen.blit(no5_text, no5_rect)
    
    elif game_state == "question6":
        screen.fill((0,0,0))

        sixth_text = f"Is there something wrong with this "

        if glitched_q5:
            glitch6_timer += 1

            if glitch6_timer % 10 == 0:
                glitch_img = "".join(random.choice("@$1q49") for _ in range(len(f"{base_img_text}")))

            img_color = (0, 255, 255)
            yes6_btn =pygame.Rect((569, 109, 34, 100))
            no6_btn = pygame.Rect((902, 23, 199, 34))
            screen.blit(anomaly_img, anomaly_img_rect)

            if not pygame.mixer.get_busy():
                eerie_sound.play(-1)
        else:
            glitch_img = base_img_text
            img_color = (255, 255, 255)
            yes6_btn = pygame.Rect((440, 250, 150, 50))
            no6_btn = pygame.Rect((690, 250, 150, 50))
            screen.blit(cat_img, cat_img_rect)

        text1 = font2.render(sixth_text, True, (255, 255, 255))
        text2 = font2.render(glitch_img, True, img_color)
        text1_rect = text1.get_rect(center=(640 - text2.get_width()//2, 200))
        text2_rect = text2.get_rect(midleft=(text1_rect.right, text1_rect.centery))
        screen.blit(text1, text1_rect)
        screen.blit(text2, text2_rect)

        pygame.draw.rect(screen, (0,0,30), yes6_btn)
        yes6_text = font2.render("There is", True, "White")
        yes6_rect = yes6_text.get_rect(center=yes6_btn.center)
        screen.blit(yes6_text, yes6_rect)

        pygame.draw.rect(screen, (0,0,30), no6_btn)
        no6_text = font2.render("Nothing", True, "White")
        no6_rect = no6_text.get_rect(center=no6_btn.center)
        screen.blit(no6_text, no6_rect)

    elif game_state == "post_end":
        screen.fill((0,0,0))
        post_end_timer += 1

        if post_end_stage == 0:
            end_text = font2.render(f"Result: {'There is something' if glitched_6 else 'Nothing'}", True, (255,255,255))
            end_rect = end_text.get_rect(center=(640, 300))
            screen.blit(end_text, end_rect)
            if post_end_timer > 120:
                post_end_timer = 0
                post_end_stage = 1

        elif post_end_stage == 1:
            fail_text1 = font2.render("Failed to load Test Subject #6.", True, (255, 0, 0))
            fail_text2 = font2.render("Restarting the program...", True, (255, 255, 0))
            screen.blit(fail_text1, fail_text1.get_rect(center=(640, 280)))
            screen.blit(fail_text2, fail_text2.get_rect(center=(640, 350)))
            if post_end_timer > 120:
                post_end_timer = 0 
                post_end_stage = 2
        
        elif post_end_stage == 2:
            credits_text = font2.render("Thanks for playing! Made by Tom", True, (0, 255, 0))
            screen.blit(credits_text, credits_text.get_rect(center=(640, 300)))
            if post_end_timer > 180:
                game_state = "menu"
                frame_count = 0
                current_text = 0
                displayed_text = ""
                char_index = 0
                shown_lines = []

                q1_input = ""
                glitch_name = ""
                glitched_q5 = False
                glitched_6 = False
                glitch_img = base_img_text
                
                post_end_timer = 0
                post_end_stage = 0

    if game_state != "question6":
        eerie_sound.stop()


    pygame.display.flip()
    clock.tick(60)