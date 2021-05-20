import cv2
import numpy as np
import mido
import time
import scales
from threading import Thread

key = "c"
scale = "pentatonic"



cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

ball_color_low = np.array([27,80,39],np.uint8)
ball_color_high = np.array([50,200,103],np.uint8)

red_low = np.array([174,194,46])
red_high = np.array([179,255,255])

blue_low = np.array([73,93,0])
blue_high = np.array([99,204,255])

green_low = np.array([174,194,46])
green_high = np.array([174,194,46])



class Instrument:
    def __init__(self,scl,key,area_detect,color_min,color_max,port):
        self.scl = scl
        self.key = key
        self.area_detect = area_detect
        self.color_min = color_min
        self.color_max = color_max
        self.port = port
        self.last_note = 0

    def play(self):
        ret,img = cap.read()
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(imgHSV,self.color_min,self.color_max)
        contours,hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        for c in contours:
            area = cv2.contourArea(c)
            if area > self.area_detect:
                m = cv2.moments(c)
                if (m["m00"]==0): m["m00"]=1
                x = int(m["m10"]/m["m00"])
                y = int(m["m01"]/m["m00"])
                note = scales.Scale.process(y,self.key,self.scl)
                velocity = int(1+(x/5))
                
                cv2.circle(img,(x,y),7,(0,255,0),-1)
                new_contour = cv2.convexHull(c)
                cv2.drawContours(img,[new_contour], 0,(0,200,0),1) 
                cv2.putText(img, "{},{}".format(str(note),str(velocity)),(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.75,(0,0,255),1,cv2.LINE_AA)
                    
                if not self.last_note == note:
                    self.last_note = note 
                    msg = mido.Message('note_on', note=note, velocity=velocity)
                    mido.open_output(mido.get_output_names()[self.port]).send(msg)

        if all(cv2.contourArea(c) < self.area_detect for c in contours):
            self.last_note = 0  
            #inport.reset()

        if not ret:
            print("no se reciben frames, terminando...")
            return "finished"
        cv2.imshow("img",img)


hand_1 = Instrument("pentatonic","d",200,ball_color_low,ball_color_high,1)
hand_2 = Instrument("pentatonic","d",200,red_low,red_high,2)
hand_3 = Instrument("pentatonic","d",200,blue_low,blue_high,3)



def both_hands(): 
    p1 = Thread(target=hand_1.play())
    p2 = Thread(target=hand_2.play())
    p3 = Thread(target=hand_3.play())
    p1.setDaemon(True)
    p2.setDaemon(True)
    p3.setDaemon(True)
    p1.start()
    p2.start()
    p3.start()

while True:
    both_hands()
    if cv2.waitKey(1) == ord("q"):
        break



cap.release()
cv2.destroyAllWindows()
