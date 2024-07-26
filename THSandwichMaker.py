"""
Author: John Eric Ragos
Purpose: To create a program that allows the user to build and name their sandwich.
Date: 25/06/2024
Version 1: Created a GUI for the starting interface
Version 2: Created a GUI for the ordering interface
Version 3: Created a GUI for the help interface
"""

# Imports
from tkinter import *
from tkinter import ttk

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
selected_list = [
    
]
bread = ["Wholemeal","White","Cheesy White","Gluten Free"]
meat = ["None","Chicken","Beef","Salami","Vegan Slice"]
garnish = ["None","Onion","Tomato","Lettuce","Cheese"]

# Class
class Start:
    def __init__(self) -> None:
        # This is the teal green background for the starting interface
        self.background_frame1 = Frame(
            window1,width=481, height=443,bg=light_green,borderwidth=1,relief=SOLID
            )
        self.background_frame1.grid(padx=5,pady=5)
        # Header for the starting interface
        self.header1 = Label(
            self.background_frame1,bg=light_yellow,text="The Honoured Sandwich Maker",
            font=header_courier,width=30,borderwidth=1,relief=SOLID
            )
        self.header1.grid(padx=3,pady=5)
        # Subheader for the starting interface
        self.subheader1 = Label(
            self.background_frame1,bg=light_yellow,text="Sandwich that alone is an honoured one",
            font=sub_head_courier,width=48,borderwidth=1,relief=SOLID
            )
        self.subheader1.grid(padx=3,pady=0)
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
        create_help_window()
        # This is the teal green background for the starting interface
        self.background_frame2 = Frame(
            window2, width=481, height=443,bg=light_green,borderwidth=1,relief=SOLID
            )
        self.background_frame2.grid(padx=5,pady=5)
        # Header for the starting interface
        self.header2 = Label(
            self.background_frame2,bg=light_yellow,text="The Honoured Sandwich Maker",
            font=header_courier,width=30,borderwidth=1,relief=SOLID
            )
        self.header2.grid(padx=3,pady=5)
        # Subheader for the starting interface
        self.subheader2 = Label(
            self.background_frame2,bg=light_yellow,text="Info",
            font=sub_head_courier,width=48,borderwidth=1,relief=SOLID
            )
        self.subheader2.grid(padx=3,pady=0)
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
        create_order_window()
        # This is the teal green background for the starting interface
        self.background_frame3 = Frame(
            window3,width=481, height=443,bg=light_green,borderwidth=1,relief=SOLID
            )
        self.background_frame3.grid(padx=2,pady=5,column=0,row=0)

        self.background_frame4 = Frame(
            window3,width=180, height=443, bg=light_yellow, borderwidth=1, relief=SOLID
            )
        self.background_frame4.grid(padx=0,pady=0,column=1,row=0)

        # 1st Frame labels, images, and buttons
        # header for the starting interface
        self.top_text_frame2 = Label(
            self.background_frame3,bg=light_yellow,text="Bring out 120% of the sandwich flavourness",
            font=sub_head_courier,width=49,borderwidth=1,relief=SOLID
            )
        self.top_text_frame2.grid(padx=3,pady=3,columnspan=3)

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

        # Combo box
        self.chosen_bread = StringVar()
        self.chosen_bread.set("")

        self.chosen_meat1 = StringVar()
        self.chosen_meat1.set("")

        self.chosen_meat2 = StringVar()
        self.chosen_meat2.set("")

        self.chosen_garnish1 = StringVar()
        self.chosen_garnish1.set("")

        self.chosen_garnish2 = StringVar()
        self.chosen_garnish2.set("")

        self.chosen_garnish3 = StringVar()
        self.chosen_garnish3.set("")

        self.combobox_bread = ttk.Combobox(
            self.background_frame3,textvariable=self.chosen_bread,state="readonly",width=22
        )
        self.combobox_bread['values'] = bread
        self.combobox_bread.grid(padx=3,pady=2,column=0,row=4)

        self.combobox_meat1 = ttk.Combobox(
            self.background_frame3,textvariable=self.chosen_meat1,state="readonly",width=22
        )
        self.combobox_meat1['values'] = meat
        self.combobox_meat1.grid(padx=3,pady=2,column=1,row=4)

        self.combobox_meat2 = ttk.Combobox(
            self.background_frame3,textvariable=self.chosen_meat2,state="readonly",width=22
        )
        self.combobox_meat2['values'] = meat
        self.combobox_meat2.grid(padx=3,pady=2,column=1,row=5)

        self.combobox_garnish1 = ttk.Combobox(
            self.background_frame3,textvariable=self.chosen_garnish1,state="readonly",width=22
        )
        self.combobox_garnish1['values'] = garnish
        self.combobox_garnish1.grid(padx=3,pady=2,column=2,row=4)

        self.combobox_garnish2 = ttk.Combobox(
            self.background_frame3,textvariable=self.chosen_garnish2,state="readonly",width=22
        )
        self.combobox_garnish2['values'] = garnish
        self.combobox_garnish2.grid(padx=3,pady=2,column=2,row=5)

        self.combobox_garnish3 = ttk.Combobox(
            self.background_frame3,textvariable=self.chosen_garnish3,state="readonly",width=22
        )
        self.combobox_garnish3['values'] = garnish
        self.combobox_garnish3.grid(padx=3,pady=2,column=2,row=6)

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
            font=sub_head_courier,borderwidth=1,relief=SOLID,width=17,
            command=Export
        )
        self.proceed_button.grid(padx=3,pady=2)

        self.list_label1 = Label(
            self.background_frame4,textvariable=selected_list,
            bg=light_peach,font=sub_head_courier,borderwidth=1,relief=SOLID,
            width=17,height=8
        )
        self.list_label1.grid(padx=3,pady=3)

        self.cancel_button = Button(
            self.background_frame4,text="Cancel Order",bg=light_red,
            font=sub_head_courier,borderwidth=1,relief=SOLID,width=17,
            command=close_order
        )
        self.cancel_button.grid(padx=3,pady=4)

class Export:
    def __init__(self) -> None:
        create_export_window()
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
            bg=light_magenta,command=close_export
            )
        self.back_button.grid(row=7,sticky="E",padx=4,pady=5,column=1)

# Functions
# Functions that closes a window

def close_help():
    '''Closes the help window'''
    window1.deiconify()
    window2.withdraw()

def close_order():
    '''Closes the order window'''
    window1.deiconify()
    window3.withdraw()

def close_export():
    '''Closes the export window'''
    window3.deiconify()
    window4.withdraw()

# Functions that create a window
def create_help_window():
    '''Create the help window and closes the start window'''
    global window2

    window1.withdraw()

    window2 = Toplevel()
    window2.title("Help Interface")
    window2.configure(bg=light_peach)
    window2.geometry("503x418")
    window2.resizable(0,0)

def create_order_window():
    '''create the ordering window and closes the start window'''
    global window3

    window1.withdraw()

    window3 = Toplevel()
    window3.title("Order Interface")
    window3.configure(bg=light_peach)
    window3.geometry("700x418")
    window3.resizable(0,0)

def create_export_window():
    '''create the export window and closes the start window'''
    global window4

    window3.withdraw()

    window4 = Toplevel()
    window4.title("Export Interface")
    window4.configure(bg=light_peach)
    window4.geometry("503x418")
    window4.resizable(0,0)

# Main Program

# Adjusted the window2 to make it not resizable for future proofing
window1 = Tk()
window1.title("Main Interface")
window1.configure(bg=light_peach)
window1.geometry("503x418")
window1.resizable(0,0)

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
window1.mainloop()