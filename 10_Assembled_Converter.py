from tkinter import *
from functools import partial  # To prevent unwanted windows

import random


class Converter:
    def __init__(self, parent):

        # Formatting Variables
        background_colour = '#2883F4'

        # List to Hold Calculation History
        self.all_calc_list = []

        # Converter Frame
        self.converter_frame = Frame(bg=background_colour, pady=10)
        self.converter_frame.grid()

        # Temperature Converter Heading
        self.temp_heading_label = Label(self.converter_frame, text="Temperature Converter",
                                        font=('Arial', '19', 'bold'), bg=background_colour,
                                        padx=10, pady=10)
        self.temp_heading_label.grid(row=0)

        # User Instructions
        self.temp_instructions_label = Label(self.converter_frame, text="Type in the amount to be converted "
                                             "and then push one of the buttons below:", wrap=290, padx=10,
                                             pady=10, font=('Arial', '10', 'italic'), justify=LEFT,
                                             bg=background_colour)
        self.temp_instructions_label.grid(row=1)

        # Temperature Entry Box
        self.to_convert_entry = Entry(self.converter_frame, width=20, font=('Arial', '14', 'bold'))
        self.to_convert_entry.grid(row=2)

        # Conversion Buttons Frame
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        self.to_c_button = Button(self.conversion_buttons_frame, text="To Centigrade", bg="#FC8621",
                                  font=('Arial', '10', 'bold'), padx=10, pady=10,
                                  command=lambda: self.temp_convert(-459))
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame, text="To Fahrenheit", bg="#FC8621",
                                  font=('Arial', '10', 'bold'), padx=10, pady=10,
                                  command=lambda: self.temp_convert(-273))
        self.to_f_button.grid(row=0, column=1)

        # Answer Label
        self.converted_label = Label(self.converter_frame, font=("Arial", "12", "bold"), fg="purple",
                                     bg=background_colour, pady=10)
        self.converted_label.grid(row=4)

        # History + Help Button Frame
        self.hist_help_frame = Frame(self.converter_frame)
        self.hist_help_frame.grid(row=5, pady=10)

        self.history_button = Button(self.hist_help_frame, font=("Arial", "12", "bold"), width=15,
                                     text="Calculation History", command=lambda: self.history(self.all_calc_list))
        self.history_button.grid(row=0, column=0)

        if len(self.all_calc_list) == 0:
            self.history_button.config(state=DISABLED)

        self.help_button = Button(self.hist_help_frame, font=("Arial", "12", "bold"), width=5,
                                  text="Help")
        self.help_button.grid(row=0, column=1)

    def temp_convert(self, low):
        error = "#ffafaf"

        # Retrieve amount in text box
        to_convert = self.to_convert_entry.get()

        # Check amount is valid
        try:
            to_convert = float(to_convert)
            has_errors = "no"

            # Convert to F
            if low == -273 and to_convert >= low:
                fahrenheit = (to_convert * 9/5) + 32
                to_convert = self.rounding(to_convert)
                fahrenheit = self.rounding(fahrenheit)
                answer = "{} degrees C is {} degrees F" .format(to_convert, fahrenheit)

            # Convert to C
            elif low == -459 and to_convert >= low:
                celsius = (to_convert - 32) * 5/9
                to_convert = self.rounding(to_convert)
                celsius = self.rounding(celsius)
                answer = "{} degrees F is {} degrees C" .format(to_convert, celsius)

            else:
                # Input is too cold
                answer = "Too Cold!"
                has_errors = "yes"

            # Display Answer
            if has_errors == "no":
                self.converted_label.configure(text=answer, fg="blue")
                self.to_convert_entry.configure(bg="white")

            else:
                self.converted_label.configure(text=answer, fg="red")
                self.to_convert_entry.configure(bg=error)

            # Add answer to list
            if has_errors != "yes":
                self.all_calc_list.append(answer)
                self.history_button.config(state=NORMAL)

        # Store Answer

        except ValueError:
            self.converted_label.configure(text="Please enter a number!", fg="red")
            self.to_convert_entry.configure(bg=error)

    def rounding(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)

        else:
            rounded = round(to_round, 1)

        return rounded

    def history(self, calc_history):
        History(self, calc_history)


class History:
    def __init__(self, partner, calc_history):

        background = "orange"

        # Disable History Button
        partner.history_button.config(state=DISABLED)

        # Set up child window (history box)
        self.history_box = Toplevel()

        # Release History Button if cross is used
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        # Set up GUI Frame
        self.history_frame = Frame(self.history_box, bg=background, width=300)
        self.history_frame.grid()

        # History Heading
        self.history_heading = Label(self.history_frame, text="Calculation History",
                                     font=("Arial", "10", "bold"), bg=background)
        self.history_heading.grid(row=0)

        # History Text
        self.history_text = Label(self.history_frame, text="Here are you most recent calculations. "
                                                           "Use the export button to create a txt file of all "
                                                           "your calculations for this session.", wrap=250,
                                  font=("arial", "10", "italic"), justify=LEFT, width=40, bg=background)
        self.history_text.grid(row=1)

        # Generate string from Calculation List
        history_string = ""

        if len(calc_history) > 7:
            for item in range(0, 7):
                history_string += calc_history[len(calc_history) - item - 1] + "\n"
        else:
            for item in calc_history:
                history_string += calc_history[len(calc_history) - calc_history.index(item) - 1] + "\n"

                self.history_text.config(text="Here is your calculation history. You can use the export data to save "
                                              "this data to a txt file if desired.")

        # Display Calc History
        self.calc_label = Label(self.history_frame, text=history_string, bg=background,
                                font=("arial", "12"), justify=LEFT)
        self.calc_label.grid(row=2)

        # Export / Dismiss Button Frame
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export Button
        self.export_button = Button(self.export_dismiss_frame, text="Export", font=("arial", "12", "bold"))
        self.export_button.grid(row=0, column=0)

        # Dismiss Button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss", font=("arial", "12", "bold"),
                                     command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1)

    def close_history(self, partner):

        # Put history button back to normal
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Converter(root)
    root.mainloop()
