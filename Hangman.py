import pygame
from sys import exit
from random import randint


def get_word(filename):
    '''
    This function gets and returns a random word from a text file that contains a lot of words.
    :param filename: String
    :return word_file_lines: String
    '''
    try: # checking to see if you have a file.
        with open(filename, "r") as word_file:
            word_file_lines = word_file.readlines()
            return word_file_lines[randint(0, len(word_file_lines) - 1)].strip()
    except FileNotFoundError:
        # PLACEHOLDER, PRINT AN ERROR MESSAGE ON THE GUI
        pass


def game(file):
    '''
    This is the hangman GUI.
    :param: file: String
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

    # game
    guesses = 6

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_input = user_input[0:-1]
                elif event.key == pygame.K_RETURN:
                    check(user_input)
                else:
                    user_input += event.unicode

        window.fill((254, 254, 254)) # window background color (whitish)

        draw_hangman(window, guesses)

        # User input box
        pygame.draw.rect(window, "blue", input_box, 2)
        text_surface = base_font.render(user_input, True, (0, 0, 0))
        window.blit(text_surface, (input_box.x + 5, input_box.y + 5))

        pygame.display.update()
        clock.tick(60)


def check(user_input):
    if len(user_input) > 1:
        if user_input == "end":
            # End Game
            pass
        elif user_input == "restart":
            # Restart game
            pass
        else:
            pass  # Error message
    else:
        pass


def draw_hangman(window, chances):
    '''
    This function draws the hangman.
    :param window: pygame.display
    :param chances: int
    :return:
    '''

    black = (0, 0, 0)

    if chances == 6:
        # Gallows
        pygame.draw.line(window, black, (150, 100), (250, 100), 3)  # Top
        pygame.draw.line(window, black, (250, 100), (250, 150), 3)  # Rope
        pygame.draw.line(window, black, (150, 100), (150, 310), 3)  # Trunk
        pygame.draw.line(window, black, (150, 310), (200, 310), 3)  # Base
    elif chances == 5:
        # Gallows
        pygame.draw.line(window, black, (150, 100), (250, 100), 3)  # Top
        pygame.draw.line(window, black, (250, 100), (250, 150), 3)  # Rope
        pygame.draw.line(window, black, (150, 100), (150, 310), 3)  # Trunk
        pygame.draw.line(window, black, (150, 310), (200, 310), 3)  # Base

        # Man
        pygame.draw.circle(window, black, (250, 170), 20, 2)  # Head

    elif chances == 4:
        # Gallows
        pygame.draw.line(window, black, (150, 100), (250, 100), 3)  # Top
        pygame.draw.line(window, black, (250, 100), (250, 150), 3)  # Rope
        pygame.draw.line(window, black, (150, 100), (150, 310), 3)  # Trunk
        pygame.draw.line(window, black, (150, 310), (200, 310), 3)  # Base

        # Man
        pygame.draw.circle(window, black, (250, 170), 20, 2)  # Head
        pygame.draw.line(window, black, (250, 190), (250, 240), 2)  # Body

    elif chances == 3:
        # Gallows
        pygame.draw.line(window, black, (150, 100), (250, 100), 3)  # Top
        pygame.draw.line(window, black, (250, 100), (250, 150), 3)  # Rope
        pygame.draw.line(window, black, (150, 100), (150, 310), 3)  # Trunk
        pygame.draw.line(window, black, (150, 310), (200, 310), 3)  # Base

        # Man
        pygame.draw.circle(window, black, (250, 170), 20, 2)  # Head
        pygame.draw.line(window, black, (250, 190), (250, 240), 2)  # Body
        pygame.draw.line(window, black, (250, 195), (240, 240), 2)  # Left Arm

    elif chances == 2:
        # Gallows
        pygame.draw.line(window, black, (150, 100), (250, 100), 3)  # Top
        pygame.draw.line(window, black, (250, 100), (250, 150), 3)  # Rope
        pygame.draw.line(window, black, (150, 100), (150, 310), 3)  # Trunk
        pygame.draw.line(window, black, (150, 310), (200, 310), 3)  # Base

        # Man
        pygame.draw.circle(window, black, (250, 170), 20, 2)  # Head
        pygame.draw.line(window, black, (250, 190), (250, 240), 2)  # Body
        pygame.draw.line(window, black, (250, 195), (240, 240), 2)  # Left Arm
        pygame.draw.line(window, black, (250, 195), (260, 240), 2)  # Right Arm

    elif chances == 1:
        # Gallows
        pygame.draw.line(window, black, (150, 100), (250, 100), 3)  # Top
        pygame.draw.line(window, black, (250, 100), (250, 150), 3)  # Rope
        pygame.draw.line(window, black, (150, 100), (150, 310), 3)  # Trunk
        pygame.draw.line(window, black, (150, 310), (200, 310), 3)  # Base

        # Man
        pygame.draw.circle(window, black, (250, 170), 20, 2)  # Head
        pygame.draw.line(window, black, (250, 190), (250, 240), 2)  # Body
        pygame.draw.line(window, black, (250, 195), (240, 240), 2)  # Left Arm
        pygame.draw.line(window, black, (250, 195), (260, 240), 2)  # Right Arm
        pygame.draw.line(window, black, (250, 240), (240, 280), 2)  # Left Leg

    else:
        # Gallows
        pygame.draw.line(window, black, (150, 100), (250, 100), 3)  # Top
        pygame.draw.line(window, black, (250, 100), (250, 150), 3)  # Rope
        pygame.draw.line(window, black, (150, 100), (150, 310), 3)  # Trunk
        pygame.draw.line(window, black, (150, 310), (200, 310), 3)  # Base

        # Man
        pygame.draw.circle(window, black, (250, 170), 20, 2)  # Head
        pygame.draw.line(window, black, (250, 190), (250, 240), 2)  # Body
        pygame.draw.line(window, black, (250, 195), (240, 240), 2)  # Left Arm
        pygame.draw.line(window, black, (250, 195), (260, 240), 2)  # Right Arm
        pygame.draw.line(window, black, (250, 240), (240, 280), 2)  # Left Leg
        pygame.draw.line(window, black, (250, 240), (260, 280), 2)  # Right Leg


def main():
    word = get_word("word_bank.txt")
    game(word)


if __name__ == '__main__':
    main()