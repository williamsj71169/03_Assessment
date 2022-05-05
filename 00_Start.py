from tkinter import *
from functools import partial  # to prevent unwanted windows
import random


class Start:
    def __init__(self, parent):

        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        self.push_me_button = Button(text="Push Me", command=self.to_game)
        self.push_me_button.grid(row=0, pady=10)

    def to_game(self):

        # num of rounds
        rounds = 10

        Game(self, rounds)

        # hide pop up window
        root.withdraw()


class Game:
    def __init__(self, rounds):
        starting_score = 0
        print(rounds)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("change me")
    something = Start(root)
    root.mainloop()
