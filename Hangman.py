import pygame
from sys import exit


def game():
    '''
    This is the hangman GUI.
    :return:
    '''

    pygame.init()
    window = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Hangman")
    clock = pygame.time.Clock()

    # Colors
    BLACK = (0, 0, 0)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        window.fill((254, 254, 254)) # window background color (whitish)

        # Gallows
        pygame.draw.line(window, BLACK, (150, 100), (250, 100), 3)  # Top
        pygame.draw.line(window, BLACK, (250, 100), (250, 150), 3)  # Rope
        pygame.draw.line(window, BLACK, (150, 100), (150, 310), 3)  # Trunk
        pygame.draw.line(window, BLACK, (150, 310), (200, 310), 3)  # Base

        # Man
        pygame.draw.circle(window, BLACK, (250, 170), 20, 2)  # Head
        pygame.draw.line(window, BLACK, (250, 190), (250, 240), 2)  # Body
        pygame.draw.line(window, BLACK, (250, 195), (240, 240), 2)  # Left Arm
        pygame.draw.line(window, BLACK, (250, 195), (260, 240), 2)  # Right Arm
        pygame.draw.line(window, BLACK, (250, 240), (240, 280), 2)  # Left Leg
        pygame.draw.line(window, BLACK, (250, 240), (260, 280), 2)  # Right Leg

        pygame.display.update()
        clock.tick(60)


def main():
    game()



if __name__ == '__main__':
    main()