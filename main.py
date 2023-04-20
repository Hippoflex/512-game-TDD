import sys
import pygame

from logics import *

mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

mas[0][3] = 2
mas[3][2] = 4

COLORS = {
    0: (130, 130, 130),
    2: (255, 255, 200),
    4: (255, 255, 128),
    8: (255, 255, 0),
    16: (255, 228, 0),
    32: (255, 175, 67),
    64: (255, 100, 0),
    128: (255, 32, 0),
    256: (255, 0, 34),
    512: (240, 0, 0),
    2048: (128, 0, 0)
}

WHITE = (255, 255, 255)
GRAY = (130, 130, 130)
BLACK = (0, 0, 0)

BLOCK = 4
SIZE_BLOCK = 110
MARGIN = 10
WIDTH = BLOCK * SIZE_BLOCK + MARGIN * 5
HEIGHT = WIDTH + 110
TITLE_REC = pygame.Rect(0, 0, WIDTH, 110)


def drawing():

    font = pygame.font.SysFont("Calibre", 70)
    print_arr(mas)
    for row in range(BLOCK):
        for column in range(BLOCK):
            value = mas[row][column]
            text = font.render(f'{value}', True, BLACK)
            w = column * SIZE_BLOCK + (column + 1) * MARGIN
            h = row * SIZE_BLOCK + (row + 1) * MARGIN + 110
            pygame.draw.rect(screen, COLORS[value], (w, h, 110, 110))
            if value != 0:
                font_width, font_height = text.get_size()
                text_x = w + (SIZE_BLOCK - font_width) / 2
                text_y = h + (SIZE_BLOCK - font_height) / 2
                screen.blit(text, (text_x, text_y))


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("512")
drawing()
pygame.display.update()

print(empty_list(mas))

while zero_in_mas(mas):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                mas = to_the_left(mas)
            elif event.key == pygame.K_RIGHT:
                mas = to_the_right(mas)


            empty = empty_list(mas)

            random_num = empty.pop()
            x, y = get_index_from_number(random_num)
            mas = rand_2_4(mas, x, y)
            print(f'Элемент номер {random_num}')
            drawing()
            pygame.display.update()
