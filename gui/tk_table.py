from tkintertable.Tables import TableCanvas
from tkintertable.TableModels import TableModel
from Tkinter import *
master = Tk()
tframe = Frame(master)
tframe.pack()
model = TableModel()

model.addColumn('c1')
model.addColumn('c2')
model.addRow('1')
model.addRow('2')
row= 1
column = 1
table = TableCanvas(tframe,model=model)
table.model.data['1']['c1']= 10  
table.createTableFrame()

#table.pack()
master.mainloop()
