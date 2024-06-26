import cv2 as cv
import pyautogui
import time as time
import handtrackmodule as htm
import numpy as np
import math
import alsaaudio
########################################################
wCam, hCam = 640,480
########################################################
cap = cv.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
detector = htm.handDetector(detectionCon=0.6)
pTime = 0
cTime = 0
mixer = alsaaudio.Mixer()
mixer.setmute(1)
mute = True
while True:
    success, img = cap.read()
    
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    flipped = cv.flip(img,1)
    #cv.putText(flipped, str(int(fps)), (40,70), cv.FONT_HERSHEY_COMPLEX, 1, (250,250,0),2)
    flipped = detector.findHands(flipped,draw=False)
    lmList = detector.findPositions(flipped,draw=False)
    if len(lmList)!=0:
        x1,y1 = lmList[4][1], lmList[4][2]
        x2,y2 = lmList[8][1], lmList[8][2]
        cx,cy = (x1+x2)//2, (y1+y2)//2
        #cv.circle(flipped, (x1,y1), 10, (255,255,0), -1)
        #cv.circle(flipped, (cx,cy), 10, (255,255,0), -1)
        #cv.circle(flipped, (x2,y2), 10, (255,255,0), -1)
        #cv.line(flipped, (x1,y1), (x2,y2), (190,200,0), 3)
        length = math.hypot(x2-x1, y2-y1)
        n = 0
        fin = 0
        if length<50:
            if mute:
                #cv.circle(flipped, (cx,cy), 10, (0,0,255), -1)
                mixer.setmute(0)
                mute = False
                print("Unmuted")
                continue
            if not mute:
                #cv.circle(flipped, (cx,cy), 10, (0,255,0), -1)
                mixer.setmute(1)
                mute = True
                print("Muted")
                continue
            fin = time.now()
        duration = (fin-n)
        print(duration)
    #cv.imshow("Footage",flipped)
    cv.waitKey(1)


