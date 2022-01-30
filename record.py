import tkinter as tk
from tkinter import *
from style import colors

editable = False
parent = "null"
class RecordDisplay:

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

    def record_display(choice, data):
        chosen = data[choice][0]
        global colors

        window = tk.Tk()
        window.title("Record: " + choice)
        top_frame = Frame(window)
        top_frame.grid(row=0, column=0, sticky="n")
        item_info_frame = Frame(top_frame)
        item_info_frame.grid(row=0, column=0, sticky="n")


        mainlabel = tk.Label(item_info_frame, text=choice, justify='center', font=("Arial", 25))
        mainlabel.grid(row=0, column=0, columnspan=3, sticky='ew')

        x, y = 0, 2
        width = 40
        


        for key, value in chosen.items():
            if key == "Tags":
                l = tk.Label(item_info_frame, text=key)
                l.grid(row=y, column=x)
                f = RecordDisplay.frame_grid(item_info_frame, value)
                f.grid(row=y, column=x+1)
                y += 1
            else:
                print(str(key) + " " + str(value))
                l = tk.Label(item_info_frame, text=key)
                l.grid(row = y, column = x)
                height = min(10, len(str(value)) // width + 1)
                t = tk.Text(item_info_frame, height=height, width=width)
                t.insert("1.0", value)
                t.grid(row=y, column = x+1)
                y += 1

        def edit_update(event):
            global editable
            if not editable:
                editable = True
                event.widget.config(text="Update")
            else:
                editable = False
                event.widget.config(text="Edit")
                i=0
                items = item_info_frame.grid_slaves()
                major_key = items[16].cget("text")
                while i < (len(items)-1):
                    minor_key = items[i+1].cget("text")
                    minor_value = items[i].get("1.0", END)
                    data[major_key][minor_key] = minor_value
                    i+=2
                """ for item in item_info_frame.grid_slaves():
                    #print(type(item))
                    if str(type(item)) == "<class 'tkinter.Text'>":
                        print(str(i) + " " + item.get("1.0", END))
                    elif str(type(item)) == "<class 'tkinter.Label'>":
                        print(str(i) + " " + item.cget("text"))
                    else:
                        print("other")
                    i+=1"""
        update_button = tk.Button(top_frame, text="Edit")
        update_button.grid(row=1, column=0, columnspan=2, sticky="e",ipadx=40, ipady=10)
        update_button.bind("<Button-1>", lambda event:edit_update(event))
        cancel_button = tk.Button(top_frame, text="Cancel")
        cancel_button.grid(row=1, column=2, columnspan=2, sticky="w",ipadx=40, ipady=10)


        window.mainloop()
        return RecordDisplay

