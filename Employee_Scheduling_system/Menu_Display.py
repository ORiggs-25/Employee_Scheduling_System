import tkinter as tk  # GUI module
from tkinter import Canvas
import os   # package to call executable file
from PIL import ImageTk  # Display background



def main():


    # -----following code pertains to main user input window------------------------------------------------------------
    # creating object from Tkinter module
    root = tk.Tk()
    # renames the title of the window
    root.title("Menu Display")
    # sets the dimensions of the window to measurement
    root.geometry('1200x800')
    # prevents user to resize the window
    root.resizable(width=False, height=False)

    # canvas function will create a background for the GUI
    my_canvas: Canvas = tk.Canvas(root, width=1200, height=800, bd=0, highlightthickness=0)
    my_canvas.pack(fill="both", expand=True)

    # using pillow's ImageTk class and PhotoImage function to display background photo
    bg = ImageTk.PhotoImage(file="background.png")
    my_canvas.create_image(0, 0, image=bg, anchor="nw")

    # Create Employee button =================================================================================
    create_button = tk.Button(root, text="Create/Add Employee", activeforeground='blue', font=("Helvetica", 20),
                              width=50, height=50, borderwidth=5,
                              command=lambda: [root.destroy(), os.system("Create_Employee.py")])

    create_button_window = my_canvas.create_window(200, 100, height=40, anchor="nw", window=create_button)

    # Show All Employees button ===============================================================================
    create_button = tk.Button(root, text="Show Employees", activeforeground='blue', font=("Helvetica", 20),
                              width=50, height=50, borderwidth=5,
                              command=lambda: [root.destroy(), os.system("Display_All_Employees.py")])

    create_button_window = my_canvas.create_window(200, 200, height=40, anchor="nw", window=create_button)

    # Assign Schedule ===========================================================================================
    create_button = tk.Button(root, text="Assign Schedule", activeforeground='blue', font=("Helvetica", 20),
                              width=50, height=50, borderwidth=5,
                              command=lambda: [root.destroy(), os.system("Assign_employees_schedule.py")])

    create_button_window = my_canvas.create_window(200, 300, height=40, anchor="nw", window=create_button)

    # Show Schedule =============================================================================================
    create_button = tk.Button(root, text="Show Schedule", activeforeground='blue', font=("Helvetica", 20),
                              width=50, height=50, borderwidth=5,
                              command=lambda: [root.destroy(), os.system("Get_and_Show_Schedule.py")])

    create_button_window = my_canvas.create_window(200, 400, height=40, anchor="nw", window=create_button)

    # Exit =====================================================================================================
    create_button = tk.Button(root, text="Exit System", activeforeground='blue', font=("Helvetica", 20),
                              width=50, height=50, borderwidth=5,
                              command=lambda: [root.destroy(), os.system("Welcome_Display.py")])

    create_button_window = my_canvas.create_window(200, 500, height=40, anchor="nw", window=create_button)
    # ==========================================================================================================


    root.mainloop()


if __name__ == '__main__':
    main()
