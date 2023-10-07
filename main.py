!pip install opencv-python
!pip install pytesseract
!apt update
!apt install tesseract-ocr libtesseract-dev libleptonica-dev
!wget https://github.com/tesseract-ocr/tessdata/raw/main/eng.traineddata
!mv -v eng.traineddata /usr/share/tesseract-ocr/4.00/tessdata


import pytesseract
from PIL import Image
import os
import cv2
import numpy as np
from google.colab.patches import cv2_imshow
import matplotlib.pyplot as plt
import requests

import cv2

import filecmp


url2 = 'https://flyclipart.com/thumb2/i-love-you-png-transparent-images-pictures-photos-png-arts-876371.png'

#Код для вставки изображения
response = requests.get(url2)
img = cv2.imdecode(np.frombuffer(response.content, np.uint8), cv2.IMREAD_COLOR)
#cv2_imshow(img)
text = pytesseract.image_to_string(img)
print(text)


