# Finger-tracking-gestures

---
Ever wanted to issue commands using hand signs? This is the project for You!

---
This is a python program which uses OpenCV to track the fingers of a person, and measures the distances of two vectors, such as vector A (wrist(0) to Thumb_Tip(4)) vs vector B (wrist(0) to Thumb_IP(3)), if the legnth of the first vector is longer it indiacates that the thumb is straighted while the opposite respresents that the thumb is down. 

This suppourts multiple fingers to tracked at once, so particular finger combination gestures be tracked together to act as a single command action. 

Due to the numerous python libraries available this can be easily modified to work with all of them. 

---
To use this program, have the cv2, mediapipe libraries installed.

You can find a documentation image atactched to the readme, which labels the joints of the fingers tracked by the program for making custom changes

![Finger Labels](https://i.imgur.com/v1do68E.png "Image Title")

---
[Link to youtube demo](https://youtu.be/antiUyaTSao)
