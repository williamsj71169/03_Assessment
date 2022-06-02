from tkinter import *
from functools import partial  # to prevent unwanted windows
import random


class Start:
    def __init__(self, parent):

        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # quiz title
        self.quiz_title = Label(self.start_frame,
                                text="Assessment Game!",
                                font="Arial 19 bold")
        self.quiz_title.grid(row=0)

        # info section
        self.info_section = Label(self.start_frame,
                                  text="This is a maths quiz, the "
                                       "questions are infinite and "
                                       "you can quit at any time.",
                                  font="Arial 10 italic", wrap=275,
                                  justify=LEFT, padx=10, pady=10)
        self.info_section.grid(row=1)

        # play button
        self.play_button = Button(self.start_frame,
                                  font="Arial 14 bold",
                                  text="PLAY")
        self.play_button.grid(row=2)

        # quit button
        self.quit_button = Button(self.start_frame,
                                  font="Arial 12 bold",
                                  text="Quit")
        self.quit_button.grid(row=3, column=1, pady=5, padx=5)

        # help button
        self.help_button = Button(self.start_frame,
                                  font="Arial 12 bold",
                                  text="Help")
        self.help_button.grid(row=3, column=0, pady=5, padx=5)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Assessment Game")
    something = Start(root)
    root.mainloop()
