from tkinter import *
from tkinter import ttk

# INCOMPLETE AS OF THIS PUSH
import requests

# Create an instance of tkinter frame
win = Tk()

# Set the size of the tkinter window
win.geometry("1200x800")

# Create an object of Style widget
style = ttk.Style()
style.theme_use('clam')
# Configure the style of Heading in Treeview widget
style.configure('Treeview.Heading', background="light yellow")

headers = {"Content-Type": "application/json",
           "Connection": "keep-alive"}

try:

    response = requests.get("https://uhwxroslh0.execute-api.us-east-1.amazonaws.com/dev/employmentHistory")
    jsonData = response.json()["Items"]

    tree = ttk.Treeview(win, column=("Employee ID", "Start Date", "Role ID"), show='headings',
                        height=100)
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="Employee ID")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="Start Date")
    tree.column("# 3", anchor=CENTER)
    tree.heading("# 3", text="Role ID")

    arr = []  # An array is declared, so we can iterate through the numbers in the database
    res = []
    # 200 max employees

    counter = 0




    for data in jsonData:
        if data["roleID"] == "1":
            data["roleID"] = "Intern"
        elif data["roleID"] == "2":
            data["roleID"] = "Associate"
        elif data["roleID"] == "3":
            data["roleID"] = "Supervisor"
        elif data["roleID"] == "4":
            data["roleID"] = "Manager"
        if data["roleID"] == "5":
            data["roleID"] = "Executive"

        emplID = data['employeeID']
        rolID = data['roleID']
        sd = data['start_date']
        arr.append(emplID + " " + rolID + " " + sd)
        arr.sort()

    for employee in arr:
        empID, rol, sd = employee.split(" ")
        tree.insert('', 'end', text="1",
                    values=(empID, sd, rol))




    tree.pack()

    ''' #OLD CODE
        
        print(data)
        currentEmployee = data['employeeID']
        print(currentEmployee)
        arr.append(currentEmployee)
        print(arr)
        res = [*set(arr)]
        res.sort()
        print(res)
        for currentEmployee in jsonData:
            for x in range(len(res)):
                if currentEmployee == res[int(x)]:
                    print(currentEmployee['roleID'])
                    
        

        tree.insert('', 'end', text="1",
                    values=(data['employeeID'], data['id'], data['start_date'], data['roleID']))
    tree.pack()
    
    '''

except requests.exceptions.HTTPError as err:
    print(err)
# Add a Treeview widget


win.mainloop()
