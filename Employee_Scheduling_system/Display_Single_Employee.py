import tkinter as tk  # GUI module
import requests
import json
from tkinter import Canvas
from PIL import ImageTk  # Display background


def main():
    # -----following code pertains to main user input window------------------------------------------------------------
    # creating object from Tkinter module
    root = tk.Tk()
    # renames the title of the window
    root.title("Display an Employee")
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
    def getFirstName(first):
        # user input  is saved into variables
        first = first_entry.get()

    def getLastname(last):
        last = last_entry.get()

    def get_ID(IDnumber):
        IDnumber = employeeID.get()

    def printDataInput(first, last, email, dob, phone, position, earn):
        import tk
        root = tk.Tk()
        root.title("Display Employee")
        root.geometry('1200x800')

        print_fullname = "Fullname     : " + str(first.get()) + " " + str(last.get())
        full_name = Label(root, text=print_fullname, font=("Helvetica", 21), justify=LEFT)
        full_name.pack()

        print_email = "Email        : " + str(email.get())
        display_email = Label(root, text=print_email, font=("Helvetica", 21), justify=LEFT)
        display_email.pack()

        print_dob = "Date of Birth: " + str(dob.get())
        display_dob = Label(root, text=print_dob, font=("Helvetica", 21), justify=LEFT)
        display_dob.pack()

        print_phone = "Phone        : " + str(phone.get())
        display_phone = Label(root, text=print_phone, font=("Helvetica", 21), justify=LEFT)
        display_phone.pack()

        print_position = "Position     : " + str(position.get())
        display_position = Label(root, text=print_position, font=("Helvetica", 21), justify=LEFT)
        display_position.pack()

        print_earning = "Pay         : $ " + str(earn.get()) + "per hour"
        display_earn = Label(root, text=print_earning, font=("Helvetica", 21), justify=LEFT)
        display_earn.pack()


    def display_an_employee(first, last, IDnumber):
        root = tk.Tk()
        root.title("Display Employee")
        root.geometry('1200x800')

        headers = {"Content-Type": "application/json",
                   "Connection": "keep-alive"}

        # ------------------------------needs to find out how to pull data from database ???

        '''
        view_employee = {
            "lastName": str(first),
            "dob": str(dob),
            "status": "Active",
            "address": "423 Candy Lane, Los Angeles C",
            "id": "4",
            "email": str(email),
            "phone": str(phone),
            "firstName": str(last),
            "roleID": "4"
        }
        '''

        try:
            response = requests.get("https://uhwxroslh0.execute-api.us-east-1.amazonaws.com/dev/create/employee",
                                    data=json.dumps(display_an_employee), headers=headers)
            print(response.status_code)
        except requests.exceptions.HTTPError as err:
            print(err)
        root.mainloop()



    # ==================================================================================================================

    # create_text function from tkinter will display text onto GUI
    my_canvas.create_text(575, 50, text="Display Employee", font=("Helvetica", 21), fill="white")
    my_canvas.create_text(300, 140, text="First Name", font=("Helvetica", 16), fill="white")
    my_canvas.create_text(300, 190, text="Last Name", font=("Helvetica", 16), fill="white")
    my_canvas.create_text(300, 240, text="Email", font=("Helvetica", 16), fill="white")

    # create Entry text boxes
    first_entry = tk.Entry(my_canvas, font=("Helvetica", 12), width=50, bg="white", borderwidth=2)
    first_entry.pack()
    last_entry = tk.Entry(my_canvas, font=("Helvetica", 12), width=50, bg="white", borderwidth=2)
    last_entry.pack()
    employeeID = tk.Entry(my_canvas, font=("Helvetica", 12), width=50, bg="white", borderwidth=2)
    employeeID.pack()

    first_entry_window = my_canvas.create_window(375, 125, anchor="nw", window=first_entry)
    last_entry_window = my_canvas.create_window(375, 175, anchor="nw", window=last_entry)
    employeeID_window = my_canvas.create_window(375, 225, anchor="nw", window=employeeID)

    create_button = tk.Button(root, text="Some Button", activeforeground='white', font=("Helvetica", 15),
                              width=15, height=20, borderwidth=2,
                              command=lambda: do_something())

    create_button_window = my_canvas.create_window(550, 550, height=35, anchor="nw", window=create_button)

    root.mainloop()

if __name__ == '__main__':
    main()
