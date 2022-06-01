from tkinter import *
from functools import partial  # to prevent unwanted windows
import random


class Intro:
    def __init__(self, parent):

        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        self.push_me_button = Button(text="Push Me", command=self.to_start)
        self.push_me_button.grid(row=0, pady=10)

    def to_start(self):

        Start(self)

        # hide pop up window
        root.withdraw()


class Start:
    def __init__(self, parent):

        # GUI setup
        self.game_box = Toplevel()
        self.start_frame = Frame(self.game_box)
        self.start_frame.grid()

        '''self.questions = ["a", 'b', "c"]
        self.answers = ["A", "B", "C"]

        # giu to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()'''

        # set initial balance to zero
        self.starting_funds = IntVar()
        self.starting_funds.set(0)

        # mystery heading (row 0)
        self.mystery_box_label = Label(self.start_frame, text="Mystery Box Game",
                                       font="Arial 19 bold")
        self.mystery_box_label.grid(row=0)

        # Initial instructions (row 1)
        self.mystery_instructions = Label(self.start_frame, font="Arial 10 italic",
                                          text="Please enter a dollar amount "
                                               "(between $5 and $50) in the box below. "
                                               "Then choose the stakes. The higher the "
                                               "stakes the more you can win!",
                                          wrap=275, justify=LEFT, padx=10, pady=10)
        self.mystery_instructions.grid(row=1)

        # Entry box, button and error label (row 2)
        self.entry_error_frame = Frame(self.start_frame, width=200)
        self.entry_error_frame.grid(row=2)

        self.answer_entry = Entry(self.entry_error_frame,
                                  font="Arial 19 bold", width=10)
        self.answer_entry.grid(row=0, column=0)

        random_num = (random.randint(0, 2))

        self.add_funds_button = Button(self.entry_error_frame,
                                       font="Arial 14 bold",
                                       text="Add Funds",
                                       command=self.check_funds(random_num))
        self.add_funds_button.grid(row=0, column=1)

        self.amount_error_label = Label(self.entry_error_frame, fg="maroon",
                                        text="", font="Arial 10 bold", wrap=275,
                                        justify=LEFT)
        self.amount_error_label.grid(row=1, columnspan=2, pady=5)

        # button frame ()row 3
        self.stakes_frame = Frame(self.start_frame)
        self.stakes_frame.grid(row=3)

        # Buttons go here  ***************
        button_font = "Arial 12 bold"

        # yellow low stakes button
        self.lowstakes_button = Button(self.stakes_frame, text="Low ($5)",
                                       command=lambda: self.to_game(1),
                                       font=button_font, bg="yellow")
        self.lowstakes_button.grid(row=0, column=0, pady=10)

        # orange med stakes button
        self.medstakes_button = Button(self.stakes_frame, text="Medium ($10)",
                                       command=lambda: self.to_game(2),
                                       font=button_font, bg="orange")
        self.medstakes_button.grid(row=0, column=1, padx=5, pady=10)

        # red high stakes button
        self.highstakes_button = Button(self.stakes_frame, text="High ($15)",
                                        command=lambda: self.to_game(3),
                                        font=button_font, bg="red")
        self.highstakes_button.grid(row=0, column=2, pady=10)

        # disable all stakes buttons at start
        self.lowstakes_button.config(state=DISABLED)
        self.medstakes_button.config(state=DISABLED)
        self.highstakes_button.config(state=DISABLED)

        # Help button
        self.help_button = Button(self.start_frame, text="How to Play",
                                  bg="#808080", fg="white", font=button_font,
                                  command=self.to_help)
        self.help_button.grid(row=4, pady=10)

    def to_help(self):
        get_help = Help(self)

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
        # self.amount_error_label.config(text="")

        # disable all stakes buttons in case user changes mind and decreases amount entered
        # self.enter_button.config(state=DISABLED)

        try:
            given_answer = str(given_answer)  # string?

            #  if len(self.all_calc_list) == 0:

            if given_answer == self.answers[random_num]:
                print("h")

        except ValueError:
            has_errors = "yes"
            error_feedback = "spelling?"

        if has_errors == "yes":
            self.answer_entry.config(bg=error_back)
            self.amount_error_label.config(text=error_feedback)

        else:
            # set starting balance to amount entered by user
            # self.starting_funds.set(given_answer)
            self.answer_entry.config(bg="#33ff3d")

        # do stuff here?

    def check_funds(self, random_num):
        given_answer = self.answer_entry.get()
        print("***********")
        print(self.answer_entry)
        print("***********")

        starting_balance = 5

        # Set error background colours and assume no errors
        error_back = "#ffafaf"
        has_errors = "no"

        # change background to white
        self.answer_entry.config(bg="white")
        self.amount_error_label.config(text="")

        # disable all stakes buttons in case user changes mind and decreases amount entered
        self.lowstakes_button.config(state=DISABLED)
        self.medstakes_button.config(state=DISABLED)
        self.highstakes_button.config(state=DISABLED)

        try:
            starting_balance = int(starting_balance)

            if starting_balance < 5:
                has_errors = "yes"
                error_feedback = "Sorry, the least you can play with is $5"
            elif starting_balance > 50:
                has_errors = "yes"
                error_feedback = "Too High! The most you can risk in this game is $50"

            elif starting_balance >= 15:
                # enable all buttons
                self.lowstakes_button.config(state=NORMAL)
                self.medstakes_button.config(state=NORMAL)
                self.highstakes_button.config(state=NORMAL)

            elif starting_balance >= 10:
                # enable low and medium stakes buttons
                self.lowstakes_button.config(state=NORMAL)
                self.medstakes_button.config(state=NORMAL)

            else:
                self.lowstakes_button.config(state=NORMAL)

        except ValueError:
            has_errors = "yes"
            error_feedback = "Please enter a dollar amount (no text / decimals)"

        if has_errors == "yes":
            self.answer_entry.config(bg=error_back)
            self.amount_error_label.config(text=error_feedback)

        else:
            # set starting balance to amount entered by user
            self.starting_funds.set(starting_balance)

    def to_game(self, stakes):

        # retrieve starting balance
        starting_balance = self.starting_funds.get()

        Game(self, stakes, starting_balance)

        # hide start up window
        root.withdraw()


