import cv2 as cv
import mediapipe as mp
import time
class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5,trackCon=0.5):
        self.mode=mode

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
    imgRGB = cv.cvtColor(flipped, cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(flipped, handLms, mpHands.HAND_CONNECTIONS)
            for id, lm in enumerate(handLms.landmark):
                #print(id,lm)
                h,w = img.shape[:2]
                cx, cy = int(lm.x*w), int(lm.y*h)

def main():
pTime = 0
cTime = 0
while True:
    success, img = cap.read()
    flipped = cv.flip(img,1)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv.putText(flipped, str(int(fps)), (10,70), cv.FONT_HERSHEY_COMPLEX,2, (255,0,255), 3)
    cv.imshow("Cam", flipped)
    cv.waitKey(1)






if __name__ = "__main":
    main()

