import pygame

class KOSHMAR(AssertionError):
    pass


if __name__ == '__main__':
    try:

        x = input().split()
        w, h = int(x[0]), int(x[1])
        pygame.init()
        pygame.display.set_caption('жесть, прямоугольник')
        size = width, height = w, h
        screen = pygame.display.set_mode(size)
        screen.fill(pygame.Color('black'))
        screen.fill(pygame.Color('red'), pygame.Rect(1, 1, w - 1, h - 1))

        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()

    except ValueError:
        print('Неправильный формат ввода')
    except KOSHMAR:
        print('Неправильный формат ввода')


