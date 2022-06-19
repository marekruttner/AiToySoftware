"""
AI TOY OBJECT RECOGNITION 
Author: Marek Ruttner (for nvias.org)
Date: 2022/5/26
Description: Modified version of Srihari Humbarwadi RetinaNet object recognition for Raspberry Pi 4 (nvias.org AI TOY)
"""

import cv2
import numpy as np

from gpiozero import Button

from take import take

btn = Button(14)

def preview():
    cap = cv2.VideoCapture(0)

    currentFrame = 0
    while(True):
        # Capture frame-by-frame
        _, frame = cap.read()

        # Handles the mirroring of the current frame
        frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)

        # Display the resulting frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & btn.is_pressed:
            break

        # To stop duplicate images
        currentFrame += 1

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows() 
    btn.close()

