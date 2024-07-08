import cv2 
import datetime
import math
from colors import colors
from colors import radius
from colors import center

def get_ticking():
    hours_in=[]
    hours_de=[]
    
    for i in range(0,360,6):
        x_range=int(center[0]+radius*math.cos(i*math.pi/180))
        y_range=int(center[1]+radius*math.sin(i*math.pi/180))
        
        hours_in.append((x_range,y_range))
    for i in range(0,360,6):
        x_range=int(center[0]+(radius-20)*math.cos(i*math.pi/180))
        y_range=int(center[1]+(radius-20)*math.sin(i*math.pi/180))
        
        hours_de.append((x_range,y_range))
    return hours_in,hours_de

def gettime(h,m,s):
    time =""
    hour=""
    minute=""
    second=""
    
    if h<10:
        hour ="0{}:".format(h)
    else:
        hour ="{}:".format(h)
    if m<10:
        minute ="0{}:".format(m)
    else:
        minute ="{}:".format(m)
    if s<10:
        second ="0{}".format(s)
    else:
        second ="{}".format(s)
    
    return hour+minute+second
def clock(image):
    #the time get from time module is
    time_now=datetime.datetime.now().time()
    hour=math.fmod(time_now.hour,12)
    minute=time_now.minute
    second=time_now.second
    
    #get the ticking points
    second_angle=math.fmod(second*6+270,360)
    minute_angle=math.fmod(minute*6+270,360)
    hour_angle=math.fmod((hour*30)+(minute/2)+270,360)
    
    second_x=int(center[0]+(radius-30)*math.cos(second_angle*math.pi/180))
    second_y=int(center[1]+(radius-30)*math.sin(second_angle*math.pi/180))
    cv2.line(image, center, (second_x, second_y),colors['blue'],2)
    
    minute_x=int(center[0]+(radius-50)*math.cos(minute_angle*math.pi/180))
    minute_y=int(center[1]+(radius-50)*math.sin(minute_angle*math.pi/180))
    cv2.line(image, center, (minute_x, minute_y),colors['black'],4)
    
    hour_x=int(center[0]+(radius-150)*math.cos(hour_angle*math.pi/180))
    hour_y=int(center[1]+(radius-150)*math.sin(hour_angle*math.pi/180))
    cv2.line(image,center, (hour_x, hour_y), colors['cyan'], 8)
     
    cv2.circle(image, center,6,colors['gray'],-1)  
    time=gettime(int(hour),minute,second) 
    cv2.putText(image,time,(325,390),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,colors['green'],2,cv2.LINE_AA)
    
    return image
        
    