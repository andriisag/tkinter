import mysql.connector
import tkinter as tk

connection = mysql.connector.connect(host="localhost",
                                         database="test",
                                         user="root",
                                         password="root")

def bd():
    a = entry.get()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM entry WHERE id = %s", (a, ))
    result = cursor.fetchone()
    if result:
        label.config(text = result)
    else:
        label.config(text = "Користувача не існує")

    connection.commit()        
    


window = tk.Tk()
window.minsize(500, 200)

label = tk.Label(
    text="Введи id",
)

entry = tk.Entry()

button = tk.Button(
    text="Зберегти",
    width=20,
    height=5,
    command=bd
    )

label.pack()
entry.pack()
button.pack()


window.mainloop()    







