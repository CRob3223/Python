#Bubblesort visualizer utilizing pygame from https://www.geeksforgeeks.org/bubble-sort-visualizer-using-pygame/

import pygame

pygame.init()

win = pygame.display.set_mode((700, 600))
pygame.display.set_caption("Bubble Sort")

x = 40
y = 40

width = 20

height = [200, 50, 130, 90, 250, 61, 110,
            88, 33, 80, 70, 159, 180, 20]

run = True

def show(height):

    for i in range(len(height)):

        pygame.draw.rect(win, (0, 200, 20), (x + 30 * i, y, width, height[i]))

while run:

    execute = False

    pygame.time.delay(20)

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            run = False

    if keys[pygame.K_SPACE]:

        execute = True

    if execute == False:

        win.fill((0, 0, 0))

        show(height)

        pygame.display.update()

  
    else:
 
        
        for i in range(len(height) - 1):
 
           
            for j in range(len(height) - i - 1):
 
                
                if height[j] > height[j + 1]:
 
                    
                   
                    t = height[j]
                    height[j] = height[j + 1]
                    height[j + 1] = t
 
                
                win.fill((0, 0, 0))
 
                
                show(height)
 
                
                pygame.time.delay(50)
 
               
                pygame.display.update()
 

pygame.quit()        