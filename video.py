import cv2
import os

########################################################################
### SETTING ###
SHOW_REAL_VIDEO = False   # Set this to True to get real camera video from cv2

########################################################################


def flattenList(inputList):
    output = inputList[:]
    while type(output[0]) == list:
        temp = []
        for sub in output:
            temp += sub
        output = temp[:]            
    return output

def convert_to_ascii(inputGrays):
    # 17-long
    order = [' ', '.', "'", ',', ':', ';', 'c', 'l', 'x', 'o', 'k', 'X', 'd', 'O', '0', 'K', 'N']

    outputArray = []

    for row in inputGrays:
        adjusted_row = [int(x/(255/16)) for x in row]
        newRow = []
        for i in adjusted_row:
            newRow.append(order[i])
        outputArray.append(newRow)

    #print output
    return outputArray

def printArray(inputAsciiArray):
    fullImage = []
    for row in inputAsciiArray:
        fullImage.append(''.join(row))
    os.system("clear")
    print('\n'.join(fullImage))



#Get screensize for reduction
screen_height,  screen_width = os.popen('stty size', 'r').read().split()
print(screen_width, screen_height)

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    #Get image data
    ret, frame = cap.read()

    # Our operations on the frame come here
    #Convert data to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    

    # Display the resulting frame
    if SHOW_REAL_VIDEO:
        cv2.imshow('frame',gray)

    #Reduce grayscale array to proper resolution
    reduced = cv2.resize(gray, (int(screen_width), int(screen_height)))

    #Plug in reduced resolution numpy array for ascii converter func
    converted = convert_to_ascii(reduced)
    printArray(converted)


    print("")
    #Test for break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
