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
    def __init__(self, partner, rounds):
        starting_score = 0
        print(rounds)

        self.questions = ["a", 'b', "c"]
        self.answers = ["A", "B", "C"]
        print(self.questions)

        # GUI setup
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Heading row
        self.heading_label = Label(self.game_frame, text="Play!",
                                   font="Arial 24 bold",
                                   padx=10, pady=10)
        self.heading_label.grid(row=0)

        random_num = (random.randint(0, 2))

        self.heading_label = Label(self.game_frame,
                                   text="Question #{}: {}".format(rounds, self.questions[random_num]),
                                   font="Arial 20", fg="#991212",
                                   padx=10, pady=10)
        self.heading_label.grid(row=1)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("change me")
    something = Start(root)
    root.mainloop()
