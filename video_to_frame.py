

'''
Using OpenCV takes a mp4 video and produces a number of images.

Requirements
----
You require OpenCV 3.2 to be installed.

Run
----
Edit the path of data in cv2.videoCapture()

save
----
The images will be saved in Data folder in the same directory where your videos are stored. 

'''
import cv2

import os

# Playing video from file:
cap = cv2.VideoCapture('/home/ashwini12/Downloads/VID-20180325-WA0002.mp4')
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(length)
currentFrame = 0

while(currentFrame<=(length)):
     ret, frame = cap.read()
     #if(currentFrame%30==0):
         
     # Capture frame-by-frame
     ret, frame = cap.read()
     # Saves image of the current frame in jpg file
     name = './data/2/frame'+'23'+'_' + str(currentFrame) + '.jpg'
     print ('Creating...' + name)
     resize = cv2.resize(frame, (640, 360))
     cv2.imwrite(name, resize)
     currentFrame += 30
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