class Game:
    def __init__(self, partner, stakes, starting_balance):
        print(stakes)
        print(starting_balance)

        # initialize variables
        self.balance = IntVar()

        # set starting balance to amount entered by user at start of game
        self.balance.set(starting_balance)

        # get value of stakes (ues it as a multiplier when calculating winnings)
        self.multiplier = IntVar()
        self.multiplier.set(stakes)

        # list for holding stats
        self.round_stats_list = []
        self.game_stats_list = [starting_balance, starting_balance]

        # GUI setup
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Heading row
        self.heading_label = Label(self.game_frame, text="Play...",
                                   font="Arial 24 bold",
                                   padx=10, pady=10)
        self.heading_label.grid(row=0)

        # Instructions Label
        self.instructions_label = Label(self.game_frame, font="Arial 10",
                                        text="Please <enter> of click 'Open "
                                             "Boxes' button to revel the "
                                             "contents of the mystery boxes",
                                        wrap=300, justify=LEFT, padx=10, pady=10)
        self.instructions_label.grid(row=1)

        # Boxes go here (row 2)
        box_text = "Arial 16 bold"
        box_back = "#b9ea96"   # light green
        box_width = 5
        self.box_frame = Frame(self.game_frame)
        self.box_frame.grid(row=2, pady=10)

        self.prize1_label = Label(self.box_frame, text="?\n", font=box_text,
                                  bg=box_back, width=box_width, padx=10, pady=10)
        self.prize1_label.grid(row=0, column=0)

        self.prize2_label = Label(self.box_frame, text="?\n", font=box_text,
                                  bg=box_back, width=box_width, padx=10, pady=10)
        self.prize2_label.grid(row=0, column=1, padx=10)

        self.prize3_label = Label(self.box_frame, text="?\n", font=box_text,
                                  bg=box_back, width=box_width, padx=10, pady=10)
        self.prize3_label.grid(row=0, column=2)

        # Play button goes here (row 3)
        self.play_button = Button(self.game_frame, text="Open Boxes",
                                  bg="#FFFF33", font="Arial 15 bold", width=20,
                                  padx=10, pady=10, command=self.reveal_boxes)
        self.play_button.grid(row=3)

        # enter to revel boxes

        self.play_button.focus()
        self.play_button.bind('<Return>', lambda e: self.reveal_boxes())
        self.play_button.grid(row=3)

        # Balance label (row 4)

        start_text = "Game Cost: ${} \n""\nHow much " \
                     "will you win?".format(stakes * 5)

        self.balance_frame = Frame(self.game_frame)
        self.balance_frame.grid(row=1)

        self.balance_label = Label(self.game_frame, font="Arial 12 bold", text=start_text,
                                   fg="green", wrap=300, justify=LEFT)
        self.balance_label.grid(row=4, pady=10)

        # help and game stats button (row 5)
        self.export_help_frame = Frame(self.game_frame)
        self.export_help_frame.grid(row=5, pady=10)

        # Help button
        self.help_button = Button(self.export_help_frame, text="Help / Rules",
                                  font="Arial 15 bold",
                                  bg="#808080", fg="white",
                                  command=self.to_help)
        self.help_button.grid(row=0, column=0, padx=2)

        self.stats_button = Button(self.export_help_frame, text="Game Stats",
                                   font="Arial 15 bold",
                                   bg="#003366", fg="white",
                                   command=lambda: self.to_stats(self.round_stats_list, self.game_stats_list))
        self.stats_button.grid(row=0, column=1, padx=2)

        # quit button
        self.quit_button = Button(self.game_frame, text="Quit", fg="white",
                                  bg="#660000", font="Arial 15 bold", width=20,
                                  command=self.to_quit)
        self.quit_button.grid(row=6, pady=10)

    def to_stats(self, game_history, game_stats):
        GameStats(self, game_history, game_stats)

    def to_help(self):
        get_help = Help(self)

    def reveal_boxes(self):
        # get the balance from the initial function...
        current_balance = self.balance.get()
        stakes_multiplier = self.multiplier.get()

        round_winnings = 0
        prizes = []

        for item in range(0, 3):
            prize_num = random.randint(1, 100)

            if 0 < prize_num <= 5:
                prize = "gold\n(${})".format(5 * stakes_multiplier)
                round_winnings += 5 * stakes_multiplier

            elif 5 < prize_num <= 25:
                prize = "silver\n(${})".format(2 * stakes_multiplier)
                round_winnings += 2 * stakes_multiplier

            elif 25 < prize_num <= 65:
                prize = "copper\n(${})".format(1 * stakes_multiplier)
                round_winnings += stakes_multiplier

            else:
                prize = "lead\n($0)"

            prizes.append(prize)

        # display prizes...

        self.prize1_label.config(text=prizes[0])
        self.prize2_label.config(text=prizes[1])
        self.prize3_label.config(text=prizes[2])

        # deduct cost of game
        current_balance -= 5 * stakes_multiplier

        # add winnings
        current_balance += round_winnings

        # set balance to new balance
        self.balance.set(current_balance)
        # update game_stats_list with current balance (replace item in
        # position 1 with current balance
        self.game_stats_list[1] = current_balance

        balance_statement = "Game Cost: ${} \nPayback: ${} \n" \
                            "Current Balance: ${}".format(5*stakes_multiplier,
                                                          round_winnings,
                                                          current_balance)
        # Edit Label so user can see their balance
        self.balance_label.configure(text=balance_statement)

        if current_balance < 5 * stakes_multiplier:
            self.play_button.config(state=DISABLED)
            self.game_box.focus()
            self.play_button.config(text="Game Over")

            balance_statement = "Current balance: ${}\n" \
                                "Your balance in too low. You can only quit " \
                                "or view your stats. Sorry about that.".format(current_balance)
            self.balance_label.config(fg="#660000", font="Arial 10 bold",
                                      text=balance_statement)

        # add round results to stats list
        round_summary = "{} | {} | {} - Cost: ${} |" \
                        "Payback: ${} | Current Balance: " \
                        "${}".format(prizes[0], prizes[1], prizes[2],
                                     5 * stakes_multiplier, round_winnings, current_balance)
        self.round_stats_list.append(round_summary)
        print(self.round_stats_list)

    def to_quit(self):
        root.destroy()


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

        help_text = "Choose and amount to play with and then choose the stakes." \
                    "Higher stakes cost more per round but you can win more as well.\n\n" \
                    "When you enter the play area, you will see three mystery boxes. To reveal" \
                    "the contents of the boxes, click the 'Open Boxes' button. If you don't have " \
                    "enough money to play, the button will turn red and you need to quit the game.\n\n" \
                    "The contents of the boxes will be added to your balance. The boxes could contain...\n\n" \
                    "Low: Lead($0) | Copper ($1) | Silver($2) | Gold ($10)\n" \
                    "Medium: Lead($0) | Copper ($2) | Silver($4) | Gold ($25)\n" \
                    "High: Lead($0) | Copper ($5) | Silver($10) | Gold ($50)\n\n" \

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
    def __init__(self, partner, game_history, game_stats):

        print(game_history)

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

        self.start_balance_label = Label(self.details_frame, text="Starting Balance: ",
                                         font=heading, anchor="e")
        self.start_balance_label.grid(row=0, column=0, padx=0)

        self.start_balance_value_label = Label(self.details_frame, font=content,
                                               text="${}".format(game_stats[0]))   # meant to something else here
        self.start_balance_value_label.grid(row=0, column=1, padx=0)

        # current balance (row 2.2)
        self.current_balance_label = Label(self.details_frame, text="Current Balance: ",
                                           font=heading, anchor="e")
        self.current_balance_label.grid(row=1, column=0, padx=0)

        self.current_balance_value_label = Label(self.details_frame, font=content,
                                                 text="${}".format(game_stats[1]))  # meant to something else here
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
                                          text="${}".format(amount), fg=win_loss_fg,
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
                                    command=lambda: self.to_export(game_history, game_stats))
        self.export_button.grid(row=3, column=1, pady=10)

    def close_stats(self, partner):
        # put calc history button back to normal
        partner.stats_button.config(state=NORMAL)
        self.stats_box.destroy()

    def to_export(self, game_history, all_game_stats):
        Export(self, game_history, all_game_stats)


class Export:
    def __init__(self, partner, game_history, all_game_stats):

        print(game_history)

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
                                  command=partial(lambda: self.save_history(partner, game_history, all_game_stats)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    font="Arial 15 bold", bg="#660000", fg="white",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def save_history(self, partner, game_history, game_stats):

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
            for item in game_history:
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
    root.title("Mystery Box Game")
    something = Start(root)
    root.mainloop()
