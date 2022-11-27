import json
import tkinter as tk  # GUI module
from tkinter import Canvas, LEFT
from PIL import ImageTk  # Display background
import requests


def main():
    # -----following code pertains to main user input window------------------------------------------------------------
    # creating object from Tkinter module
    global employeeID
    root = tk.Tk()
    # renames the title of the window
    root.title("Update Employee Display")
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

    # ==================================================================================================================
    def fetch_employee_info():

        firstName = ''
        lastName = ''
        email = ''
        dob = ''
        phone = ''
        address = ''
        role = 0
        status = ''
        headers = {"Content-Type": "application/json",
                   "Connection": "keep-alive"}

        try:
            response = requests.get("https://uhwxroslh0.execute-api.us-east-1.amazonaws.com/dev/employees")
            jsonData = response.json()["Items"]
            for data in jsonData:
                if employeeID == str(data["id"]):
                    if data["roleID"] == 1:
                        data["roleID"] = "Intern"
                    elif data["roleID"] == 2:
                        data["roleID"] = "Associate"
                    elif data["roleID"] == 3:
                        data["roleID"] = "Supervisor"
                    elif data["roleID"] == 4:
                        data["roleID"] = "Manager"
                    if data["roleID"] == 5:
                        data["roleID"] = "Executive"

                    firstName = data['firstName']
                    lastName = data['lastName']
                    email = data['email']
                    dob = data['dob']
                    phone = data['phone']
                    address = data['address']
                    role = data['roleID']

            edit_employee(firstName, lastName, email, dob, phone, address, role, status)

        except requests.exceptions.HTTPError as err:
            print(err)

    # ==================================================================================================================
    def edit_employee(first, last, email, dob, phone, address, role, status):

        # create_text function from tkinter will display text onto GUI
        my_canvas.create_text(300, 200, text="First Name", font=("Helvetica", 16), fill="white")
        my_canvas.create_text(300, 250, text="Last Name", font=("Helvetica", 16), fill="white")
        my_canvas.create_text(300, 300, text="Email", font=("Helvetica", 16), fill="white")
        my_canvas.create_text(300, 350, text="DOB", font=("Helvetica", 16), fill="white")
        my_canvas.create_text(300, 400, text="Phone", font=("Helvetica", 16), fill="white")
        my_canvas.create_text(300, 450, text="Address", font=("Helvetica", 16), fill="white")
        my_canvas.create_text(300, 500, text="Role", font=("Helvetica", 16), fill="white")
        my_canvas.create_text(300, 550, text="Status", font=("Helvetica", 16), fill="white")


        # create Entry text boxes
        first_entry = tk.Entry(my_canvas, font=("Helvetica", 12), width=50, bg="white", borderwidth=2, )
        first_entry.pack()
        last_entry = tk.Entry(my_canvas, font=("Helvetica", 12), width=50, bg="white", borderwidth=2)
        last_entry.pack()
        email_entry = tk.Entry(my_canvas, font=("Helvetica", 12), width=50, bg="white", borderwidth=2)
        email_entry.pack()
        dob_entry = tk.Entry(my_canvas, font=("Helvetica", 12), width=50, bg="white", borderwidth=2)
        dob_entry.pack()
        phone_entry = tk.Entry(my_canvas, font=("Helvetica", 12), width=50, bg="white", borderwidth=2)
        phone_entry.pack()
        address_entry = tk.Entry(my_canvas, font=("Helvetica", 12), width=50, bg="white", borderwidth=2)
        address_entry.pack()
        # =============== drop down box for employee roles ========================================================
        clicked = tk.StringVar()
        clicked.set("Select a role")
        drop_entry = tk.OptionMenu(root, clicked, "Intern", "Associate", "Supervisor", "Manager", "Executive")
        drop_entry.pack()
        # roleID = role(clicked.get())
        # ==========================================================================================================
        # =============== drop down box for employee status ========================================================
        clicked_status = tk.StringVar()
        clicked_status.set("Select a status")
        status_drop_entry = tk.OptionMenu(root, clicked_status, "active", "terminated")
        status_drop_entry.pack()
        # ==========================================================================================================



        first_entry_window = my_canvas.create_window(375, 185, anchor="nw", window=first_entry)
        last_entry_window = my_canvas.create_window(375, 240, anchor="nw", window=last_entry)
        email_entry_window = my_canvas.create_window(375, 290, anchor="nw", window=email_entry)
        dob_entry_window = my_canvas.create_window(375, 340, anchor="nw", window=dob_entry)
        phone_entry_window = my_canvas.create_window(375, 390, anchor="nw", window=phone_entry)
        address_entry_window = my_canvas.create_window(375, 440, anchor="nw", window=address_entry)
        selectRoleButton = tk.Button(root, text="Select a role", activeforeground='white', font=("Helvetica", 15),
                                     width=15, height=20, borderwidth=1)
        role_button_window = my_canvas.create_window(375, 485, height=35, anchor="nw", window=drop_entry)
        selectStatusButton = tk.Button(root, text="Select a status", activeforeground='white', font=("Helvetica", 15),
                                     width=15, height=20, borderwidth=1)
        status_button_window = my_canvas.create_window(375, 530, height=35, anchor="nw", window=status_drop_entry)

        '''
        #Nice to have ==============================================================================================
        # entry_clear(e) function is used to clear the pre-input text inside the widgets once user clicks on them
        def entry_clear(e):
            if first_entry.get == first:
                first_entry.delete(0, 'end')
            elif last_entry.get() == last:
                last_entry.delete(0, 'end')
            elif email_entry.get() == email:
                email_entry.delete(0, 'end')
            elif dob_entry.get() == dob:
                dob_entry.delete(0, 'end')
            elif phone_entry.get == phone:
                phone_entry.delete(0, 'end')
            elif address_entry.get == address:
                address_entry.delete(0, 'end')

        # preset text will appear at the start of the code to give user formatting instructions of their inputs
        first_entry.insert(0, first)
        last_entry.insert(0, last)
        email_entry.insert(0, email)
        dob_entry.insert(0, dob)
        phone_entry.insert(0, phone)
        address.insert(0, address)
        #================================
        first_entry.bind("<Button-1>", entry_clear)
        last_entry.bind("<Button-2>", entry_clear)
        email_entry.bind("<Button-3>", entry_clear)
        dob_entry.bind("<Button-4>", entry_clear)
        phone_entry.bind("<Button-5>", entry_clear)
        address.bind("<Button-6>", entry_clear)
        # ============================================================================================================
        '''

        # We used the Button function in Tkinter which will call the function once user click save
        # Once user hit save, the system validates input and check whether account exists or not.
        update_employee = tk.Button(root, text="Save", activeforeground='white', width=15,
                                    font=("Helvetica", 15), height=20, borderwidth=2,
                                    command=lambda: confirm_update(first_entry, last_entry, email_entry, dob_entry,
                                                                   phone_entry, address_entry, clicked.get(),clicked_status))

        update_employee_window = my_canvas.create_window(500, 600, height=35, anchor="nw", window=update_employee)

        root.mainloop()

    def assignRole(role):
        if role == "Intern":
            return '1'
        elif role == "Associate":
            return '2'
        elif role == "Supervisor":
            return '3'
        elif role == "Manager":
            return '4'
        elif role == "Executive":
            return '5'

    def confirm_update(first, last, email, dob, phone, address, role, status):
            headers = {"Content-Type": "application/json",
                       "Connection": "keep-alive"}

            roleID = assignRole(role)

            try:
                updateEmployee = {
                    "lastName": str(last.get()),
                    "dob": str(dob.get()),
                    "status": str(status.get()),
                    "address": str(address.get()),
                    "id": str(employeeID.get()),
                    "email": str(email.get()),
                    "phone": str(phone.get()),
                    "firstName": str(first.get()),
                    "roleID": roleID
                }

                response = requests.put("https://uhwxroslh0.execute-api.us-east-1.amazonaws.com/dev/create/employee",
                                        data=json.dumps(updateEmployee), headers=headers)
                print(response.status_code)
            except requests.exceptions.HTTPError as err:
                print(err)

    # ==================================================================================================================
    # create_text function from tkinter will display text onto GUI
    my_canvas.create_text(575, 50, text="Enter an employee ID that needs to be updated", font=("Helvetica", 21),
                          fill="white")
    my_canvas.create_text(300, 115, text="Employee ID", font=("Helvetica", 16), fill="white")

    # create Entry text boxes
    employeeID = tk.Entry(my_canvas, font=("Helvetica", 12), width=50, bg="white", borderwidth=2)
    employeeID.pack()

    employeeID_window = my_canvas.create_window(375, 100, anchor="nw", window=employeeID)

    create_button = tk.Button(root, text="Update Employee", activeforeground='white', font=("Helvetica", 14),
                              width=15, height=20, borderwidth=2,
                              command=lambda: fetch_employee_info())

    create_button_window = my_canvas.create_window(500, 140, height=25, anchor="nw", window=create_button)

    # ==================================================================================================================
    root.mainloop()


if __name__ == '__main__':
    main()
