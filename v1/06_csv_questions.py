from tkinter import *
# from functools import partial  # to prevent unwanted windows
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
                                  bg="#6200ff", fg="white", font=button_font)
        self.help_button.grid(row=3, pady=10, column=0)

        # quit button
        self.quit_button = Button(self.rounds_frame, text="Quit", fg="white",
                                  bg="#ff00dd", font=button_font, padx=10,
                                  command=self.to_quit)
        self.quit_button.grid(row=3, pady=10, column=1, padx=10)

    def to_quit(self):
            root.destroy()

    def to_game(self):

        # retrieve starting score
        starting_score = self.starting_funds.get()
        rounds = 1

        Game(self, rounds, starting_score)

        # hide start up window
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
                                   font="Arial 20", fg="#bd1a1a",
                                   padx=10, pady=10)
        self.heading_label.grid(row=1)

        # info section(row 2)
        score_text = "Current Score: {}".format(rounds * 5)

        self.score_frame = Frame(self.game_frame)
        self.score_frame.grid(row=2)

        self.score_label = Label(self.game_frame, font="Arial 12 bold", text=score_text,
                                 fg="#bd741a", wrap=300, justify=LEFT)
        self.score_label.grid(row=2, pady=10)

        # Entry box, button and error label
        self.entry_error_frame = Frame(self.game_frame, width=200)
        self.entry_error_frame.grid(row=3, column=0)

        self.answer_entry = Entry(self.entry_error_frame,
                                  font="Arial 15 bold", width=15)
        self.answer_entry.grid(row=0, column=0, padx=2)

        self.enter_help_frame = Frame(self.game_frame)
        self.enter_help_frame.grid(row=5)

        # Play button goes here (row 2)
        self.enter_button = Button(self.enter_help_frame, text="Enter",
                                   bg="#FFFF33", font="Arial 15 bold",
                                   command=lambda: self.check_answer(random_num, rounds))  # adding - (random_num) - will glitch
        self.enter_button.grid(row=0, column=0, padx=2)

        self.next_button = Button(self.enter_help_frame, text="Skip",
                                  bg="#33ff3d", font="Arial 15 bold")
        self.next_button.grid(row=0, column=1, padx=2)

        self.amount_error_label = Label(self.game_frame, fg="#bd1a1a",
                                        text="", font="Arial 10 bold", wrap=275,
                                        justify=LEFT)
        self.amount_error_label.grid(row=4, columnspan=2, pady=5)

        # enter to revel boxes
        self.enter_button.focus()
        self.enter_button.bind('<Return>', lambda e: self.check_answer(random_num, rounds))

        # help and game stats button (row 5)
        self.export_help_frame = Frame(self.game_frame)
        self.export_help_frame.grid(row=6, pady=10)

        # Help button
        self.help_button = Button(self.export_help_frame, text="Help / Rules",
                                  font="Arial 15 bold",
                                  bg="#9233ff", fg="white")
        self.help_button.grid(row=0, column=0, padx=2)

        self.stats_button = Button(self.export_help_frame, text="Game Stats",
                                   font="Arial 15 bold",
                                   bg="#33b1ff", fg="white")
        self.stats_button.grid(row=0, column=1, padx=2)

        # quit button
        self.quit_button = Button(self.game_frame, text="Quit", fg="white",
                                  bg="#ff00dd", font="Arial 15 bold", width=20,    # 21 to make in line with help.
                                  command=self.to_quit)
        self.quit_button.grid(row=7, pady=10)

    def check_answer(self, random_num, rounds):
        self.enter_button.config(state=NORMAL)

        given_answer = self.answer_entry.get()
        print(random_num)

        # Set error background colours and assume no errors
        error_back = "#ffafaf"
        has_errors = "no"

        # change background to white
        # self.answer_entry.config(bg="white")
        # self.amount_error_label.config(text="")

        # disable all stakes buttons in case user changes mind and decreases amount entered
        self.enter_button.config(state=DISABLED)
        error_feedback = "Wrong!"
        correct_feedback = "Right!"

        try:
            given_answer = str(given_answer)  # string?

            #  if len(self.all_calc_list) == 0:

            if given_answer == self.answers[random_num]:
                print("h")

        except ValueError:
            has_errors = "yes"

        if has_errors == "yes":
            self.answer_entry.config(bg=error_back)
            self.amount_error_label.config(text=error_feedback)

        elif given_answer != self.answers[random_num]:
            self.answer_entry.config(bg=error_back)
            self.amount_error_label.config(text=error_feedback)

        elif given_answer == self.answers[random_num]:
            # set starting balance to amount entered by user
            # self.starting_funds.set(given_answer)
            self.answer_entry.config(bg="#afffb2")
            self.amount_error_label.config(text=correct_feedback, fg="#1abd1d")

        # add round results to stats list
        round_summary = "Question:{}:{} | "\
                        "Given Answer:{} | " \
                        "Correct Answer:{} ".format(rounds, self.questions[random_num], given_answer,
                                                    self.answers[random_num])
        self.round_stats_list.append(round_summary)
        print(self.round_stats_list)

    def to_quit(self):
        root.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Assessment Game")
    something = Start(root)
    root.mainloop()
