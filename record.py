import tkinter as tk
from tkinter import *
from style import colors
import pyperclip
from tag_grid import tag_grid



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
        self.item_info_frame = Frame(top_frame)
        self.item_info_frame.grid(row=0, column=0, sticky="n")

        def label_to_clipboard(event):
            pyperclip.copy(event.widget.cget("text"))

        mainlabel = tk.Label(self.item_info_frame, text=choice, justify='center', font=("Arial", 25))
        mainlabel.grid(row=0, column=0, columnspan=3, sticky='ew')
        mainlabel.bind("<Button-1>", lambda event:label_to_clipboard(event))


        x, y = 0, 2
        width = 40
        text_items = []
        for key, value in chosen.items():
            if key == "Tags":
                l = tk.Label(self.item_info_frame, text=key)
                l.grid(row=y, column=x)
                tg = tag_grid(self.item_info_frame, data, column_max=10, editable=False, chosen=chosen)
                tg.grid(row = y, column=x+1,)
                y += 1
            else:
                print(str(key) + " " + str(value))
                l = tk.Label(self.item_info_frame, text=key)
                l.grid(row = y, column = x)
                height = min(10, len(str(value)) // width + 1)
                t = tk.Text(self.item_info_frame, height=height, width=width)
                t.insert("1.0", value)
                t.config(state="disabled")
                text_items.append(t)
                t.grid(row=y, column = x+1)
                y += 1

        def edit_update(event):
            items = self.item_info_frame.grid_slaves()
            if not self.editable:
                self.editable = True
                event.widget.config(text="Update")
                for t in text_items:
                    t.config(state="normal")
                tg.set_editable(True)
            else:
                self.editable = False
                for t in text_items:
                    t.config(state="disabled")
                tg.set_editable(True)
                event.widget.config(text="Edit")
                record_display.save_record(data, items, tg.get_tags())
        update_button = tk.Button(top_frame, text="Edit")
        update_button.grid(row=1, column=0, columnspan=2, sticky="e",ipadx=40, ipady=10)
        update_button.bind("<Button-1>", lambda event:edit_update(event))


        cancel_button = tk.Button(top_frame, text="Cancel")
        cancel_button.grid(row=1, column=2, columnspan=2, sticky="w",ipadx=40, ipady=10)
        cancel_button.bind("<Button-1>", lambda event:self.destroy())

    def save_record(data, items, tags):
            i=0
            major_key = items[16].cget("text")
            data[major_key][0]["Tags"] = tags
            while i < (len(items)-1):
                minor_key, minor_value = False, False
                if str(type(items[i+1])) == "<class 'tkinter.Label'>":
                    minor_key = items[i+1].cget("text")
                if str(type(items[i])) == "<class 'tkinter.Text'>":
                    minor_value = items[i].get("1.0", END)
                if minor_key and minor_value:
                    data[major_key][0][minor_key] = minor_value
                i+=2