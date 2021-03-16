from tkinter import *
from functools import partial  # To prevent unwanted windows

import random


class Converter:
    def __init__(self, parent):

        # Formatting Variables
        background_colour = '#2883F4'

        # Converter Frame
        self.converter_frame = Frame(width=300, bg=background_colour, pady=10)
        self.converter_frame.grid()

        # Temperature Converter Heading
        self.temp_heading_label = Label(self.converter_frame, text="Temperature Converter",
                                        font=('Arial', '16', 'bold'), bg=background_colour,
                                        padx=10, pady=10)
        self.temp_heading_label.grid(row=0)

        # User Instructions
        self.temp_instructions_label = Label(self.converter_frame, text="Type in the amount to be converted "
                                             "and then push one of the buttons below:", wrap=250, padx=10,
                                             pady=10, font=('Arial', '10', 'italic'), justify=LEFT,
                                             bg=background_colour)
        self.temp_instructions_label.grid(row=1)

        # Temperature Entry Box
        self.to_convert_entry = Entry(self.converter_frame, width=20, font=('Arial', '14', 'bold'))
        self.to_convert_entry.grid(row=2)

        # Conversion Buttons Frame
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        self.to_c_button = Button(self.conversion_buttons_frame, text="To Centigrade", bg="Khaki",
                                  font=('Arial', '10', 'bold'), padx=10, pady=10)
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame, text="To Fahrenheit", bg="Khaki",
                                  font=('Arial', '10', 'bold'), padx=10, pady=10)
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


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Converter(root)
    root.mainloop()