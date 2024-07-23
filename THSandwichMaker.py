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
light_red = "#F4CCCC"
light_green = "#D9EAD3"

# Fonts
courier = ("Courier", 17, "bold")
header_courier = ("Courier", 20, "bold")
sub_head_courier = ("Courier", 12, "bold")
info_courier = ("Courier", 10, "bold")

# List
selected_list = []

# Class
class Start:
    def __init__(self) -> None:
        global image, image_name
        # This is the teal green background for the starting interface
        self.background_frame1 = Frame(
            root,width=481, height=443,bg=light_green,borderwidth=1,relief=SOLID
            )
        self.background_frame1.grid(padx=5,pady=5)
        # Header for the starting interface
        self.top_text_frame1 = Label(
            self.background_frame1,bg=light_yellow,text="The Honoured Sandwich Maker",
            font=header_courier,width=30,borderwidth=1,relief=SOLID
            )
        self.top_text_frame1.grid(padx=3,pady=5)
        # Subheader for the starting interface
        self.top_text_frame2 = Label(
            self.background_frame1,bg=light_yellow,text="Sandwich that alone is an honoured one",
            font=sub_head_courier,width=48,borderwidth=1,relief=SOLID
            )
        self.top_text_frame2.grid(padx=3,pady=0)
        # Starting interface image
        self.image_label_frame = Label(
            self.background_frame1,image=image_name,justify=CENTER
            )
        self.image_label_frame.grid(padx=0,pady=3)
        # Start button to proceed on making the sandwich
        self.start_button = Button(
            self.background_frame1,text=" Start Ordering ",font=courier,width=16,borderwidth=1,relief=SOLID,bg=light_cornflower_blue,
            command=Order
            )
        self.start_button.grid(row=4,sticky="W",padx=4,pady=5)
        # Help button for new users
        self.help_button = Button(
            self.background_frame1,text=" Help/Info ",font=courier,width=16,borderwidth=1,relief=SOLID,bg=light_magenta,
            command=Help
            )
        self.help_button.grid(row=4,sticky="E",padx=4,pady=5)

class Help:
    def __init__(self) -> None:
        global root
        create_help_window()
        # This is the teal green background for the starting interface
        self.background_frame2 = Frame(
            window2, width=481, height=443,bg=light_green,borderwidth=1,relief=SOLID
            )
        self.background_frame2.grid(padx=5,pady=5)
        # Header for the starting interface
        self.top_text_frame1 = Label(
            self.background_frame2,bg=light_yellow,text="The Honoured Sandwich Maker",
            font=header_courier,width=30,borderwidth=1,relief=SOLID
            )
        self.top_text_frame1.grid(padx=3,pady=5)
        # Subheader for the starting interface
        self.top_text_frame2 = Label(
            self.background_frame2,bg=light_yellow,text="Info",
            font=sub_head_courier,width=48,borderwidth=1,relief=SOLID
            )
        self.top_text_frame2.grid(padx=3,pady=0)
        # Main Information
        self.main_information = Label(
            self.background_frame2,bg=light_yellow,text=info,
            font=info_courier,width=51,borderwidth=1,relief=SOLID,
            justify=LEFT
            )
        self.main_information.grid(padx=3,pady=3,ipadx=37,ipady=65)
        # Start button to proceed on making the sandwich
        self.start_button = Button(
            self.background_frame2,text=" Return ",font=courier,width=16,borderwidth=1,relief=SOLID,bg=light_magenta,
            command=close_help
            )
        self.start_button.grid(sticky="WE",padx=4,pady=5)

class Order:
    def __init__(self) -> None:
        global root
        create_order_window()
        # This is the teal green background for the starting interface
        self.background_frame3 = Frame(
            window3, width=481, height=443,bg=light_green,borderwidth=1,relief=SOLID
            )
        self.background_frame3.grid(padx=2,pady=5,column=0,row=0)

        self.background_frame4 = Frame(
            window3, width=180, height=443, bg=light_yellow, borderwidth=1, relief=SOLID
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
        self.image_label_frame1 = Label(
            self.background_frame3,image=image_name1,borderwidth=1,relief=SOLID
            )
        self.image_label_frame1.grid(padx=0,pady=3,row=3,column=0)

        self.image_label_frame2 = Label(
            self.background_frame3,image=image_name2,borderwidth=1,relief=SOLID
            )
        self.image_label_frame2.grid(padx=0,pady=3,row=3,column=1)

        self.image_label_frame3 = Label(
            self.background_frame3,image=image_name3,borderwidth=1,relief=SOLID
            )
        self.image_label_frame3.grid(padx=0,pady=3,row=3, column=2)

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
        self.error_label.grid(padx=3,pady=4)

        self.total_label = Label(
            self.background_frame4,bg=light_peach,text="Total",
            font=sub_head_courier,borderwidth=1,relief=SOLID,width=17,height=2
            )
        self.total_label.grid(padx=3,pady=2)

        self.calculate_buttons = Button(
            self.background_frame4,bg=light_green,text="Calculate",
            font=sub_head_courier,borderwidth=1,relief=SOLID,width=17
        )
        self.calculate_buttons.grid(padx=3,pady=2)

        self.proceed_button = Button(
            self.background_frame4,bg=light_cornflower_blue,text="Proceed",
            font=sub_head_courier,borderwidth=1,relief=SOLID,width=17
        )
        self.proceed_button.grid(padx=3,pady=2)

        self.list_label = Label(
            self.background_frame4,textvariable=selected_list,
            bg=light_peach,font=sub_head_courier,borderwidth=1,relief=SOLID,
            width=17,height=8
        )
        self.list_label.grid(padx=3,pady=2)

        self.cancel_button = Button(
            self.background_frame4,text="Cancel Order",bg=light_red,
            font=sub_head_courier,borderwidth=1,relief=SOLID,width=17,
            command=close_order
        )
        self.cancel_button.grid(padx=3,pady=3)

# Functions
# Functions that closes a window

def close_help():
    '''Closes the help window'''
    root.deiconify()
    window2.withdraw()

def close_order():
    '''Closes the order window'''
    root.deiconify()
    window3.withdraw()

# Functions that create a window
def create_help_window():
    '''Create the help window and closes the start window'''
    global window2, root

    root.withdraw()

    window2 = Toplevel()
    window2.title("Help Interface")
    window2.configure(bg=light_peach)
    window2.geometry("503x418")
    window2.resizable(0,0)

def create_order_window():
    '''create the ordering window and closes the start window'''
    global window3, root

    root.withdraw()

    window3 = Toplevel()
    window3.title("Order Interface")
    window3.configure(bg=light_peach)
    window3.geometry("700x418")
    window3.resizable(0,0)

# Main Program

# Adjusted the window2 to make it not resizable for future proofing
root = Tk()
root.title("Main Interface")
root.configure(bg=light_peach)
root.geometry("503x418")
root.resizable(0,0)

# Loading the images
image = "images\HSImage2.gif"
image_name = PhotoImage(file=image)
image1 = "images\Hamito.gif"
image_name1 = PhotoImage(file=image1)
image2 = "images\Todo.gif"
image_name2 = PhotoImage(file=image2)
image3 = "images\Yuji.gif"
image_name3 = PhotoImage(file=image3)

# Call the class
Start()

# Start the mainloop
root.mainloop()