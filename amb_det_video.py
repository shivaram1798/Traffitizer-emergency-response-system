import cv2
import serial #for Serial communication
import time   #for delay functions
 
arduino = serial.Serial('COM3',9600) #Create Serial port object called arduinoSerialData

video_src = 'amb_present.mp4'

ambulance_cap= cv2.VideoCapture(video_src)

ambulance_cascade = cv2.CascadeClassifier('cascade.xml')

print("started")

time.sleep(1)

while True:
    ret, img = ambulance_cap.read()
   
    if (type(img) == type(None)):
        break
    c=0
    
    yellow = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    ambulances = ambulance_cascade.detectMultiScale(yellow, 1.1, 2)
    
    for (x,y,w,h) in ambulances:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        if(c==0):
            print("Ambulance detected from ",time.strftime("%H:%M:%S",time.localtime()))
        c=c+1
        arduino.write(b"1")
        time.sleep(0.1)
    else:
        print("No Ambulance at:",time.strftime("%H:%M:%S",time.localtime()))
        arduino.write(b"0")
        #time.sleep(1)

    cv2.imshow('traffitizer', img)
    
    if cv2.waitKey(33) == 27:
        break
    
cv2.destroyAllWindows()
