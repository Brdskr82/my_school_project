# final assessment

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import ctypes

#设置DPI感知，使窗口大小适应屏幕分辨率
ctypes.windll.shcore.SetProcessDpiAwareness(1)

root = tk.Tk()
root.title("Julie's party hire store rental details")

#创建标题标签并居中显示
title_label = tk.Label(root, text="Julie's party hire store rental details", font=("Arial", 16, "bold"))
title_label.pack(pady=20)

#创建输入框和标签来记录客户姓名
name_frame = tk.Frame(root)
name_frame.pack(pady=5)
name_label = tk.Label(name_frame, text="客户姓名")
name_label.pack(side=tk.LEFT)
name_entry = tk.Entry(name_frame)
name_entry.pack(side=tk.LEFT)

#创建输入框和标签来记录收据号码
receipt_frame = tk.Frame(root)
receipt_frame.pack(pady=5)
receipt_label = tk.Label(receipt_frame, text="收据号码")
receipt_label.pack(side=tk.LEFT)
receipt_entry = tk.Entry(receipt_frame)
receipt_entry.pack(side=tk.LEFT)

#创建下拉菜单和标签来记录租用物品
item_frame = tk.Frame(root)
item_frame.pack(pady=5)
item_label = tk.Label(item_frame, text="租用物品")
item_label.pack(side=tk.LEFT)
item_var = tk.StringVar()
item_options = ["Table", "Chair"]
item_dropdown = ttk.Combobox(item_frame, textvariable=item_var, values=item_options)
item_dropdown.pack(side=tk.LEFT)

#创建spinbox和标签来记录租用数量
quantity_frame = tk.Frame(root)
quantity_frame.pack(pady=5)
quantity_label = tk.Label(quantity_frame, text="租用数量")
quantity_label.pack(side=tk.LEFT)
quantity_spinbox = tk.Spinbox(quantity_frame, from_=1, to=500, wrap=True)
quantity_spinbox.pack(side=tk.LEFT)

#跟踪treeview中的行数
row_id = 0

#定义一个function来添加数据到treeview中
def add_data():
    global row_id
   
    name = name_entry.get()
    receipt = receipt_entry.get()
    item = item_var.get()
    quantity = quantity_spinbox.get()


    #检查收据号码是否只包含数字
    if not receipt.isdigit():
        messagebox.showerror("错误", "Receipt Number can only be in numbers")
        return

    #检查租用数量是否只包含数字
    if not quantity.isdigit():
        messagebox.showerror("错误", "租用数量只能是数字")
        return

    #检查租用数量是否超过500
    if int(quantity) > 500:
        messagebox.showerror("错误", "The quantity cannot be greater than 500")
        return


 #在treeview中插入一行数据
    row_id += 1
    tree.insert("", "end", values=(row_id, name, receipt, item, quantity))

 #清除输入框中的数据以便输入新的数据
    name_entry.delete(0, "end")
    receipt_entry.delete(0, "end")
    item_dropdown.set("")
    quantity_spinbox.delete(0, "end")


#定义一个function来删除treeview中的数据
def delete_data():
 #获取输入框中的值
    id_to_delete = id_entry.get()

 #查询treeview找到匹配的行并删除
    for row in tree.get_children():
        if tree.item(row)["values"][0] == int(id_to_delete):
            tree.delete(row)
            break

 #更新剩余行的ID
    for i,row in enumerate(tree.get_children()):
        tree.set(row,"ID",i+1)

#创建按钮来添加数据到treeview中
add_button = tk.Button(root, text="添加数据", command=add_data)
add_button.pack(pady=10)

#创建输入框和标签来获取要删除的行的ID
id_frame = tk.Frame(root) 
id_frame.pack(pady=5) 
id_label = tk.Label(id_frame, text="输入要删除的行的ID") 
id_label.pack(side=tk.LEFT) 
id_entry = tk.Entry(id_frame) 
id_entry.pack(side=tk.LEFT)

#创建按钮来删除treeview中的数据
delete_button = tk.Button(root, text="删除数据", command=delete_data) 
delete_button.pack(pady=10)

#创建退出按钮
exit_button = tk.Button(root, text="退出", command=root.destroy) 
exit_button.pack(pady=20)

#创建treeview来显示租赁详情
tree_label = tk.Label(root, text="Rental details", font=("Arial", 12, "bold"))
tree_label.pack(pady=10)
tree = ttk.Treeview(root, columns=("ID", "Name", "Receipt", "Item", "Quantity"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Name", text="客户姓名")
tree.heading("Receipt", text="收据号码")
tree.heading("Item", text="租用物品")
tree.heading("Quantity", text="租用数量")
tree.pack()


root.mainloop()