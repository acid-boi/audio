import cv2 as cv
import mediapipe as mp
import time
mpHands = mp.solutions.hands
class handDetector():
    def __init__(self, mode=False, maxHands=2, complexity = 1, detectionCon=0.5,trackCon=0.5):
        self.mode=mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.complexity = complexity
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands, self.complexity , self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils


    def findHands(self,img,draw=True):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img




    def findPositions(self, img, handNo=0, draw=True):
        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id,lm in enumerate(myHand.landmark):
                h,w = img.shape[:2]
                cx,cy = int(lm.x*w), int(lm.y*h)
                if draw:
                    cv.circle(img,(cx,cy),15,(255,255,0), -1)
                lmList.append([id,cx,cy])

        return lmList




def main():
    pTime = 0
    cTime = 0
    cap = cv.VideoCapture(0)
    detector = handDetector()
    while True:
        success, img = cap.read()
        flipped = cv.flip(img,1)
        flipped = detector.findHands(flipped)
        lmList = detector.findPositions(flipped)
        if len(lmList) != 0:
            print(lmList[4])






        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv.putText(flipped, str(int(fps)), (10,70), cv.FONT_HERSHEY_COMPLEX,2, (255,0,255), 3)
        cv.imshow("Cam", flipped)
        cv.waitKey(1)






if __name__ == "__main__":
    main()

