import os
from pathlib import Path

import cv2

files = os.listdir('temp/')
if files:
    p = Path('result')
    p.mkdir(exist_ok=True)
for file in files:
    print(file)
    image = cv2.imread('temp/'+file, 0)
    resized_img = cv2.resize(image, (100, 100))
    cv2.imwrite('result/'+file, resized_img)


