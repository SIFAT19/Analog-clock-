import cv2
import numpy as np
from colors import colors,canvas,radius
from Function_count import clock,get_ticking
#making canvas
image=np.zeros(canvas,dtype=np.uint8)
#making background white
image[:]=[255,255,255]

#the end and start point of ticks
hours_in,hours_de=get_ticking()
for i in range(len(hours_in)):
    if i%5==0:
        cv2.line(image,hours_in[i],hours_de[i],colors['red'],3)
    else:
        cv2.circle(image,hours_in[i],6,colors['dark'],-1)
    cv2.circle(image,(400,400),radius+8,colors['black'],2)
    cv2.putText(image,"SIFAT",(315,300),cv2.FONT_HERSHEY_COMPLEX,2,colors['black'],1,cv2.LINE_AA)
    
    #running the test
while True:
	image_original = image.copy()

	#Use draw time to make clock hands on the canvas
	clock_face = clock(image_original)

	#Show the watch
	cv2.imshow('clock', image_original)
	if(cv2.waitKey(1)==ord('a')):
		break
        
cv2.destroyAllWindows()     
        