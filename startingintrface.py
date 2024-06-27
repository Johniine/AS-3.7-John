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

# Class
class Start:
    def __init__(self) -> None:
        # This is the teal green background for the starting interface
        self.background_frame = Frame(width=481, height=443,bg=light_green)
        self.background_frame.grid(padx=5,pady=5)

        self.top_text_frame1 = Frame(self.background_frame,width=481, height=70, bg=light_yellow)
        self.top_text_frame1.grid(padx=5,pady=5)

        self.top_text_frame2 = Frame(self.background_frame,width=481, height=40, bg=light_yellow)
        self.top_text_frame2.grid(padx=5,pady=3)
        image = "HSImage2.gif"
        self.image_name = PhotoImage(file=image)
        self.image_label_frame = Label(root,image=self.image_name)
        self.image_label_frame.grid(padx=5,pady=3)

# Main Program
root = Tk()
root.title("Main Interface")
root.configure(bg=light_peach)
root.geometry("499x453")
#root.resizable(0,0)
Start()
root.mainloop()