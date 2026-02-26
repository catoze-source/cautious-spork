import random

# Generate amount of rows and the payouts
ROWS = 6
COLUMNS = 6  # bottom row slots
PAYOUTS = [0, 0.5, 1, 2, 1, 0.5]

balance = int(input("How much money are you betting today?: "))

while balance > 1:
    print("Balance:", balance)
    bet = int(input("Enter your bet: "))

    # If bet is more than balance, ask again
    if bet > balance:
        print("You cannot bet more than your balance!")
        continue

    # start at the middle for a nicer drop
    ball_col = COLUMNS // 2

    # store the horizontal positions of the slots for alignment
    slot_positions = []

    for row in range(ROWS):
        row_display = ""
        # Calculate spaces before first slot
        spaces = " " * (ROWS - row - 1)
        row_display += spaces
        # build row and store slot positions
        row_slots = []
        for col in range(row + 1):
            if col == ball_col:
                row_display += "X "
            else:
                row_display += ". "
            row_slots.append(len(row_display) - 2)  # record horizontal index
        print(row_display.rstrip())
        slot_positions = row_slots  # overwrite each row; last row will match payouts

        # move ball left or right randomly for next row
        if row < ROWS - 1:
            ball_col += random.choice([-1, 1])
            if ball_col < 0:
                ball_col = 0
            elif ball_col > row + 1:
                ball_col = row + 1

    # 🎯 PRINT PAYOUT ROW aligned with last row
    payout_line = [" "] * (slot_positions[-1] + 1)
    for i, value in enumerate(PAYOUTS):
        if i < len(slot_positions):
            payout_line[slot_positions[i]] = str(value)
    print("\nPayouts:")
    print("".join(payout_line))

    # 
    win = PAYOUTS[ball_col]
    print("\nBall landed in slot:", ball_col)
    print("You won:", win * bet, "dollars!")

    # Update balance
    balance -= bet
    balance += win * bet

    # Ask if player wants to play again
    if balance <= 0:
        print("\nYou have run out of money! Game over.")
        break
    play_again = input("\nDo you wat to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("You leave with:", balance, "dollars. Thanks for playing!")
        break
