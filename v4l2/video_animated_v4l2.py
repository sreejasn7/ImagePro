import Image
import select
import v4l2capture
from matplotlib import pyplot as plt
import numpy
import cv2
from matplotlib import animation


# Open the video device.
video = v4l2capture.Video_device("/dev/video0")

size_x, size_y = video.set_format(1280, 1024)

# Create a buffer to store image data in. This must be done before
# calling 'start' if v4l2capture is compiled with libv4l2. Otherwise
# raises IOError.
video.create_buffers(1)

# Send the buffer to the device. Some devices require this to be done
# before calling 'start'.
video.queue_all_buffers()

# Start the device. This lights the LED if it's a camera that has one.
video.start()

# Wait for the device to fill the buffer.
select.select((video,), (), ())
# The rest is easy :-)
fig = plt.figure()
nx = 1280
ny = 1500
data = numpy.zeros((nx,ny))
im = plt.imshow(data,vmin=0, vmax = 1)

def init():
    im.set_data(numpy.zeros((nx,ny)))

def animate(i):
	image_data = video.read_and_queue()
	image = Image.fromstring("RGB",(size_x,size_y),image_data)
	imageNumpy = numpy.asarray(image)
	im.set_data(imageNumpy)
	return im
	
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=nx * ny,
                               interval=50)	
plt.show()
video.close()
