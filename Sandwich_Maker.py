"""
Author: John Eric Ragos
Purpose: To create a program that allows the user to build and name their sandwich.
Date: 25/06/2024
Version 1: Created a GUI for the starting interface
Version 2: Created a GUI for the ordering interface
Version 3: Created a GUI for the help interface
Version 4: Created the GUI for the export interface
Version 5: Changed the GUI for ordering interface 
"""

# Imports
from tkinter import *
from tkinter import ttk
import datetime

# Date and time to name the files
date = datetime.datetime.now()
current_date = f"{date.strftime('%d-%m-%Y')}"

# Folder to add the created files
FOLDER_NAME = "receipts"

# Constant
SANDWICH_NAME_LENGTH = 25
NAME_LENGTH = 20
ADDRESS_LENGTH = 30
AMOUNT_BOUNDARY = 10

# info text
INFO = """
 This program allows you to make your very own customizable
 sandwiches

 Things you can do using this program:
 1. Make your very own customisable sandwiches
 2. Name your own sandwich
 3. Order the sandwich you made
 4. Order comes with free condiments
"""
# Total
total_price = 0

# Colours
LIGHT_GREEN = "#D9EAD3"
LIGHT_PEACH = "#FCE5CD"
LIGHT_YELLOW = "#FFF2CC"
LIGHT_CORNFLOWER_BLUE = "#C9DAF8"
LIGHT_MAGENTA = "#EAD1DC"
LIGHT_RED = "#F4CCCC"

# Fonts
courier = ("Courier",  17,  "bold")
header_courier = ("Courier",  20,  "bold")
sub_head_courier = ("Courier",  12,  "bold")
info_courier = ("Courier",  10,  "bold")

# List
bread = ["Wholemeal", "White", "Cheesy White", "Gluten Free"]
meat = ["Chicken", "Beef", "Salami", "Vegan Slice"]
garnish1 = ["Onion", "Tomato", "Lettuce", "Cheese"]
garnish2 = ["None", "Onion", "Tomato", "Lettuce", "Cheese"]
customers_order = []

# Hover information
hover_info = "Hover on the\nImage to see\nThe item prices"

# The ingredient list
ingredient_list = ""

# Dictionary
prices = {"None": 0, "Wholemeal": 1.00, "White": 0.80, "Cheesy White": 1.20, "Gluten Free": 1.40, "Chicken": 2.60,
          "Beef": 3.00, "Salami": 4.00, "Vegan Slice": 3.30, "Onion": 1.69, "Tomato": 1.00, "Lettuce": 2.00,
          "Cheese": 2.50}
# Class
class Start:
    def __init__(self) -> None:
        # This is the teal green background for the starting interface
        self.background_frame1 = Frame(
            window1, width=481,  height=443, bg=LIGHT_GREEN, borderwidth=1, relief=SOLID
            )
        self.background_frame1.grid(padx=5, pady=5)
        # Header for the starting interface
        self.header1 = Label(
            self.background_frame1, bg=LIGHT_YELLOW, text="The Honoured Sandwich Maker", 
            font=header_courier, width=30, borderwidth=1, relief=SOLID
            )
        self.header1.grid(padx=3, pady=5)
        # Sub header for the starting interface
        self.subheader1 = Label(
            self.background_frame1, bg=LIGHT_YELLOW, text="Sandwich that alone is an honoured one", 
            font=sub_head_courier, width=48, borderwidth=1, relief=SOLID
            )
        self.subheader1.grid(padx=3, pady=0)
        # Starting interface image
        self.image_label_frame = Label(
            self.background_frame1, image=image_name, justify=CENTER
            )
        self.image_label_frame.grid(padx=0, pady=3)
        # Start button to proceed on making the sandwich
        self.start_button = Button(
            self.background_frame1, text=" Start Ordering ", font=courier, width=16, borderwidth=1, relief=SOLID, bg=LIGHT_CORNFLOWER_BLUE, 
            command=Order
            )
        self.start_button.grid(row=4, sticky="W", padx=4, pady=5, ipady=3)
        # Help button for new users
        self.help_button = Button(
            self.background_frame1, text=" Help/Info ", font=courier, width=16, borderwidth=1, relief=SOLID, bg=LIGHT_MAGENTA, 
            command=Help
            )
        self.help_button.grid(row=4, sticky="E", padx=4, pady=5, ipady=3)

