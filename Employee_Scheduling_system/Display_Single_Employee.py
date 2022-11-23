import tkinter as tk  # GUI module
import requests
from tkinter import Canvas, LEFT
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

    #===============================================================================================================

    def display_an_employee(first, last, IDnumber):
        headers = {"Content-Type": "application/json",
                   "Connection": "keep-alive"}

        try:
            response = requests.get("https://uhwxroslh0.execute-api.us-east-1.amazonaws.com/dev/employees")
            jsonData = response.json()["Items"]
            for data in jsonData:
                if first == data["firstName"] and last == data["lastName"] and int(IDnumber) == data["id"]:
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

                    my_canvas.create_text(600, 400, text="Employee Info #" + str(data["id"]), font=("Helvetica", 20), fill="black")
                    my_canvas.create_text(600, 450, text="Full Name : " + data["firstName"] + " " + data["lastName"], font=("Helvetica", 16), fill="black", justify=LEFT)
                    my_canvas.create_text(600, 475, text="Email : " + data["email"], font=("Helvetica", 16), fill="black", justify=LEFT)
                    my_canvas.create_text(600, 500, text="Date of Birth : " + data["dob"], font=("Helvetica", 16), fill="black", justify=LEFT)
                    my_canvas.create_text(600, 525, text="Phone : " + data["phone"], font=("Helvetica", 16), fill="black", justify=LEFT)
                    my_canvas.create_text(600, 550, text="Address   : " + data["address"], font=("Helvetica", 16), fill="black", justify=LEFT)
                    my_canvas.create_text(600, 575, text="Role  : " + data["roleID"], font=("Helvetica", 16), fill="black", justify=LEFT)

        except requests.exceptions.HTTPError as err:
            print(err)
    # ==================================================================================================================

    # create_text function from tkinter will display text onto GUI
    my_canvas.create_text(575, 50, text="Search an Employee", font=("Helvetica", 21), fill="white")
    my_canvas.create_text(300, 140, text="First Name", font=("Helvetica", 16), fill="white")
    my_canvas.create_text(300, 190, text="Last Name", font=("Helvetica", 16), fill="white")
    my_canvas.create_text(300, 240, text="Employee ID", font=("Helvetica", 16), fill="white")

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

    create_button = tk.Button(root, text="View Employee", activeforeground='white', font=("Helvetica", 15),
                              width=15, height=20, borderwidth=2,
                              command=lambda: display_an_employee(first_entry.get(), last_entry.get(), employeeID.get()))

    create_button_window = my_canvas.create_window(500, 275, height=35, anchor="nw", window=create_button)

    root.mainloop()

if __name__ == '__main__':
    main()