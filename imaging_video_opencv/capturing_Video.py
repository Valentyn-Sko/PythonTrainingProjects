import cv2, time

video = cv2.VideoCapture(0)
time.sleep(3)
print(1)
check, frame = video.read()
if check == False:
    print("NO CAMERA")
video.release()
