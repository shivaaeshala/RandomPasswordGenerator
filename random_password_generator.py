from tkinter import *
import string
import random
from tkinter import messagebox
characters= ''

def req():
    global characters
    try:
        length = int(len.get())
        if length<=0:
            raise ValueError("Password length must be greater than 0")

        inc_upper = upper.get()
        inc_lower = lower.get()
        inc_numbers = digit.get()
        inc_special = special.get()
        exc_char = display.get()
        
        char_set = ''
        if inc_upper:
            char_set += string.ascii_uppercase
        if inc_lower:
            char_set += string.ascii_lowercase
        if inc_numbers:
            char_set += str(string.digits)
        if inc_special:
            char_set += str(string.punctuation)
        for i in exc_char:
            char_set = char_set.replace(i, '')
        if not char_set:
            raise ValueError("Select at least one character type")  
              
        password = ''.join(random.choice(char_set) for _ in range(length))
        entry_generated_password.delete(0, END)
        entry_generated_password.insert(0, password)

    except ValueError as ve:
        messagebox.showerror("Error", str(ve))

if __name__=='__main__':
    root = Tk()
    root.geometry("500x650")
    root.configure(background="white")
    root.title("Random password generator")
    h1_label = Label(text="Random Password Generator", background="white", font=30, pady=20)
    h1_label.pack()
    h2_label = Label(text="Choose the types of characters", background="white", pady=10)
    h2_label.pack()

    Label(root, text="Enter the length of the password", bg="white", pady=10).pack()
    len = Entry(root, justify="center", width=20, borderwidth=2)
    len.pack(ipady=10,pady=10)


    upper = BooleanVar()
    lower = BooleanVar()
    digit = BooleanVar()
    special = BooleanVar()

    opt1 = Checkbutton(root, text="Uppercase letters", variable=upper, onvalue=1, offvalue=0, width=20, height=2, background="white", cursor="hand2")
    opt1.pack()
    opt2 = Checkbutton(root, text="Lowercase letters", variable=lower, onvalue=1, offvalue=0, width=20, height=2, background="white", cursor="hand2")
    opt2.pack()
    opt3 = Checkbutton(root, text="Numbers", variable=digit, onvalue=1, offvalue=0, width=20, height=2, background="white", cursor="hand2")
    opt3.pack()
    opt4 = Checkbutton(root, text="Special characters", variable=special, onvalue=1, offvalue=0, width=20, height=2, background="white", cursor="hand2")
    opt4.pack()

    display = StringVar()
    Label(root, text="Enter the characters you want to exclude", bg="white", pady=10).pack()
    exclude = Entry(root, textvariable=display, justify="center", width=20, borderwidth=2)
    exclude.pack(ipady=10,pady=10)
    
    gen_pass = Button(root, text="Generate password", command=req, width=30, height=3)
    gen_pass.pack(ipady=10)

    entry_generated_password = Entry(root)
    entry_generated_password.pack(ipady=10)

    root.mainloop()