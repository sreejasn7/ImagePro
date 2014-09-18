from Tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

master = Tk()
frame = Frame()
#frame.rowconfigure( 6, weight = 1 )
#frame.columnconfigure( 4, weight = 1 )
frame.grid()


f1 = Figure(figsize=(4,4), dpi=50)
#axis = f1.add_subplot(111)
canvas = FigureCanvasTkAgg(f1, master=master)
canvas.get_tk_widget().grid(row=0,columnspan=2)

f2 = Figure(figsize=(4,4),dpi = 50)
canvas = FigureCanvasTkAgg(f2,master=master)
canvas.get_tk_widget().grid(row=0,column=2,columnspan=2)

lb1 = Label(master,text = 'Coeffcient')
lb1.grid(row=2,sticky=S)
e1 = Entry(master)
e1.grid(row=3,sticky=N)

f3= Figure(figsize=(4,4),dpi = 50)
canvas = FigureCanvasTkAgg(f3,master=master)
canvas.get_tk_widget().grid(row=1,rowspan = 6,column=2,columnspan=2)

master.mainloop()

