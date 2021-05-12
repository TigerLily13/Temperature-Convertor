from tkinter import *
from functools import partial  # To prevent unwanted windows

import random


class Converter:
    def __init__(self, parent):

        # Formatting Variables
        background_colour = '#2883F4'

        # List to Hold Calculation History
        self.all_calulations = []

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

        self.calc_hist_button = Button(self.hist_help_frame, font=("Arial", "12", "bold"), width=15,
                                       text="Calculation History")
        self.calc_hist_button.grid(row=0, column=0)

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
            if answer != "Too Cold!":
                self.all_calulations.append(answer)
                print(self.all_calulations)

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


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Converter(root)
    root.mainloop()
