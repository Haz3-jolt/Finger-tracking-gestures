import cv2
import time
import HandTrackingModule as htm
import pyttsx3
import datetime
import itin 

wCam, hCam = 1920, 1080
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
frame = cap.read()
pTime = 0

detector = htm.handDetector(detectionCon=1)

Player1 = []
lights_on = False

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

while True:
    
    success, img = cap.read()
    img = detector.findHands(img)
    lmlist = detector.findPosition(img, handNo=0, draw=False)

    if len(lmlist) != 0:
        Player1 = []

        # Thumb Finger 
        if lmlist[4][1] > lmlist[3][1]:
            Player1.append('1')
        else:
            Player1.append('0')

        # Index FInger 
        if lmlist[8][2] < lmlist[6][2]:
            Player1.append('1')
        else:
            Player1.append('0')

        # Middle
        if lmlist[12][2] < lmlist[10][2]:
            Player1.append('1')
        else:
            Player1.append('0')
        
        # Ring
        if lmlist[16][2] < lmlist[14][2]:
            Player1.append('1')
        else:
            Player1.append('0')

        # Pinkie
        if lmlist[20][2] < lmlist[18][2]:
            Player1.append('1')
        else:
            Player1.append('0')        

        # Example command Thumb, pointer and Pinkie are extended here
        if lmlist[4][1] > lmlist[3][1] and lmlist[8][2] < lmlist[6][2] and lmlist[12][2] > lmlist[10][2] and lmlist[16][2] > lmlist[14][2] and lmlist[20][2] < lmlist[18][2]:
            if not lights_on:
                Player1.append('Lights on')
                speak("Lights on")
                lights_on = True
            else:
                Player1.append('Lights on')
                speak("Lights off")
                lights_on = False
        
        # Example command Thumb, pointer and middle are extended here and it calls out to a nurse
        if lmlist[4][1] > lmlist[3][1] and lmlist[8][2] < lmlist[6][2] and lmlist[12][2] < lmlist[10][2] and lmlist[16][2] > lmlist[14][2] and lmlist[20][2] > lmlist[18][2]:
            Player1.append('Nurse')
            speak("Nurse")

        # Example command Thumb and pinkie are extended and it adds a food request to their itineary
        if lmlist[4][1] > lmlist[3][1] and lmlist[8][2] > lmlist[6][2] and lmlist[12][2] > lmlist[10][2] and lmlist[16][2] > lmlist[14][2] and lmlist[20][2] < lmlist[18][2]:
            Player1.append('Food')
            food_time = (datetime.datetime.now() + datetime.timedelta(minutes=20)).time()
            itin.add_activity(food_time, "Food")
            speak(itin.get_next_activity())
            print(itin.patient_itinerary)

        # Thumb alone extended here and it clears the itinerary
        if lmlist[4][1] > lmlist[3][1] and lmlist[8][2] > lmlist[6][2] and lmlist[12][2] > lmlist[10][2] and lmlist[16][2] > lmlist[14][2] and lmlist[20][2] > lmlist[18][2]:
            Player1.append('Clear')
            itin.patient_itinerary.clear()
            speak("Itinerary cleared")

        # Pointer middle and ring are extended here and it signals pain
        if lmlist[4][1] < lmlist[3][1] and lmlist[8][2] < lmlist[6][2] and lmlist[12][2] < lmlist[10][2] and lmlist[16][2] < lmlist[14][2] and lmlist[20][2] > lmlist[18][2]:
            Player1.append('Pain')
            speak("Pain Please help")
            with open('pain_log.txt', 'a') as f:
                f.write(f'Pain reported at {datetime.datetime.now()}\n')
                
        print('Player1', Player1)
    
    

        
    
    cTime = time.time()
    fps = 1 / (cTime-pTime)
    pTime = cTime

    # Shows the FPS of the program
    cv2.putText(img, f'FPS: {int(fps)}',(400,70), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)



