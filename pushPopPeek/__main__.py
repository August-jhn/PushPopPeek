import pygame
import math
from stack import *
from copy import *

pygame.init()

WIDTH = 500
GUI_WIDTH = WIDTH/2
ROWS = 4
win = pygame.display.set_mode((WIDTH + GUI_WIDTH, WIDTH))
pygame.display.set_caption("Push Pop Peek")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
TAN = (255, 220, 110)

BLACK_STONE = pygame.transform.scale(pygame.image.load("images/BlackGoStone.png"), (WIDTH/5,WIDTH/5))
WHITE_STONE = pygame.transform.scale(pygame.image.load("images/WhiteGoStone.png"), (WIDTH/5,WIDTH/5))
RED_STONE = pygame.transform.scale(pygame.image.load("images/RedGoStone.png"), (WIDTH/5,WIDTH/5))
BlackButton = pygame.transform.scale(pygame.image.load("images/BlackButton.png"), (GUI_WIDTH*.8,GUI_WIDTH*.2))
WhiteButton = pygame.transform.scale(pygame.image.load("images/WhiteButton.png"), (GUI_WIDTH*.8,GUI_WIDTH*.2))
Neutral = pygame.transform.scale(pygame.image.load("images/RedButton.png"), (GUI_WIDTH*.8,GUI_WIDTH*.2))
Remove = pygame.transform.scale(pygame.image.load("images/Remove.png"), (GUI_WIDTH*.8,GUI_WIDTH*.2))
EndTurn = pygame.transform.scale(pygame.image.load("images/EndTurn.png"), (GUI_WIDTH*.8,GUI_WIDTH*.2))
BACKGROUND = pygame.transform.scale(pygame.image.load("images/wood.jpg"), (WIDTH,WIDTH))
BLACKWIN = pygame.transform.scale(pygame.image.load("images/BlackWins.png"), (WIDTH*.75,WIDTH*.75))
WHITEWIN = pygame.transform.scale(pygame.image.load("images/WhiteWins.png"), (WIDTH*.75,WIDTH*.75))
# OUTOFMOVES = pygame.transform.scale(pygame.image.load("images/wood.jpg"), (WIDTH*.75,WIDTH*.75))

dis_to_cen = WIDTH // ROWS // 2

def init_buttons():
    global images, buttons, BlackButtonY, NeutralY, RemoveY, UndoY, EndTurnY
    images[GUI_WIDTH/2,WIDTH*.4] = BlackButton
    images[GUI_WIDTH/2,WIDTH*.525] = Neutral
    images[GUI_WIDTH/2,WIDTH*.65] = Remove
    images[GUI_WIDTH/2,WIDTH*.9] = EndTurn
    BlackButtonY = int(WIDTH*.4-WIDTH*.05)
    NeutralY = int(WIDTH*.525-WIDTH*.05)
    RemoveY = int(WIDTH*.65-WIDTH*.05)
    EndTurnY = int(WIDTH*.9-WIDTH*.05)
    buttons.append(pygame.Rect(GUI_WIDTH/2-GUI_WIDTH*.4,BlackButtonY,GUI_WIDTH*.8,GUI_WIDTH*.2)) # both
    buttons.append(pygame.Rect(GUI_WIDTH/2-GUI_WIDTH*.4,NeutralY,GUI_WIDTH*.8,GUI_WIDTH*.2)) # 3 red
    buttons.append(pygame.Rect(GUI_WIDTH/2-GUI_WIDTH*.4,RemoveY,GUI_WIDTH*.8,GUI_WIDTH*.2)) # remove
    buttons.append(pygame.Rect(GUI_WIDTH/2-GUI_WIDTH*.4,EndTurnY,GUI_WIDTH*.8,GUI_WIDTH*.2)) # end turn
    

def init_grid():
    dis_to_cen = WIDTH // ROWS // 2

    # Initializing the array
    coord_array = [[None for i in range(4)] for j in range(4)]
    stack_array = [[Stack() for i in range(4)] for j in range(4)]

    game_array = [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]

    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            x = dis_to_cen * (2 * j + 1) + GUI_WIDTH
            y = dis_to_cen * (2 * i + 1)

            # Adding center coordinates
            coord_array[i][j] = (x,y)

    return (stack_array,coord_array)

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

