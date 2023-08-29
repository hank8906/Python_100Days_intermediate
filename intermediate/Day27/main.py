import tkinter

window = tkinter.Tk()
window.title("My first GUI")
window.minsize(width=300, height=150)
window.config(padx=50,pady=20)


# Entry

input_text = tkinter.Entry(width=10)
input_text.grid(row=0, column=1)

# Miles Label

miles_text = tkinter.Label(text="Miles")
miles_text.grid(row=0, column=2)

# is_equal_to Label

equal_text = tkinter.Label(text="is equal to")
equal_text.grid(row=1, column=0)

# result Label

result_label = tkinter.Label(text="result", font=("Arial", 12, "bold"))
result_label.config(padx=10,pady=10)
result_label.grid(row=1, column=1)

# KM Label

km_label = tkinter.Label(text="KM", font=("Arial", 12, "bold"))
km_label.grid(row=1, column=2)

# Button


def button_clicked():
    result_label["text"] = round(float(input_text.get()) * 1.60934)


my_button = tkinter.Button(text="Calculate", command=button_clicked)
my_button.grid(row=2, column=1)

window.mainloop()
