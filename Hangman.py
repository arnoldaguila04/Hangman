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

    # Input box
    base_font = pygame.font.Font(None, 32)
    input_box = pygame.Rect(150, 320, 100, 40)
    user_input = ""

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_input = user_input[0:-1]
                elif event.key == pygame.K_RETURN:
                    pass
                else:
                    user_input += event.unicode

        window.fill((254, 254, 254)) # window background color (whitish)

        draw_hangman(window, 0)

        # User input box
        pygame.draw.rect(window, ("Blue"), input_box, 2)
        text_surface = base_font.render(user_input, True, (0, 0, 0))
        window.blit(text_surface, (input_box.x + 5, input_box.y + 5))

        pygame.display.update()
        clock.tick(60)


def draw_hangman(window, chances):
    '''
    This function draws the hangman.
    :param window: pygame.display
    :param chances: int
    :return:
    '''
    BLACK = (0, 0, 0)

    if chances == 6:
        # Gallows
        pygame.draw.line(window, BLACK, (150, 100), (250, 100), 3)  # Top
        pygame.draw.line(window, BLACK, (250, 100), (250, 150), 3)  # Rope
        pygame.draw.line(window, BLACK, (150, 100), (150, 310), 3)  # Trunk
        pygame.draw.line(window, BLACK, (150, 310), (200, 310), 3)  # Base
    elif chances == 5:
        # Gallows
        pygame.draw.line(window, BLACK, (150, 100), (250, 100), 3)  # Top
        pygame.draw.line(window, BLACK, (250, 100), (250, 150), 3)  # Rope
        pygame.draw.line(window, BLACK, (150, 100), (150, 310), 3)  # Trunk
        pygame.draw.line(window, BLACK, (150, 310), (200, 310), 3)  # Base

        # Man
        pygame.draw.circle(window, BLACK, (250, 170), 20, 2)  # Head

    elif chances == 4:
        # Gallows
        pygame.draw.line(window, BLACK, (150, 100), (250, 100), 3)  # Top
        pygame.draw.line(window, BLACK, (250, 100), (250, 150), 3)  # Rope
        pygame.draw.line(window, BLACK, (150, 100), (150, 310), 3)  # Trunk
        pygame.draw.line(window, BLACK, (150, 310), (200, 310), 3)  # Base

        # Man
        pygame.draw.circle(window, BLACK, (250, 170), 20, 2)  # Head
        pygame.draw.line(window, BLACK, (250, 190), (250, 240), 2)  # Body

    elif chances == 3:
        # Gallows
        pygame.draw.line(window, BLACK, (150, 100), (250, 100), 3)  # Top
        pygame.draw.line(window, BLACK, (250, 100), (250, 150), 3)  # Rope
        pygame.draw.line(window, BLACK, (150, 100), (150, 310), 3)  # Trunk
        pygame.draw.line(window, BLACK, (150, 310), (200, 310), 3)  # Base

        # Man
        pygame.draw.circle(window, BLACK, (250, 170), 20, 2)  # Head
        pygame.draw.line(window, BLACK, (250, 190), (250, 240), 2)  # Body
        pygame.draw.line(window, BLACK, (250, 195), (240, 240), 2)  # Left Arm

    elif chances == 2:
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

    elif chances == 1:
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

    else:
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


def main():
    game()


if __name__ == '__main__':
    main()