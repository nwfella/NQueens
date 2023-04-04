import pygame
import sys

# Initialize board
def initialize_board(n):
    board = [[0 for x in range(n)] for y in range(n)]
    return board

# Is this Queen placement valid given current configuration of the board?  Check all de thingz!!
def is_valid(board, row, col):
    n = len(board)
    # left side row
    for i in range(col):
        if board[row][i] == 1:
            return False
    # left side upper diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # left side lower diagonal
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

# Where the magic happens
def n_queens(board, col, square_size):
    n = len(board)
    # Big Badda Boom, we Audi!!
    if col == n:
        return True
    # Place queen for each row of current column
    for i in range(n):
        if is_valid(board, i, col):
            board[i][col] = 1
            # Recursively place queens in remaining columns
            if n_queens(board, col + 1, square_size) == True:
                return True
            # If placing a queen in (i, col) doesn't lead to a solution, backtrack
            board[i][col] = 0
    return False

# Display board
def display_board(board, square_size):
    n = len(board)
    screen_width = n * square_size
    screen_height = n * square_size
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    # Display board squares
    for i in range(n):
        for j in range(n):
            rect = pygame.Rect(j * square_size, i * square_size, square_size, square_size)
            if (i + j) % 2 == 0:
                color = (255, 255, 255)
            else:
                color = (0, 0, 0)
            pygame.draw.rect(screen, color, rect)
    # Use red circles for queens
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                center_x = int((j + 0.5) * square_size)
                center_y = int((i + 0.5) * square_size)
                radius = int(square_size * 0.4)
                pygame.draw.circle(screen, (255, 0, 0), (center_x, center_y), radius)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# Big Block
def main():
    n = int(input("Enter the number of queens: "))
    square_size = 75
    board = initialize_board(n)
    if n_queens(board, 0, square_size) == False:
        print("No solution found.")
    else:
        print("Solution:")
        for row in board:
            print(row)
        display_board(board, square_size)

if __name__ == "__main__":
    main()
