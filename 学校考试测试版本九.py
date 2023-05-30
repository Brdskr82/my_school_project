# 导入必要的库
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import ctypes

# 设置DPI感知，使窗口大小适应屏幕分辨率
ctypes.windll.shcore.SetProcessDpiAwareness(1)

# 创建主窗口并设置标题
root = tk.Tk()
root.title("Julie’s party hire store rental details")

# 创建标题标签并居中显示
title_label = tk.Label(root, text="Julie’s party hire store rental details", font=("Arial", 16, "bold"))
title_label.pack(pady=20)

# 创建输入框和标签来记录客户姓名
name_label = tk.Label(root, text="客户姓名")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

# 创建输入框和标签来记录收据号码
receipt_label = tk.Label(root, text="收据号码")
receipt_label.pack()
receipt_entry = tk.Entry(root)
receipt_entry.pack()

# 创建下拉菜单和标签来记录租用物品
item_label = tk.Label(root, text="租用物品")
item_label.pack()
item_var = tk.StringVar()
item_options = ["Table", "Chair"]
item_dropdown = ttk.Combobox(root, textvariable=item_var, values=item_options)
item_dropdown.pack()

# 创建spinbox和标签来记录租用数量
quantity_label = tk.Label(root, text="租用数量")
quantity_label.pack()
quantity_spinbox = tk.Spinbox(root, from_=1, to=500, wrap=True)
quantity_spinbox.pack()

# 创建treeview来显示租赁详情
tree_label = tk.Label(root, text="Rental details", font=("Arial", 12, "bold"))
tree_label.pack(pady=10)
tree = ttk.Treeview(root, columns=("ID", "Name", "Receipt", "Item", "Quantity"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Name", text="客户姓名")
tree.heading("Receipt", text="收据号码")
tree.heading("Item", text="租用物品")
tree.heading("Quantity", text="租用数量")
tree.pack()

# 定义一个变量来跟踪treeview中的行数
row_id = 0

# 定义一个函数来添加数据到treeview中
def add_data():
    global row_id
    # 获取输入框中的值
    name = name_entry.get()
    receipt = receipt_entry.get()
    item = item_var.get()
    quantity = quantity_spinbox.get()

    # 检查收据号码是否只包含数字
    if not receipt.isdigit():
        messagebox.showerror("错误", "Receipt Number can only be in numbers")
        return

    # 在treeview中插入一行数据
    row_id += 1
    tree.insert("", "end", values=(row_id, name, receipt, item, quantity))

    # 清除输入框中的数据以便输入新的数据
    name_entry.delete(0, "end")
    receipt_entry.delete(0, "end")
    item_dropdown.set("")
    quantity_spinbox.delete(0, "end")

# 定义一个函数来删除treeview中的数据
def delete_data():
    # 获取输入框中的值
    id_to_delete = id_entry.get()

    # 遍历treeview中的所有行，找到匹配的行并删除
    for row in tree.get_children():
        if tree.item(row)["values"][0] == int(id_to_delete):
            tree.delete(row)
            break

# 创建按钮来添加数据到treeview中
add_button = tk.Button(root, text="添加数据", command=add_data)
add_button.pack(pady=10)

# 创建输入框和标签来获取要删除的行的ID
id_label = tk.Label(root, text="输入要删除的行的ID")
id_label.pack()
id_entry = tk.Entry(root)
id_entry.pack()

# 创建按钮来删除treeview中的数据
delete_button = tk.Button(root, text="删除数据", command=delete_data)
delete_button.pack(pady=10)

#创建退出按钮
exit_button = tk.Button(root, text="退出", command=root.destroy) 
exit_button.pack(pady=20)

#运行主循环
root.mainloop()