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
                                  command=self.to_help,
                                  bg="#6200ff", fg="white", font=button_font)
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

    def to_game(self):

        # retrieve starting score
        starting_score = self.starting_scores.get()
        rounds = 1

        Game(self, rounds, starting_score)

        # hide start up window
        root.withdraw()


class Game:
    def __init__(self, partner, rounds, starting_score):
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

        # GUI setup
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Heading row
        self.heading_label = Label(self.game_frame, text="Play!",
                                   font="Arial 24 bold",
                                   padx=10, pady=10)
        self.heading_label.grid(row=0)

        random_num = random.randint(0, 113)

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
                                   command=lambda: self.check_answer(random_num, rounds, starting_score))
        self.enter_button.grid(row=0, column=0, padx=2)

        # enter to play
        # self.enter_button.focus()
        # self.enter_button.bind('<Return>', lambda e: self.check_answer(random_num, rounds, starting_score))
        # self.enter_button.grid(row=0, column=0, padx=2)

        self.next_button = Button(self.enter_help_frame, text="Next",
                                  bg="#33ff3d", font="Arial 15 bold",
                                  command=lambda: self.next_game(starting_score, rounds))
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
                                  command=self.to_help,
                                  bg="#9233ff", fg="white")
        self.help_button.grid(row=0, column=0, padx=2)

        self.stats_button = Button(self.export_help_frame, text="Game Stats",
                                   font="Arial 15 bold",
                                   bg="#33b1ff", fg="white",
                                   command=lambda: self.to_stats(round, self.game_stats_list))
        self.stats_button.grid(row=0, column=1, padx=2)

        # quit button
        self.quit_button = Button(self.game_frame, text="Quit", fg="white",
                                  bg="#ff00dd", font="Arial 15 bold", width=20,    # 21 to make in line with help.
                                  command=self.to_quit)
        self.quit_button.grid(row=7, pady=10)

    def check_answer(self, random_num, rounds, starting_score):
        print(rounds)
        self.enter_button.config(state=NORMAL)

        given_answer = self.answer_entry.get().lower()

        # Set error background colours and assume no errors
        error_back = "#ffafaf"
        has_errors = "no"

        # change background to white
        # self.answer_entry.config(bg="white")
        # self.amount_error_label.config(text="")

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
            self.answer_entry.config(bg=error_back)
            self.amount_error_label.config(text=error_feedback)

        elif given_answer != self.answers[random_num]:
            self.answer_entry.config(bg=error_back)
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
                        "Correct Answer:{}".format(rounds, self.questions[random_num], given_answer,
                                                   self.answers[random_num])
        self.round_stats_list.append(round_summary)
        print(self.round_stats_list)
        self.next_button.config(state=NORMAL)
        rounds = rounds + 1
        print(rounds)

        root.withdraw()
        
    def next_game(self, starting_scores, rounds):
        # retrieve starting score
        starting_score = 0
        
        # starting_score = self.starting_scores.get()
        rounds = rounds + 1

        Game(self, rounds, starting_score)

        # hide start up window
        root.withdraw()

    def to_stats(self, rounds, game_stats):
        GameStats(self, rounds, game_stats)

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

        help_text = "Press play to play. " \
                    "The game will keep going till you quit.\n\n" \
                    "you can see your stats, get help or quit at any time." \
                    "caps don't matter" \

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


