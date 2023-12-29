import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        
        # Player X starts
        self.current_player = "X"

        # Initialize the board
        self.board = [[" " for _ in range(3)] for _ in range(3)]

        # Create buttons for the board
        self.buttons = [[tk.Button(self.window, text=" ", font=("Helvetica", 20), width=6, height=3, command=lambda row=i, col=j: self.on_click(row, col)) for j in range(3)] for i in range(3)]

        # Place buttons on the grid
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].grid(row=i, column=j)

    def on_click(self, row, col):
        # Check if the chosen cell is empty
        if self.board[row][col] == " ":
            # Update the board and button text
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            # Check if the current player wins
            if self.check_winner():
                self.show_winner()
            elif self.is_board_full():
                self.show_draw()
            else:
                # Switch to the other player
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if all(self.board[i][j] == self.current_player for j in range(3)) or all(self.board[j][i] == self.current_player for j in range(3)):
                return True
        if all(self.board[i][i] == self.current_player for i in range(3)) or all(self.board[i][2 - i] == self.current_player for i in range(3)):
            return True
        return False

    def is_board_full(self):
        # Check if the board is full
        return all(self.board[i][j] != " " for i in range(3) for j in range(3))

    def show_winner(self):
        messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
        self.reset_game()

    def show_draw(self):
        messagebox.showinfo("Tic Tac Toe", "It's a draw!")
        self.reset_game()

    def reset_game(self):
        # Reset the board and button texts
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ")

        # Player X starts again
        self.current_player = "X"

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
