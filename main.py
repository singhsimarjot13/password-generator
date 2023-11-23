import tkinter
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
count=0
password=""
def password():
    global count,password
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # password_list = []
    #
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    password_list=[random.choice(letters) for char in range(nr_letters)]

    for char in range(nr_symbols):
      password_list += random.choice(symbols)
    password_list+=[random.choice(symbols) for char in range(nr_symbols)]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    password_list+=[random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    # for char in password_list:
    #   password += char
    count+=1
    if count > 1:
        ent3.delete(0,'end')
    ent3.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    global ent1,ent2,ent3
    new_data={ent1.get():{"email":ent2.get(),"password":ent3.get()}}
    if len(ent1.get()) < 1 or len(ent2.get()) < 1  or len(ent3.get()) < 1:
        messagebox.showwarning(title="oops",message="Please don't leave any fields empty!")
    else:
        is_ok=messagebox.askokcancel(title=ent1.get(),message=f"These are details you entered\nwebsite-{ent1.get()}\nemail-{ent2.get()}\npassword-{ent3.get()}\nis it ok to save?")
        if is_ok:
            try:
             with open("data.json", mode='r') as data:
                existing=json.load(data)
            except:
                with open("data.json",mode='w') as data:
                    json.dump(new_data,data,indent=4)
            else:
             existing.update(new_data)
             with open("data.json",mode='w') as data:
                    json.dump(existing,data,indent=4)

            ent1.delete(0,'end')
            ent3.delete(0,'end')
            ent1.focus()
def clip():
    pyperclip.copy(password)
def search():
    try:
     with open("data.json") as data:
        a=json.load(data)
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No data file found!")
    except json.JSONDecodeError:
            messagebox.showwarning(title="Error", message="No data found!")
    else:
        if ent1.get() in a:
            messagebox.showinfo(title="Info",
                                message=f"Email:{a[ent1.get()]['email']}\nPassword:{a[ent1.get()]['password']}")
        else:
            messagebox.showwarning(title="Error", message="No details of website exits!")


# ---------------------------- UI SETUP ------------------------------- #
window=tkinter.Tk()
window.config(padx=50,pady=50)
photo=tkinter.Canvas(width=200,height=200,highlightthickness=0)
a=tkinter.PhotoImage(file="logo.png")
photo.create_image(100,100,image=a)
photo.grid(column=1,row=0)
label1=tkinter.Label(text="Website")
label1.grid(column=0,row=1)
label2=tkinter.Label(text="Email/Username")
label2.grid(column=0,row=2)
label3=tkinter.Label(text="Password")
label3.grid(column=0,row=3)
ent1=tkinter.Entry(width=33)
ent1.focus()
ent1.grid(column=1,row=1)
ent2=tkinter.Entry(width=52)
ent2.insert(0,"abcd@gmail.com")
ent2.grid(column=1,row=2,columnspan=2)
ent3=tkinter.Entry(width=33)
ent3.grid(column=1,row=3)
button=tkinter.Button(text="Generate Password",highlightthickness=0,width=15,command=password)
button.grid(column=2,row=3,padx=2)
button2=tkinter.Button(text="Add",width=44,highlightthickness=0,command=save)
button2.grid(column=1,row=4,columnspan=2)
button3=tkinter.Button(text="🔗",highlightthickness=0,width=2,command=clip)
button3.grid(column=3,row=3,padx=5)
button4=tkinter.Button(text="Search",width=15,highlightthickness=0,command=search)
button4.grid(column=2,row=1,padx=2)
window.mainloop()
