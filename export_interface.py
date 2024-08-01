"""
Author: John Eric Ragos
Purpose: To create a program that allows the user to build and name their sandwich.
Date: 25/06/2024
Version 1: Created a GUI for the starting interface
Version 2: Created a GUI for the ordering interface
Version 3: Created a GUI for the help interface
Version 4: Created a GUI for the export interface
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
light_red = "#F4CCCC"
light_green = "#D9EAD3"

# Fonts
courier = ("Courier", 17, "bold")
header_courier = ("Courier", 20, "bold")
sub_head_courier = ("Courier", 12, "bold")
info_courier = ("Courier", 10, "bold")

# Class

class Export:
    def __init__(self) -> None:
        # Background frames
        self.background_frame5 = Frame(
            window4,width=481,height=443,bg=light_green,borderwidth=1,relief=SOLID
            )
        self.background_frame5.grid(padx=2,pady=5)

        # Label
        self.header4 = Label(
            self.background_frame5,text="The Honoured Sandwich Maker",font=header_courier,
            bg=light_yellow,width=30,borderwidth=1,relief=SOLID
        )
        self.header4.grid(ipadx=4,ipady=10,padx=2,pady=2,columnspan=3)

        self.subheader4 = Label(
            self.background_frame5,bg=light_yellow,text="Receipt",
            font=sub_head_courier,width=48,borderwidth=1,relief=SOLID
        )
        self.subheader4.grid(ipadx=4,ipady=3,padx=2,pady=2,columnspan=3)

        self.subheader5 = Label(
            self.background_frame5,text="Enter Sandwich Name:",bg=light_yellow,
            font=sub_head_courier,borderwidth=1,relief=SOLID,width=23
        )
        self.subheader5.grid(ipadx=4,ipady=3,padx=2,pady=2,column=0,row=2,sticky="W")

        self.list_label2 = Label(
            self.background_frame5,text="",
            bg=light_peach,font=sub_head_courier,borderwidth=1,relief=SOLID,
            width=23,height=7
        )
        self.list_label2.grid(ipadx=4,ipady=3,padx=2,pady=2,column=0,row=3,sticky="W")

        self.error_label = Label(
            self.background_frame5,text="Error Message",bg=light_red,
            font=sub_head_courier,borderwidth=1,relief=SOLID,width=23,height=7
        )
        self.error_label.grid(ipadx=4,ipady=4,padx=2,pady=2,column=1,row=3,sticky="E")

        self.name_label = Label(
            self.background_frame5,text="Enter Name:",bg=light_yellow,
            font=sub_head_courier,borderwidth=1,relief=SOLID,width=23
        )
        self.name_label.grid(ipadx=4,ipady=4,padx=2,pady=2,column=0,row=4)

        self.address_label = Label(
            self.background_frame5,text="Enter Address:",bg=light_yellow,
            font=sub_head_courier,borderwidth=1,relief=SOLID,width=23
        )
        self.address_label.grid(ipadx=4,ipady=4,padx=2,pady=2,column=0,row=5)

        self.phone_label = Label(
            self.background_frame5,text="Enter Sandwich Quantity:",bg=light_yellow,
            font=sub_head_courier,borderwidth=1,relief=SOLID,width=23
        )
        self.phone_label.grid(ipadx=4,ipady=4,padx=2,pady=2,column=0,row=6)

        # Entries
        self.sandwich_name = Entry(
            self.background_frame5,font=sub_head_courier,borderwidth=1,relief=SOLID,width=23
        )
        self.sandwich_name.grid(ipadx=4,ipady=3,padx=2,pady=2,column=1,row=2,sticky="E")

        self.name_entry = Entry(
            self.background_frame5,font=sub_head_courier,borderwidth=1,relief=SOLID,width=23
        )
        self.name_entry.grid(ipadx=4,ipady=3,padx=2,pady=2,column=1,row=4,sticky="E")

        self.address_entry = Entry(
            self.background_frame5,font=sub_head_courier,borderwidth=1,relief=SOLID,width=23
        )
        self.address_entry.grid(ipadx=4,ipady=3,padx=2,pady=2,column=1,row=5,sticky="E")

        self.number_entry = Entry(
            self.background_frame5,font=sub_head_courier,borderwidth=1,relief=SOLID,width=23
        )
        self.number_entry.grid(ipadx=4,ipady=3,padx=2,pady=2,column=1,row=6,sticky="E")

        # Buttons
        self.export_button = Button(
            self.background_frame5,text=" Export ",font=sub_head_courier,width=23,borderwidth=1,relief=SOLID,
            bg=light_cornflower_blue
            )
        self.export_button.grid(row=7,sticky="W",padx=4,pady=5,column=0)

        self.back_button = Button(
            self.background_frame5,text=" Back ",font=sub_head_courier,width=23,borderwidth=1,relief=SOLID,
            bg=light_magenta
            )
        self.back_button.grid(row=7,sticky="E",padx=4,pady=5,column=1)

# Main Program

# Adjusted the window to make it not resizable for future proofing
window4 = Tk()
window4.title("Export Interface")
window4.configure(bg=light_peach)
window4.geometry("503x418")
window4.resizable(0,0)

# Loads the image first to use later
image = "images\HSImage2.gif"
image_name = PhotoImage(file=image)

# Call the class
Export()

# Start the mainloop
window4.mainloop()
