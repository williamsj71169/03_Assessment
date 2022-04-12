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

        # retrieve starting balance
        starting_balance = 50
        stakes = 1

        Game(self, stakes, starting_balance)

        # hide pop up window
        root.withdraw()


class Game:
    def __init__(self, partner, rounds, starting_score):
        print(rounds)
        print(starting_score)

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

        # info section(row 2)
        start_text = "Game Cost: ${} \n""\nHow much " \
                     "will you win?".format(rounds * 5)

        self.score_frame = Frame(self.game_frame)
        self.score_frame.grid(row=1)

        self.score_label = Label(self.game_frame, font="Arial 12 bold", text=start_text,
                                 fg="green", wrap=300, justify=LEFT)
        self.score_label.grid(row=1, pady=10)

        # Entry box, button and error label (row 2 column 0)
        self.entry_error_frame = Frame(self.game_frame, width=200)
        self.entry_error_frame.grid(row=2)

        self.start_amount_entry = Entry(self.entry_error_frame,
                                        font="Arial 15 bold", width=10)
        self.start_amount_entry.grid(row=0, column=0)

        # Play button goes here (row 2)
        self.play_button = Button(self.entry_error_frame, text="Enter",
                                  bg="#FFFF33", font="Arial 15 bold")
        self.play_button.grid(row=0, column=1)

        # enter to revel boxes

        self.play_button.focus()
        self.play_button.bind('<Return>', lambda e: self.reveal_boxes())
        self.play_button.grid(row=3)

        # help and game stats button (row 5)
        self.export_help_frame = Frame(self.game_frame)
        self.export_help_frame.grid(row=5, pady=10)

        # Help button
        self.help_button = Button(self.export_help_frame, text="Help / Rules",
                                  font="Arial 15 bold",
                                  bg="#6200ff", fg="white",
                                  command=self.to_help)
        self.help_button.grid(row=0, column=0, padx=2)

        self.stats_button = Button(self.export_help_frame, text="Game Stats",
                                   font="Arial 15 bold",
                                   bg="#00e5ff", fg="white",
                                   command=lambda: self.to_stats(self.round_stats_list, self.game_stats_list))
        self.stats_button.grid(row=0, column=1, padx=2)

        # quit button
        self.quit_button = Button(self.game_frame, text="Quit", fg="white",
                                  bg="#ff00dd", font="Arial 15 bold", width=20,
                                  command=self.to_quit)
        self.quit_button.grid(row=6, pady=10)

    def to_stats(self, game_history, game_stats):
        GameStats(self, game_history, game_stats)

    def to_help(self):
        get_help = Help(self)

    def reveal_boxes(self):
        # get the score from the initial function...
        current_score = self.score.get()
        rounds_multiplier = self.multiplier.get()

        round_winnings = 0
        prizes = []

        for item in range(0, 3):
            prize_num = random.randint(1, 100)

            if 0 < prize_num <= 5:
                prize = "gold\n(${})".format(5 * rounds_multiplier)
                round_winnings += 5 * rounds_multiplier

            elif 5 < prize_num <= 25:
                prize = "silver\n(${})".format(2 * rounds_multiplier)
                round_winnings += 2 * rounds_multiplier

            elif 25 < prize_num <= 65:
                prize = "copper\n(${})".format(1 * rounds_multiplier)
                round_winnings += rounds_multiplier

            else:
                prize = "lead\n($0)"

            prizes.append(prize)

        # deduct cost of game
        current_score -= 5 * rounds_multiplier

        # add winnings
        current_score += round_winnings

        # set score to new score
        self.score.set(current_score)
        # update game_stats_list with current score (replace item in
        # position 1 with current score
        self.game_stats_list[1] = current_score

        score_statement = "Game Cost: ${} \nPayback: ${} \n" \
                          "Current Score: ${}".format(5*rounds_multiplier,
                                                      round_winnings,
                                                      current_score)
        # Edit Label so user can see their score
        self.score_label.configure(text=score_statement)

        if current_score < 5 * rounds_multiplier:
            self.play_button.config(state=DISABLED)
            self.game_box.focus()
            self.play_button.config(text="Game Over")

            score_statement = "Current score: ${}\n" \
                              "Your score in too low. You can only quit " \
                              "or view your stats. Sorry about that.".format(current_score)
            self.score_label.config(fg="#660000", font="Arial 10 bold",
                                    text=score_statement)

        # add round results to stats list
        round_summary = "{} | {} | {} - Cost: ${} |" \
                        "Payback: ${} | Current Score: " \
                        "${}".format(prizes[0], prizes[1], prizes[2],
                                     5 * rounds_multiplier, round_winnings, current_score)
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
