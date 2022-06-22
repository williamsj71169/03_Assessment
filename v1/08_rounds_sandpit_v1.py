from tkinter import *
from functools import partial  # to prevent unwanted windows
import csv
import random


class Start:
    def __init__(self, parent):

        # giu to get starting score and rounds
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # set initial score to zero
        self.starting_scores = IntVar()
        self.starting_scores.set(0)

        # mystery heading (row 0)
        self.mystery_box_label = Label(self.start_frame, text="Assessment Game",
                                       font="Arial 19 bold")
        self.mystery_box_label.grid(row=0)

        # Initial instructions (row 1)
        self.mystery_instructions = Label(self.start_frame, font="Arial 10 italic",
                                          text="This is an animals and their young quiz, the "
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
        starting_score = self.starting_scores.get()
        rounds = 0

        Game(self, rounds, starting_score)

        # hide start up window
        root.withdraw()


class Game:
    def __init__(self, partner, rounds, starting_score):
        rounds += 1
        print(rounds)
        print(starting_score)

        file = open("young_lower_t.csv", "r")
        csv_reader = csv.reader(file)

        lists_from_csv = []
        for row in csv_reader:
            lists_from_csv.append(row)

        self.questions = lists_from_csv[0]
        self.answers = lists_from_csv[1]

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
        self.round_list = []
        self.round_list.append(rounds)

        # GUI setup
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Heading row
        self.heading_label = Label(self.game_frame, text="Play!",
                                   font="Arial 24 bold",
                                   padx=10, pady=10)
        self.heading_label.grid(row=0)

        random_num = random.randint(0, 112)

        # print question and answer
        print("Question:{} | Answer:{}".format(self.questions[random_num], self.answers[random_num]))

        # Heading row
        self.question_label = Label(self.game_frame,
                                    text="#{}: What is the name\n of a young {}".
                                    format(rounds, self.questions[random_num]),
                                    font="Arial 20", fg="#bd1a1a",
                                    padx=10, pady=10)
        self.question_label.grid(row=1)
        print()

        # info section(row 2)
        score = rounds-1
        score_text = "Current Score: {}".format(score * 5)

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
                                   command=lambda: self.check_answer(random_num, starting_score))
        self.enter_button.grid(row=0, column=0, padx=2)

        # enter to play
        # self.enter_button.focus()
        # self.enter_button.bind('<Return>', lambda e: self.check_answer(random_num, rounds, starting_score))
        # self.enter_button.grid(row=0, column=0, padx=2)

        self.next_button = Button(self.enter_help_frame, text="Next",
                                  bg="#33ff3d", font="Arial 15 bold",
                                  command=lambda: self.check_answer(random_num, starting_score))
        self.next_button.grid(row=0, column=1, padx=2)
        self.next_button.config(state=DISABLED)

        self.amount_error_label = Label(self.game_frame, fg="#bd1a1a",
                                        text="", font="Arial 10 bold", wrap=275,
                                        justify=LEFT)
        self.amount_error_label.grid(row=4, columnspan=2, pady=5)

        # help and game stats button (row 5)
        self.export_help_frame = Frame(self.game_frame)
        self.export_help_frame.grid(row=6, pady=10)

        # Help button
        self.help_button = Button(self.export_help_frame, text="Help / Rules",
                                  font="Arial 15 bold",
                                  command=lambda: self.to_help,
                                  bg="#9233ff", fg="white")
        self.help_button.grid(row=0, column=0, padx=2)

        self.stats_button = Button(self.export_help_frame, text="Game Stats",
                                   font="Arial 15 bold",
                                   bg="#33b1ff", fg="white")
        self.stats_button.grid(row=0, column=1, padx=2)

        # quit button
        self.quit_button = Button(self.game_frame, text="Quit", fg="white",
                                  bg="#ff00dd", font="Arial 15 bold", width=20,
                                  command=self.to_quit)
        self.quit_button.grid(row=7, pady=10)

    def check_answer(self, random_num, starting_score):
        rounds_2 = self.round_list[-1]
        print("rounds:{}".format(rounds_2))

        if self.round_list[-1] >= 2:
            print("**********************")
            random_num = random.randint(0, 113)

            print("Question:{} | Answer:{}".format(self.questions[random_num], self.answers[random_num]))

            self.question_label.config(text="#{}: What is the name\n of a young {}".
                                       format(rounds_2, self.questions[random_num]))

            # self.answer_entry.delete(0, 'end')

            self.enter_button.config(state=NORMAL)
            self.next_button.config(state=DISABLED)

        else:
            print("%^&%^&%^&")

        given_answer = self.answer_entry.get().lower()

        # Set error background colours and assume no errors
        error_back = "#ffafaf"
        has_errors = "no"

        # change background to white
        self.answer_entry.config(bg="white")
        self.amount_error_label.config(text="")

        # disable all stakes buttons in case user changes mind and decreases amount entered
        self.enter_button.config(state=DISABLED)
        error_feedback = "Wrong!"
        correct_feedback = "Correct!"

        try:
            given_answer = str(given_answer)  # string?

            #  if len(self.all_calc_list) == 0:

        except ValueError:
            has_errors = "yes"

        if has_errors == "yes":
            self.answer_entry.config(bg=error_back, fg="red")
            self.amount_error_label.config(text=error_feedback)

        elif given_answer != self.answers[random_num]:
            self.answer_entry.config(bg=error_back, fg="red")
            self.amount_error_label.config(text=error_feedback)

        elif given_answer == self.answers[random_num]:
            # set starting balance to amount entered by user
            # self.starting_scores.set(given_answer)
            self.answer_entry.config(bg="#afffb2")
            self.amount_error_label.config(text=correct_feedback, fg="#1abd1d")
            score = starting_score + 1
            print("Score:{}".format(score))

        # add round results to stats list
        round_summary = "Question:{}:{} | "\
                        "Given Answer:{} | " \
                        "Correct Answer:{}".format(rounds_2, self.questions[random_num], given_answer,
                                                   self.answers[random_num])
        self.round_stats_list.append(round_summary)
        print(self.round_stats_list)
        self.next_button.config(state=NORMAL)
        rounds_2 += 1
        self.round_list.append(rounds_2)
        print("&&{}&&".format(rounds_2))

        root.withdraw()

    def to_quit(self):
        root.destroy()

    def to_help(self):
        get_help = Help(self)


class Help:
    def __init__(self, partner):
        # disable help button
        partner.help_button.config(state=DISABLED)

        # sets up child window
        self.help_box = Toplevel()

        # if user press cross at top closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # set up gui frame
        self.help_frame = Frame(self.help_box, width=300)
        self.help_frame.grid()

        # set up heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                 font="arial 14 bold")
        self.how_heading.grid(row=0)

        help_text = "help text"

        # help text (label, row 1)
        self.help_text = Label(self.help_frame, text=help_text,
                               justify=LEFT, wrap=400, padx=10, pady=10)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                  width=10, bg="#660000", fg="white",
                                  font="arial 15 bold", command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=3, pady=10)

    def close_help(self, partner):
        # put calc history button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Assessment Game")
    something = Start(root)
    root.mainloop()
