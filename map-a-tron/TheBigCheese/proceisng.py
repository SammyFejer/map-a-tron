from cv2 import imshow
import numpy as np  
img = cv2.imread('8927-3N_Corang_GetlostMap_V15.tif', cv2.IMREAD_UNCHANGED)
cv2.imshow=('yahoo', img)
cv2.waitKey(0)
cv2.distroyAllWindows()
