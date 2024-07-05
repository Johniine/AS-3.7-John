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
light_red = "#F4CCCC"
light_green = "#D9EAD3"

# Fonts
courier = ("Courier", 17, "bold")
header_courier = ("Courier", 20, "bold")
sub_head_courier = ("Courier", 12, "bold")

# Class
class Order:
    def __init__(self) -> None:
        # This is the teal green background for the starting interface
        self.background_frame3 = Frame(
            window3,width=481, height=443,bg=light_green,borderwidth=1,relief=SOLID
            )
        self.background_frame3.grid(padx=5,pady=5,column=0,row=0)

        self.background_frame4 = Frame(
            width=189, height=443, bg=light_yellow, borderwidth=1, relief=SOLID
            )
        self.background_frame4.grid(padx=0,pady=0,column=1,row=0)

        # 1st Frame labels, images, and buttons
        # Header for the starting interface
        self.top_text_frame1 = Label(
            self.background_frame3,bg=light_peach,text="Honoured Sandwich Online",
            font=header_courier,width=31,borderwidth=1,relief=SOLID
            )
        self.top_text_frame1.grid(padx=3,pady=5,columnspan=3)

        # Subheader for the starting interface
        self.top_text_frame2 = Label(
            self.background_frame3,bg=light_yellow,text="Bring out 120% of the sandwich flavourness",
            font=sub_head_courier,width=49,borderwidth=1,relief=SOLID
            )
        self.top_text_frame2.grid(padx=3,pady=0,columnspan=3)

        # Ordering interface images
        self.image_label_frame = Label(
            self.background_frame3,image=image_name1,borderwidth=1,relief=SOLID
            )
        self.image_label_frame.grid(padx=0,pady=3,row=3,column=0)

        self.image_label_frame = Label(
            self.background_frame3,image=image_name2,borderwidth=1,relief=SOLID
            )
        self.image_label_frame.grid(padx=0,pady=3,row=3,column=1)

        self.image_label_frame = Label(
            self.background_frame3,image=image_name3,borderwidth=1,relief=SOLID
            )
        self.image_label_frame.grid(padx=0,pady=3,row=3, column=2)

        # Ordering Menu labels
        self.bread_label = Label(
            self.background_frame3,text="Bread",bg=light_cornflower_blue,font=sub_head_courier,width=15,borderwidth=1,relief=SOLID
        )
        self.bread_label.grid(padx=5,pady=5,row=2,column=0)

        self.meat_label = Label(
            self.background_frame3,text="Meat",bg=light_cornflower_blue,font=sub_head_courier,width=15,borderwidth=1,relief=SOLID
        )
        self.meat_label.grid(padx=5,pady=5,row=2,column=1)

        self.garnish_label = Label(
            self.background_frame3,text="Garnish",bg=light_cornflower_blue,font=sub_head_courier,width=15,borderwidth=1,relief=SOLID
        )
        self.garnish_label.grid(padx=5,pady=5,row=2,column=2)
        # Ordering Menu Buttons
        self.bread_button = Button(
            self.background_frame3,text="Continue",bg=light_peach,font=sub_head_courier,width=15,borderwidth=1,relief=SOLID
        )
        self.bread_button.grid(padx=5,pady=5,row=5,column=0)

        self.meat_button = Button(
            self.background_frame3,text="Continue",bg=light_peach,font=sub_head_courier,width=15,borderwidth=1,relief=SOLID
        )
        self.meat_button.grid(padx=5,pady=5,row=5,column=1)

        self.garnish_button = Button(
            self.background_frame3,text="Continue",bg=light_peach,font=sub_head_courier,width=15,borderwidth=1,relief=SOLID
        )
        self.garnish_button.grid(padx=5,pady=5,row=5,column=2)

        # 2nd frame labels, entry box and buttons
        self.error_label = Label(
            self.background_frame4,bg=light_red,text="Error Message",
            font=sub_head_courier,borderwidth=1,relief=SOLID,width=17,height=5
            )
        self.error_label.grid(padx=3,pady=3)

        self.total_label = Label(
            self.background_frame4,bg=light_peach,text="Error Message",
            font=sub_head_courier,borderwidth=1,relief=SOLID,width=17,height=2
            )
        self.total_label.grid(padx=3,pady=2)

        self.calculate_buttons = Button(
            self.background_frame4,bg=light_green,text="Calculate",
            font=sub_head_courier,borderwidth=1,relief=SOLID,width=17
        )
        self.calculate_buttons.grid(padx=3,pady=2)

# Main Program

# Adjusted the window to make it not resizable for future proofing
window3 = Tk()
window3.title("Ordering Interface")
window3.configure(bg=light_peach)
window3.geometry("700x418")
window3.resizable(0,0)

# Loads the image first to use later
image1 = "images\Hamito.gif"
image_name1 = PhotoImage(file=image1)
image2 = "images\Todo.gif"
image_name2 = PhotoImage(file=image2)
image3 = "images\Yuji.gif"
image_name3 = PhotoImage(file=image3)

# Call the class
Order()

# Start the mainloop
window3.mainloop()