class Help:
    def __init__(self) -> None:
        create_help_window()
        # This is the teal green background for the starting interface
        self.background_frame2 = Frame(
            window2,  width=481,  height=443, bg=LIGHT_GREEN, borderwidth=1, relief=SOLID
            )
        self.background_frame2.grid(padx=5, pady=5)
        # Header for the starting interface
        self.header2 = Label(
            self.background_frame2, bg=LIGHT_YELLOW, text="The Honoured Sandwich Maker", 
            font=header_courier, width=30, borderwidth=1, relief=SOLID
            )
        self.header2.grid(padx=3, pady=5)
        # Sub header for the starting interface
        self.subheader2 = Label(
            self.background_frame2, bg=LIGHT_YELLOW, text="Info", 
            font=sub_head_courier, width=48, borderwidth=1, relief=SOLID
            )
        self.subheader2.grid(padx=3, pady=0)
        # Main Information
        self.main_information = Label(
            self.background_frame2, bg=LIGHT_YELLOW, text=INFO, 
            font=info_courier, width=51, borderwidth=1, relief=SOLID, 
            justify=LEFT
            )
        self.main_information.grid(padx=3, pady=3, ipadx=37, ipady=59)
        # Start button to proceed on making the sandwich
        self.start_button = Button(
            self.background_frame2, text=" Return ", font=courier, width=16, borderwidth=1, relief=SOLID, bg=LIGHT_MAGENTA, 
            command=close_help
            )
        self.start_button.grid(sticky="WE", padx=4, pady=5)

