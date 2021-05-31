import pygame, sys
from numpy import zeros
pygame.init()

width = 600
height = width
line_width = 15
bord_rows = 3
bord_col = 3
square_size = width//bord_col
circle_radius = 60
circle_width = 15
cross_width = 20
space = 50

back_color = (28, 170, 156)
line_color = (23, 145, 135)
circle_color = (240, 230, 200)
cross_color = (66, 66, 66)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sheded game")
screen.fill(back_color)

board = zeros((3, 3))


def draw_lines():
    pygame.draw.line(screen, line_color, (0, 200), (600, 200), line_width)
    pygame.draw.line(screen, line_color, (0, 400), (600, 400), line_width)
    pygame.draw.line(screen, line_color, (200, 0), (200, 600), line_width)
    pygame.draw.line(screen, line_color, (400, 0), (400, 600), line_width)


def draw_figures():
    for row in range(bord_rows):
        for col in range(bord_col):
            if board[row][col] ==1:
                pygame.draw.circle(screen, circle_color, (int(col*200+100), int(row*200+100)), circle_radius, circle_width)
            elif board[row][col]==2:
                pygame.draw.line(screen, cross_color, (col * 200+ space, row * 200+200- space), (col*200 + 200-space, row*200+space), cross_width)
                pygame.draw.line(screen, cross_color, (col * 200 +space, row * 200+space), (col*200+200-space, row*200+200-space), cross_width)


def mark_square(row, col, player):
    board[row][col] = player


def available_squere(row, col):
    return board[row][col] == 0


def is_board_full():
    for row in range(bord_rows):
        for col in range(bord_col):
            if board[row][col] == 0:
                return False
    return True


def check_win(player):
    # vertical win
    for col in range(bord_col):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True

    # horizontal win check
    for row in range(bord_rows):
        if board[row][0]== player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True

    # asc win check
    if board[2][0]==player and board [1][1] == player and board[0][2]==player:
        draw_asc_diagonal(player)
        return True

    # desc win check
    if board[0][0]==player and board[1][1]==player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True

    return False


def draw_vertical_winning_line(col, player):
    posX = col *200 + 100
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color

    pygame.draw.line(screen, color, (posX, 15), (posX, height -15), 17)


def draw_horizontal_winning_line(row, player):
    posY = row*200 +100
    if player == 1:
        color =circle_color
    elif player == 2:
        color = cross_color

    pygame.draw.line(screen, color, (15, posY), (width-15, posY), 17)


def draw_asc_diagonal(player):
    if player == 1:
        color =circle_color
    elif player == 2:
        color = cross_color

    pygame.draw.line(screen, color, (15, height-15), (width-15, 15), 17)


def draw_desc_diagonal(player):
    if player == 1:
        color =circle_color
    elif player == 2:
        color = cross_color

    pygame.draw.line( screen, color, (15, 15), (width-15, height- 15), 17)

def restart():
    screen.fill(back_color)
    draw_lines()
    player = 1
    GameOver = False
    for row in range(bord_rows):
        for col in range(bord_col):
            board[row][col]=0


draw_lines()

player = 1
GameOver = False


def display_message():
    myfont = pygame.font.SysFont("monospace", 30)
    label = myfont.render("Press R to Restart", 1, (0,0,0))
    screen.blit(label, (10, 10))
    pygame.display.update()


# main loop
while True:

    for event in pygame.event.get():
         if event.type == pygame.QUIT:
             sys.exit()

         if event.type == pygame.MOUSEBUTTONDOWN and not GameOver:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX //200)

            if available_squere(clicked_row, clicked_col):
                if player ==1:
                    mark_square(clicked_row, clicked_col, 1)
                    if check_win(player):
                        GameOver = True
                        display_message()
                    player = 2
                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    if check_win(player):
                        GameOver = True
                        display_message()
                    player=1
                draw_figures()


         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_r:
                restart()

    pygame.display.update()
