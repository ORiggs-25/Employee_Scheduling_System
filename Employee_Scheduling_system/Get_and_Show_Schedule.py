from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk
from tkcalendar import *  # for calendar view
import requests

def main():
    def viewSchedule(date_input):

        # create table to view schedules ===============================================================================
        # Create an instance of tkinter frame
        win = Tk()

        # Set the size of the tkinter window
        win.geometry("1200x500")
        # Create an object of Style widget
        style = ttk.Style()
        style.theme_use('clam')
        # Configure the style of Heading in Treeview widget
        style.configure('Treeview.Heading', background="blue")

        headers = {"Content-Type": "application/json",
                   "Connection": "keep-alive"}

        try:
            tree = ttk.Treeview(win, column=("Date", "Employee ID", "First Name", "Last Name"), show='headings',
                                height=30)
            tree.column("# 1", anchor=CENTER)
            tree.heading("# 1", text="Date")
            tree.column("# 2", anchor=CENTER)
            tree.heading("# 2", text="Employee ID")
            tree.column("# 3", anchor=CENTER)
            tree.heading("# 3", text="First Name")
            tree.column("# 4", anchor=CENTER)
            tree.heading("# 4", text="Last Name")
            response = requests.get("https://uhwxroslh0.execute-api.us-east-1.amazonaws.com/dev/attendance/all")
            jsonData = response.json()["Items"]

            employeeInfo = requests.get("https://uhwxroslh0.execute-api.us-east-1.amazonaws.com/dev/employees")
            employeeData = employeeInfo.json()["Items"]

            # variable to display name and last name that will be called in the column
            firstName = ''
            lastName = ''


            for data in jsonData:
                # Insert the data in Treeview widget
                if date_input == data["scheduledDate"]:
                    for info in employeeData:
                        if int(data['employeeID']) == info['id']:
                            firstName = info['firstName']
                            lastName = info['lastName']
                    tree.insert('', 'end', text="1", values=(date_input,
                                                    data['employeeID'], firstName, lastName))
            tree.pack()


        except requests.exceptions.HTTPError as err:
            print(err)

        win.mainloop()
    # end of viewSchedule function ====================================================================================


    # -----following code pertains to main user input window------------------------------------------------------------
    # creating object from Tkinter module

    root = tk.Tk()
    # renames the title of the window
    root.title("Show Employee Schedule")
    # sets the dimensions of the window to measurement
    root.geometry('1200x800')
    # prevents user to resize the window
    root.resizable(width=False, height=False)

    cal = Calendar(root, selectmode="day", year=2022)
    cal.pack(pady=20, fill="both", expand=True)

    def grab_date():
        date.config(text=cal.get_date())

    # Add Button and Label
    Button(root, text="Get Date",
           command=grab_date).pack(pady=5)
    date = Label(root, text="")
    date.pack(pady=5)
    date_input = grab_date()

    # canvas function will create a background for the GUI
    my_canvas: Canvas = tk.Canvas(root, width=1200, height=800, bd=0, highlightthickness=0)
    my_canvas.pack(fill="both", expand=True)

    # using pillow's ImageTk class and PhotoImage function to display background photo
    bg = ImageTk.PhotoImage(file="BasicBlue.jpeg")
    my_canvas.create_image(0, 0, image=bg, anchor="nw")
    # ==================================================================================================================

    view_schedule_button = tk.Button(root, text="View Schedule", activeforeground='white', font=("Helvetica", 12),
                              width=15, height=15, borderwidth=2, command=lambda:viewSchedule(date_input))

    view_schedule_window = my_canvas.create_window(500, 10, height=20, anchor="nw", window=view_schedule_button)

    root.mainloop()

if __name__ == '__main__':
    main()
