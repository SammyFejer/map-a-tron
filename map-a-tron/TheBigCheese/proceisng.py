import cv2
import numpy as np  
img = cv2.imread('8927-3N_Corang_GetlostMap_V15.tif', cv2.IMREAD_UNCHANGED)
cv2.imwrite('C:\Users\sammy\source\repos\SammyFejer\map-a-tron\map-a-tron\static\images\conrang.png')
cv2.waitKey(0)
cv2.distroyAllWindows()
