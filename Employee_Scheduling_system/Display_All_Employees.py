from tkinter import *
from tkinter import ttk

import requests

# Create an instance of tkinter frame
win = Tk()

# Set the size of the tkinter window
win.geometry("1200x800")

# Create an object of Style widget
style = ttk.Style()
style.theme_use('clam')
# Configure the style of Heading in Treeview widget
style.configure('Treeview.Heading', background="blue")

headers = {"Content-Type": "application/json",
           "Connection": "keep-alive"}

try:
    response = requests.get("https://uhwxroslh0.execute-api.us-east-1.amazonaws.com/dev/employees")
    jsonData = response.json()["Items"]

    tree = ttk.Treeview(win, column=("Employee ID", "First Name", "Last Name", "Status", "Role ID"), show='headings',
                        height=100)
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="Employee ID")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="First Name")
    tree.column("# 3", anchor=CENTER)
    tree.heading("# 3", text="Last Name")
    tree.column("# 4", anchor=CENTER)
    tree.heading("# 4", text="Status")
    tree.column("# 5", anchor=CENTER)
    tree.heading("# 5", text="Role ID")

    for data in jsonData:
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

        # Insert the data in Treeview widget
        tree.insert('', 'end', text="1",
                    values=(data['id'], data['firstName'], data['lastName'], data['status'], data['roleID']))
    tree.pack()

except requests.exceptions.HTTPError as err:
    print(err)
# Add a Treeview widget

win.mainloop()
