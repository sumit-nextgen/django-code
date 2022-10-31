import cv2
from PIL import Image 
import PIL
 
img = cv2.imread('D:/New folder/media/170249.jpg')
cv2.imshow("img",img)
print('Original Dimensions : ',img.shape)
 
scale_percent = 80 # percent of original size
width = int(320)
height = int(640)
dim = (width, height)
  
# resize image
resized = cv2.resize(img, dim, interpolation =int(5))
 
print('Resized Dimensions : ',resized.shape)
 
cv2.imshow("Resized image", resized)
cv2.imwrite('D:/New folder/media/landscape.jpg', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
