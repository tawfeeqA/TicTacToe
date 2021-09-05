import pygame
import sys

#Global variables
screen_width = 1200
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.init()
font = pygame.font.SysFont(None, 24)
board = [["", "", ""], ["", "", ""], ["", "", ""]]
clicker =""
#font = None
def redraw():
    clock = pygame.time.Clock()
    # Setting up Screen
    pygame.display.set_caption('TicTacToe')

    # Game Buttons
    x_button = pygame.Rect((screen_width / 2)+200 , (screen_height / 2) +150, 30, 30)
    o_button = pygame.Rect((screen_width / 2) + 250, (screen_height / 2) + 150, 30, 30)
    s_button = pygame.Rect((screen_width/2) +200, (75),100,50)

    # Board Buttons
    one_one = pygame.Rect((screen_width/2) -125, 0, 100, (500/3))
    one_two = pygame.Rect((screen_width/2) -25, 0, 100, (500/3))
    one_three = pygame.Rect((screen_width/2) +75, 0, 100, (500/3))
    two_one = pygame.Rect((screen_width/2) -125, 500/3, 100, (500/3))
    two_two = pygame.Rect((screen_width/2) -25,  500/3,100, (500/3))
    two_three = pygame.Rect((screen_width/2) +75, 500/3,100, (500/3))
    three_one = pygame.Rect((screen_width/2) -125, (500/3)*2, 100, (500/3))
    three_two = pygame.Rect((screen_width/2) -25,   (500/3)*2,100, (500/3))
    three_three = pygame.Rect((screen_width/2) +75,  (500/3)*2,100, (500/3))

    bg_color = pygame.Color('grey12')
    light_grey = (200, 200, 200)
    light_grey2= (224, 236, 255)
    green = (40, 189, 52)

    # Set up
    screen.fill(bg_color)

    #Board Buttons
    pygame.draw.rect(screen, light_grey, x_button)
    pygame.draw.rect(screen, light_grey, o_button)
    pygame.draw.rect(screen, light_grey, one_one)
    pygame.draw.rect(screen, light_grey, one_two)
    pygame.draw.rect(screen, light_grey, one_three)
    pygame.draw.rect(screen, light_grey, two_one)
    pygame.draw.rect(screen, light_grey, two_two)
    pygame.draw.rect(screen, light_grey, two_three)
    pygame.draw.rect(screen, light_grey, three_one)
    pygame.draw.rect(screen, light_grey, three_two)
    pygame.draw.rect(screen, light_grey, three_three)
    pygame.draw.rect(screen, green, s_button)
    #Horizontal Lines
    pygame.draw.aaline(screen,light_grey2, ((screen_width/2) +175,0),((screen_width/2)+175,screen_height))
    pygame.draw.aaline(screen,light_grey2, ((screen_width/2) +75,0),((screen_width/2)+75,screen_height))
    pygame.draw.aaline(screen,light_grey2, ((screen_width/2) -25,0),((screen_width/2)-25,screen_height))
    pygame.draw.aaline(screen,light_grey2, ((screen_width/2) -125,0),((screen_width/2)-125,screen_height))

    #Vertical Lines
    pygame.draw.aaline(screen,light_grey2, ((screen_width/2) -125,(screen_height/3)),((screen_width/2)+175,(screen_height/3)))
    pygame.draw.aaline(screen,light_grey2, ((screen_width/2) -125,(screen_height/3)*2 ),((screen_width/2)+175,(screen_height/3)*2))

    #Text for game
    img = font.render("X", True, (214, 55, 47))
    img2 = font.render("O", True, (214, 55, 47))
    img3 = font.render('Start', True, (214, 55, 47))
    img4 = font.render('Stop', True, (214, 55, 47))
    screen.blit(img,((screen_width / 2)+210 , (screen_height / 2) +160))
    screen.blit(img2, ((screen_width / 2) + 260, (screen_height / 2) + 160))

