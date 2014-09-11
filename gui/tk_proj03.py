import cv2
from RepeatedTimer import RepeatedTimer
from Tkinter import *
import pylab
import numpy
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

#================================Functions==================================================
def video():

    global Gray_1
    ret, frame = cap.read()
    axis.imshow(frame)
    canvas.show()

    Gray_2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    Difference = abs(Gray_2 - Gray_1)
    Mean_value = numpy.mean(Difference)
    print Mean_value
    Gray_1 = Gray_2
    Values.append(Mean_value)
    Values.remove(Values[0])
    Plot[0].set_data(X_Axis, pylab.array(Values))
    canvas2.show()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        exit()


def video_start():
    t.start()

def video_stop():
    t.stop()
#================================Functions==================================================

#================================Main Program===============================================
cap = cv2.VideoCapture(0)
Gray_1 = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2GRAY)
t = RepeatedTimer(0,video)
Values = [0 for x in range(100)]
#===========================================================================================

#=================================GUI Section=============================================
root = Tk()
root.geometry('1000x700')

#frame1 = Frame(root)
#frame1.pack(side=LEFT)
f = Figure(figsize=(4,4), dpi=50)
axis = f.add_subplot(111)
canvas = FigureCanvasTkAgg(f, master=root)
canvas.get_tk_widget().place(x=10,y=30)
#frame2 = Frame(root)
#frame2.pack(side=RIGHT)
X_Axis = pylab.arange(0, 100, 1)
#Y_Axis = pylab.array([0]*100)
plotFigure = Figure(figsize=(4,4),dpi=50)
axis2 = plotFigure.add_subplot(111)
axis2.grid(True)
axis2.set_title("Mean value per Frame")
axis2.axis([0, 100, 0, 255])
Plot = axis2.plot(X_Axis, [0]*100, 'o-', color='r', markersize=6)

#axis2.set_xlabel("Frame")
#axis2.set_ylabel("Mean value")
canvas2 = FigureCanvasTkAgg(plotFigure, master=root)
canvas2.get_tk_widget().place(x=500,y=30)

b1 = Button(root,text="Start", bg='white', command=video_start).place(x=50,y=600)
b2 = Button(root,text="Stop", bg='white', command=video_stop).place(x=400,y=600)
root.mainloop()
#===========================================================================================