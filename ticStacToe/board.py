import pygame
import math
from stack import *

pygame.init()

WIDTH = 1000
GUI_WIDTH = WIDTH/2
ROWS = 4
win = pygame.display.set_mode((WIDTH + GUI_WIDTH, WIDTH))
pygame.display.set_caption("TicStacToe")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
TAN = (255, 220, 110)

BLACK_STONE = pygame.transform.scale(pygame.image.load("BlackGoStone.png"), (WIDTH/5,WIDTH/5))
WHITE_STONE = pygame.transform.scale(pygame.image.load("WhiteGoStone.png"), (WIDTH/5,WIDTH/5))
RED_STONE = pygame.transform.scale(pygame.image.load("RedGoStone.png"), (WIDTH/5,WIDTH/5))
BlackButton = pygame.transform.scale(pygame.image.load("BlackButton.png"), (GUI_WIDTH*.8,GUI_WIDTH*.2))
WhiteButton = pygame.transform.scale(pygame.image.load("WhiteButton.png"), (GUI_WIDTH*.8,GUI_WIDTH*.2))
Neutral = pygame.transform.scale(pygame.image.load("RedButton.png"), (GUI_WIDTH*.8,GUI_WIDTH*.2))
Remove = pygame.transform.scale(pygame.image.load("Remove.png"), (GUI_WIDTH*.8,GUI_WIDTH*.2))
EndTurn = pygame.transform.scale(pygame.image.load("EndTurn.png"), (GUI_WIDTH*.8,GUI_WIDTH*.2))
Undo = pygame.transform.scale(pygame.image.load("Undo.png"), (GUI_WIDTH*.8,GUI_WIDTH*.2))
BACKGROUND = pygame.transform.scale(pygame.image.load("wood.jpg"), (WIDTH,WIDTH))

dis_to_cen = WIDTH // ROWS // 2

def init_buttons():
    global images, buttons, BlackButtonY, NeutralY, RemoveY, UndoY, EndTurnY
    images[GUI_WIDTH/2,WIDTH*.4] = BlackButton
    images[GUI_WIDTH/2,WIDTH*.525] = Neutral
    images[GUI_WIDTH/2,WIDTH*.65] = Remove
    images[GUI_WIDTH/2,WIDTH*.775] = Undo
    images[GUI_WIDTH/2,WIDTH*.9] = EndTurn
    BlackButtonY = int(WIDTH*.4-WIDTH*.05)
    NeutralY = int(WIDTH*.525-WIDTH*.05)
    RemoveY = int(WIDTH*.65-WIDTH*.05)
    UndoY = int(WIDTH*.775-WIDTH*.05)
    EndTurnY = int(WIDTH*.9-WIDTH*.05)
    buttons.append(pygame.Rect(GUI_WIDTH/2-GUI_WIDTH*.4,BlackButtonY,GUI_WIDTH*.8,GUI_WIDTH*.2)) # both
    buttons.append(pygame.Rect(GUI_WIDTH/2-GUI_WIDTH*.4,NeutralY,GUI_WIDTH*.8,GUI_WIDTH*.2)) # 3 red
    buttons.append(pygame.Rect(GUI_WIDTH/2-GUI_WIDTH*.4,RemoveY,GUI_WIDTH*.8,GUI_WIDTH*.2)) # remove
    buttons.append(pygame.Rect(GUI_WIDTH/2-GUI_WIDTH*.4,UndoY,GUI_WIDTH*.8,GUI_WIDTH*.2)) # undo
    buttons.append(pygame.Rect(GUI_WIDTH/2-GUI_WIDTH*.4,EndTurnY,GUI_WIDTH*.8,GUI_WIDTH*.2)) # end turn
    

