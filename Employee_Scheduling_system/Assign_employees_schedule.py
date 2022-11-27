import json
from tkinter import *
import tkinter as tk

import requests
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

    # getting date from the calendar
    def grab_date():
        my_label.config(text=str(cal.get_date()))

    def schedule_an_Employee(date, employeeID, leaveType):
        headers = {"Content-Type": "application/json",
                   "Connection": "keep-alive"}

        try:
            scheduleEmployee = {
                "leaveID": str(leaveType.get()),
                "employeeID": str(employeeID.get()),
                "id": "",       # get auto generated
                "scheduledDate": str(date)
            }

            response = requests.put("https://uhwxroslh0.execute-api.us-east-1.amazonaws.com/dev/create/attendance",
                                    data=json.dumps(scheduleEmployee), headers=headers)
            response_API = ("Code " + str(response.status_code) + ": Shift assigned")
            my_canvas.create_text(600, 200, text=response_API, font=("Helvetica", 16), fill="white")

        except requests.exceptions.HTTPError as err:
            response_API = ("Code " + str(err) + ": Failed to assigned")
            my_canvas.create_text(525, 200, text=response_API, font=("Helvetica", 16), fill="white")


    # add button to load the date clicked on calendar
    date_button = Button(root, text="Select Date", command=grab_date, bg="blue", fg='white')
    # displaying button on the main display
    date_button.pack()

    my_label = Label(root, text="")
    my_label.pack()



    # canvas function will create a background for the GUI
    my_canvas: Canvas = tk.Canvas(root, width=1200, height=800, bd=0, highlightthickness=0)
    my_canvas.pack(fill="both", expand=True)

    # using pillow's ImageTk class and PhotoImage function to display background photo
    bg = ImageTk.PhotoImage(file="BasicBlue.jpeg")
    my_canvas.create_image(0, 0, image=bg, anchor="nw")

    # ==================================================================================================================

    my_canvas.create_text(600, 20, text="Please enter an employeeID to be assigned into schedule", font=("Helvetica", 14), fill="white")
    my_canvas.create_text(525, 65, text="Employee ID", font=("Helvetica", 16), fill="white")
    my_canvas.create_text(525, 105, text="Employee's Name", font=("Helvetica", 16), fill="white")

    employeeID = tk.Entry(my_canvas, font=("Helvetica", 12), width=15, bg="white", borderwidth=1)
    employeeID.pack()
    employeeName = tk.Entry(my_canvas, font=("Helvetica", 12), width=15, bg="white", borderwidth=1)
    employeeName.pack()
    employeeID_entry_window = my_canvas.create_window(625, 55, anchor="nw", window=employeeID)
    employeeName_entry_window = my_canvas.create_window(625, 100, anchor="nw", window=employeeName)




    #my_canvas.create_text(525, 110, text="Leave type", font=("Helvetica", 16), fill="white")
    #leaveType = tk.Entry(my_canvas, font=("Helvetica", 12), width=15, bg="white", borderwidth=1)
    #leaveType.pack()
    #leaveType_entry_window = my_canvas.create_window(600, 100, anchor="nw", window=leaveType)





    assign_button = tk.Button(root, text="Schedule this employee", activeforeground='white', font=("Helvetica", 12),
                                width=25, height=15, borderwidth=2, command=lambda: schedule_an_Employee(cal.get_date(), employeeID, employeeName))
    assign_button_window = my_canvas.create_window(500, 150, height=20, anchor="nw", window=assign_button)


    root.mainloop()

if __name__ == '__main__':
    main()


