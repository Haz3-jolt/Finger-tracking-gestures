import cv2
import time
import HandTrackingModule as htm

wCam, hCam = 1920, 1080
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
frame = cap.read()
pTime = 0

detector = htm.handDetector(detectionCon=1)

Player1 = []

while True:
    
    success, img = cap.read()
    img = detector.findHands(img)
    lmlist = detector.findPosition(img, handNo=0, draw=False)

    if len(lmlist) != 0:
        Player1 = []

        #Thumb 
        if lmlist[4][1] > lmlist[3][1]:
            Player1.append('1')
        else:
            Player1.append('0')

        #Index 
        if lmlist[8][2] < lmlist[6][2]:
            Player1.append('1')
        else:
            Player1.append('0')

        #Middle
        if lmlist[12][2] < lmlist[10][2]:
            Player1.append('1')
        else:
            Player1.append('0')
        
        #Ring
        if lmlist[16][2] < lmlist[14][2]:
            Player1.append('1')
        else:
            Player1.append('0')

        #Pinkie
        if lmlist[20][2] < lmlist[18][2]:
            Player1.append('1')
        else:
            Player1.append('0')        

        #Example command Thumb, pointer and Pinkie are extended here
        if lmlist[4][1] > lmlist[3][1] and lmlist[8][2] < lmlist[6][2] and lmlist[12][2] > lmlist[10][2] and lmlist[16][2] > lmlist[14][2] and lmlist[20][2] < lmlist[18][2]:
            Player1.append('code')
                                    #Add any additional commands to be executed over here




        print('Player1', Player1)
    

    
        
    
    cTime = time.time()
    fps = 1 / (cTime-pTime)
    pTime = cTime

    # Shows the FPS of the program
    cv2.putText(img, f'FPS: {int(fps)}',(400,70), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)


