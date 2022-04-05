from tkinter import *

# Create an empty Tkinter window
window = Tk()


def from_kg():

    grams = float(e1_value.get()) * 1000 # Get user value from input box and multiply by 1000 to get kilograms
    t1.delete("1.0", END) # Deletes the content of the Text box from start to END
    t1.insert(END, grams) # Fill in the text box with the value of gram variable

    pounds = float(e1_value.get()) * 2.20462
    t2.delete("1.0", END)
    t2.insert(END, pounds)

    ounces = float(e1_value.get()) * 35.274
    t3.delete("1.0", END)
    t3.insert(END, ounces)

# Create a button widget
# The from_kg() function is called when the button is pushed
b1 = Button(window, text="Convert", command=from_kg)
b1.grid(row=0, column=2)

e1_value = StringVar()  # Create a special StringVar object
e1 = Entry(window, textvariable=e1_value) # Create an Entry box for users to enter the value
e1.grid(row=0, column=1)

# Create Labels widget with mass labels
e2 = Label(window, text="Kg")
e2.grid(row=0, column=0)

e3 = Label(window, text="g")
e3.grid(row=1, column=0)

e4 = Label(window, text="lbs")
e4.grid(row=1, column=1)

e5 = Label(window, text="ounces")
e5.grid(row=1, column=2)

# Create three empty text boxes, t1, t2, and t3
t1 = Text(window, height=1, width=20)
t1.grid(row=2, column=0)
t2 = Text(window, height=1, width=20)
t2.grid(row=2, column=1)
t3 = Text(window, height=1, width=20)
t3.grid(row=2, column=2)

window.mainloop()
