import repeated_timer
import cv2
from repeated_timer import repeatedTimer

cap = cv2.VideoCapture(0)

def video():
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        exit()

t = repeatedTimer(0,video)
t.start()
# When everything done, release the capture
#cap.release()
#cv2.destroyAllWindows()
for i in range(0,(10**7)+1):
    if i == 10**7:
        #cap.release()
        #cv2.destroyAllWindows()
        t.stop()

