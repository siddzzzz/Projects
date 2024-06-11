##this program will highlight and pop the colour GREEN on the live video
## i have tried to explain what some statements of the program is doing
## Hope i have fullfilled what the type of program you were looking for
##i have also added a feature in which it will make ONE box around all the green objects

import cv2 as c
import numpy as np
from PIL import Image

green= [0,255,0]    ##you can change it to any BRG value you want and the program will detect and pop that colour only
                    ##for this program i have chosen the colour green
  
web_cam = c.VideoCapture(0)

def get_limit(colour):
    col = np.uint8([[colour]])

    hsv = c.cvtColor(col,c.COLOR_BGR2HSV)

    ll = hsv[0][0][0] - 10,100,100
    ul = hsv[0][0][0] + 10,255,255

    lower = np.array(ll,dtype = np.uint8)
    upper = np.array(ul,dtype = np.uint8)
    return lower,upper
    
def colour_popping(frame, mask, colour): ##making the colour popint effect
    new = frame.copy()
    new[np.where(mask == 255)] = colour
    return new




while True:
    ret , frames = web_cam.read()

    h_img = c.cvtColor(frames,c.COLOR_BGR2HSV)##converting the image from the BGR aka RGB colours to HSV colours

    lower,upper = get_limit(colour = green) ##getting the lower and upper limits from the function defined above
    
    mask = c.inRange(h_img,lower,upper) ##detects the areas in the frames whivh are between the upper and the lower range of the colour

    mask_ = Image.fromarray(mask)

    bounding_box = mask_.getbbox() ##making a bounding box

    frames = colour_popping(frames,mask,green) ##using the user defined function to pop the colour in the frames
    
    
    if bounding_box is not None:
        x1,y1,x2,y2 = bounding_box 
        frames = c.rectangle(frames,(x1,y1),(x2,y2),(0,255,0),3) ##making a rectangle above the colour
        frames = c.putText(frames,"GREEN", (x1,y1-7),c.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),c.LINE_4) ##putting text on the frames
    
    c.imshow("Gradient Project - ColourSplash Cam", frames) ##Displays the video frame by frame

    if c.waitKey(1) & 0xFF == ord("p"):     ##FOR exiting the program press 1 followd by 
        break

web_cam.release()
c.destroyAllWindows()