class Order:
    def __init__(self) -> None:
        create_order_window()
        # This is the teal green background for the starting interface
        self.background_frame3 = Frame(
            window3, width=481, height=443, bg=LIGHT_GREEN, borderwidth=1, relief=SOLID
            )
        self.background_frame3.grid(padx=2, pady=5, column=0, row=0)

        self.background_frame4 = Frame(
            window3, width=180, height=443, bg=LIGHT_YELLOW, borderwidth=1, relief=SOLID
            )
        self.background_frame4.grid(padx=0, pady=0, column=1, row=0)

        # 1st Frame labels,  images,  and buttons
        # header for the starting interface
        self.top_text_frame2 = Label(
            self.background_frame3, bg=LIGHT_YELLOW, text="Bring out 120% of the sandwich flavourness", 
            font=sub_head_courier, width=49, borderwidth=1, relief=SOLID
            )
        self.top_text_frame2.grid(padx=3, pady=3, columnspan=3)

        # Ordering interface images
        self.image_label_frame1 = Label(
            self.background_frame3, image=image_name1, borderwidth=1, relief=SOLID, text=""
            )
        self.image_label_frame1.grid(padx=0, pady=3, row=3, column=0)
        self.image_label_frame1.bind('<Enter>', lambda event: self.on_enter(event, image_type='bread'))
        self.image_label_frame1.bind('<Leave>', lambda event: self.on_leave(event, image_type='bread'))

        self.image_label_frame2 = Label(
            self.background_frame3, image=image_name2, borderwidth=1, relief=SOLID, text=""
            )
        self.image_label_frame2.grid(padx=0, pady=3, row=3, column=1)
        self.image_label_frame2.bind('<Enter>', lambda event: self.on_enter(event, image_type='meat'))
        self.image_label_frame2.bind('<Leave>', lambda event: self.on_leave(event, image_type='meat'))

        self.image_label_frame3 = Label(
            self.background_frame3, image=image_name3, borderwidth=1, relief=SOLID, text=""
            )
        self.image_label_frame3.grid(padx=0, pady=3, row=3,  column=2)
        self.image_label_frame3.bind('<Enter>', lambda event: self.on_enter(event, image_type='garnish'))
        self.image_label_frame3.bind('<Leave>', lambda event: self.on_leave(event, image_type='garnish'))

        # Ordering Menu labels
        self.bread_label = Label(
            self.background_frame3, text="Bread", bg=LIGHT_CORNFLOWER_BLUE, font=sub_head_courier, width=15, borderwidth=1, relief=SOLID
        )
        self.bread_label.grid(padx=5, pady=5, row=2, column=0)

        self.meat_label = Label(
            self.background_frame3, text="Meat", bg=LIGHT_CORNFLOWER_BLUE, font=sub_head_courier, width=15, borderwidth=1, relief=SOLID
        )
        self.meat_label.grid(padx=5, pady=5, row=2, column=1)

        self.garnish_label = Label(
            self.background_frame3, text="Garnish", bg=LIGHT_CORNFLOWER_BLUE, font=sub_head_courier, width=15, borderwidth=1, relief=SOLID
        )
        self.garnish_label.grid(padx=5, pady=5, row=2, column=2)

        # Reset Buttons
        self.bread_button = Button(
            self.background_frame3, text="Reset Bread", bg=LIGHT_RED, font=sub_head_courier, width=15, borderwidth=1, relief=SOLID, 
            command=lambda: self.reset_order("bread")
        )
        self.bread_button.grid(padx=5, pady=1, row=6, column=0)

        self.meat_button = Button(
            self.background_frame3, text="Reset Meat", bg=LIGHT_RED, font=sub_head_courier, width=15, borderwidth=1, relief=SOLID, 
            command=lambda: self.reset_order("meat")
        )
        self.meat_button.grid(padx=5, pady=1, row=6, column=1)

        self.garnish_button = Button(
            self.background_frame3, text="Reset Garnish", bg=LIGHT_RED, font=sub_head_courier, width=15, borderwidth=1, relief=SOLID, 
            command=lambda: self.reset_order("garnish")
        )
        self.garnish_button.grid(padx=5, pady=1, row=6, column=2)

        # Combo box
        self.chosen_bread = StringVar()
        self.chosen_bread.set("")

        self.chosen_meat1 = StringVar()
        self.chosen_meat1.set("")

        self.chosen_garnish1 = StringVar()
        self.chosen_garnish1.set("")

        self.chosen_garnish2 = StringVar()
        self.chosen_garnish2.set("")

        self.combobox_bread = ttk.Combobox(
            self.background_frame3, textvariable=self.chosen_bread, state="readonly", width=22
        )
        self.combobox_bread['values'] = bread
        self.combobox_bread.grid(padx=3, pady=2, column=0, row=4)

        self.combobox_meat1 = ttk.Combobox(
            self.background_frame3, textvariable=self.chosen_meat1, state="readonly", width=22
        )
        self.combobox_meat1['values'] = meat
        self.combobox_meat1.grid(padx=3, pady=2, column=1, row=4)

        self.combobox_garnish1 = ttk.Combobox(
            self.background_frame3, textvariable=self.chosen_garnish1, state="readonly", width=22
        )
        self.combobox_garnish1['values'] = garnish1
        self.combobox_garnish1.grid(padx=3, pady=2, column=2, row=4)

        self.combobox_garnish2 = ttk.Combobox(
            self.background_frame3, textvariable=self.chosen_garnish2, state="readonly", width=22
        )
        self.combobox_garnish2['values'] = garnish2
        self.combobox_garnish2.grid(padx=3, pady=2, column=2, row=5)

        # 2nd frame labels,  entry box and buttons
        self.error_label = Label(
            self.background_frame4, bg=LIGHT_RED, text=hover_info,
            font=sub_head_courier, borderwidth=1, relief=SOLID, width=17, height=5, 
            justify=LEFT
            )
        self.error_label.grid(padx=3, pady=5)

        self.total_label = Label(
            self.background_frame4, bg=LIGHT_PEACH, text="Total: $0.00", 
            font=sub_head_courier, borderwidth=1, relief=SOLID, width=17, height=2
            )
        self.total_label.grid(padx=3, pady=2)

        self.calculate_button = Button(
            self.background_frame4, bg=LIGHT_GREEN, text="Calculate", 
            font=sub_head_courier, borderwidth=1, relief=SOLID, width=17, 
            command=self.calculate
        )
        self.calculate_button.grid(padx=3, pady=2)

        self.proceed_button = Button(
            self.background_frame4, bg=LIGHT_CORNFLOWER_BLUE, text="Proceed", 
            font=sub_head_courier, borderwidth=1, relief=SOLID, width=17, state=DISABLED,
            command=Export
        )
        self.proceed_button.grid(padx=3, pady=2)

        self.list_label1 = Label(
            self.background_frame4, text="", 
            bg=LIGHT_PEACH, font=sub_head_courier, borderwidth=1, relief=SOLID, 
            width=17, height=8
        )
        self.list_label1.grid(padx=3, pady=3)

        self.cancel_button = Button(
            self.background_frame4, text="Cancel Order", bg=LIGHT_RED, 
            font=sub_head_courier, borderwidth=1, relief=SOLID, width=17,
            command=close_order
        )
        self.cancel_button.grid(padx=3, pady=5)

    # This functions will disable and enable calculate and proceed button
    def disable_proc(self):
        """This method disable the proceed button and enable the calculate button"""
        self.proceed_button.configure(state=DISABLED)
        self.calculate_button.configure(state=ACTIVE)
    
    def disable_calc(self):
        """This method disable the calculate button and enable the proceed button"""
        self.proceed_button.configure(state=ACTIVE)
        self.calculate_button.configure(state=DISABLED)

    # This method get the users order and append them in a list to be user for calculation later
    def get_order(self):
        """this method get the user's order and add them in a list"""
        self.customers_order = []
        self.customers_order.append(self.chosen_bread.get())
        self.customers_order.append(self.chosen_meat1.get())
        self.customers_order.append(self.chosen_garnish1.get())
        self.customers_order.append(self.chosen_garnish2.get())
    
    # This method will calculate the users order total and put them in the label
    def calculate(self):
        """This method calculate the order ammount"""
        global total_price, ingredient_list
        self.get_order()
        for i in self.customers_order:
            try: # Removes 'None' from the list
                self.customers_order.remove("None")
            except ValueError:
                try:
                    ingredient_list = "".join([str(f"{items}\n") for items in self.customers_order])
                    self.list_label1.configure(text=ingredient_list, justify=LEFT)
                    total_price += float(prices[i])
                    self.total_label.configure(text=f"Total: ${total_price:.2f}")
                    self.disable_calc()
                    self.error_label.configure(text=hover_info)
                    self.combobox_bread.configure(state=DISABLED)
                    self.combobox_meat1.configure(state=DISABLED)
                    self.combobox_garnish1.configure(state=DISABLED)
                    self.combobox_garnish2.configure(state=DISABLED)

                except KeyError: # Will verify if the combo-boxes are empty and will set the total to 0 and remove everything from the list
                    self.error_label.configure(text="Please Select\nAn Order First", justify=LEFT)
                    self.total_label.configure(text=f"Total: ${0:.2f}")
                    self.customers_order.clear()
                    self.list_label1.configure(text="")
                    self.disable_proc()
                    
    # Resets methods
    def reset_order(self, order_type):
        """This method reset the user's orders"""
        global total_price
        try:
            if order_type == "bread": # This will reset the bread combo-box and the selected bread in the list
                self.customers_order.remove(self.chosen_bread.get())
                self.chosen_bread.set("")
                self.combobox_bread.configure(state=ACTIVE)
            
            elif order_type == "meat": # This will reset the meat combo-box and the selected meat in the list
                self.customers_order.remove(self.chosen_meat1.get())
                self.chosen_meat1.set("")
                self.combobox_meat1.configure(state=ACTIVE)
            
            elif order_type == "garnish": # This will reset the garnish combo-box and the selected garnish in the list
                self.customers_order.remove(self.combobox_garnish1.get())
                self.chosen_garnish1.set("")
                
                if self.chosen_garnish2.get() == 'None':
                    self.chosen_garnish2.set("")
                elif self.chosen_garnish2.get() != 'None':
                    self.customers_order.remove(self.chosen_garnish2.get())
                    self.chosen_garnish2.set("")
                
                self.combobox_garnish1.configure(state=ACTIVE)
                self.combobox_garnish2.configure(state=ACTIVE)

            self.disable_proc()
            self.ingredient_list = "".join([str(f"{items}\n") for items in self.customers_order])
            self.list_label1.configure(text=self.ingredient_list, justify=LEFT)
            total_price = 0
            self.total_label.configure(text=f"Total: ${total_price:.2f}")
            self.error_label.configure(text=hover_info, justify=LEFT)

        except: # This will put an error message to the user if it encountered an error
            self.error_label.configure(text=f"Can't reset\n{order_type.title()} order", justify=LEFT)
            self.disable_proc()


    def on_enter(self, event, image_type):
        """This method will change the image to the menu after the user hover on it"""
        if image_type == 'bread':
            self.image_label_frame1.config(image=bread_menu_image)
        elif image_type == 'meat':
            self.image_label_frame2.config(image=meat_menu_image)
        elif image_type == 'garnish':
            self.image_label_frame3.config(image=garnish_menu_image)
    
    def on_leave(self, event, image_type):
        """This method will change the image back after the user stop hover on it"""
        if image_type == 'bread':
            self.image_label_frame1.config(image=image_name1)
        elif image_type == 'meat':
            self.image_label_frame2.config(image=image_name2)
        elif image_type == 'garnish':
            self.image_label_frame3.config(image=image_name3)

