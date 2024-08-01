"""
Author: John Eric Ragos
Purpose: To create a GUI for the starting interface
Date: 25/06/2024
Version 1: Create a GUI for the starting interface
"""
# Imports
from tkinter import *

# info text
info = """
 This program allows you to make your very own customizable
 sandwiches

 Things you can do using this program:
 1. Make your very own customisable sandwiches
 2. Name your own sandwich
 3. Order the sandwich you made
"""

# Colours
light_green = "#D9EAD3"
light_peach = "#FCE5CD"
light_yellow = "#FFF2CC"
light_cornflower_blue = "#C9DAF8"
light_magenta = "#EAD1DC"

# Fonts
courier = ("Courier", 17, "bold")
header_courier = ("Courier", 20, "bold")
sub_head_courier = ("Courier", 12, "bold")
info_courier = ("Courier", 10, "bold")

# Class
class Help:
    def __init__(self) -> None:
        # This is the teal green background for the starting interface
        self.background_frame = Frame(
            width=481, height=443,bg=light_green,borderwidth=1,relief=SOLID
            )
        self.background_frame.grid(padx=5,pady=5)
        # Header for the starting interface
        self.top_text_frame1 = Label(
            self.background_frame,bg=light_yellow,text="The Honoured Sandwich Maker",
            font=header_courier,width=30,borderwidth=1,relief=SOLID
            )
        self.top_text_frame1.grid(padx=3,pady=5)
        # Subheader for the starting interface
        self.top_text_frame2 = Label(
            self.background_frame,bg=light_yellow,text="Info",
            font=sub_head_courier,width=48,borderwidth=1,relief=SOLID
            )
        self.top_text_frame2.grid(padx=3,pady=0)
        # Main Information
        self.main_information = Label(
            self.background_frame,bg=light_yellow,text=info,
            font=info_courier,width=51,borderwidth=1,relief=SOLID,
            justify=LEFT
            )
        self.main_information.grid(padx=3,pady=3,ipadx=37,ipady=65)
        # Start button to proceed on making the sandwich
        self.start_button = Button(
            self.background_frame,text=" Return ",font=courier,width=16,borderwidth=1,relief=SOLID,bg=light_magenta,
            command=close_window
            )
        self.start_button.grid(sticky="WE",padx=4,pady=5)

# Functions
def close_window():
    window.destroy()
# Main Program

# Adjusted the window to make it not resizable for future proofing
window = Tk()
window.title("Main Interface")
window.configure(bg=light_peach)
window.geometry("503x418")
window.resizable(0,0)


# Call the class
Help()

# Start the mainloop
window.mainloop()
