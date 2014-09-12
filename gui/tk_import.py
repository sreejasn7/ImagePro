from tkintertable.Tables import TableCanvas
from tkintertable.TableModels import TableModel
from Tkinter import *
master = Tk()
tframe = Frame(master)
tframe.pack()
model = TableModel()
table = TableCanvas(tframe, model=model)

#model = table.model
#model.addColumn('col1')
#model.addColumn('col2')
#model.addColumn()
data = { '1' : {'col1': 99.88, 'col2': 108.79 }, '2' : {'col1': 99.88, 'col2': 108.79}}

model.importDict(data)
table.createTableFrame()

#table.pack()
master.mainloop()