class Export:
    def __init__(self) -> None:
        global ingredient_list
        create_export_window()
        # Background frames
        self.background_frame5 = Frame(
            window4, width=481, height=443, bg=LIGHT_GREEN, borderwidth=1, relief=SOLID
            )
        self.background_frame5.grid(padx=2, pady=5)

        # Label
        self.header4 = Label(
            self.background_frame5, text="The Honoured Sandwich Maker", font=header_courier,
            bg=LIGHT_YELLOW, width=30, borderwidth=1, relief=SOLID
        )
        self.header4.grid(ipadx=4, ipady=10, padx=2, pady=2, columnspan=3)

        self.subheader4 = Label(
            self.background_frame5, bg=LIGHT_YELLOW ,text="Receipt",
            font=sub_head_courier, width=48, borderwidth=1, relief=SOLID
        )
        self.subheader4.grid(ipadx=4, ipady=3, padx=2, pady=2, columnspan=3)

        self.subheader5 = Label(
            self.background_frame5, text="Enter Sandwich Name:", bg=LIGHT_YELLOW,
            font=sub_head_courier, borderwidth=1, relief=SOLID, width=23
        )
        self.subheader5.grid(ipadx=4, ipady=3, padx=2, pady=2, column=0, row=2, sticky="W")

        self.list_label2 = Label(
            self.background_frame5, text=f"{ingredient_list}\nTotal:{total_price:.2f}",
            bg=LIGHT_PEACH, font=sub_head_courier, borderwidth=1, relief=SOLID,
            width=23, height=7, justify=LEFT
        )
        self.list_label2.grid(ipadx=4, ipady=3, padx=2, pady=2, column=0, row=3, sticky="W")

        self.error_label = Label(
            self.background_frame5, text="", bg=LIGHT_RED,
            font=sub_head_courier, borderwidth=1, relief=SOLID, width=23, height=7
        )
        self.error_label.grid(ipadx=4, ipady=4, padx=2, pady=2, column=1, row=3, sticky="E")

        self.name_label = Label(
            self.background_frame5, text="Enter Name:", bg=LIGHT_YELLOW,
            font=sub_head_courier, borderwidth=1, relief=SOLID, width=23
        )
        self.name_label.grid(ipadx=4, ipady=4, padx=2, pady=2, column=0, row=4)

        self.address_label = Label(
            self.background_frame5, text="Enter Address:", bg=LIGHT_YELLOW,
            font=sub_head_courier, borderwidth=1, relief=SOLID, width=23
        )
        self.address_label.grid(ipadx=4, ipady=4, padx=2, pady=2, column=0, row=5)

        self.phone_label = Label(
            self.background_frame5, text="Sandwich Quantity:", bg=LIGHT_YELLOW,
            font=sub_head_courier, borderwidth=1, relief=SOLID, width=23
        )
        self.phone_label.grid(ipadx=4, ipady=4, padx=2, pady=2, column=0, row=6)

        # Entries
        self.sandwich_name = Entry(
            self.background_frame5, font=sub_head_courier, borderwidth=1, relief=SOLID, width=23
        )
        self.sandwich_name.grid(ipadx=4, ipady=3, padx=2, pady=2, column=1, row=2, sticky="E")

        self.name_entry = Entry(
            self.background_frame5, font=sub_head_courier, borderwidth=1, relief=SOLID, width=23
        )
        self.name_entry.grid(ipadx=4, ipady=3, padx=2, pady=2, column=1, row=4, sticky="E")

        self.address_entry = Entry(
            self.background_frame5, font=sub_head_courier, borderwidth=1, relief=SOLID, width=23
        )
        self.address_entry.grid(ipadx=4, ipady=3, padx=2, pady=2, column=1, row=5, sticky="E")

        self.number_entry = Entry(
            self.background_frame5, font=sub_head_courier, borderwidth=1, relief=SOLID, width=23
        )
        self.number_entry.grid(ipadx=4, ipady=3, padx=2, pady=2, column=1, row=6, sticky="E")

        # Buttons
        self.export_button = Button(
            self.background_frame5, text=" Export ", font=sub_head_courier, width=23, borderwidth=1, relief=SOLID,
            bg=LIGHT_CORNFLOWER_BLUE,command=self.length_validation
            )
        self.export_button.grid(row=7, sticky="W", padx=4, pady=5, column=0)

        self.back_button = Button(
            self.background_frame5, text=" Back ", font=sub_head_courier, width=23, borderwidth=1, relief=SOLID,
            bg=LIGHT_MAGENTA, command=close_export
            )
        self.back_button.grid(row=7, sticky="E", padx=4, pady=5, column=1)

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
        """This method check if the user exceeded the set order boundary"""
        try:
            self.order_amount = int(self.number_entry.get())
            if self.order_amount > AMOUNT_BOUNDARY:
                self.error_label.configure(text=f"The ordered amount\nOf {self.order_amount} has exceeded\nThe order limit of {AMOUNT_BOUNDARY}")
            elif self.order_amount <= 0:
                self.error_label.configure(text=f"You must atleast\nOrder 1 Sandwich")
            elif self.order_amount > 0 and self.order_amount <= AMOUNT_BOUNDARY:
                self.export_to_folder()
        except ValueError:
            self.error_label.configure(text=f"Please Enter A\nNumber In\nThe Sandwich Box")
    
    def export_to_folder(self):
        """This method import the order into a file and put it in a folder"""
        self.user_info = f"""=====\nSandwich Name: {self.sandwich_name.get()}\nName: {self.name_entry.get()}\n=====\nItems:
        \n{ingredient_list}=====\nQuantity: {self.number_entry.get()}\ntotal_price: ${total_price*int(self.number_entry.get()):.2f}\n=====""" # This add a little design to the receipt

        self.sandwich_file_name = self.sandwich_name.get().replace(" ","-").lower().rstrip().lstrip()
        self.file_path = f"{FOLDER_NAME}\{self.sandwich_file_name}-{current_date}.txt"
        with open(self.file_path, "w") as file:
            file.write(f"{self.user_info}")
        self.error_label.configure(text=f"Order Succesfull\nPlease Look In The\nReceipt Folder")
        self.export_button.configure(state=DISABLED)
        self.back_button.configure(text="Exit")
        self.back_button.configure(command=exit_export)
        self.list_label2.configure(text=f"{ingredient_list}\nQuantity: {self.number_entry.get()}\nTotal: ${total_price*int(self.number_entry.get()):.2f}")

