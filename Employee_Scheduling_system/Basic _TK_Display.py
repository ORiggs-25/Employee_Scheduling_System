import tkinter as tk  # GUI module
from tkinter import Canvas

from PIL import ImageTk  # Display background


def main():
    # -----following code pertains to main user input window------------------------------------------------------------
    # creating object from Tkinter module
    root = tk.Tk()
    # renames the title of the window
    root.title("Some Display")
    # sets the dimensions of the window to measurement
    root.geometry('1200x800')
    # prevents user to resize the window
    root.resizable(width=False, height=False)

    # canvas function will create a background for the GUI
    my_canvas: Canvas = tk.Canvas(root, width=1200, height=800, bd=0, highlightthickness=0)
    my_canvas.pack(fill="both", expand=True)

    # using pillow's ImageTk class and PhotoImage function to display background photo
    bg = ImageTk.PhotoImage(file="BasicBlue.jpeg")
    my_canvas.create_image(0, 0, image=bg, anchor="nw")

    def do_something():
        pass

    # ==================================================================================================================
    """
    Enter your function code here
    ......................
    ......................
    ......................
    """


    # ==================================================================================================================

    create_button = tk.Button(root, text="Some Button", activeforeground='white', font=("Helvetica", 15), \
                              width=15, height=20, borderwidth=2,
                              command=lambda: do_something())

    create_button_window = my_canvas.create_window(550, 550, height=35, anchor="nw", window=create_button)

    root.mainloop()

if __name__ == '__main__':
    main()
