from tkinter import *
from tkinter import messagebox


class TextField:
    def __init__(self, win, txt, bg="white", password=False):
        self.win = win
        self.txt = txt
        self.bg = bg
        self.password = password
        if password:
            disp = "*"
        else:
            disp = ""
        self.lbl = Label(self.win, text=self.txt, background=self.bg, font=("Bold", -14), foreground="white")
        self.entry = Entry(self.win, show=disp, font=('bold', -12), width=40)

    def show(self, index):
        self.lbl.grid(column=0, row=index+1, padx=5, pady=10, ipadx=3, ipady=3, sticky=EW)
        self.entry.grid(column=1, row=index+1, padx=5, pady=10, ipadx=3, ipady=3, sticky=W)

    def value(self):
        return self.txt, self.entry.get()

    def clear(self):
        self.entry.delete(0, END)


class Select:
    def __init__(self, win, txt, values, bg="white"):
        self.win = win
        self.txt = txt
        self.bg = bg
        self.values = values
        self.selction = StringVar()
        self.selction.set(self.values[0])
        self.lbl = Label(self.win, text=self.txt, background=self.bg, font=("Bold", -14), foreground="white")
        self.drop = OptionMenu(self.win, self.selction, *self.values)
        self.drop.config(width=40)

    def show(self, index):
        self.lbl.grid(column=0, row=index+1, padx=5, pady=10, ipadx=3, ipady=3, sticky=EW)
        self.drop.grid(column=1, row=index+1, padx=5, pady=10, ipadx=3, ipady=3, sticky=W)

    def value(self):
        return self.txt, self.selction.get()

    def clear(self):
        self.selction.set(self.values[0])


def save():
    valid = True
    p1 = None
    for f in fields:
        if f.value()[1] == "":
            valid = False
            messagebox.showerror('Error', "All fields should be filled")
            break
        if f.value()[0] == "Password":
            p1 = f.value()[1]
        if f.value()[0] == "Confirm Password":
            if p1 != f.value()[1]:
                valid = False
                messagebox.showerror('Error', "Incorrect Password")
                break
    if valid:
        file = open("user.txt", "a")
        for f in fields:
            file.write(f"{f.value()[0]} : {f.value()[1]}\n")
        file.write('\n')
        file.close()
        messagebox.showinfo("success", "Successfully Registered")
        for f in fields:
            f.clear()


root = Tk()
root.geometry('700x600')
root.title('Email Registration')
root.resizable(False, False)
root.config(background="#213141")
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=3)
Label(root, text="Email Registration",
      background="#56CD63", font=('bold', 20), pady=5).grid(column=0, row=0, columnspan=2, sticky=EW)
fields = [
    TextField(root, "First Name", bg="#213141"),
    TextField(root, "Last Name", bg="#213141"),
    TextField(root, "User Id", bg="#213141"),
    Select(root, "Gender", bg="#213141", values=["male", "female", "transgender", "others"]),
    TextField(root, "Age", bg="#213141"),
    TextField(root, "Password", bg="#213141", password=True),
    TextField(root, "Confirm Password", bg="#213141", password=True),
]
for i, field in enumerate(fields):
    field.show(i)

btn = Button(root, text="REGISTER", width=40, background="#56CD63", foreground="black", font=("bold", -12), command=save)
btn.grid(column=1, row=8, sticky=W, padx=5, pady=5)

root.mainloop()
