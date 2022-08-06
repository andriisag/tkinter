import mysql.connector
import tkinter as tk

connection = mysql.connector.connect(host="localhost",
                                         database="test",
                                         user="root",
                                         password="root")

def bd():
    a = entry1.get()
    b = entry2.get()
    c = entry3.get()
    cursor = connection.cursor()

    sql = "INSERT INTO entry (entry1, entry2, entry3) VALUES (%s, %s, %s)"
    val = (a, b, c)
    cursor.execute(sql, val)    

    connection.commit()
    
window = tk.Tk()

window.minsize(500, 200)
entry1 = tk.Entry()
entry2 = tk.Entry()
entry3 = tk.Entry()
a = entry1.get()
b = entry2.get()
c = entry3.get()

button = tk.Button(
    text="Зберегти",
    width=20,
    height=5,
    command=bd
    )

entry1.pack()
entry2.pack()
entry3.pack()
button.pack()


window.mainloop()


