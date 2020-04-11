import cv2 
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe' #se deu pau ao executar, procure onde foi instalado Tesseract e altere aqui.

import preprocessing as pp

img = cv2.imread('teste.png')
custom_config = r'--oem 3 --psm 6'

print(pytesseract.image_to_string(img, config=custom_config))


'''
image = cv2.imread('teste.png')

gray = pp.grayscale(image)
#thresh = pp.thresholding(gray)
#opening = pp.opening(gray)
#canny = pp.canny(gray)

cv2.imshow('image',gray)
cv2.waitKey(0)
'''