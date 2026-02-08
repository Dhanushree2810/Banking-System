import tkinter as tk
from operations import create_account, deposit, withdraw


def create_account_gui():
    name = name_entry.get()
    acc_no = int(acc_entry.get())
    balance = int(balance_entry.get())

    create_account(name, acc_no, balance)

    result_label.config(text="Account Created Successfully")


def deposit_gui():
    acc_no = int(acc_entry.get())
    amount = int(amount_entry.get())

    bal = deposit(acc_no, amount)

    result_label.config(text=f"New Balance: {bal}")


def withdraw_gui():
    acc_no = int(acc_entry.get())
    amount = int(amount_entry.get())

    bal = withdraw(acc_no, amount)

    result_label.config(text=f"Result: {bal}")


root = tk.Tk()
root.title("Banking System GUI")
root.geometry("400x400")

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Account No").pack()
acc_entry = tk.Entry(root)
acc_entry.pack()

tk.Label(root, text="Balance").pack()
balance_entry = tk.Entry(root)
balance_entry.pack()

tk.Label(root, text="Amount").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Button(root, text="Create Account", command=create_account_gui).pack(pady=5)
tk.Button(root, text="Deposit", command=deposit_gui).pack(pady=5)
tk.Button(root, text="Withdraw", command=withdraw_gui).pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
