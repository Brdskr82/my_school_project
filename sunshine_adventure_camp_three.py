import tkinter as tk
import datetime as dt
from tkinter import ttk
from tkinter import messagebox
from ctypes import windll

# Constants
groups = []
min_campers = 5
max_campers = 10
weather_conditions = ['Sunny', 'Cloudy', 'Windy', 'Rainy', 'Stormy']

# Function to add or update group details in list
def add_to_list():
    # Retrieve input values
    group_leader_name = group_leader_name_entry.get().strip().title()
    group_location = group_location_entry.get().strip()
    weather_condition = weather_condition_combobox.get().strip()
    no_campers = int(current_value.get())
    moving_on = moving_on_var.get()
    time = dt.datetime.now()

    # Input Validation
    if not group_leader_name:
        messagebox.showerror('Error', 'Please enter Group Leader Name')
        return
    elif not group_location:
        messagebox.showerror('Error', 'Please enter Group Location')
        return
    elif not weather_condition:
        messagebox.showerror('Error', 'Please enter Current Weather Condition')
        return
    elif any(i.isdigit() for i in group_leader_name):
        messagebox.showerror('Error', 'Please enter valid Group Leader Name')
        return
    elif group_location.isdigit():
        messagebox.showerror('Error', 'Please enter valid Current Weather Condition')
        return
    
    # Check if group leader already exists in the list
    elif any(group_leader_name in sl for sl in groups) == True:
        if moving_on == False:
            for i, (name, location, campers, weather) in enumerate(groups):
                # Update group details if not moving on
                if name == group_leader_name:
                    groups[i] = [group_leader_name, group_location, no_campers, weather_condition]
                    update_details()
                    break
        # Delete group details if moving on
        else:
            for i, (name, location, campers, weather) in enumerate(groups):
                if name == group_leader_name:
                    del groups[i] 
                    update_details()
                    break
    # Otherwise add new group details
    else:
        groups.append([group_leader_name, group_location, no_campers, weather_condition])
        update_details()

# Function to update the treeview with current group details
def update_details():
    time = dt.datetime.now()
    # Clear the treeview
    for row in treeview.get_children():
        treeview.delete(row)
    # Insert current group details
    for i, (name, location, campers, weather) in enumerate(groups):
        treeview.insert('', 'end', text=f'Group {i+1}', values=(f'{time:%H:%M %p}', name, location, campers, weather))

# GUI Code
windll.shcore.SetProcessDpiAwareness(1)

window = tk.Tk()
window.title('Sunshine Adventure Camp Group Manager')

padx = (0, 10)
pady = (0, 10)

frame = tk.Frame(window, padx = 10, pady = 10)
frame.pack(expand = True, fill = 'both')

title = ttk.Label(frame, text = 'Sunshine Adventure Camp Group Manager', font = 'Helvetica 10 bold')
title.grid(row = 0, columnspan = 2, pady = pady)

group_leader_name_label = ttk.Label(frame, text = 'Group Leader Name:')
group_leader_name_label.grid(row = 1, column = 0, pady = pady, padx = padx, sticky = tk.E)

group_leader_name_entry = ttk.Entry(frame)
group_leader_name_entry.grid(row = 1, column = 1, pady = pady, sticky = tk.W)

group_location_label = ttk.Label(frame, text = 'Group Location:')
group_location_label.grid(row = 2, column = 0, pady = pady, padx = padx, sticky = tk.E)

group_location_entry = ttk.Entry(frame)
group_location_entry.grid(row = 2, column = 1, pady = pady, sticky = tk.W)

no_campers_label = ttk.Label(frame, text = 'Number of Campers:')
no_campers_label.grid(row = 3, column = 0, pady = pady, padx = padx, sticky = tk.E)

current_value = tk.StringVar(value = 5) 
no_campers_spinbox = ttk.Spinbox(frame, from_ = min_campers, to = max_campers, state = 'readonly', textvariable = current_value, wrap = True, width = 15)
no_campers_spinbox.grid(row = 3, column = 1, pady = pady, sticky = tk.W)

weather_condition_label = ttk.Label(frame, text = 'Current Weather Condition:')
weather_condition_label.grid(row = 4, column = 0, pady = pady, padx = padx, sticky = tk.E)

weather_condition_combobox = ttk.Combobox(frame, values = weather_conditions, state = 'readonly', width = 14)
weather_condition_combobox.current(0)
weather_condition_combobox.grid(row = 4, column = 1, pady = pady, sticky = tk.W)

moving_on_label = ttk.Label(frame, text = 'Moving On?')
moving_on_label.grid(row = 5, column = 0, padx = 30, sticky = tk.E)

moving_on_var = tk.BooleanVar()

moving_on_checkbutton = ttk.Checkbutton(frame, variable = moving_on_var, onvalue = True, offvalue = False)
moving_on_checkbutton.grid(row = 5, column = 0, sticky = tk.E)

enter_button = ttk.Button(frame, text = 'Enter', command = add_to_list, width = 20)
enter_button.grid(row = 5, column = 1, sticky = tk.W)

details_label = ttk.Label(frame, text = 'Group Details', font = 'Helvetica 10 bold')
details_label.grid(row = 6, columnspan = 2, pady = (20, 0))

columns = ('Updated', 'Group Leader', 'Location', 'Campers', 'Weather')
treeview = ttk.Treeview(frame, columns = columns, show = 'headings')

for col in columns:
    treeview.heading(col, text = col)

treeview.grid(row = 7, column = 0, columnspan = 2)

window.mainloop()


