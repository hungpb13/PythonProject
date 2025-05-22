# Exercise: Slot Machine
import random


def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']

    return [random.choice(symbols) for _ in range(3)]


def print_row(row):
    print(" | ".join(row))


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        match row[0]:
            case '🍒':
                return bet * 2
            case '🍉':
                return bet * 3
            case '🍋':
                return bet * 4
            case '🔔':
                return bet * 5
            case '⭐':
                return bet * 10
    return 0


def slot_machine(balance=0):
    print(" Welcome to Slot Machine ")
    print("---- 🍒 🍉 🍋 🔔 ⭐ ----")

    while balance > 0:
        print(f"Current balance: ${balance:.2f}")

        bet = input("Place your bet: ")

        if not bet.isdigit():
            print("Please enter a valid number!")
            continue

        bet = float(bet)

        if bet > balance:
            print("Insufficient funds!")
            continue
        elif bet <= 0:
            print("Bet must be greater than 0")
            continue

        row = spin_row()
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout:.2f}!")
            balance += payout
        else:
            print("You lose this round!")
            balance -= bet

        play_again = input("Play again? (Press Q to quit): ").upper()
        if play_again == "Q":
            break

    print(f"Game over! Your final balance is: ${balance:.2f}")


def main():
    balance = 100
    slot_machine(balance)


if __name__ == "__main__":
    main()
