import cv2
import numpy as np

import cv2
import array
imge=cv2.imread('3.jpg')
imge =cv2.resize(imge ,(428,560))
(h,w)=imge .shape[:2]
center=(w/2,h/2)
imge1=cv2.getRotationMatrix2D((center),180,1.0)
imge_result=cv2.warpAffine(imge ,imge1 ,(w,h))
cv2.imshow('smail',imge_result  )
cv2.waitKey()