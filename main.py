import pygame

print('Setup Start')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print('Setup End')

print('loop Start')
while True:
    # check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            _  # Close window
            quit()
            _  # end pygame
