import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Julie's party hire store rental details")

# 创建变量来存储输入的数据
customer_name = tk.StringVar()
receipt_number = tk.StringVar()
item_var = tk.StringVar()
quantity_var = tk.IntVar()

# 创建函数来处理提交按钮的点击事件
def submit_data():
    # 获取输入的数据
    name = customer_name.get()
    receipt = receipt_number.get()
    item = item_var.get()
    quantity = quantity_var.get()

    # 在 treeview 中插入一行数据
    table.insert("", "end", values=(name, receipt, item, quantity))

    # 清空输入框中的数据
    customer_name_entry.delete(0, "end")
    receipt_number_entry.delete(0, "end")
    quantity_spinbox.delete(0, "end")

#创建删除按钮
def delete_data():
    # 获取 treeview 中选中的行
    selected_items = table.selection()

    # 删除选中的行
    for item in selected_items:
        table.delete(item)

# 创建标签和输入框来输入顾客姓名和收据号码
customer_name_label = ttk.Label(root, text="Customer Name:")
customer_name_label.pack()
customer_name_entry = ttk.Entry(root, textvariable=customer_name)
customer_name_entry.pack()

receipt_number_label = ttk.Label(root, text="Receipt Number:")
receipt_number_label.pack()
receipt_number_entry = ttk.Entry(root, textvariable=receipt_number)
receipt_number_entry.pack()

# 创建下拉菜单来选择租用物品
item_label = ttk.Label(root, text="Item:")
item_label.pack()
item_combobox = ttk.Combobox(root, textvariable=item_var)
item_combobox["values"] = ("Table", "Chair", "Tent")
item_combobox.pack()

# 创建 spinbox 来选择租用数量
quantity_label = ttk.Label(root, text="Quantity:")
quantity_label.pack()
quantity_spinbox = tk.Spinbox(root, from_=1, to=500, textvariable=quantity_var)
quantity_spinbox.pack()

# 创建提交按钮来提交数据
submit_button = ttk.Button(root, text="Submit", command=submit_data)
submit_button.pack()

# 创建删除按钮来删除数据
delete_button = ttk.Button(root, text="Delete", command=delete_data)
delete_button.pack()


frame2 = tk.Frame(root, width=600, height=200, background="aqua")
frame2.pack()

# create the table
cols = ("row ID", "name", "receipt", "item", "quantity")
table = ttk.Treeview(frame2, columns=cols, show='headings')
table.pack()

# define headings
for col in cols:
    table.heading(col, text=col)

root.mainloop()