def init_grid():
    dis_to_cen = WIDTH // ROWS // 2

    # Initializing the array
    coord_array = [[None for i in range(4)] for j in range(4)]
    stack_array = [[Stack("") for i in range(4)] for j in range(4)]

    game_array = [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]

    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            x = dis_to_cen * (2 * j + 1) + GUI_WIDTH
            y = dis_to_cen * (2 * i + 1)

            # Adding centre coordinates
            coord_array[i][j] = (x,y)
            # game_array[i][j] = (x, y,"")

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
    global x_turn, images, maxMoves, mode, buttonsLocked
    # check if any buttons are clicked
    pos = pygame.mouse.get_pos()
    clicked_sprites = [b for b in buttons if b.collidepoint(pos)]
    for i in clicked_sprites:
        print(i)
        if not buttonsLocked:
            if i.y == BlackButtonY: # place 1 of each
                mode = "both"
                maxMoves = 2
                buttonsLocked = True
                print("both")

            elif i.y == NeutralY: # place 3 neutral
                mode = "neutral"
                maxMoves = 3
                buttonsLocked = True
                print("neutral")

            elif i.y == RemoveY: # remove 2
                mode = "remove"
                maxMoves = 2
                buttonsLocked = True
                print("remove")

        if i.y == UndoY: # undo
            print("undo")
            buttonsLocked = False

        elif i.y == EndTurnY: # end turn
            buttonsLocked = False
            print("end turn")
            mode = "both"
            maxMoves = 2
            x_turn = not x_turn
            if images[GUI_WIDTH/2, WIDTH*.4] == BlackButton:
                images[GUI_WIDTH/2, WIDTH*.4] = WhiteButton
            else:
                images[GUI_WIDTH/2, WIDTH*.4] = BlackButton

    m_x, m_y = pygame.mouse.get_pos()
    if maxMoves <= 0:
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
                        print(piece, 'peek')
                        print(stack.print())
                        images.pop((x, y)) # add to stack
                    maxMoves -= 1
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
                    elif mode == 'remove':
                        # if piece:
                        #     images.pop((x,y))
                        stack.pop()
                        print(stack.peek())
                        
                        if stack.peek() == 'white':
                            images[(x,y)] = WHITE_STONE
                        elif stack.peek() == 'black':
                            images[(x,y)] = BLACK_STONE
                        elif stack.peek() == 'neutral':
                            images[(x,y)] = RED_STONE
                        


def win_game(color):
    print("YOUVE WONNNNNNN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", color)
    run = False
                    

def check_win(stack_array):
    # check rows
    for row in stack_array:
        pieces = set([piece.peek() for piece in row])
        if len(pieces) == 1 and '' not in pieces:
            win_game(row[0].peek())

    # check cols
    for col in range(len(stack_array[0])):
        pieces = set()
        for row in stack_array:
            pieces.add(row[col].peek())
        if len(pieces) == 1 and '' not in pieces:
            win_game(col[0])

    # # check diagonals
    diag1 = set()
    
    diag2 = set()
    
    # for i, cols in enumerate(game_array[0]):
    #     for j, row in enumerate(game_array):
    #         if i == j:
    #             diag1.add(game_array[i][j][2])
    #         if i+j == len(game_array):
    #             diag2.add(game_array[i][j][2])
    # if len(diag1) == 1 and '' not in diag1:
    #         print("win")
    # if len(diag2) == 1 and '' not in diag2:
    #         print("win")

    for i in range(len(stack_array)):
        diag1.add(stack_array[i][i].peek())
        diag2.add(stack_array[len(stack_array)-i-1][i].peek())

    if len(diag1) == 1 and '' not in diag1:
        win_game(stack_array[0][0].peek())
    if len(diag2) == 1 and '' not in diag2:
        win_game(stack_array[len(stack_array) - 1][0])

def render():
    win.fill(TAN)
    draw_grid()
    for (x,y) in images:
        IMAGE = images[(x,y)]
        win.blit(IMAGE, (x - IMAGE.get_width() // 2, y - IMAGE.get_height() // 2))

    pygame.display.update()

def main():
    global x_turn, images, buttons, mode, buttonsLocked, maxMoves


    images = {}
    buttons = []
    run = True
    x_turn = True
    stack_array, coord_array = init_grid()
    images[(GUI_WIDTH+WIDTH/2, WIDTH/2)] = BACKGROUND
    

    mode = "both"
    maxMoves = 2
    buttonsLocked = False
    
    init_buttons()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click(stack_array, coord_array)
                check_win(stack_array)
        render()



if __name__ == '__main__':
    main()

# 4x4

# moves:
# place up to 3 neutral
# place 1 colored + 1 neutral
# remove 2 pieces