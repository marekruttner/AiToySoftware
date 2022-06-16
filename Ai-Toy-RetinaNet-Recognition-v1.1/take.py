"""
AI TOY OBJECT RECOGNITION 
Author: Marek Ruttner (for nvias.org)
Date: 2022/5/26
Description: Modified version of Srihari Humbarwadi RetinaNet object recognition for Raspberry Pi 4 (nvias.org AI TOY)
"""

import cv2

def take():
        cap = cv2.VideoCapture(0)
        #cap.set(3,1920) #setting width
        #cap.set(4,1080) #setting high

        if cap.isOpened():
            _,frame = cap.read()
            frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
            cap.release() #releasing camera immediately after capturing picture
            if _ and frame is not None:
                cv2.imwrite('img.jpg', frame)

