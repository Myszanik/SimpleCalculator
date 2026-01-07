import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create the entry field
        self.entry = tk.Entry(master, width=10, justify='center', font=('Arial', 100))
        self.entry.grid(row=0, column=0, columnspan=4, padx=15, pady=15)

        # Create the buttons
        self.create_button("1", 1, 0)
        self.create_button("2", 1, 1)
        self.create_button("3", 1, 2)
        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("7", 3, 0)
        self.create_button("8", 3, 1)
        self.create_button("9", 3, 2)
        self.create_button("0", 4, 1)
        self.create_button(".", 4, 2)

        self.create_button("+", 1, 3)
        self.create_button("-", 2, 3)
        self.create_button("*", 3, 3)
        self.create_button("/", 4, 3)

        self.create_button("=", 4, 0)
        self.create_button("C", 5, 0)
        self.create_button("CE", 5, 1)
        self.create_button("(", 5, 2)
        self.create_button(")", 5, 3)

    def create_button(self, text, row, column):
        button = tk.Button(self.master, text=text, width=12, height=6, font=('Arial', 25), command=lambda: self.button_click(text))
        button.grid(row=row, column=column, padx=0, pady=0)

    def button_click(self, text):
        if text == "=":
            try:
                result = eval(self.entry.get())
                num_decimal_places = 2
                result = round(result, num_decimal_places)
                result = str(result)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        elif text == "C":
            self.entry.delete(0, tk.END)
        elif text == "CE":
            self.entry.delete(len(self.entry.get())-1, tk.END)
        else:
            self.entry.insert(tk.END, text)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()