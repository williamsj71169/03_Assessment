from tkinter import *
from functools import partial  # to prevent unwanted windows
import random


class Start:
    def __init__(self, parent):

        # giu to get starting score and rounds
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # set initial score to zero
        self.starting_funds = IntVar()
        self.starting_funds.set(0)

        # mystery heading (row 0)
        self.mystery_box_label = Label(self.start_frame, text="Assessment Game",
                                       font="Arial 19 bold")
        self.mystery_box_label.grid(row=0)

        # Initial instructions (row 1)
        self.mystery_instructions = Label(self.start_frame, font="Arial 10 italic",
                                          text="This is a maths quiz, the "
                                               "questions are infinite and "
                                               "you can quit at any time.",
                                          wrap=275, justify=LEFT, padx=10, pady=10)
        self.mystery_instructions.grid(row=1)

        # Entry box, button and error label (row 2)
        self.entry_error_frame = Frame(self.start_frame, width=200)
        self.entry_error_frame.grid(row=2)

        self.play_button = Button(self.entry_error_frame,
                                  font="Arial 14 bold",
                                  text="Play",
                                  command=self.to_game)
        self.play_button.grid(row=2)

        # button frame (row 3)
        self.rounds_frame = Frame(self.start_frame)
        self.rounds_frame.grid(row=3)

        # Buttons go here  ***************
        button_font = "Arial 14 bold"

        # Help button
        self.help_button = Button(self.rounds_frame, text="Help", padx=10,
                                  bg="#6200ff", fg="white", font=button_font,
                                  command=self.to_help)
        self.help_button.grid(row=3, pady=10, column=0)

        # quit button
        self.quit_button = Button(self.rounds_frame, text="Quit", fg="white",
                                  bg="#ff00dd", font=button_font, padx=10,
                                  command=self.to_quit)
        self.quit_button.grid(row=3, pady=10, column=1, padx=10)

    def to_quit(self):
            root.destroy()

    def to_help(self):
        get_help = Help(self)

    def to_game(self, rounds):

        # retrieve starting score
        starting_score = self.starting_funds.get()

        Game(self, rounds, starting_score)

        # hide start up window
        root.withdraw()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Assessment Game")
    something = Start(root)
    root.mainloop()
