import cv2
import numpy as np
import cv2
import numpy as np

imag = cv2.imread('2.jpeg')
imge= cv2.cvtColor(imag,cv2.COLOR_RGB2GRAY )
imge=255-imge
imge=cv2.resize(imge,(300,300))
imge1=cv2.imread('4.jpeg')
imge1 =cv2.cvtColor(imge1 ,cv2.COLOR_RGB2GRAY )
imge1 =255-imge1
imge1 =cv2.resize(imge1 ,(300,300))
imge_result=np.concatenate((imge ,imge1 ) )
cv2.imshow('ss',imge_result  )
cv2.waitKey()
