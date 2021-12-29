import tkinter as tk
from tkinter.ttk import *
from estadobarba import *
    
root = tk.Tk()
root.geometry ('250x100')
frame = tk.Frame(root)
frame.pack()

barba = tk.Button(frame,
                   text="Barba",
                   command=estado_barba)
barba.pack(side=tk.LEFT)
button = tk.Button(frame, 
                   text="Salir", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)

root.mainloop()
