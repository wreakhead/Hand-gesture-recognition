import serial 
import time
import pyautogui
import sys

ArduinoSerial = serial.Serial('COM6',9600)
time.sleep(2)
print ("lets do some work")
test=''

while 1:
    
    incoming = str (ArduinoSerial.readline()) #read the serial data and print it as line
   
    if incoming!=test:
    
        if 'B_hello' in incoming:
            print ('Hello')

        if 'Bye' in incoming:
            print ('Bye')
        if 'Yes' in incoming:
            print ('Yes')    
        
    test=incoming 
