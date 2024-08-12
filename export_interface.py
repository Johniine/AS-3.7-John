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

# files
RECEIPT_NAME = "receipts\orders-receipt.txt"

# Constant
SANDWICH_NAME_LENGTH = 25
NAME_LENGTH = 20
ADDRESS_LENGTH = 30
AMOUNT_BOUNDARY = 10

# Colours
LIGHT_GREEN = "#D9EAD3"
LIGHT_PEACH = "#FCE5CD"
LIGHT_YELLOW = "#FFF2CC"
LIGHT_CORNFLOWER_BLUE = "#C9DAF8"
LIGHT_MAGENTA = "#EAD1DC"
LIGHT_RED = "#F4CCCC"

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
            window4,width=481,height=443,bg=LIGHT_GREEN,borderwidth=1,relief=SOLID
            )
        self.background_frame5.grid(padx=2,pady=5)

        # Label
        self.header4 = Label(
            self.background_frame5,text="The Honoured Sandwich Maker",font=header_courier,
            bg=LIGHT_YELLOW,width=30,borderwidth=1,relief=SOLID
        )
        self.header4.grid(ipadx=4,ipady=10,padx=2,pady=2,columnspan=3)

        self.subheader4 = Label(
            self.background_frame5,bg=LIGHT_YELLOW,text="Receipt",
            font=sub_head_courier,width=48,borderwidth=1,relief=SOLID
        )
        self.subheader4.grid(ipadx=4,ipady=3,padx=2,pady=2,columnspan=3)

        self.subheader5 = Label(
            self.background_frame5,text="Enter Sandwich Name:",bg=LIGHT_YELLOW,
            font=sub_head_courier,borderwidth=1,relief=SOLID,width=23
        )
        self.subheader5.grid(ipadx=4,ipady=3,padx=2,pady=2,column=0,row=2,sticky="W")

        self.list_label2 = Label(
            self.background_frame5,text="",
            bg=LIGHT_PEACH,font=sub_head_courier,borderwidth=1,relief=SOLID,
            width=23,height=7
        )
        self.list_label2.grid(ipadx=4,ipady=3,padx=2,pady=2,column=0,row=3,sticky="W")

        self.error_label = Label(
            self.background_frame5,text="",bg=LIGHT_RED,
            font=sub_head_courier,borderwidth=1,relief=SOLID,width=23,height=7
        )
        self.error_label.grid(ipadx=4,ipady=4,padx=2,pady=2,column=1,row=3,sticky="E")

        self.name_label = Label(
            self.background_frame5,text="Enter Name:",bg=LIGHT_YELLOW,
            font=sub_head_courier,borderwidth=1,relief=SOLID,width=23
        )
        self.name_label.grid(ipadx=4,ipady=4,padx=2,pady=2,column=0,row=4)

        self.address_label = Label(
            self.background_frame5,text="Enter Address:",bg=LIGHT_YELLOW,
            font=sub_head_courier,borderwidth=1,relief=SOLID,width=23
        )
        self.address_label.grid(ipadx=4,ipady=4,padx=2,pady=2,column=0,row=5)

        self.phone_label = Label(
            self.background_frame5,text="Enter Sandwich Quantity:",bg=LIGHT_YELLOW,
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
            bg=LIGHT_CORNFLOWER_BLUE, command=self.length_validation
            )
        self.export_button.grid(row=7,sticky="W",padx=4,pady=5,column=0)

        self.back_button = Button(
            self.background_frame5,text=" Back ",font=sub_head_courier,width=23,borderwidth=1,relief=SOLID,
            bg=LIGHT_MAGENTA
            )
        self.back_button.grid(row=7,sticky="E",padx=4,pady=5,column=1)
    
    def length_validation(self):
        """This method check the character length """
        length = {
            "sandwich name": len(self.sandwich_name.get()),
            "name": len(self.name_entry.get()),
            "address": len(self.address_entry.get())
        }
        
        limit = {
            "sandwich name": SANDWICH_NAME_LENGTH,
            "name": NAME_LENGTH,
            "address": ADDRESS_LENGTH
        }

        self.length_checker = [] # I will append True or False in this list to be able to use using the add function

        for keys in length:
            if length[keys] > limit[keys]:
                self.error_label.configure(text=f"{keys.title()}\nhas reached\nThe character\nlimit Of {limit[keys]}",justify=LEFT)
                self.length_checker.append(False)
            elif length[keys] <= limit[keys]:
                self.length_checker.append(True)

        if length[keys] <= 0:
            self.length_checker.append(False)
            self.error_label.configure(text=f"Please Fill In\nThe Boxes")
            
        elif all(self.length_checker):
            self.error_label.configure(text="")
            self.amount_boundary()
    
    def amount_boundary(self):
        """Thie method check if the user exceeded the order boundary of 10"""
        try:
            self.order_amount = int(self.number_entry.get())
            if self.order_amount > AMOUNT_BOUNDARY:
                self.error_label.configure(text=f"The ordered amount\nOf {self.order_amount} has exceeded\nThe order limit of {AMOUNT_BOUNDARY}")
            elif self.order_amount <= 0:
                self.error_label.configure(text=f"You must atleast\nOrder 1 Sandwich")
        except ValueError:
            self.error_label.configure(text=f"Enter Number\nOnly When Entering\nSandwich Quantity")
        

# Main Program

# Adjusted the window to make it not resizable for future proofing
window4 = Tk()
window4.title("Export Interface")
window4.configure(bg=LIGHT_PEACH)
window4.geometry("503x418")
window4.resizable(0,0)

# Loads the image first to use later
image = "images\HSImage2.gif"
image_name = PhotoImage(file=image)

# Call the class
Export()

# Start the mainloop
window4.mainloop()