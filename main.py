import numpy as np
import cv2

ColorLabel = {
    "0" : (255, 255, 255), #NoLabel
    "1" : (0, 240, 190), #Meal_Preparation
    "2" : (178, 255, 102), #Relax
    "3" : (255, 255, 0), #Eating
    "4" : (200, 200, 200), #Work
    "5" : (250, 206, 135), #Sleeping
    "6" : (193, 182, 255), #Wash_Dishes
    "7" : (0, 0, 255), #Bed_to_Toilet
    "8" : (0, 153, 0), #Enter_Home
    "9" : (100, 10, 110), #Leave_Home
    "10" : (255, 0, 255), #Housekeeping
    "11" : (0, 0, 0) #Respirate
}

height = 900
width = 1700
emptyImage = np.ones((height, width, 3), np.uint8) * 255
images = []
LasteMinute = ""
rows = 0
counter = 0

cv2.rectangle(emptyImage, (200, 60), (1640, 660), (255, 250, 250), cv2.FILLED)
cv2.line(emptyImage, (185, 60), (185, 675), (255, 200, 200)) #vertical axis
cv2.line(emptyImage, (185, 675), (1640, 675), (255, 200, 200)) #horizontal axis

for i in range(0, 24):
    cv2.line(emptyImage, (200 + 60 * i, 675-2), (200 + 60 * i, 675+2), (0, 0, 0))  # horizontal axis sign
    cv2.line(emptyImage, (200 + 60 * i, 660), (200 + 60 * i, 60), (230, 220, 220))  # vertical lines
    cv2.putText(emptyImage, str(i), (193 + 60 * i, 675+23), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0))

cv2.rectangle(emptyImage, (200+0*250, 750), (250+0*250, 800), ColorLabel["1"], cv2.FILLED)
cv2.putText(emptyImage, "Meal_Preparation", (250+0*300+10, 800-20), 1, 1, (0, 0, 0))
cv2.rectangle(emptyImage, (200+0*250, 825), (250+0*250, 875), ColorLabel["2"], cv2.FILLED)
cv2.putText(emptyImage, "Relax", (250+0*300+10, 875-20), 1, 1, (0, 0, 0))

cv2.rectangle(emptyImage, (200+1*250, 750), (250+1*250, 800), ColorLabel["3"], cv2.FILLED)
cv2.putText(emptyImage, "Eating", (250+1*250+10, 800-20), 1, 1, (0, 0, 0))
cv2.rectangle(emptyImage, (200+1*250, 825), (250+1*250, 875), ColorLabel["4"], cv2.FILLED)
cv2.putText(emptyImage, "Work", (250+1*250+10, 875-20), 1, 1, (0, 0, 0))

cv2.rectangle(emptyImage, (200+2*250, 750), (250+2*250, 800), ColorLabel["5"], cv2.FILLED)
cv2.putText(emptyImage, "Sleeping", (250+2*250+10, 800-20), 1, 1, (0, 0, 0))
cv2.rectangle(emptyImage, (200+2*250, 825), (250+2*250, 875), ColorLabel["6"], cv2.FILLED)
cv2.putText(emptyImage, "Wash_Dishes", (250+2*250+10, 875-20), 1, 1, (0, 0, 0))

cv2.rectangle(emptyImage, (200+3*250, 750), (250+3*250, 800), ColorLabel["7"], cv2.FILLED)
cv2.putText(emptyImage, "Bed_to_Toilet", (250+3*250+10, 800-20), 1, 1, (0, 0, 0))
cv2.rectangle(emptyImage, (200+3*250, 825), (250+3*250, 875), ColorLabel["8"], cv2.FILLED)
cv2.putText(emptyImage, "Enter_Home", (250+3*250+10, 875-20), 1, 1, (0, 0, 0))

cv2.rectangle(emptyImage, (200+4*250, 750), (250+4*250, 800), ColorLabel["9"], cv2.FILLED)
cv2.putText(emptyImage, "Leave_Home", (250+4*250+10, 800-20), 1, 1, (0, 0, 0))
cv2.rectangle(emptyImage, (200+4*250, 825), (250+4*250, 875), ColorLabel["10"], cv2.FILLED)
cv2.putText(emptyImage, "Housekeeping", (250+4*250+10, 875-20), 1, 1, (0, 0, 0))

cv2.rectangle(emptyImage, (200+5*250, 750), (250+5*250, 800), ColorLabel["11"], cv2.FILLED)
cv2.putText(emptyImage, "Respirate", (250+5*250+10, 800-20), 1, 1, (0, 0, 0))

img = emptyImage.copy()

with open("/home/hhak/PycharmProjects/DatasetDecoder/Dataset/OutPut", "r") as Dataset:
    for line in Dataset:
        if(line.split()[1] == "23:59:59"):
            counter += 1
            print(line.split()[0])

        if(counter == 10):
            images.append(img)
            img = emptyImage.copy()
            counter = 0
            print(" --- ")

        hour = int(line.split()[1].split(":")[0])
        minute = int(line.split()[1].split(":")[1])
        second = int(line.split()[1].split(":")[2])

        if(LasteMinute != line.split()[1].split(":")[1]):
            CurrentTime = hour * 60 + minute + int(round(second / 60, 0))

            if(line.split()[42] == "0"):
                continue

            cv2.line(img, (200 + CurrentTime, 65 + counter*60), (200 + CurrentTime, 115+ counter*60), ColorLabel[line.split()[42]])
            cv2.putText(img, line.split()[0], (35, 95 + counter*60), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0))
            LasteMinute = line.split()[1].split(":")[1]
    Dataset.close()

for i in range(0, len(images)):
    cv2.imwrite(str(i)+".png", images[i])