def main():
    clock = pygame.time.Clock()
    # Setting up Screen
    pygame.display.set_caption('TicTacToe')

    # Game Buttons
    x_button = pygame.Rect((screen_width / 2)+200 , (screen_height / 2) +150, 30, 30)
    o_button = pygame.Rect((screen_width / 2) + 250, (screen_height / 2) + 150, 30, 30)
    s_button = pygame.Rect((screen_width/2) +200, (75),100,50)

    # Board Buttons
    one_one = pygame.Rect((screen_width/2) -125, 0, 100, (500/3))
    one_two = pygame.Rect((screen_width/2) -25, 0, 100, (500/3))
    one_three = pygame.Rect((screen_width/2) +75, 0, 100, (500/3))
    two_one = pygame.Rect((screen_width/2) -125, 500/3, 100, (500/3))
    two_two = pygame.Rect((screen_width/2) -25,  500/3,100, (500/3))
    two_three = pygame.Rect((screen_width/2) +75, 500/3,100, (500/3))
    three_one = pygame.Rect((screen_width/2) -125, (500/3)*2, 100, (500/3))
    three_two = pygame.Rect((screen_width/2) -25,   (500/3)*2,100, (500/3))
    three_three = pygame.Rect((screen_width/2) +75,  (500/3)*2,100, (500/3))

    bg_color = pygame.Color('grey12')
    light_grey = (200, 200, 200)
    light_grey2= (224, 236, 255)
    green = (40, 189, 52)

    # Set up
    screen.fill(bg_color)

    #Board Buttons
    pygame.draw.rect(screen, light_grey, x_button)
    pygame.draw.rect(screen, light_grey, o_button)
    pygame.draw.rect(screen, light_grey, one_one)
    pygame.draw.rect(screen, light_grey, one_two)
    pygame.draw.rect(screen, light_grey, one_three)
    pygame.draw.rect(screen, light_grey, two_one)
    pygame.draw.rect(screen, light_grey, two_two)
    pygame.draw.rect(screen, light_grey, two_three)
    pygame.draw.rect(screen, light_grey, three_one)
    pygame.draw.rect(screen, light_grey, three_two)
    pygame.draw.rect(screen, light_grey, three_three)
    pygame.draw.rect(screen, green, s_button)
    #Horizontal Lines
    pygame.draw.aaline(screen,light_grey2, ((screen_width/2) +175,0),((screen_width/2)+175,screen_height))
    pygame.draw.aaline(screen,light_grey2, ((screen_width/2) +75,0),((screen_width/2)+75,screen_height))
    pygame.draw.aaline(screen,light_grey2, ((screen_width/2) -25,0),((screen_width/2)-25,screen_height))
    pygame.draw.aaline(screen,light_grey2, ((screen_width/2) -125,0),((screen_width/2)-125,screen_height))

    #Vertical Lines
    pygame.draw.aaline(screen,light_grey2, ((screen_width/2) -125,(screen_height/3)),((screen_width/2)+175,(screen_height/3)))
    pygame.draw.aaline(screen,light_grey2, ((screen_width/2) -125,(screen_height/3)*2 ),((screen_width/2)+175,(screen_height/3)*2))

    #Text for game
    img = font.render("X", True, (214, 55, 47))
    img2 = font.render("O", True, (214, 55, 47))
    img3 = font.render('Start', True, (214, 55, 47))
    img4 = font.render('Stop', True, (214, 55, 47))
    screen.blit(img,((screen_width / 2)+210 , (screen_height / 2) +160))
    screen.blit(img2, ((screen_width / 2) + 260, (screen_height / 2) + 160))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position
                if x_button.collidepoint(mouse_pos):
                    # prints current location of mouse
                    clicker ="x"

                elif o_button.collidepoint(mouse_pos):
                    clicker = "o"
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if one_one.collidepoint(mouse_pos):
                    #screen.fill(bg_color)
                    redraw()
                    #print("aaaaa")
                    board[0][0]=str(clicker)
                    print(board)
                    fonty = pygame.font.SysFont(None, 250)
                    img = fonty.render(str(clicker), True, (214, 55, 47))
                    screen.blit(img,((screen_width/2) -125, 0))
                if one_two.collidepoint(mouse_pos):
                    #screen.fill(bg_color)
                    redraw()
                    #print("aaaaa")
                    board[0][1]=str(clicker)
                    print(board)
                    fonty = pygame.font.SysFont(None, 250)
                    img = fonty.render(str(clicker), True, (214, 55, 47))
                    screen.blit(img,((screen_width/2) -25, 0))
        #Updates window
        pygame.display.flip()
        clock.tick(60)

    # print(checkwon(board))






def checkDuplicates(listOfElems):
    setOfElems = set()
    for elem in listOfElems:
        if elem in setOfElems:
            return True
        else:
            setOfElems.add(elem)
    return False


def checkwon(board):
    if is_row_win(board) == 0 and is_col_win(board) == 0 and is_diagonal_win(board) == 0:
        return "Is a draw"
    elif is_row_win(board) != 0:
        return is_row_win(board)
    elif is_col_win(board) != 0:
        return is_row_win(board)
    elif is_diagonal_win(board) != 0:
        return is_diagonal_win(board)


def is_row_win(board):
    lst = []
    for row in range(len(board)):
        for col in range(len(board)):
            lst.append(board[row][col])
        if lst[0] == lst[1] and lst[1] == lst[2]:
            return lst[0]
        lst = []
    return 0


def is_col_win(board):
    if board[1][0] == board[2][0] and board[2][0] == board[0][0]:
        return board[0][1]
    elif board[1][1] == board[2][1] and board[2][1] == board[0][1]:
        return board[0][1]
    elif board[1][2] == board[0][2] and board[0][2] == board[2][2]:
        return board[0][1]
    return 0


def is_diagonal_win(board):
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[2][0] == board[1][1]:
        return board[0][0]
    return 0


if __name__ == "__main__":
    main()
