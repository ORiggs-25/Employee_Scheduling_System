import tkinter as tk  # GUI module
from PIL import ImageTk  # Display background
import requests
import json
import boto3
from numpy.ma import var


def main():

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
    def create_Employee(first, last, email, dob, phone, address, role, employeeID):

        '''
        # finding the count data in DynamoDB
        dynamoDBResource = boto3.resource("https://uhwxroslh0.execute-api.us-east-1.amazonaws.com/dev/employees")
        table = dynamoDBResource.Table('ScannedCount')
        employeeID = table + 1
        '''

        headers = {"Content-Type": "application/json",
                   "Connection": "keep-alive"}

        try:
            createEmployee = {
                "lastName": str(last.get()),
                "dob": str(dob.get()),
                "status": "Active",  # active by default
                "address": str(address.get()),
                "id": str(employeeID.get()), # temporary fix
                "email": str(email.get()),
                "phone": str(phone.get()),
                "firstName": str(first.get()),
                "roleID": str(role.get()) #temporary fix
            }

            response = requests.put("https://uhwxroslh0.execute-api.us-east-1.amazonaws.com/dev/create/employee",
                                    data=json.dumps(createEmployee), headers=headers)
            print(response.status_code)
        except requests.exceptions.HTTPError as err:
            print(err)


    # -----following code pertains to main user input window-----------------------------------------------------------
    # creating object from Tkinter module
    root = tk.Tk()
    # renames the title of the window
    root.title("Admin Portal")
    # sets the dimensions of the window to measurement
    root.geometry('1200x800')
    # prevents user to resize the window
    root.resizable(width=False, height=False)

    # canvas function will create a background for the GUI
    my_canvas = tk.Canvas(root, width=1200, height=800, bd=0, highlightthickness=0)
    my_canvas.pack(fill="both", expand=True)

    # using pillow's ImageTk class and PhotoImage function to display background photo
    bg = ImageTk.PhotoImage(file="addEmployee1.jpg")
    my_canvas.create_image(0, 0, image=bg, anchor="nw")

    # create_text function from tkinter will display text onto GUI
    my_canvas.create_text(575, 50, text="Create a new Employee", font=("Helvetica", 21), fill="white")
    my_canvas.create_text(300, 140, text="First Name", font=("Helvetica", 16), fill="white")
    my_canvas.create_text(300, 190, text="Last Name", font=("Helvetica", 16), fill="white")
    my_canvas.create_text(300, 240, text="Email", font=("Helvetica", 16), fill="white")
    my_canvas.create_text(300, 290, text="DOB", font=("Helvetica", 16), fill="white")
    my_canvas.create_text(300, 340, text="Phone", font=("Helvetica", 16), fill="white")
    my_canvas.create_text(300, 390, text="Address", font=("Helvetica", 16), fill="white")
    my_canvas.create_text(300, 440, text="Role", font=("Helvetica", 16), fill="white")
    my_canvas.create_text(300, 490, text="Employee ID", font=("Helvetica", 16), fill="white") # temporary fix

    # create Entry text boxes
    first_entry = tk.Entry(my_canvas, font=("Helvetica", 12), width=50, bg="white", borderwidth=2)
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
    role_entry = tk.Entry(my_canvas, font=("Helvetica", 12), width=50, bg="white", borderwidth=2)
    role_entry.pack()
    employeeID_entry = tk.Entry(my_canvas, font=("Helvetica", 12), width=50, bg="white", borderwidth=2)
    employeeID_entry.pack()

    # =============== drop down box for employee roles ========================================================
    '''
    clicked = tk.StringVar()
    clicked.set("Select a role")
    drop_entry = tk.OptionMenu(root, clicked, "Intern", "Associate", "Supervisor", "Manager", "Executive")
    drop_entry.pack()
    '''
    #roleID = assignRole(clicked.get())
    # ==========================================================================================================

    first_entry_window = my_canvas.create_window(375, 125, anchor="nw", window=first_entry)
    last_entry_window = my_canvas.create_window(375, 175, anchor="nw", window=last_entry)
    email_entry_window = my_canvas.create_window(375, 225, anchor="nw", window=email_entry)
    dob_entry_window = my_canvas.create_window(375, 275, anchor="nw", window=dob_entry)
    phone_entry_window = my_canvas.create_window(375, 325, anchor="nw", window=phone_entry)
    address_entry_window = my_canvas.create_window(375, 375, anchor="nw", window=address_entry)
    #selectRoleButton = tk.Button(root, text=str(drop_entry.pack()), activeforeground='white', font=("Helvetica", 15),
                                #width=15, height=20, borderwidth=1, command=lambda: drop_entry.pack())
    #selectRoleButton_window = my_canvas.create_window(375, 425, height=35, anchor="nw", window=drop_entry)

    role_entry_window = my_canvas.create_window(375, 425, anchor="nw", window=role_entry)
    employeeID_window = my_canvas.create_window(375, 475, anchor="nw", window=employeeID_entry) # temporary fix



    '''
    selectRoleButton = tk.Button(root, text="Select a role", activeforeground='white', font=("Helvetica", 15),
                                 width=15, height=20, borderwidth=1, command= lamda:assignRole(drop.pack()))
    role_button_window = my_canvas.create_window(375, 425, height=35, anchor="nw", window=drop)
    selectRoleButton_window = my_canvas.create_window(375, 425, height=35, anchor="nw", window=selectRoleButton)
    
    '''




    # We used the Button function in Tkinter which will call the function once user click save
    # Once user hit save, the system validates input and check whether account exists or not.
    create_button = tk.Button(root, text="Save", activeforeground='white', width=15,
                              font=("Helvetica", 15), height=20, borderwidth=2,
                              command=lambda: create_Employee(first_entry, last_entry, email_entry, dob_entry,
                                                              phone_entry, address_entry, role_entry, employeeID_entry))


    create_button_window = my_canvas.create_window(550, 560, height=35, anchor="nw", window=create_button)

    root.mainloop()


if __name__ == '__main__':
    main()
