import cv2

image = cv2.imread("galaxy.jpg", 0)
print(type(image))
print(image.shape)

resized_img=cv2.resize(image, (int(image.shape[1]/2),int(image.shape[0]/2)))

cv2.startWindowThread()
cv2.imshow("Galaxy", resized_img)
cv2.imwrite("resized.jpg",resized_img)
cv2.waitKey(0)
cv2.destroyAllwindow()




