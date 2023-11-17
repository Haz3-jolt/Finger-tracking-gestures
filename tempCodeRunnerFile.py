        # Pinkie alone extended here and it reads the itinerary
        if lmlist[4][1] < lmlist[3][1] and lmlist[8][2] > lmlist[6][2] and lmlist[12][2] > lmlist[10][2] and lmlist[16][2] > lmlist[14][2] and lmlist[20][2] < lmlist[18][2]:
            speak(itin.get_next_activity())
            print(itin.patient_itinerary)