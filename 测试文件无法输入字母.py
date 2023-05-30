import tkinter as tk

def validate(new_value):
    # 如果新值为空或只包含数字，则允许更改
    if new_value == "" or new_value.isdigit():
        return True
    else:
        return False

root = tk.Tk()

# 注册验证命令
vcmd = (root.register(validate), '%P')

# 创建一个 Spinbox 控件并指定验证命令
spinbox = tk.Spinbox(root, from_=1, to=500, wrap=True, validate='key', validatecommand=vcmd)
spinbox.pack()

root.mainloop()