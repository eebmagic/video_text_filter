import numpy as np
import cv2
import os

def flattenList(inputList):
    output = inputList[:]
    while type(output[0]) == list:
        temp = []
        for sub in output:
            temp += sub
        output = temp[:]            
    return output




cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Get image size and window size
    org_height = len(gray.tolist())
    org_width = len(gray.tolist()[0])
    screen_height,  screen_width = os.popen('stty size', 'r').read().split()
    
    
    print(screen_width, screen_height)
    print(org_width, org_height)


    # Display the resulting frame
    cv2.imshow('frame',gray)

    #0-255
    flatGray = flattenList(gray.tolist())



    print("")
    #Test for break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()