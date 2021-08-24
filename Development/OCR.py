#Importing necessary library
import numpy as np  
import cv2  
from PIL import Image  
import pytesseract as tess  



#Checking the area range and width height ratio  for

def check_area(area,width,height):
        ratio=float(width)/float(height)
        if ratio<1:
                ratio=1/ratio #
        if (area<1063.62 or area>73862.5)  or (ratio<3or ratio>6):
                return False
        return True

