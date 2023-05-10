import tkinter as tk

class TicTacToeApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tic Tac Toe")
        self.geometry("300x300")

        self.current_player = "X"

        self.create_widgets()

    def create_widgets(self):
        self.buttons = []
        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = tk.Button(self, text=" ", font=("Helvetica", 16), width=5, height=2, command=lambda r=i, c=j: self.on_button_click(r, c))
                button.grid(row=i, column=j, padx=5, pady=5)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def on_button_click(self, row, column):
        if self.buttons[row][column]["text"] == " ":
            self.buttons[row][column]["text"] = self.current_player
            self.check_for_winner()
            self.switch_player()

    def check_for_winner(self):
        for i in range(3):
            if self.check_line(self.buttons[i][0]["text"], self.buttons[i][1]["text"], self.buttons[i][2]["text"]):
                self.show_winner()
            if self.check_line(self.buttons[0][i]["text"], self.buttons[1][i]["text"], self.buttons[2][i]["text"]):
                self.show_winner()
        if self.check_line(self.buttons[0][0]["text"], self.buttons[1][1]["text"], self.buttons[2][2]["text"]):
            self.show_winner()
        if self.check_line(self.buttons[0][2]["text"], self.buttons[1][1]["text"], self.buttons[2][0]["text"]):
            self.show_winner()

    def check_line(self, a, b, c):
        return a == b == c and a != " "

    def show_winner(self):
        tk.messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
        self.reset_board()

    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def reset_board(self):
        for row in self.buttons:
            for button in row:
                button["text"] = " "

if __name__ == "__main__":
    app = TicTacToeApp()
    app.mainloop()
