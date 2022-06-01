from tkinter import *
# from functools import partial  # to prevent unwanted windows
import random


class Start:
    def __init__(self, parent):

        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        self.push_me_button = Button(text="Push Me", command=self.to_game)
        self.push_me_button.grid(row=0, pady=10)

    def to_game(self):

        # retrieve starting balance
        given_answer = 50
        stakes = 1

        Game(self, stakes, given_answer)

        # hide pop up window
        root.withdraw()


class Game:
    def __init__(self, partner, rounds, starting_score):
        print(rounds)
        print(starting_score)

        self.questions = ["a", 'b', "c"]
        self.answers = ["A", "B", "C"]
        print(self.questions)

        # initialize variables
        self.score = IntVar()

        # set starting score to amount entered by user at start of game
        self.score.set(starting_score)

        # get value of rounds (ues it as a multiplier when calculating winnings)
        self.multiplier = IntVar()
        self.multiplier.set(rounds)

        # list for holding stats
        self.round_stats_list = []
        self.game_stats_list = [starting_score, starting_score]

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

        # Heading row
        self.heading_label = Label(self.game_frame,
                                   text="Question #{}: {}".format(rounds, self.questions[random_num]),
                                   font="Arial 20", fg="#991212",
                                   padx=10, pady=10)
        self.heading_label.grid(row=1)

        # info section(row 2)
        start_text = "Current Score: {} \nSkips Remaining: ?".format(rounds * 5)

        self.score_frame = Frame(self.game_frame)
        self.score_frame.grid(row=2)

        self.score_label = Label(self.game_frame, font="Arial 12 bold", text=start_text,
                                 fg="#129944", wrap=300, justify=LEFT)
        self.score_label.grid(row=2, pady=10)

        # Entry box, button and error label
        self.entry_error_frame = Frame(self.game_frame, width=200)
        self.entry_error_frame.grid(row=3, column=0)

        self.answer_entry = Entry(self.entry_error_frame,
                                  font="Arial 15 bold", width=10)
        self.answer_entry.grid(row=0, column=0, padx=2)

        self.enter_help_frame = Frame(self.game_frame)
        self.enter_help_frame.grid(row=5)

        # Play button goes here (row 2)
        self.enter_button = Button(self.enter_help_frame, text="Enter",
                                   bg="#FFFF33", font="Arial 15 bold",
                                   command=self.check_answer(random_num))  #
        self.enter_button.grid(row=0, column=0, padx=2)

        self.skip_button = Button(self.enter_help_frame, text="Skip",
                                  bg="#33ff3d", font="Arial 15 bold")
        self.skip_button.grid(row=0, column=1, padx=2)

        self.amount_error_label = Label(self.game_frame, fg="maroon",
                                        text="", font="Arial 10 bold", wrap=275,
                                        justify=LEFT)
        self.amount_error_label.grid(row=4, columnspan=2, pady=5)

        # help and game stats button (row 5)
        self.export_help_frame = Frame(self.game_frame)
        self.export_help_frame.grid(row=6, pady=10)

        # Help button
        self.help_button = Button(self.export_help_frame, text="Help / Rules",
                                  font="Arial 15 bold",
                                  bg="#6200ff", fg="white")
        self.help_button.grid(row=0, column=0, padx=2)

        self.stats_button = Button(self.export_help_frame, text="Game Stats",
                                   font="Arial 15 bold",
                                   bg="#00e5ff", fg="white")
        self.stats_button.grid(row=0, column=1, padx=2)

        # quit button
        self.quit_button = Button(self.game_frame, text="Quit", fg="white",
                                  bg="#ff00dd", font="Arial 15 bold", width=20,    # 21 to make in line with help.
                                  command=self.to_quit)
        self.quit_button.grid(row=7, pady=10)

    def check_answer(self, random_num):
        given_answer = self.answer_entry.get()
        print("number:{}".format(random_num))
        print(self.answer_entry)
        print("given answer:{}".format(given_answer))

        # Set error background colours and assume no errors
        error_back = "#ffafaf"
        has_errors = "no"

        # change background to white
        self.answer_entry.config(bg="white")
        # self.amount_error_label.config(text="")     # will glitch

        # disable all stakes buttons in case user changes mind and decreases amount entered
        # self.enter_button.config(state=DISABLED)     # will glitch

        try:
            given_answer = str(given_answer)  # string?

            #  if len(self.all_calc_list) == 0:

            if given_answer == self.answers[random_num]:
                print("h")

        except ValueError:
            has_errors = "yes"
            error_feedback = "spelling?"

        if has_errors == "yes":   # or given_answer == ""
            self.answer_entry.config(bg=error_back)
            # self.amount_error_label.config(text=error_feedback)

        else:
            # set starting balance to amount entered by user
            # self.starting_funds.set(given_answer)
            self.answer_entry.config(bg="#33ff3d")

        # do stuff here?

    def to_quit(self):
        root.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Assessment Game")
    something = Start(root)
    root.mainloop()
