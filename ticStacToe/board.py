import pygame
import math

pygame.init()

WIDTH = 500
GUI_WIDTH = WIDTH/2
ROWS = 4
win = pygame.display.set_mode((WIDTH + GUI_WIDTH, WIDTH))
pygame.display.set_caption("TicStacToe")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

X_IMAGE = pygame.transform.scale(pygame.image.load("X_image.png"), (100,100))
O_IMAGE = pygame.transform.scale(pygame.image.load("O_image.png"), (100,100))
Both = pygame.transform.scale(pygame.image.load("Both.png"), (200,50))
Neutral = pygame.transform.scale(pygame.image.load("Neutral.png"), (200,50))
Remove = pygame.transform.scale(pygame.image.load("Remove.png"), (200,50))
BACKGROUND = pygame.transform.scale(pygame.image.load("wood.jpg"), (WIDTH,WIDTH))

dis_to_cen = WIDTH // ROWS // 2

def init_buttons():
    global images
    images.append((GUI_WIDTH/2,WIDTH*.7,Both))
    images.append((GUI_WIDTH/2,WIDTH*.5,Neutral))
    images.append((GUI_WIDTH/2,WIDTH*.3,Remove))

def init_grid():
    dis_to_cen = WIDTH // ROWS // 2

    # Initializing the array
    game_array = [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]

    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            x = dis_to_cen * (2 * j + 1) + GUI_WIDTH
            y = dis_to_cen * (2 * i + 1)

            # Adding centre coordinates
            game_array[i][j] = (x, y,"")

    return game_array

def draw_grid():
    gap = WIDTH // ROWS

    # Starting points
    x = 0
    y = 0

    for i in range(ROWS):
        x = i * gap + GUI_WIDTH
        y = i * gap

        pygame.draw.line(win, GRAY, (x, 0), (x, WIDTH), 3)
        pygame.draw.line(win, GRAY, (GUI_WIDTH, y), (WIDTH + GUI_WIDTH, y), 3)

def click(game_array):
    global x_turn, images

    m_x, m_y = pygame.mouse.get_pos()
    for i in range(len(game_array)):
        for j in range(len(game_array[0])):
            x, y, piece = game_array[i][j]
            dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
            if dis < WIDTH // ROWS // 2:
                # remove previous piece
                
                if x_turn:
                    x_turn = False
                    if piece == 'x':
                        x_turn = True
                    else:
                        if piece == 'o':
                            images.remove((x, y, O_IMAGE))
                        images.append((x, y, X_IMAGE))
                        game_array[i][j] = (x, y, 'x')

                else:
                    x_turn = True
                    if piece == 'o':
                        x_turn = False
                    else:
                        if piece == 'x':
                            images.remove((x, y, X_IMAGE))
                        images.append((x, y, O_IMAGE))
                        game_array[i][j] = (x, y, 'o')

def check_win(game_array):
    # check rows
    for row in game_array:
        pieces = set([piece for _,_,piece in row])
        if len(pieces) == 1 and '' not in pieces:
            print("win")

    # check cols
    for cols in range(len(game_array[0])):
        pieces = set()
        for row in game_array:
            pieces.add(row[cols][2])
        if len(pieces) == 1 and '' not in pieces:
            print("win")

    # check diagonals
    diag1 = set()
    diag2 = set()
    for i, cols in enumerate(game_array[0]):
        for j, row in enumerate(game_array):
            if i == j:
                diag1.add(game_array[i][j][2])
            if i+j == len(game_array):
                diag2.add(game_array[i][j][2])
    if len(diag1) == 1 and '' not in diag1:
            print("win")
    if len(diag2) == 1 and '' not in diag2:
            print("win")

def render():
    win.fill(WHITE)
    draw_grid()
    for image in images:
        x, y, IMAGE = image
        win.blit(IMAGE, (x - IMAGE.get_width() // 2, y - IMAGE.get_height() // 2))

    pygame.display.update()

def main():
    global x_turn, images

    images = []
    run = True
    x_turn = True
    game_array = init_grid()
    images.append((GUI_WIDTH+WIDTH/2, WIDTH/2, BACKGROUND))
    init_buttons()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click(game_array)
                check_win(game_array)
        render()


while True:
    if __name__ == '__main__':
        main()

# 4x4

# moves:
# place up to 3 neutral
# place 1 colored + 1 neutral
# remove 2 pieces