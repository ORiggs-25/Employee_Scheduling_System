from tkinter import Label, LEFT


def viewEmployee(first, last, email, dob, phone, position, earn):
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


    root.mainloop()

