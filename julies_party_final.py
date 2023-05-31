# final assessment

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import ctypes

# Adjust the clarity of the software
ctypes.windll.shcore.SetProcessDpiAwareness(1)

root = tk.Tk()
root.title("Julie's party hire store rental details")

# Create a title
title_label = tk.Label(root, text="Julie's party hire store rental details", font=("Arial", 16, "bold"))
title_label.pack(pady=20)

# Record customer name entry box
name_frame = tk.Frame(root)
name_frame.pack(pady=5)
name_label = tk.Label(name_frame, text="Customer name:")
name_label.pack(side=tk.LEFT)
name_entry = tk.Entry(name_frame)
name_entry.pack(side=tk.LEFT)

# Record receipt number entry box
receipt_frame = tk.Frame(root)
receipt_frame.pack(pady=5)
receipt_label = tk.Label(receipt_frame, text="Receipt number:")
receipt_label.pack(side=tk.LEFT)
receipt_entry = tk.Entry(receipt_frame)
receipt_entry.pack(side=tk.LEFT)

# Record rental item dropdown menus
item_frame = tk.Frame(root)
item_frame.pack(pady=5)
item_label = tk.Label(item_frame, text="Item name:")
item_label.pack(side=tk.LEFT)
item_var = tk.StringVar()
item_options = ["Table", "Chair"]
item_dropdown = ttk.Combobox(item_frame, textvariable=item_var, values=item_options)
item_dropdown.pack(side=tk.LEFT)

# Record quantity spinbox
quantity_frame = tk.Frame(root)
quantity_frame.pack(pady=5)
quantity_label = tk.Label(quantity_frame, text="Quantity:")
quantity_label.pack(side=tk.LEFT)
quantity_spinbox = tk.Spinbox(quantity_frame, from_=1, to=500, wrap=True)
quantity_spinbox.pack(side=tk.LEFT)


row_id = 0

maxLength = 15

# Submit function
def add_data():
    global row_id

    name = name_entry.get()
    receipt = receipt_entry.get()
    item = item_var.get()
    quantity = quantity_spinbox.get()

    # Checking for error
    if len(name) > maxLength or len(receipt) > maxLength or len(item) > maxLength:
        messagebox.showerror("Error", "Input cannot exceed 20 characters")
        return
    
    if not name or not receipt or not item or not quantity:
        messagebox.showerror("error", "The input information has blank")
        return

    if not receipt.isdigit():
        messagebox.showerror("error", "Receipt Number can only be in numbers")
        return

    if not quantity.isdigit():
        messagebox.showerror("error", "The Quantity can only be in number")
        return

    if int(quantity) > 500:
        messagebox.showerror("error", "The quantity cannot be greater than 500")
        return

    row_id += 1
    tree.insert("", "end", values=(row_id, name, receipt, item, quantity))

    # Clear data in entry box when submiting
    name_entry.delete(0, "end")
    receipt_entry.delete(0, "end")
    item_dropdown.set("")
    quantity_spinbox.delete(0, "end")

# Delete function
def delete_data():
    global row_id

    id_to_delete = id_entry.get()

    if not id_to_delete.isdigit():
        messagebox.showerror("error", "Row ID have to be a number")
        return

    deleted = False
    for row in tree.get_children():
        if tree.item(row)["values"][0] == int(id_to_delete):
            tree.delete(row)
            deleted = True
            break

    if not deleted:
        messagebox.showerror("error", "Row ID does not excit")
        return

    for i,row in enumerate(tree.get_children()):
        tree.set(row,"ID",i+1)

    row_id = i + 1


# Create submit button
add_button = tk.Button(root, text="Submit", command=add_data)
add_button.pack(pady=10)

# Record row ID to delete
id_frame = tk.Frame(root)
id_frame.pack(pady=5)
id_label = tk.Label(id_frame, text="Enter Row ID to delete:")
id_label.pack(side=tk.LEFT)
id_entry = tk.Entry(id_frame)
id_entry.pack(side=tk.LEFT)

# Create delete button
delete_button = tk.Button(root, text="Delete Row", command=delete_data)
delete_button.pack(pady=10)

# Create exit button
exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack(pady=20)

# Create treeview
tree_label = tk.Label(root, text="Rental details", font=("Arial", 12, "bold"))
tree_label.pack(pady=10)
tree = ttk.Treeview(root, columns=("ID", "Name", "Receipt", "Item", "Quantity"), show="headings")
tree.heading("ID", text="Row ID")
tree.heading("Name", text="Customer name")
tree.heading("Receipt", text="Receipt number")
tree.heading("Item", text="Item name")
tree.heading("Quantity", text="Quantity")
tree.pack()

root.mainloop()