import cv2 
import numpy as np
from matplotlib import pyplot as plt
import imutils
import easyocr

img = cv2.imread('images/car1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))

bfilter = cv2.bilateralFilter(gray, 11, 17, 17, 17)
edged = cv2.Canny(bfilter, 30, 200)
plt.imshow(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))

#Importing necessary library
# import numpy as np  
# import cv2  
# from PIL import Image  
# import pytesseract as tess  



# #Checking the area range and width height ratio  for

# def check_area(area,width,height):
#         ratio=float(width)/float(height)
#         if ratio<1:
#                 ratio=1/ratio #
#         if (area<1063.62 or area>73862.5)  or (ratio<3or ratio>6):
#                 return False
#         return True
# >>>>>>> 38772ea74eef0111a8308af48dfe0cca21bcea89

