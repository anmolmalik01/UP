import numpy as np
import cv2
import time
import math
from subprocess import call
import pyscreenshot

from hand_detection_module import handDetector


name = 0
def screenshot():
    if len(lmList) != 0:
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[12][1], lmList[12][2]

        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)

        length = distance( x1, y1, x2, y2 ) 

        global name
        if length<40:
            name+=1
            image = pyscreenshot.grab()
            image.save(str(name) + '.png' )


def distance( x1 , y1, x2, y2 ):
    d = math.sqrt( math.pow( ( x2 - x1 ), 2 ) + math.pow( ( y2 - y1 ), 2 ) )
    return d


def volume_control():

    if len(lmList) != 0:
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]

        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2),(255, 0, 255), 3)
        
        length = distance( x1, y1, x2, y2 ) 
        print(length)
        
        volume = np.interp( length, [50, 150], [0, 100] )
        call(["amixer", "-D", "pulse", "sset", "Master", str(volume)+"%"])

def epic():
    if len(lmList) != 0:
        x1, y1 = lmList[8][1], lmList[8][2]
        x2, y2 = lmList[12][1], lmList[12][2]

        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)

        length = distance( x1, y1, x2, y2 ) 
        print(length)

        if length<=20:
            cv2.circle(img, (x1, y1), 15, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (255, 0, 0), cv2.FILLED)
              

pTime = 0
cTime = 0

cap = cv2.VideoCapture(0)
detector = handDetector()


while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    
    epic()

    # fps    
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    
    # Flip the image horizontally for a selfie-view display.
    # cv2.imshow('MediaPipe Objectron', cv2.flip(img, 1))

    cv2.imshow('MediaPipe Objectron', img )

    if cv2.waitKey(5) & 0xFF == 27:
        break

    cv2.waitKey(1)


