import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title("Julie’s party hire store rental details")

root.geometry("600x400+100+100")

customer_name = tk.StringVar()
receipt_number = tk.StringVar()
item_name = tk.StringVar()
quantity_number = tk.IntVar(value=1)
row_id = tk.StringVar()


def submit_data():

    name = customer_name.get()
    receipt = receipt_number.get()
    item = item_name.get()
    quantity = quantity_number.get()

    # 检查收据号码是否只包含数字
    if not receipt.isdigit():
        messagebox.showerror("Error", "Receipt Number can only be in numbers.")
        return

    tree.insert("", "end", values=(name, receipt, item, quantity))

    # 清空输入框中的数据
    customer_name_entry.delete(0, "end")
    receipt_number_entry.delete(0, "end")
    quantity_spinbox.delete(0, "end")


def delete_data():
 
    row_id_str = row_id.get()

    # 检查行编号是否只包含数字
    if not row_id_str.isdigit():
        messagebox.showerror("Error", "Row ID can only be in numbers.")
        return

    # 获取 treeview 中所有行的 iid
    rows = tree.get_children()

    # 检查行编号是否在有效范围内
    row_index = int(row_id_str) - 1
    if row_index < 0 or row_index >= len(rows):
        messagebox.showerror("Error", "Invalid row ID.")
        return

    # 删除指定行
    tree.delete(rows[row_index])

# 创建标签和输入框来输入顾客姓名和收据号码
customer_name_label = ttk.Label(root, text="Customer Name:")
customer_name_label.grid(row=0, column=0, padx=10, pady=10)
customer_name_entry = ttk.Entry(root, textvariable=customer_name)
customer_name_entry.grid(row=0, column=1, padx=10)

receipt_number_label = ttk.Label(root, text="Receipt Number:")
receipt_number_label.grid(row=1, column=0, padx=10)
receipt_number_entry = ttk.Entry(root, textvariable=receipt_number)
receipt_number_entry.grid(row=1, column=1)

# 创建下拉菜单来选择租用物品
item_label = ttk.Label(root, text="Item:")
item_label.grid(row=2, column=0, padx=10)
item_combobox = ttk.Combobox(root, textvariable=item_name)
item_combobox["values"] = ("Table", "Chair")
item_combobox.grid(row=2, column=1)

# 创建 spinbox
quantity_label = ttk.Label(root, text="Quantity:")
quantity_label.grid(row=3, column=0, padx=10)
quantity_spinbox = tk.Spinbox(root, from_=1, to=500, wrap=True,textvariable=quantity_number)
quantity_spinbox.grid(row=3, column=1)

# 创建提交按钮
submit_button = ttk.Button(root, text="Submit", command=submit_data)
submit_button.grid(row=4, column=0, padx=10)

# 创建标签和输入框来输入要删除的行编号
row_id_label = ttk.Label(root, text="Row ID:")
row_id_label.grid(row=4, column=1, padx=10)
row_id_entry = ttk.Entry(root, textvariable=row_id)
row_id_entry.grid(row=4, column=2)

# 创建删除按钮来删除数据
delete_button = ttk.Button(root, text="Delete", command=delete_data)
delete_button.grid(row=4, column=3)

# 创建 treeview 来显示数据
tree = ttk.Treeview(root)
tree["columns"] = ("name", "receipt", "item", "quantity")
tree.column("#0", width=0, stretch="NO")
tree.column("name", anchor="w", width=120)
tree.column("receipt", anchor="w", width=120)
tree.column("item", anchor="w", width=120)
tree.column("quantity", anchor="center", width=120)

tree.heading("#0", text="", anchor="w")
tree.heading("name", text="Name", anchor="w")
tree.heading("receipt", text="Receipt", anchor="w")
tree.heading("item", text="Item", anchor="w")
tree.heading("quantity", text="Quantity", anchor="center")

tree.grid(row=5, column=0, columnspan=4)

# 创建退出按钮
exit_button = ttk.Button(root, text="Exit", command=root.destroy)
exit_button.grid(row=6, column=3)


root.mainloop()
