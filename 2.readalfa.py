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
        if 'A' in incoming:
            print ('A')
        if 'B_hello' in incoming:
            print ('B')
        if 'C' in incoming:
            print ('C')
        if 'D' in incoming:
            print ('D')
        if 'E' in incoming:
            print ('E')
        
    test=incoming        
        
