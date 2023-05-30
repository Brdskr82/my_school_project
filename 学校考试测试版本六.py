# 导入必要的库
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import ctypes

# 设置DPI感知，使窗口大小适应屏幕
ctypes.windll.shcore.SetProcessDpiAwareness(1)

# 定义主窗口
root = tk.Tk()
root.title("Julie’s party hire store rental details") # 窗口标题

# 定义标题标签
title_label = tk.Label(root, text="Julie’s party hire store rental details", font=("Arial", 16, "bold"))
title_label.pack(pady=20) # 放置标题标签

# 定义输入框和标签的函数
def create_entry(label_text):
    frame = tk.Frame(root)
    label = tk.Label(frame, text=label_text)
    label.pack(side=tk.LEFT)
    entry = tk.Entry(frame)
    entry.pack(side=tk.RIGHT)
    frame.pack(pady=5)
    return entry

# 创建输入框和标签
name_entry = create_entry("Full Name:")
receipt_entry = create_entry("Receipt Number:")

# 定义下拉菜单和标签
item_frame = tk.Frame(root)
item_label = tk.Label(item_frame, text="Item:")
item_label.pack(side=tk.LEFT)
item_var = tk.StringVar()
item_options = ["Table", "Chair"]
item_dropdown = ttk.Combobox(item_frame, textvariable=item_var, values=item_options)
item_dropdown.pack(side=tk.RIGHT)
item_frame.pack(pady=5)

# 定义spinbox和标签
quantity_frame = tk.Frame(root)
quantity_label = tk.Label(quantity_frame, text="Quantity:")
quantity_label.pack(side=tk.LEFT)
quantity_spinbox = tk.Spinbox(quantity_frame, from_=1, to=500, wrap=True)
quantity_spinbox.pack(side=tk.RIGHT)
quantity_frame.pack(pady=5)

# 定义treeview和标题
tree_label = tk.Label(root, text="Rental details", font=("Arial", 14, "bold"))
tree_label.pack(pady=10)
tree_columns = ("ID", "Name", "Receipt Number", "Item", "Quantity")
tree = ttk.Treeview(root, columns=tree_columns, show="headings")
for col in tree_columns:
    tree.heading(col, text=col)
tree.pack()

# 定义添加数据的函数
id_counter = 1 # 计数器，用于分配ID
def add_data():
    global id_counter
    name = name_entry.get()
    receipt_number = receipt_entry.get()
    item = item_var.get()
    quantity = quantity_spinbox.get()

    # 检查收据号码是否只包含数字
    if not receipt_number.isdigit():
        messagebox.showerror("Error", "Receipt Number can only be in numbers")
        return

    # 在treeview中插入数据
    tree.insert("", "end", values=(id_counter, name, receipt_number, item, quantity))
    id_counter += 1

# 定义删除数据的函数
def delete_data():
    selected_items = tree.selection()
    for item in selected_items:
        tree.delete(item)

# 定义按钮
button_frame = tk.Frame(root)
add_button = tk.Button(button_frame, text="Add Data", command=add_data)
add_button.pack(side=tk.LEFT, padx=5)
delete_button = tk.Button(button_frame, text="Delete Data", command=delete_data)
delete_button.pack(side=tk.RIGHT, padx=5)
button_frame.pack(pady=10)

# 定义退出按钮
exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack(pady=10)

root.mainloop()
