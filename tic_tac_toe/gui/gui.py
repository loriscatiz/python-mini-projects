import pygame
import sys
from tic_tac_toe.game_logic import game_logic  # Import the game game_logic

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
LINE_COLOR = (0, 0, 0)
BG_COLOR = (255, 255, 255)
CELL_SIZE = WIDTH // 3  # Each cell is 200x200 if WIDTH=600
LINE_WIDTH = 5


FONT = pygame.font.SysFont(None, 120)  # Choose a font and size
X_COLOR = (200, 0, 0)  # Red for X
O_COLOR = (0, 0, 200)  # Blue for O

def draw_marks():
    """Draw X and O on the board based on game_logic.board"""
    for row in range(3):
        for col in range(3):
            mark = game_logic.board[row][col]
            if mark != ' ':  # If the cell isn't empty
                text = FONT.render(mark, True, X_COLOR if mark == 'X' else O_COLOR)
                text_rect = text.get_rect(center=cells[row][col].center)
                screen.blit(text, text_rect)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Create a 3x3 list to store the rects of each cell
cells = [[pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE) 
          for col in range(3)] for row in range(3)]

def draw_grid():
    """Draw the Tic-Tac-Toe grid"""
    screen.fill(BG_COLOR)
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), LINE_WIDTH)

def get_cell_from_mouse(pos: tuple[int, int]):
    """Return the (row, col) of the clicked cell based on mouse position"""
    for row in range(3):
        for col in range(3):
            if cells[row][col].collidepoint(pos):
                return row, col
    return None  # Clicked outside grid (shouldn't happen)



def main():
    running = True
    player = "X"
    victory_line = 0 # Tracks the line type and index when there's a win
    victory_time = 0  # Tracks the time of the victory
    victory_delay = 3000  # 3-second delay before reset

    game_over = False  # Flag to track if the game is over

    def draw_victory_line(win_type: str, index: int):
        """Draw the winning line on the board."""
        if win_type == 'horizontal':
            pygame.draw.line(screen, (0, 255, 0), (0, index * CELL_SIZE + CELL_SIZE // 2),
                            (WIDTH, index * CELL_SIZE + CELL_SIZE // 2), 10)  # Green line for horizontal win
        elif win_type == 'vertical':
            pygame.draw.line(screen, (0, 255, 0), (index * CELL_SIZE + CELL_SIZE // 2, 0),
                            (index * CELL_SIZE + CELL_SIZE // 2, HEIGHT), 10)  # Green line for vertical win
        elif win_type == 'diagonal':
            if index == 0:  # First diagonal (top-left to bottom-right)
                pygame.draw.line(screen, (0, 255, 0), (0, 0), (WIDTH, HEIGHT), 10)
            elif index == 1:  # Second diagonal (top-right to bottom-left)
                pygame.draw.line(screen, (0, 255, 0), (WIDTH, 0), (0, HEIGHT), 10)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                pos = pygame.mouse.get_pos()
                cell = get_cell_from_mouse(pos)
                if cell:
                    row, col = cell
                    if game_logic.board[row][col] == ' ':
                        game_logic.update_board((row, col), player)

                        # ✅ Check for win after making the move
                        if game_logic.check_win(player):  # If a win is detected
                            # Save which type of line to draw
                            if [game_logic.board[0][0], game_logic.board[1][1], game_logic.board[2][2]] == [player, player, player]:
                                victory_line = ('diagonal', 0)
                            elif [game_logic.board[0][2], game_logic.board[1][1], game_logic.board[2][0]] == [player, player, player]:
                                victory_line = ('diagonal', 1)
                            elif any(game_logic.board[row] == [player, player, player] for row in range(3)):
                                for i, row in enumerate(game_logic.board):
                                    if row == [player, player, player]:
                                        victory_line = ('horizontal', i)
                                        break
                            elif any([game_logic.board[0][col], game_logic.board[1][col], game_logic.board[2][col]] == [player, player, player] for col in range(3)):
                                for col in range(3):
                                    if [game_logic.board[0][col], game_logic.board[1][col], game_logic.board[2][col]] == [player, player, player]:
                                        victory_line = ('vertical', col)
                                        break

                            victory_time = pygame.time.get_ticks()  # Record the victory time
                            game_over = True  # Set game_over to True once the game finishes
                            print(f"{player} wins!")
                            continue  # Skip drawing this turn, wait for 3 seconds

                        # Check for a draw (all cells filled, no winner)
                        if all(cell != ' ' for row in game_logic.board for cell in row):
                            print("It's a draw!")
                            victory_time = pygame.time.get_ticks()  # Record the draw time
                            game_over = True  # Set game_over to True for a draw
                            continue  # Skip drawing this turn, wait for 3 seconds

                        player = game_logic.switch_player(player)

        # Draw everything
        draw_grid()
        draw_marks()  # Draw Xs and Os

        # If there's a victory, draw the line
        if victory_line:
            draw_victory_line(victory_line[0], victory_line[1])

        # Wait 3 seconds before resetting the game (both for win and draw)
        if game_over and pygame.time.get_ticks() - victory_time >= victory_delay: # type: ignore
            game_logic.board = [[' ' for _ in range(3)] for _ in range(3)]  # Reset the board after delay
            victory_line = None  # Clear the victory line
            victory_time = None  # Reset the victory timer
            game_over = False  # Reset the game_over flag

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
