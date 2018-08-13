import numpy as np
import cv2

ColorLabel = {
    "0" : (0, 0, 0), #NoLabel
    "1" : (100, 10, 110), #Meal_Preparation
    "2" : (255, 0, 0), #Relax
    "3" : (0, 255, 0), #Eating
    "4" : (200, 200, 200), #Work
    "5" : (0, 0, 255), #Sleeping
    "6" : (80, 80, 80), #Wash_Dishes
    "7" : (255, 33, 0), #Bed_to_Toilet
    "8" : (85, 200, 255), #Enter_Home
    "9" : (255, 90, 255), #Leave_Home
    "10" : (255, 0, 255), #Housekeeping
    "11" : (10, 255, 131) #Resperate
}

height = 850
width = 1700
emptyImage = np.ones((height, width, 3), np.uint8) * 255
rows = 0
counter = 0

cv2.rectangle(emptyImage, (200, 60), (1640, 660), (255, 250, 250), cv2.FILLED)
cv2.line(emptyImage, (185, 60), (185, 675), (255, 200, 200)) #vertical axis
cv2.line(emptyImage, (185, 675), (1640, 675), (255, 200, 200)) #horizontal axis
for i in range(0, 24):
    cv2.line(emptyImage, (200 + 60 * i, 675-2), (200 + 60 * i, 675+2), (0, 0, 0))  # horizontal axis sign
    cv2.line(emptyImage, (200 + 60 * i, 660), (200 + 60 * i, 60), (230, 220, 220))  # vertical lines
    cv2.putText(emptyImage, str(i), (193 + 60 * i, 675+23), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0))

minn = ""

with open("/home/hhak/PycharmProjects/DatasetDecoder/Dataset/OutPut", "r") as Dataset:
    for line in Dataset:
        if(line.split()[1] == "23:59:59"):
            cv2.putText(emptyImage, line.split()[0], (35, 95 + counter*60), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0))
            counter += 1
            print(counter, " ", line.split()[0])
        if(counter == 10):
            rows += 1
            counter = 0
        if(rows == 1):
            print("rows: ", rows)
            break

        hour = int(line.split()[1].split(":")[0])
        minute = int(line.split()[1].split(":")[1])
        second = int(line.split()[1].split(":")[2])

        if(minn != line.split()[1].split(":")[1]):
            CurrentTime = hour * 60 + minute + int(round(second / 60, 0))

            if(line.split()[42] == "0"):
                continue

            cv2.line(emptyImage, (200 + CurrentTime, 65 + counter*60), (200 + CurrentTime, 115+ counter*60), ColorLabel[line.split()[42]])
            minn = line.split()[1].split(":")[1]


cv2.imshow("image", emptyImage)
cv2.waitKey()
