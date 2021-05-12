from tkinter import *
from functools import partial  # To prevent unwanted windows

import random


class Converter:
    def __init__(self, parent):

        # Formatting Variables
        background_colour = "#2883F4"

        self.all_calc_list = ['0 degrees C is 32 degrees F', '-17.8 degrees C is -0.0 degrees F',
                              '40 degrees C is 104 degrees F', '4.4 degrees C is 39.9 degrees F',
                              '12 degrees C is 53.6 degrees F', '24 degrees C is 75.2 degrees F',
                              '100 degrees C is 212 degrees F']

        # Convertor Main Screen GUI
        self.converter_frame = Frame(width=600, height=600, bg=background_colour, pady=10)
        self.converter_frame.grid()

        # Temperature Conversion Heading
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                          font=("Arial", "16", "bold"),
                                          padx=10, pady=10,
                                          bg=background_colour)
        self.temp_converter_label.grid(row=0)

        # History Button
        self.history_button = Button(self.converter_frame,
                                     text="History", padx=10, pady=10,
                                     font=("Arial", "14"),
                                     command=lambda: self.history(self.all_calc_list))
        self.history_button.grid(row=1)

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

        if len(calc_history) >= 7:
            for item in range(0, 7):
                history_string += calc_history[len(calc_history) - item - 1] + "\n"
        else:
            for item in calc_history:
                history_string += calc_history[len(calc_history) - calc_history.index(item) - 1] + "\n"

                self.history_text.config(text="Here is your calculation history. You can use the export data to save"
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
