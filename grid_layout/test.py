from Tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure





root = Tk()
root.geometry('1000x700')

f = Figure(figsize=(4,4), dpi=50)
axis = f.add_subplot(111)
canvas = FigureCanvasTkAgg(f, master=root)
canvas.get_tk_widget().place(x=10,y=30)
root.mainloop()