# Functions
# Functions that closes a window

def close_help():
    """Closes the help window"""
    window1.deiconify()
    window2.withdraw()

def close_order():
    """Closes the order window"""
    global ingredient_list, total_price, customers_order
    window1.deiconify()
    window3.withdraw()

    total_price = 0
    customers_order.clear()

def close_export():
    """Closes the export window"""
    window3.deiconify()
    window4.withdraw()

def exit_export():
    global ingredient_list, total_price, customers_order

    window1.deiconify()
    window4.withdraw()

    customers_order.clear()
    ingredient_list = ""
    total_price = 0

# Functions that create a window
def create_help_window():
    """Create the help window and closes the start window"""
    global window2

    window1.withdraw()

    window2 = Toplevel()
    window2.title("Help Interface")
    window2.configure(bg=LIGHT_PEACH)
    window2.geometry("503x418")
    window2.resizable(0, 0)

def create_order_window():
    """create the ordering window and closes the start window"""
    global window3

    window1.withdraw()

    window3 = Toplevel()
    window3.title("Order Interface")
    window3.configure(bg=LIGHT_PEACH)
    window3.geometry("700x418")
    window3.resizable(0, 0)

def create_export_window():
    """create the export window and closes the start window"""
    global window4

    window3.withdraw()

    window4 = Toplevel()
    window4.title("Export Interface")
    window4.configure(bg=LIGHT_PEACH)
    window4.geometry("503x418")
    window4.resizable(0, 0)

# Main Program

# Adjusted the window2 to make it not resizable for future proofing
window1 = Tk()
window1.title("Main Interface")
window1.configure(bg=LIGHT_PEACH)
window1.geometry("503x418")
window1.resizable(0, 0)

# Loads the image to add in the order interface
start_image = "images\start_image.gif"
image_name = PhotoImage(file=start_image)
bread_image = "images\lbread_image.gif"
image_name1 = PhotoImage(file=bread_image)
meat_image = "images\meat_image.gif"
image_name2 = PhotoImage(file=meat_image)
garnish_image = "images\garnish_image.gif"
image_name3 = PhotoImage(file=garnish_image)

# Loads the images for the hover menu
bread_menu = "images\menu_bread.gif"
bread_menu_image = PhotoImage(file=bread_menu)
meat_menu = "images\menu_meat.gif"
meat_menu_image = PhotoImage(file=meat_menu)
garnish_menu = "images\menu_garnish.gif"
garnish_menu_image = PhotoImage(file=garnish_menu)

# Call the class
Start()

# Start the mainloop
window1.mainloop()