# import the necessary packages
import picamera
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
stream = camera.capture_continuous(rawCapture,format="bgr", use_video_port=True)

# capture frames from the camera
for frame in stream:
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array

    # show the frame
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF
    
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
   
    
    # if the `q` key was pressed, break from the loop and close display window
    if key == ord("q"):
        cv2.destroyAllWindows()
        break
