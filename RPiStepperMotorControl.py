import RPi.GPIO as GPIO
import time 

def seconds_passed(oldepoch, seconds):
    return time.time() - oldepoch >= seconds

out1 = 13
out2 = 11
out3 = 15
out4 = 12

sleepDelay = .01

GPIO.setmode(GPIO.BOARD)
GPIO.setup(out1,GPIO.OUT)
GPIO.setup(out2,GPIO.OUT)
GPIO.setup(out3,GPIO.OUT)
GPIO.setup(out4,GPIO.OUT)

print "First calibrate by giving some +ve and -ve values....."

try:
    while(1):
        GPIO.output(out1, GPIO.LOW)
        GPIO.output(out2, GPIO.LOW)
        GPIO.output(out3, GPIO.LOW)
        GPIO.output(out4, GPIO.LOW)

        sleepDelay = input()
        speedIncreaseFactor = input()

        startTime = time.time()
        rampTime = time.time()

        oneMillion = 1000000

        currentStep = 0

        while not seconds_passed(startTime, 10):
            if seconds_passed(rampTime, 1):
                rampTime = time.time()

                nonDecimalSleepDelay = sleepDelay * oneMillion
                nonDecimalSleepDelay = nonDecimalSleepDelay * speedIncreaseFactor

                sleepDelay = nonDecimalSleepDelay / oneMillion

            if currentStep == 7:
                currentStep = 0
            else:
                currentStep = currentStep + 1

            if currentStep == 0:
                GPIO.output(out1, GPIO.HIGH)
                GPIO.output(out2, GPIO.LOW)
                GPIO.output(out3, GPIO.LOW)
                GPIO.output(out4, GPIO.LOW)

            elif currentStep == 1:
                GPIO.output(out1, GPIO.HIGH)
                GPIO.output(out2, GPIO.HIGH)
                GPIO.output(out3, GPIO.LOW)
                GPIO.output(out4, GPIO.LOW)

            elif currentStep == 2:  
                GPIO.output(out1, GPIO.LOW)
                GPIO.output(out2, GPIO.HIGH)
                GPIO.output(out3, GPIO.LOW)
                GPIO.output(out4, GPIO.LOW)

            elif currentStep == 3:    
                GPIO.output(out1, GPIO.LOW)
                GPIO.output(out2, GPIO.HIGH)
                GPIO.output(out3, GPIO.HIGH)
                GPIO.output(out4, GPIO.LOW)

            elif currentStep == 4:  
                GPIO.output(out1, GPIO.LOW)
                GPIO.output(out2, GPIO.LOW)
                GPIO.output(out3, GPIO.HIGH)
                GPIO.output(out4, GPIO.LOW)

            elif currentStep == 5:
                GPIO.output(out1, GPIO.LOW)
                GPIO.output(out2, GPIO.LOW)
                GPIO.output(out3, GPIO.HIGH)
                GPIO.output(out4, GPIO.HIGH)

            elif currentStep == 6:    
                GPIO.output(out1, GPIO.LOW)
                GPIO.output(out2, GPIO.LOW)
                GPIO.output(out3, GPIO.LOW)
                GPIO.output(out4, GPIO.HIGH)

            elif currentStep == 7:    
                GPIO.output(out1, GPIO.HIGH)
                GPIO.output(out2, GPIO.LOW)
                GPIO.output(out3, GPIO.LOW)
                GPIO.output(out4, GPIO.HIGH)

            time.sleep(sleepDelay)
      
    #   elif stepsToMove < 0 and stepsToMove >= -400:
    #       stepsToMove=stepsToMove*-1
    #       for y in range(stepsToMove,0,-1):
    #           if positive==1:
    #               if i==0:
    #                   i=7
    #               else:
    #                   i=i-1
    #               y=y+3
    #               positive=0
    #           negative=1
    #           #print((stepsToMove+1)-y) 
    #           if i==0:
    #               GPIO.output(out1,GPIO.HIGH)
    #               GPIO.output(out2,GPIO.LOW)
    #               GPIO.output(out3,GPIO.LOW)
    #               GPIO.output(out4,GPIO.LOW)
    #               time.sleep(0.03)
    #               #time.sleep(1)
    #           elif i==1:
    #               GPIO.output(out1,GPIO.HIGH)
    #               GPIO.output(out2,GPIO.HIGH)
    #               GPIO.output(out3,GPIO.LOW)
    #               GPIO.output(out4,GPIO.LOW)
    #               time.sleep(0.03)
    #               #time.sleep(1)
    #           elif i==2:  
    #               GPIO.output(out1,GPIO.LOW)
    #               GPIO.output(out2,GPIO.HIGH)
    #               GPIO.output(out3,GPIO.LOW)
    #               GPIO.output(out4,GPIO.LOW)
    #               time.sleep(0.03)
    #               #time.sleep(1)
    #           elif i==3:    
    #               GPIO.output(out1,GPIO.LOW)
    #               GPIO.output(out2,GPIO.HIGH)
    #               GPIO.output(out3,GPIO.HIGH)
    #               GPIO.output(out4,GPIO.LOW)
    #               time.sleep(0.03)
    #               #time.sleep(1)
    #           elif i==4:  
    #               GPIO.output(out1,GPIO.LOW)
    #               GPIO.output(out2,GPIO.LOW)
    #               GPIO.output(out3,GPIO.HIGH)
    #               GPIO.output(out4,GPIO.LOW)
    #               time.sleep(0.03)
    #               #time.sleep(1)
    #           elif i==5:
    #               GPIO.output(out1,GPIO.LOW)
    #               GPIO.output(out2,GPIO.LOW)
    #               GPIO.output(out3,GPIO.HIGH)
    #               GPIO.output(out4,GPIO.HIGH)
    #               time.sleep(0.03)
    #               #time.sleep(1)
    #           elif i==6:    
    #               GPIO.output(out1,GPIO.LOW)
    #               GPIO.output(out2,GPIO.LOW)
    #               GPIO.output(out3,GPIO.LOW)
    #               GPIO.output(out4,GPIO.HIGH)
    #               time.sleep(0.03)
    #               #time.sleep(1)
    #           elif i==7:    
    #               GPIO.output(out1,GPIO.HIGH)
    #               GPIO.output(out2,GPIO.LOW)
    #               GPIO.output(out3,GPIO.LOW)
    #               GPIO.output(out4,GPIO.HIGH)
    #               time.sleep(0.03)
    #               #time.sleep(1)
    #           if i==0:
    #               i=7
    #               continue
    #           i=i-1 

              
except KeyboardInterrupt:
    GPIO.cleanup()