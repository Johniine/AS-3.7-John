"""
Author: John Eric Ragos
Purpose: To create a GUI for the starting interface
Date: 25/06/2024
Version 1: Create a GUI for the starting interface
"""
# Imports
from tkinter import *

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

# Class
class Start:
    def __init__(self) -> None:
        global image, image_name
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
            self.background_frame,bg=light_yellow,text="Sandwich that alone is an honoured one",
            font=sub_head_courier,width=48,borderwidth=1,relief=SOLID
            )
        self.top_text_frame2.grid(padx=3,pady=0)
        # Starting interface image
        self.image_label_frame = Label(
            self.background_frame,image=image_name,justify=CENTER
            )
        self.image_label_frame.grid(padx=0,pady=3)
        # Start button to proceed on making the sandwich
        self.start_button = Button(
            self.background_frame,text="Start Ordering",font=courier,width=17,borderwidth=1,relief=SOLID,bg=light_cornflower_blue
            )
        self.start_button.grid(row=4,sticky="W",padx=3,pady=5)
        # Help button for new users
        self.help_button = Button(
            self.background_frame,text="Help/Info",font=courier,width=17,borderwidth=1,relief=SOLID,bg=light_magenta
            )
        self.help_button.grid(row=4,sticky="E",padx=3,pady=5)

# Main Program

# Adjusted the window to make it not resizable for future proofing
root = Tk()
root.title("Main Interface")
root.configure(bg=light_peach)
root.geometry("503x418")
root.resizable(0,0)

# Loads the image first to use later
image = "images\HSImage2.gif"
image_name = PhotoImage(file=image)

# Call the class
Start()

# Start the mainloop
root.mainloop()
