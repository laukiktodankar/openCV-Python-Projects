#import necessary libraries
import cv2
import numpy as np

#initialize with blank numpy array
img = np.zeros((768,1024,3))


def draw_arc(center,radius,startangle,endangle,color,thickness,text,fontcolor):
	axes = (radius,radius)
	font = cv2.FONT_HERSHEY_SIMPLEX
  
  #algorithm valid for alphnumeric characters
	if int(text) > 99 and int(text) < 1000:
		fontscale = radius/30
		linetype = 4
	if int(text) > 9 and int(text) < 100:
		fontscale = radius/25
		linetype = 5  #size 38
	if int(text) >= 0 and int(text) < 10: 
		fontscale = radius/20
		linetype = 6
    
   
	text_size = cv2.getTextSize(text,font,fontscale,linetype)
	tx,ty = center
	angle = 0
	displayat = ((tx-(text_size[0][0])/2),(ty+(text_size[0][1])/2)) #centering text

	#merge text with img
	cv2.ellipse(img,center,axes,angle,startangle,endangle,color,thickness) #draw arc
	cv2.putText(img,text,displayat,font,fontscale,fontcolor,linetype)  #insert text inside arc

draw_arc((800,400),200,0,360,(255,255,255),5,'500',(255,255,255)) #anticlockwise negative
#draw_arc((800,400),100,0,360,(255,255,255),5,'50') #anticlockwise negative
cv2.imwrite('gotdamnit.jpg',dashboard)
