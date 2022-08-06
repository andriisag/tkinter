from cgitb import text
import tkinter as tk


def txt():
    a = text_box.get("1.0",'end-1c')
    text_box.insert(tk.END, a)




window = tk.Tk()
window.minsize(500, 200)
text_box = tk.Text()
button = tk.Button(
    text="Зберегти",
    width=20,
    height=5,
    command=txt
    )
text_box.pack()
button.pack()


window.mainloop()    
