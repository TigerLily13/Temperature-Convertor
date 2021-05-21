from tkinter import *
from functools import partial  # To prevent unwanted windows
import re


class Converter:
    def __init__(self, parent):

        # Formatting Variables
        background_colour = "#2883F4"

        self.all_calc_list = []

        # Convertor Main Screen GUI
        self.converter_frame = Frame(width=600, height=600, bg=background_colour, pady=10)
        self.converter_frame.grid()

        # Temperature Conversion Heading
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                          font=("Arial", "16", "bold"),
                                          padx=10, pady=10,
                                          bg=background_colour)
        self.temp_converter_label.grid(row=0)

        # User Instructions
        self.temp_instructions_label = Label(self.converter_frame, text="Type in the amount to be converted "
                                                                        "and then push one of the buttons below:",
                                             wrap=290, padx=10,
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

        # Help / History Button Frame
        self.help_history_frame = Frame(self.converter_frame)
        self.help_history_frame.grid(row=5, pady=10)

        # Help Button
        self.help_button = Button(self.help_history_frame,
                                  text="Help", padx=10, pady=10,
                                  font=("Arial", "14", "bold"), command=self.help)
        self.help_button.grid(row=0)

        # History Button
        self.history_button = Button(self.help_history_frame,
                                     text="History", padx=10, pady=10,
                                     font=("Arial", "14", "bold"), command=lambda: self.history(self.all_calc_list))
        self.history_button.grid(row=0, column=1)

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
                fahrenheit = (to_convert * 9 / 5) + 32
                to_convert = self.rounding(to_convert)
                fahrenheit = self.rounding(fahrenheit)
                answer = "{} degrees C is {} degrees F".format(to_convert, fahrenheit)

            # Convert to C
            elif low == -459 and to_convert >= low:
                celsius = (to_convert - 32) * 5 / 9
                to_convert = self.rounding(to_convert)
                celsius = self.rounding(celsius)
                answer = "{} degrees F is {} degrees C".format(to_convert, celsius)

            else:
                # Input is too cold
                answer = "Too Cold!"
                has_errors = "yes"

            # Display Answer
            if has_errors == "no":
                self.converted_label.configure(text=answer, fg="white")
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

    def help(self):
        get_help = Help(self)
        get_help.help_text.configure(text="Please enter a number in the box and then push one of the buttons "
                                          "to convert to either celsius or fahrenheit.\n\nThe Calculation History"
                                          "area shows up to you most recent seven calculations (most recent at top)."
                                          "\n\nYou can also export your full calculation history to a .txt file "
                                          "if desired.")


class History:
    def __init__(self, partner, calc_history):

        background = "#2883F4"

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
        self.export_button = Button(self.export_dismiss_frame, text="Export", font=("arial", "12", "bold"),
                                    command=lambda: self.export(calc_history))
        self.export_button.grid(row=0, column=0)

        # Dismiss Button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss", font=("arial", "12", "bold"),
                                     command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1)

    def export(self, calc_history):
        Export(self, calc_history)

    def close_history(self, partner):

        # Put history button back to normal
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()


class Export:
    def __init__(self, partner, calc_history):

        background = "#2883F4"

        # Disable Export Button
        partner.export_button.config(state=DISABLED)

        # Set up child window (export box)
        self.export_box = Toplevel()

        # Release Export Button if cross is used
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, bg=background, width=300)
        self.export_frame.grid()

        # Export Heading
        self.export_heading = Label(self.export_frame, text="Export History",
                                    font=("Arial", "10", "bold"), bg=background)
        self.export_heading.grid(row=0)

        # Export Text
        self.export_text = Label(self.export_frame, text="Enter a filename in the box below and press the save button "
                                                         "to save your calculation history in a text file",
                                 justify=LEFT, width=40, bg=background, wrap=250)
        self.export_text.grid(row=1)

        self.export_text = Label(self.export_frame, text="If the filename you entered below already exists, its"
                                                         "contents will be replaced with your calculation history.",
                                 justify=LEFT, bg="#ffafaf", fg="maroon", wrap=225, padx=10)
        self.export_text.grid(row=2)

        # Filename entry box
        self.filename_entry = Entry(self.export_frame, width=20, font=("Arial", "14", "bold"), justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Error Message
        self.save_error_label = Label(self.export_frame, text="", fg="maroon", bg=background)
        self.save_error_label.grid(row=4)

        # Save / Cancel Frame
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save Button
        self.save_button = Button(self.save_cancel_frame, text="Save", font=("Arial", "10", "bold"),
                                  command=partial(lambda: self.save_history(partner, calc_history)))
        self.save_button.grid(row=0, column=0)

        # Cancel button
        self.cancel_button = Button(self.save_cancel_frame, text="Cancel", width=10, font=("Arial", "10", "bold"),
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def save_history(self, partner, calc_history):

        valid_char = "[A-Za-z0-9]"
        has_error = "no"

        filename = self.filename_entry.get()

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = "No spaces allowed"

            else:
                problem = ("No {} allowed".format(letter))
            has_error = "yes"
            break

        if filename == "":
            problem = "Can't be blank"

            has_error = "yes"

        if has_error == "yes":
            self.save_error_label.config(text="Invalid filename - {}" .format(problem))
            self.filename_entry.config(bg="#ffafaf")
            print()

        else:
            # Add .txt prefix
            filename = filename + ".txt"

            # Create file
            f = open(filename, "w+")

            # Add new line for each item
            for item in calc_history:
                f.write(item + "\n")

            # Close file
            f.close()

            self.close_export(partner)

    def close_export(self, partner):

        # Put Export button back to normal
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()


class Help:
    def __init__(self, partner):

        background = "#2883F4"

        # Disable Help Button
        partner.help_button.config(state=DISABLED)

        # Set up child window (help box)
        self.help_box = Toplevel()

        # Release Help Button if cross is used
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, bg=background, width=300)
        self.help_frame.grid()

        # Help Heading
        self.help_heading = Label(self.help_frame, text="Help/Instructions",
                                  font=("Arial", "10", "bold"), bg=background)
        self.help_heading.grid(row=0)

        # Help Text
        self.help_text = Label(self.help_frame, text="",
                               justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        # Dismiss button
        self.dismiss_button = Button(self.help_frame, text="Dismiss", width=10, font=("Arial", "10", "bold"),
                                     command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, pady=10)

    def close_help(self, partner):

        # Put Help button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Converter(root)
    root.mainloop()
