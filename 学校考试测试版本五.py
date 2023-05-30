import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import ctypes

# Set DPI Awareness
ctypes.windll.shcore.SetProcessDpiAwareness(1)

# Create main window
root = tk.Tk()
root.title("Julie’s party hire store rental details")

# Create title label
title_label = tk.Label(root, text="Julie’s party hire store rental details", font=("Arial", 16, "bold"))
title_label.pack(pady=20)

# Create input frame
input_frame = tk.Frame(root)
input_frame.pack()

# Create name label and entry
name_label = tk.Label(input_frame, text="Full Name:")
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(input_frame)
name_entry.grid(row=0, column=1, padx=10)

# Create receipt number label and entry
receipt_label = tk.Label(input_frame, text="Receipt Number:")
receipt_label.grid(row=1, column=0, padx=10, pady=10)
receipt_entry = tk.Entry(input_frame)
receipt_entry.grid(row=1, column=1, padx=10)

# Create item label and combobox
item_label = tk.Label(input_frame, text="Item:")
item_label.grid(row=2, column=0, padx=10, pady=10)
item_combobox = ttk.Combobox(input_frame, values=["Table", "Chair"])
item_combobox.grid(row=2, column=1, padx=10)

# Create quantity label and spinbox
quantity_label = tk.Label(input_frame, text="Quantity:")
quantity_label.grid(row=3, column=0, padx=10, pady=10)
quantity_spinbox = tk.Spinbox(input_frame, from_=1, to=500)
quantity_spinbox.grid(row=3,column=1,padx=10)

# Create add button
def add_item():
    # Check if receipt number is valid
    if not receipt_entry.get().isdigit():
        messagebox.showerror("Error", "Receipt Number can only be in numbers")
        return

    # Add item to treeview
    treeview.insert("", "end", values=(name_entry.get(), receipt_entry.get(), item_combobox.get(), quantity_spinbox.get()))

add_button = tk.Button(input_frame,text="Add Item",command=add_item)
add_button.grid(row=4,columnspan=2,pady=10)

# Create treeview frame
treeview_frame = tk.Frame(root)
treeview_frame.pack()

# Create treeview title label
treeview_title_label = tk.Label(treeview_frame,text="Rental details",font=("Arial",14,"bold"))
treeview_title_label.pack(pady=10)

# Create treeview
treeview = ttk.Treeview(treeview_frame,column=("Name","Receipt Number","Item","Quantity"),show="headings")
treeview.pack()

# Add headings to treeview
treeview.heading("Name",text="Name")
treeview.heading("Receipt Number",text="Receipt Number")
treeview.heading("Item",text="Item")
treeview.heading("Quantity",text="Quantity")

# Create delete frame
delete_frame = tk.Frame(root)
delete_frame.pack()

# Create delete button
def delete_item():
    # Get selected item
    selected_item = treeview.selection()[0]
    # Get receipt number of selected item
    receipt_number = treeview.item(selected_item)["values"][1]
    # Check if entered receipt number matches selected item
    if delete_entry.get() == receipt_number:
        treeview.delete(selected_item)
    else:
        messagebox.showerror("Error", "Entered Receipt Number does not match selected item")

delete_button = tk.Button(delete_frame,text="Delete Item",command=delete_item)
delete_button.grid(row=1,columnspan=2,pady=10)

# Create exit button
exit_button = tk.Button(root,text="Exit",command=root.destroy)
exit_button.pack(pady=10)

# Run main loop
root.mainloop()
