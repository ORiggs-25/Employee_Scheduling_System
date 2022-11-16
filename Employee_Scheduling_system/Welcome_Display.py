import os   # package to call executable file
import tkinter as tk  # GUI module
from tkinter import Canvas
from PIL import ImageTk  # Display background
#import EmployeeLogin


def main():
    # -----following code pertains to main user input window------------------------------------------------------------
    # creating object from Tkinter module
    root = tk.Tk()
    # renames the title of the window
    root.title("Welcome Display")
    # sets the dimensions of the window to measurement
    root.geometry('1600x800')
    # prevents user to resize the window
    root.resizable(width=False, height=False)

    # canvas function will create a background for the GUI
    my_canvas: Canvas = tk.Canvas(root, width=1200, height=800, bd=0, highlightthickness=0)
    my_canvas.pack(fill="both", expand=True)

    # using pillow's ImageTk class and PhotoImage function to display background photo
    bg = ImageTk.PhotoImage(file="Blue_Clock_background.jpg")
    my_canvas.create_image(0, 0, image=bg, anchor="nw")

    my_canvas.create_text(575, 200, text="Welcome to JAM-SOF", font=("Helvetica", 30), fill="white")
    my_canvas.create_text(575, 250, text="Employee Scheduling System", font=("Helvetica", 30), fill="white")
    my_canvas.create_text(575, 300, text="click your login option", font=("Helvetica", 15), fill="white")

    create_button = tk.Button(root, text="Admin Login", activeforeground='white', font=("Helvetica", 15),
                              width=15, height=20, borderwidth=2,
                              command=lambda: os.system("AdminLogin.py"))
    create_button_window = my_canvas.create_window(500, 500, height=35, anchor="nw", window=create_button)


    create_button = tk.Button(root, text="Employee Login", activeforeground='white', font=("Helvetica", 15),
                              width=15, height=20, borderwidth=2, command=lambda: None)
    create_button_window = my_canvas.create_window(500, 550, height=35, anchor="nw", window=create_button)

    root.mainloop()



if __name__ == '__main__':
    main()
