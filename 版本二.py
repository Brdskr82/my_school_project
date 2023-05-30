import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Julie's party hire store rental details")

customer_name = tk.StringVar()
receipt_number = tk.StringVar()
item_name = tk.StringVar()
quantity_number = tk.IntVar(value=1)

def submit_data():
    # 获取输入的数据
    name = customer_name.get()
    receipt = receipt_number.get()
    item = item_name.get()
    quantity = quantity_number.get()

    # 在 treeview 中插入一行数据
    tree.insert("", "end", values=(name, receipt, item, quantity))

    # 清空输入框中的数据
    customer_name_entry.delete(0, "end")
    receipt_number_entry.delete(0, "end")
    quantity_spinbox.delete(0, "end")

# 创建函数来处理删除按钮的点击事件
def delete_data():
    
    # 获取 treeview 中选中的行
    selected_items = tree.selection()

    # 删除选中的行
    for item in selected_items:
        tree.delete(item)

# 创建标签和输入框来输入顾客姓名和收据号码
customer_name_label = ttk.Label(root, text="Customer Name:")
customer_name_label.grid(row=0, column=0)
customer_name_entry = ttk.Entry(root, textvariable=customer_name)
customer_name_entry.grid(row=0, column=1)

receipt_number_label = ttk.Label(root, text = "Receipt Number:")
receipt_number_label.grid(row=1, column=0)
receipt_number_entry = ttk.Entry(root, textvariable = receipt_number)
receipt_number_entry.grid(row=1, column=1)

# 创建下拉菜单
item_label = ttk.Label(root, text="Item:")
item_label.grid(row=2, column=0)
item_combobox = ttk.Combobox(root, textvariable=item_name)
item_combobox["values"] = ("Table", "Chair")
item_combobox.grid(row=2, column=1)

# 创建 spinbox
quantity_label = ttk.Label(root, text="Quantity:")
quantity_label.grid(row=3, column=0)
quantity_spinbox = tk.Spinbox(root, from_=1, to=500, wrap=True, textvariable = quantity_number)
quantity_spinbox.grid(row=3, column=1)

# 创建提交按钮
submit_button = ttk.Button(root, text="Submit", command=submit_data)
submit_button.grid(row=4, column=0)

# 创建删除按钮
delete_button = ttk.Button(root, text="Delete", command=delete_data)
delete_button.grid(row=4, column=1)

# 创建 treeview
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

tree.grid(row=5, column=0, columnspan=2)

root.mainloop()
