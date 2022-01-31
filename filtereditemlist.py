import tkinter as tk
from record import record_display as rd


class filtered_table(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        
    
    def roll(self, data, activetags):
        for widget in self.winfo_children():
            widget.destroy()
        current_table = []
        for key, value in data.items():
            for t in value[0]["Tags"]:
                if value[0]["Tags"][t] and value[0]["Tags"][t] == activetags[t]:
                    current_table.append(key)
                    continue
        x, y = 0, 0
        for f in current_table:
            l = tk.Label(self, text=f)
            l.bind("<Button-1>", lambda event:rd.record_display(event.widget.cget("text"), data))
            l.grid(row=y, column=x, sticky="ew")
            if x < 4:
                x+=1
            else:
                y+=1
                x=0


