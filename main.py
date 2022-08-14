from tkinter import *
windows = Tk()
windows.title("My first GUI program")
windows.minsize(width=500, height=300)
windows.config(padx=100, pady=200)

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


# Label

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)


# Button

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry

input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)


windows.mainloop()