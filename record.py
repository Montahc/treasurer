import tkinter as tk
from tkinter import *
from style import colors


class record_display(tk.Tk):

    def __init__(self, choice, data):
        tk.Tk.__init__(self)
        self.setup(choice, data)
        self.editable = False
        self.parent = "null"

    def get_info_widgets(self):
        return self.item_info_frame.grid_slaves()

    def setup(self, choice, data):
        chosen = data[choice][0]
        global colors

        self.title("Record: " + choice)
        top_frame = Frame(self)
        top_frame.grid(row=0, column=0, sticky="n")
        item_info_frame = Frame(top_frame)
        item_info_frame.grid(row=0, column=0, sticky="n")




        mainlabel = tk.Label(item_info_frame, text=choice, justify='center', font=("Arial", 25))
        mainlabel.grid(row=0, column=0, columnspan=3, sticky='ew')

        def frame_grid(parent, list):        
                    x, y = 0, 0
                    f = tk.Frame(parent)
                    #t is a list in format "TAG":"TRUE/FALSE"
                    for t in list:
                        tl = tk.Label(f, text=str(t), bg=colors["no_red"], fg="black")
                        if list[t]:
                            tl.config(bg=colors["ashley_green"])
                        tl.grid(row=y, column=x, sticky="ew")
                        if x < 4:
                            x+=1
                        else:
                            y+=1
                            x=0
                    return f

        x, y = 0, 2
        width = 40
        text_items = []
        for key, value in chosen.items():
            if key == "Tags":
                l = tk.Label(item_info_frame, text=key)
                l.grid(row=y, column=x)
                f = frame_grid(item_info_frame, value)
                f.grid(row=y, column=x+1)
                y += 1
            else:
                print(str(key) + " " + str(value))
                l = tk.Label(item_info_frame, text=key)
                l.grid(row = y, column = x)
                height = min(10, len(str(value)) // width + 1)
                t = tk.Text(item_info_frame, height=height, width=width)
                t.insert("1.0", value)
                t.config(state="disabled")
                text_items.append(t)
                t.grid(row=y, column = x+1)
                y += 1

        def edit_update(event):
            items = item_info_frame.grid_slaves()
            if not self.editable:
                self.editable = True
                event.widget.config(text="Update")
                for t in text_items:
                    t.config(state="normal")
            else:
                self.editable = False
                for t in text_items:
                    t.config(state="disabled")
                event.widget.config(text="Edit")
                record_display.save_record(data, items)
        update_button = tk.Button(top_frame, text="Edit")
        update_button.grid(row=1, column=0, columnspan=2, sticky="e",ipadx=40, ipady=10)
        update_button.bind("<Button-1>", lambda event:edit_update(event))


        cancel_button = tk.Button(top_frame, text="Cancel")
        cancel_button.grid(row=1, column=2, columnspan=2, sticky="w",ipadx=40, ipady=10)
        cancel_button.bind("<Button-1>", lambda event:self.destroy())

    def save_record(data, items):
            i=0
            major_key = items[16].cget("text")
            while i < (len(items)-1):
                minor_key, minor_value = False, False
                if str(type(items[i+1])) == "<class 'tkinter.Label'>":
                    minor_key = items[i+1].cget("text")
                if str(type(items[i])) == "<class 'tkinter.Text'>":
                    minor_value = items[i].get("1.0", END)
                if minor_key and minor_value:
                    print(str(data[major_key]) + " : " + minor_key + " : " + minor_value)
                    data[major_key][0][minor_key] = minor_value
                i+=2