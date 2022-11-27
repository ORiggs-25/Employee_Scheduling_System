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
style.configure('Treeview.Heading', background="light blue")

headers = {"Content-Type": "application/json",
           "Connection": "keep-alive"}

try:
    response = requests.get("https://uhwxroslh0.execute-api.us-east-1.amazonaws.com/dev/leaves")
    jsonData = response.json()["Items"]

    tree = ttk.Treeview(win, column=("Employee ID", "Leave Type", "Start Date", "End Date"), show='headings',
                        height=100)
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="Employee ID")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="Leave Type")
    tree.column("# 3", anchor=CENTER)
    tree.heading("# 3", text="Start Date")
    tree.column("# 4", anchor=CENTER)
    tree.heading("# 4", text="End Date")

    for data in jsonData:
        tree.insert('', 'end', text="1",
                    values=(data['employeeID'], data['leave_type'], data['start_date'], data['end_date']))
    tree.pack()

except requests.exceptions.HTTPError as err:
    print(err)
# Add a Treeview widget

win.mainloop()
