import json
import tkinter as tk  # GUI module
import requests
from tkinter import Canvas, LEFT

from PIL import ImageTk  # Display background


def main():
    # -----following code pertains to main user input window------------------------------------------------------------
    # creating object from Tkinter module
    root = tk.Tk()
    # renames the title of the window

    root.title("Create Employee Leave")

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


    # ===============================================================================================================

    def create_Leave(id, leaveType, startDate, endDate):

        headers = {"Content-Type": "application/json",
                   "Connection": "keep-alive"}

        createLeave = {
            "employeeID": str(id),
            "leave_type": str(leaveType),
            "start_date": str(startDate),
            "end_date": str(endDate)
        }

        try:
            response = requests.put("https://uhwxroslh0.execute-api.us-east-1.amazonaws.com/dev/create/leave",
                                    data=json.dumps(createLeave), headers=headers)
            print(response.status_code)

            my_canvas.create_text(350, 370, text="Leave Was Successfully Added.", font=("Helvetica", 16), fill="white")
        except requests.exceptions.HTTPError as err:
            print(err)

    # ==================================================================================================================

    # create_text function from tkinter will display text onto GUI
    my_canvas.create_text(575, 50, text="Create A Leave (Type Exactly As Shown)", font=("Helvetica", 25), fill="white")
    my_canvas.create_text(330, 140, text="EmployeeID", font=("Helvetica", 16), fill="white")
    my_canvas.create_text(330, 190, text="Type: (paid/unpaid)", font=("Helvetica", 16), fill="white")
    my_canvas.create_text(330, 240, text="Start: (mm/dd/yyyy)", font=("Helvetica", 16), fill="white")
    my_canvas.create_text(330, 290, text="End: (mm/dd/yyyy)", font=("Helvetica", 16), fill="white")

    # create Entry text boxes
    employeeID = tk.Entry(my_canvas, font=("Helvetica", 12), width=50, bg="white", borderwidth=2)
    employeeID.pack()
    leaveType = tk.Entry(my_canvas, font=("Helvetica", 12), width=50, bg="white", borderwidth=2)
    leaveType.pack()
    startDate = tk.Entry(my_canvas, font=("Helvetica", 12), width=50, bg="white", borderwidth=2)
    startDate.pack()
    endDate = tk.Entry(my_canvas, font=("Helvetica", 12), width=50, bg="white", borderwidth=2)
    endDate.pack()

    employeeID_window = my_canvas.create_window(415, 125, anchor="nw", window=employeeID)
    leaveType_window = my_canvas.create_window(415, 175, anchor="nw", window=leaveType)
    startDate_window = my_canvas.create_window(415, 225, anchor="nw", window=startDate)
    endDate_window = my_canvas.create_window(415, 275, anchor="nw", window=endDate)

    create_button = tk.Button(root, text="Create Leave", activeforeground='blue', font=("Helvetica", 15),
                              width=15, height=20, borderwidth=2,
                              command=lambda: create_Leave(employeeID.get(), leaveType.get(), startDate.get(),
                                                           endDate.get()))

    create_button_window = my_canvas.create_window(500, 325, height=35, anchor="nw", window=create_button)

    root.mainloop()



if __name__ == '__main__':
    main()
