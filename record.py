import dataclasses
import json
import tkinter as tk
from tkinter import *
import random
from style import colors


class RecordDisplay:

    def frame_grid(parent, list):
        x, y = 0, 0
        f = tk.Frame(parent)
        for t in list:
            tl = tk.Label(f, text=str(t[0]), bg=colors["no_red"], fg="black")
            if t[1]:
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
        top_frame.grid(row=0, column=0)
        bot_frame = Frame(window)
        bot_frame.grid(row=1, column=0)

        mainlabel = tk.Label(top_frame, text=choice, justify='center', font=("Arial", 25))
        mainlabel.grid(row=0, column=0, rowspan=2, sticky='ew')

        x, y = 0, 2
        width = 40
        


        for key, value in chosen.items():
            if key == "Tags":
                l = tk.Label(top_frame, text=key)
                f = RecordDisplay.frame_grid(top_frame, value)

            else:
                print(str(key) + " " + str(value))
                l = tk.Label(top_frame, text=key)
                l.grid(row = y, column = x)
                height = min(10, len(str(value)) // width + 1)
                t = tk.Text(top_frame, height=height, width=width)
                t.insert("1.0", value)
                t.grid(row=y, column = x+1)
                y += 1
                """if y > 6:
                    y = 0
                    x+=2"""

        window.mainloop()
        return RecordDisplay

