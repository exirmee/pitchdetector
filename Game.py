from threading import Thread
import pygame
from aubioAlgo import q, get_current_note


t = Thread(target=get_current_note)
t.daemon = True
t.start()

pygame.init()
screenWidth, screenHeight = 500, 500
screen = pygame.display.set_mode((screenWidth, screenHeight))
running = True

font = pygame.font.SysFont("comicsansms", 30)
noteText = font.render("C", True, (0, 128, 0))
hzText = font.render("hz", True, (0, 128, 0))
cntText = font.render("cnts", True, (0, 128, 0))

pygame.mixer.init(44100, -16, 2, 1024)
pygame.mixer.music.set_volume(0.8)


while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((125, 10, 44))
    
    # our user should be singing if there's a note on the queue
    if not q.empty():
        b = q.get()
        noteText = font.render(b['Note'], True, (0, 128, 0))
        hzText = font.render(str(b['hz']), True, (0, 128, 0))
        cntText = font.render(str(b['Cents']), True, (0, 128, 0))
        
    y=screenHeight-int(b['hz'])
    circlePitch = pygame.draw.circle(screen, (100,100,255), (20, y), 15, 5)
    
    

    screen.blit(noteText,(80, y-20))
    screen.blit(hzText,(80, y))
    screen.blit(cntText,(80, y+20))
    pygame.display.flip()
    


# Done! Time to quit.
pygame.quit()