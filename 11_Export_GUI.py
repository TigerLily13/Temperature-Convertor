from tkinter import *
from functools import partial  # To prevent unwanted windows

import random


class Converter:
    def __init__(self, parent):

        # Formatting Variables
        background_colour = "#2883F4"

        # Convertor Main Screen GUI
        self.converter_frame = Frame(width=600, height=600, bg=background_colour, pady=10)
        self.converter_frame.grid()

        # Temperature Conversion Heading
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                          font=("Arial", "16", "bold"),
                                          padx=10, pady=10,
                                          bg=background_colour)
        self.temp_converter_label.grid(row=0)

        # Export Button
        self.export_button = Button(self.converter_frame,
                                    text="Export", padx=10, pady=10,
                                    font=("Arial", "14"),
                                    command=self.export)
        self.export_button.grid(row=1)

    def export(self):
        print("You asked for export")
        get_export = Export(self)
        get_export.export_text.configure(text="Export text goes here")


class Export:
    def __init__(self, partner):

        background = "orange"

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
        self.export_text = Label(self.export_frame, text="",
                               justify=LEFT, width=40, bg=background, wrap=250)
        self.export_text.grid(row=1)

        # Dismiss button
        self.dismiss_button = Button(self.export_frame, text="Dismiss", width=10, bg=background,
                                     command=partial(self.close_export, partner))
        self.dismiss_button.grid(row=2, pady=10)

    def close_export(self, partner):

        # Put Export button back to normal
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Converter(root)
    root.mainloop()
