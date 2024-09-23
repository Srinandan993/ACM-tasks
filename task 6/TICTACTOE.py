import random

class TicTacToe:
    def __init__(self):
        self.board = ["-"] * 9
        self.current_player = "X"
        self.winner = None
        self.game_running = True

    def print_board(self):
        print(self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        print("---------")
        print(self.board[3] + " | " + self.board[4] + " | " + self.board[5])
        print("---------")
        print(self.board[6] + " | " + self.board[7] + " | " + self.board[8])

    def player_input(self):
        valid = False
        while not valid:
            try:
                inp = int(input("Select a spot (1-9): ")) - 1
                if self.board[inp] == "-":
                    self.board[inp] = self.current_player
                    valid = True
                else:
                    print("Oops! That spot is already taken.")
            except (IndexError, ValueError):
                print("Invalid input. Please select a number between 1 and 9.")

    def check_win(self):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if self.board[i * 3] == self.board[i * 3 + 1] == self.board[i * 3 + 2] != "-":
                self.winner = self.board[i * 3]
                return True
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != "-":
                self.winner = self.board[i]
                return True
        if self.board[0] == self.board[4] == self.board[8] != "-":
            self.winner = self.board[0]
            return True
        if self.board[2] == self.board[4] == self.board[6] != "-":
            self.winner = self.board[2]
            return True
        return False

    def check_tie(self):
        return "-" not in self.board

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def computer_move(self):
        # Simple AI: Block opponent or make a random move
        for i in range(9):
            if self.board[i] == "-":
                self.board[i] = "O"
                if self.check_win():
                    return
                self.board[i] = "-"

        while True:
            position = random.randint(0, 8)
            if self.board[position] == "-":
                self.board[position] = "O"
                break

    def play(self):
        while self.game_running:
            self.print_board()
            if self.current_player == "X":
                self.player_input()
            else:
                self.computer_move()

            if self.check_win():
                self.print_board()
                print(f"The winner is {self.winner}!")
                self.game_running = False
            elif self.check_tie():
                self.print_board()
                print("It is a tie!")
                self.game_running = False

# MAIN PROGRAM
if __name__ == "__main__":
    game = TicTacToe()
    game.play()
