# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 17:27:52 2026

@author: user
"""

import tkinter as tk
from tkinter import messagebox

# Demo login va parol
TOG_RI_LOGIN = "admin"
TOG_RI_PAROL = "12345"


def kirish():
    login = login_entry.get()
    parol = parol_entry.get()

    if login == TOG_RI_LOGIN and parol == TOG_RI_PAROL:
        messagebox.showinfo("Natija", "Kirish muvaffaqiyatli!")
    else:
        messagebox.showerror("Xato", "Login yoki parol noto'g'ri!")


def parolni_korsat():
    if show_var.get():
        parol_entry.config(show="")
    else:
        parol_entry.config(show="*")


# Asosiy oyna
oyna = tk.Tk()
oyna.title("Kirish oynasi")
oyna.geometry("400x280")
oyna.resizable(False, False)

# Sarlavha
sarlavha = tk.Label(
    oyna,
    text="TIZIMGA KIRISH",
    font=("Arial", 18, "bold")
)
sarlavha.pack(pady=20)

# Login
tk.Label(oyna, text="Login:", font=("Arial", 11)).pack()

login_entry = tk.Entry(
    oyna,
    font=("Arial", 12),
    width=30
)
login_entry.pack(pady=5)

# Parol
tk.Label(oyna, text="Parol:", font=("Arial", 11)).pack()

parol_entry = tk.Entry(
    oyna,
    font=("Arial", 12),
    width=30,
    show="*"
)
parol_entry.pack(pady=5)

# Parolni ko'rsatish
show_var = tk.BooleanVar()

show_check = tk.Checkbutton(
    oyna,
    text="Parolni ko'rsatish",
    variable=show_var,
    command=parolni_korsat
)
show_check.pack()

# Kirish tugmasi
kirish_btn = tk.Button(
    oyna,
    text="KIRISH",
    font=("Arial", 12, "bold"),
    width=15,
    command=kirish
)
kirish_btn.pack(pady=20)

oyna.mainloop()