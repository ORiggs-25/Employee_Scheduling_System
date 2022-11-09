from tkinter import *
import tkinter as tk
from PIL import ImageTk
from tkcalendar import *  # for calendar view

def main():
    # -----following code pertains to main user input window------------------------------------------------------------
    # creating object from Tkinter module
    root = tk.Tk()
    # renames the title of the window
    root.title("Assign Employee")
    # sets the dimensions of the window to measurement
    root.geometry('1200x800')
    # prevents user to resize the window
    root.resizable(width=False, height=False)

    cal = Calendar(root, selectmode="day", year=2022)
    cal.pack(pady=20, fill="both", expand=True)

    # canvas function will create a background for the GUI
    my_canvas: Canvas = tk.Canvas(root, width=1200, height=800, bd=0, highlightthickness=0)
    my_canvas.pack(fill="both", expand=True)

    # using pillow's ImageTk class and PhotoImage function to display background photo
    bg = ImageTk.PhotoImage(file="BasicBlue.jpeg")
    my_canvas.create_image(0, 0, image=bg, anchor="nw")

    # ==================================================================================================================
    def getStartDate():
        pass

    def getEndEndDate():
        pass

    def do_something():
        pass

    """
    write code: drop down list of employee  
    """





    # ==================================================================================================================

    create_button = tk.Button(root, text="Create Schedule", activeforeground='white', font=("Helvetica", 12),
                              width=15, height=15, borderwidth=2,
                              command=lambda: do_something())

    create_button_window = my_canvas.create_window(500, 10, height=20, anchor="nw", window=create_button)

    root.mainloop()

if __name__ == '__main__':
    main()