class GameStats:
    def __init__(self, partner, rounds_history, game_stats):

        print(rounds_history)

        # disabled help button
        partner.stats_button.config(state=DISABLED)

        heading = "Arial 12 bold"
        content = "Arial 12"

        # sets up child window
        self.stats_box = Toplevel()

        # if users press cross at top, closes stats and 'releases' stats button
        self.stats_box.protocol('WM_DELETE_WINDOW', partial(self.close_stats, partner))

        # set up GUI frame
        self.stats_frame = Frame(self.stats_box)
        self.stats_frame.grid()

        # set up Game Stats heading (row 0)
        self.stats_heading_label = Label(self.stats_frame, text="Game Statistics",
                                         font="arial 19 bold")
        self.stats_heading_label.grid(row=0)

        # to export <instructions>(row 1)
        self.export_instructions = Label(self.stats_frame,
                                         text="Here are your Game Statistics. Please ues the "
                                              "export button to access the results of each "
                                              "round that you have played", wrap=250,
                                         font="arial 10 italic", justify=LEFT,
                                         fg="green", padx=10, pady=10)
        self.export_instructions.grid(row=1)

        # starting balance (row 2)
        self.details_frame = Frame(self.stats_frame)
        self.details_frame.grid(row=2)

        # starting balance (row 2.0/1)

        self.questions_asked_label = Label(self.details_frame, text="Questions Asked: ",
                                         font=heading, anchor="e")
        self.questions_asked_label.grid(row=0, column=0, padx=0)

        self.start_balance_value_label = Label(self.details_frame, font=content,
                                               text="{}".format(rounds_history))

        self.start_balance_value_label.grid(row=0, column=1, padx=0)

        # current balance (row 2.2)
        self.current_balance_label = Label(self.details_frame, text="Current Balance: ",
                                           font=heading, anchor="e")
        self.current_balance_label.grid(row=1, column=0, padx=0)

        self.current_balance_value_label = Label(self.details_frame, font=content,
                                                 text="{}".format(game_stats[1]))
        self.current_balance_value_label.grid(row=1, column=1, padx=0)

        if game_stats[1] > game_stats[0]:
            win_loss = "Amount Won:"
            amount = game_stats[1] - game_stats[0]
            win_loss_fg = "green"
        else:
            win_loss = "Amount Lost:"
            amount = game_stats[0] - game_stats[1]
            win_loss_fg = "#660000"

        # amount won / lost (row 2.3)
        self.win_loss_label = Label(self.details_frame, text=win_loss, font=heading,
                                    anchor="e")
        self.win_loss_label.grid(row=2, column=0, padx=0)

        self.win_loss_value_label = Label(self.details_frame, font=content,
                                          text="{}".format(amount), fg=win_loss_fg,
                                          anchor="w")
        self.win_loss_value_label.grid(row=2, column=1, padx=0)

        # Dismiss button (row 3)
        self.dismiss_btn = Button(self.details_frame, text="Dismiss",
                                  width=10, bg="#660000", fg="white",
                                  font="Arial 15 bold", command=partial(self.close_stats, partner))
        self.dismiss_btn.grid(row=3, column=0, pady=10)

        # export button (row=1)
        self.export_button = Button(self.details_frame, text="Export",
                                    width=10, bg="#0e0066", fg="white",
                                    font="Arial 15 bold",
                                    command=lambda: self.to_export(rounds_history, game_stats))
        self.export_button.grid(row=3, column=1, pady=10)

    def close_stats(self, partner):
        # put calc history button back to normal
        partner.stats_button.config(state=NORMAL)
        self.stats_box.destroy()

    def to_export(self, rounds_history, all_game_stats):
        Export(self, rounds_history, all_game_stats)


class Export:
    def __init__(self, partner, rounds_history, all_game_stats):

        print(rounds_history)

        # disable export button
        partner.export_button.config(state=DISABLED)

        # sets up child window
        self.export_box = Toplevel()

        # if users press cross at top, closes and releases
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export,
                                                             partner))

        # set up gui frame
        self.export_frame = Frame(self.export_box, width=300)
        self.export_frame.grid()

        # set up heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export / Instructions",
                                 font="arial 14 bold")
        self.how_heading.grid(row=0)

        # Export instructions (label, row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename into the box below "
                                                         "and press the Save button to save your "
                                                         "calculation history to a text file.",
                                 justify=LEFT, width=40, wrap=250)
        self.export_text.grid(row=1)

        # warning text (label, row 2)
        self.export_text = Label(self.export_frame, text="If the filename you enter below already exists, "
                                                         "its contents will be replaced with your "
                                                         "calculation history.",
                                 justify=LEFT, bg="#ffafaf", fg="maroon",
                                 font="Arial 10 italic", wrap=225, padx=10, pady=10)
        self.export_text.grid(row=2, pady=10)

        # filename entry box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # error message labels(row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="maroon")
        self.save_error_label.grid(row=4)

        # save / cancel frame (row 5)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and cancel buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  font="Arial 15 bold", bg="#003366", fg="white",
                                  command=partial(lambda: self.save_history(partner, rounds_history, all_game_stats)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    font="Arial 15 bold", bg="#660000", fg="white",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def save_history(self, partner, rounds_history, game_stats):

        # regular expression to check filename is valid
        valid_char = "[A-Za-z0-9]"
        has_error = "no"

        filename = self.filename_entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = "(no spaces allowed)"

            else:
                problem = ("(no {}'s allowed)".format(letter))
            has_error = "yes"
            break

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            # display error message
            self.save_error_label.config(text="Invalid filename - {}".format(problem))
            # Change entry box background to pink
            self.filename_entry.config(bg="#ffafaf")
            print()

        else:
            # if there are no errors, generate text file and then
            # close dialogue and .txt suffix
            filename = filename + ".txt"

            # remove previous error message, and change colour to green
            # display error message
            self.save_error_label.config(text="Confirmed", fg="Green")
            # Change entry box background to pink
            self.filename_entry.config(bg="#b0ffaf")
            self.cancel_button.config(text="Close")

            # create file to hold data
            f = open(filename, "w+")

            # heading for stats
            f.write("Game Statistics\n\n")

            # numbers at top
            f.write("[Starting Balance, Current Balance]:{}".format(game_stats))

            # heading for rounds
            f.write("\n\nRound Details\n\n")

            # add new line at the end of each item
            for item in rounds_history:
                f.write(item + "\n")

            # close file
            f.close()

    def close_export(self, partner):
        # put calc history button back to normal
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Assessment Game")
    something = Start(root)
    root.mainloop()