def click(stack_array, coord_array):
    global x_turn, images, max_moves, mode, buttons_locked, backup_stack_array, backup_images
    # check if any buttons are clicked
    pos = pygame.mouse.get_pos()
    clicked_sprites = [b for b in buttons if b.collidepoint(pos)]
    for i in clicked_sprites:
        print(i)
        if not buttons_locked:
            if i.y == BlackButtonY: # place 1 of each
                mode = "both"
                max_moves = 2
                buttons_locked = True
                print("both")

            elif i.y == NeutralY: # place 3 neutral
                mode = "neutral"
                max_moves = 3
                buttons_locked = True
                print("neutral")

            elif i.y == RemoveY: # remove 2
                mode = "remove"
                max_moves = 2
                buttons_locked = True
                print("remove")

        if i.y == EndTurnY: # end turn
            buttons_locked = False
            print("end turn")
            mode = "both"
            max_moves = 2
            x_turn = not x_turn
            if images[GUI_WIDTH/2, WIDTH*.4] == BlackButton:
                images[GUI_WIDTH/2, WIDTH*.4] = WhiteButton
            else:
                images[GUI_WIDTH/2, WIDTH*.4] = BlackButton

    m_x, m_y = pygame.mouse.get_pos()
    if max_moves <= 0:
        print("Out of Moves")
    else:
        for i in range(len(coord_array)):
            for j in range(len(coord_array)):
                x, y = coord_array[i][j]
                dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)

                stack = stack_array[i][j]
                piece = stack.peek()

                if dis < WIDTH // ROWS // 2:
                    # remove previous piece
                    
                    if piece:
                        # print(piece, 'peek')
                        # print(stack.print())
                        try:
                            images.pop((x, y)) # add to stack
                        except:
                            print('error')
                    max_moves -= 1
                    if mode == "neutral":
                        images[(x, y)] = RED_STONE

                        stack_array[i][j].push('red')

                        # game_array[i][j] = (x, y, 'red')
                    elif mode == 'both':
                        if x_turn:
                            images[(x, y)] = BLACK_STONE
                            # game_array[i][j] = (x, y, 'black')
                            stack_array[i][j].push('black')
                        else:
                            images[(x, y)] = WHITE_STONE
                            stack_array[i][j].push('white')
                        mode = 'neutral'
                    elif mode == 'remove':
                        # if piece:
                        #     images.pop((x,y))
                        if not stack.pop():
                            max_moves += 1
                        
                        if stack.peek() == 'white':
                            images[(x,y)] = WHITE_STONE
                        elif stack.peek() == 'black':
                            images[(x,y)] = BLACK_STONE
                        elif stack.peek() == 'red':
                            images[(x,y)] = RED_STONE
                        

def win_game(color):
    global run, winImage, center_x, center_y
    
    center_x = GUI_WIDTH + WIDTH/2
    center_y = WIDTH/2
    if color == 'black':
        winImage = BLACKWIN
        # images[center_x, center_y] = BLACKWIN
    else:
        winImage = WHITEWIN
        # images[center_x, center_y] = WHITEWIN
    run = False
                    

def check_win(stack_array):
    # check rows
    for row in stack_array:
        pieces = set([piece.peek() for piece in row])
        if len(pieces) == 1 and None not in pieces and 'red' not in pieces:
            win_game(row[0].peek())

    # check cols
    for col in range(len(stack_array[0])):
        pieces = set()
        for row in stack_array:
            pieces.add(row[col].peek())
        if len(pieces) == 1 and None not in pieces and 'red' not in pieces:
            win_game(stack_array[1][col].peek())

    # # check diagonals
    diag1 = set()
    
    diag2 = set()

    for i in range(len(stack_array)):
        diag1.add(stack_array[i][i].peek())
        diag2.add(stack_array[len(stack_array)-i-1][i].peek())

    if len(diag1) == 1 and None not in diag1 and 'red' not in diag1:
        win_game(stack_array[0][0].peek())
    if len(diag2) == 1 and None not in diag2 and 'red' not in diag2:
        win_game(stack_array[len(stack_array) - 1][0].peek())

def render():
    win.fill(TAN)
    draw_grid()
    for x,y in images:
        IMAGE = images[(x,y)]
        win.blit(IMAGE, (x - IMAGE.get_width() // 2, y - IMAGE.get_height() // 2))

    pygame.display.update()

def main():
    global x_turn, images, buttons, mode, buttons_locked, max_moves, run, winImage

    images = {}
    buttons = []
    run = True
    x_turn = True
    stack_array, coord_array = init_grid()
    images[(GUI_WIDTH+WIDTH/2, WIDTH/2)] = BACKGROUND
    

    mode = "both"
    max_moves = 2
    buttons_locked = False
    
    init_buttons()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click(stack_array, coord_array)
                check_win(stack_array)
        render()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
        win.blit(winImage, (center_x - winImage.get_width() // 2, center_y - winImage.get_height() // 2))
        pygame.display.update()


if __name__ == '__main__':
    main()

# 4x4

# moves:
# place up to 3 neutral
# place 1 colored + 1 neutral
# remove 2 pieces