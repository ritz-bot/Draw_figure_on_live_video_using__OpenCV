# how to draw on a video

import cv2
cap=cv2.VideoCapture(0)
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
##calbabck function Rectangle
def draw_rectangle(event,x,y,flags,param):
    
    global pt1,pt2,topleft_clicked,botright_clicked
    if event==cv2.EVENT_LBUTTONDOWN:
        #reset the rectangle(checks rectangle is there)
        if topleft_clicked == True and botright_clicked==True:
            pt1=(0,0)#top left
            pt2=(0,0)
            topleft_clicked=False
            botright_clicked=False
        if topleft_clicked == False:
            pt1=(x,y)
            topleft_clicked=True
        elif botright_clicked == False:
            pt2=(x,y)
            botright_clicked=True
            
#global variables
pt1=(0,0)#top left
pt2=(0,0)#ottom right
topleft_clicked=False
botright_clicked=False
#connecting to callback
cap=cv2.VideoCapture(0)
cv2.namedWindow('Test')
cv2.setMouseCallback('Test',draw_rectangle)
x=width//2
y=height//2

#width,height of rectangle

w=width//4
h=height//4

#bottom right corner x+w, y+h

while True:
    ret,frame=cap.read()
    #drawing on the frame based off the global vvariables
    if topleft_clicked==True:
        cv2.circle(frame,center=pt1,radius=5,color=(0,0,255),thickness=-1)
        
    if topleft_clicked and botright_clicked:
        cv2.rectangle(frame,pt1,pt2,(0,0,255),3)
   
    #first draw the rectangle then show the frame
    cv2.imshow('Test',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
