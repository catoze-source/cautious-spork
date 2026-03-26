import random
import time

ROWS = 6
COLUMNS = 7
PAYOUTS = [0, 0.5, 1, 2, 1, 0.5, 0]



def generate_board(rows, columns):
    """
    Creates the initial game board grid with pins ('o') in a staggered pattern.
    It does this by outting "o" where the sum of r and c are even. 
    list: A 2D list representing the game board.
    """
    board = [[" " for _ in range(columns)] for _ in range(rows)]
    for r in range(rows - 1):
        for c in range(columns):
            if (r + c) % 2 == 0: 
                board[r][c] = "o"
    return board



def print_board(board):
    """
    Prints the current state of the board to the console.
    """
    
    for row in board:
        print(" ".join(row))
    print()

    

def calculate_drop(start_column, total_rows):
    """
    Calculates where the ball will end up.
    It runs a loop that goes down for how many rows minus one so that it lands on the bottom row.
    It randomely pick whether to go to the left(-1) or right(+1)
    """
    
    column = start_column
    for _ in range(total_rows - 1):
        column += random.choice([-1, 1])
        if column < 0:
            column = 0
                # Stops the ball leaving the grid 
        elif column > COLUMNS - 1:
            column = COLUMNS - 1 
    return column



def animate_drop(board, start_column):
    """
    Simulates the ball falling through the pins with a visual delay.
    Starts in in the middle and makes it move down
    """
    column = start_column
    for r in range(ROWS - 1):
        board[r][column] = "X"
        print_board(board)
        time.sleep(0.2)
        
        board[r][column] = "o" if (r + column) % 2 == 0 else " " #Checks if the number is even again 
        column += random.choice([-1, 1])
        
        # Stops the ball leaving the grid 
        if column < 0:
            column = 0
        elif column > COLUMNS - 1:
            column = COLUMNS - 1 

    board[ROWS - 1][column] = "X"
    print_board(board)
    return column



def get_valid_bet(balance):
    """
    Prompts the user for a bet amount and check ig it is valid

    """
    while True:
        try:
            bet = float(input("Enter your bet: "))
            if bet <= 0:
                print("Invalid bet: Must be greater than 0.")
            elif bet > balance:
                print("Invalid bet: You only have {}.".format(balance))
            else:
                return bet
        except ValueError:
            print("Invalid input: Please enter a number.")



def update_balance(current_balance, bet, multiplier):
    """
    Calculates the new balance after applying the win/loss multiplier.

    """
    winnings = bet * multiplier
    return current_balance - bet + winnings



# Main Routine

if __name__ == "__main__":
    try:
        balance = float(input("How much money are you betting today?: "))
    except ValueError:
        print("Invalid input. Here is $100.")
        balance = 100.0

    while balance > 0:
        print("\nBalance: {:.2f}".format(balance)) #Prints the balence to 2dp
        
        bet = get_valid_bet(balance)
        
        start_column = COLUMNS // 2 # Determine the middle of the board using Floor Division //.
        board = generate_board(ROWS, COLUMNS)

        final_column = animate_drop(board, start_column) # Stores the final landing index

        multiplier = PAYOUTS[final_column] # Use the final_column as an index to look up the value in PAYOUTS.
        balance = update_balance(balance, bet, multiplier)

        print("Landed in column {}".format(final_column))
        print("Multiplier: {}x".format(multiplier))
        print("New balance: {:.2f}".format(balance))

    print("You ran out of money.")
