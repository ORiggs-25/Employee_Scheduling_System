import json
from tkinter import *
import tkinter as tk

import days as days
import requests
from PIL import ImageTk
from tkcalendar import *  # for calendar view
import requests
import datetime
from datetime import datetime, timedelta



def main():
    # -----following code pertains to main user input window------------------------------------------------------------
    # creating object from Tkinter module
    root = tk.Tk()
    # renames the title of the window
    root.title("Display Bi-Weekly Payment")
    # sets the dimensions of the window to measurement
    root.geometry('1200x800')
    # prevents user to resize the window
    root.resizable(width=False, height=False)

    cal = Calendar(root, selectmode="day", year=2022)
    cal.pack(pady=20, fill="both", expand=True)

    '''
    #find the date 2 weeks ago
    #today = datetime.datetime.strptime(cal.get_date(), "%m%d%y")
    todaysDate = datetime.datetime.today().strftime('%m/%d/%Y')
    date_2_weeks_ago = todaysDate - datetime.timedelta(days=int(14))
    #converted_date.config(text=f"Date: {end_date.strftime('%m/%d/%Y')}")
    '''

    todayDate = datetime.strptime(cal.get_date(), "%m/%d/%y")
    d = datetime.datetime.timedelta(days=14)
    a = todayDate - d
    #twoWeeksAgo = a.strftime('%m/%d/%Y')

     # getting date from the calendar
    def grab_date():
        my_label.config(text=str(todayDate) + "to" + str(a))

    def view_payment(date, employeeID):
        headers = {"Content-Type": "application/json",
                   "Connection": "keep-alive"}

        try:
            scheduleEmployee = {

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
    date_button = Button(root, text="Selected Date Range", command=grab_date, bg="blue", fg='white')
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

    my_canvas.create_text(600, 20, text="Select end Date and enter Employee ID to Display Bi-Weekly Payments", font=("Helvetica", 16), fill="white")
    my_canvas.create_text(525, 65, text="Employee ID", font=("Helvetica", 16), fill="white")

    employeeID = tk.Entry(my_canvas, font=("Helvetica", 12), width=15, bg="white", borderwidth=1)
    employeeID.pack()

    employeeID_entry_window = my_canvas.create_window(625, 55, anchor="nw", window=employeeID)


    assign_button = tk.Button(root, text="View Payment", activeforeground='white', font=("Helvetica", 12),
                                width=25, height=15, borderwidth=2, command=lambda: view_payment(cal.get_date(),employeeID, date_2_weeks_ago))
    assign_button_window = my_canvas.create_window(500, 150, height=20, anchor="nw", window=assign_button)


    root.mainloop()


if __name__ == '__main__':
    main()


