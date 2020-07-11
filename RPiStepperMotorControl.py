import RPi.GPIO as GPIO
import time 

def seconds_passed(oldepoch, seconds):
    return time.time() - oldepoch >= seconds

# Creates a sigmoid shape curve between (startSleepDelay, finalSleepDelay) at point (percentageOfFinalSpeedDelay)
accelerationSigmoidCurveShape = 2
def stepperMotorAcceleration(percentageOfFinalSpeedDelay, startSleepDelay, finalSleepDelay):
    if percentageOfFinalSpeedDelay >= 100:
        return finalSleepDelay

    standardisedPercentageOfFinalSpeedDelay = percentageOfFinalSpeedDelay / 100
    aPOFSD = standardisedPercentageOfFinalSpeedDelay
    
    sigmoidDenominator = 1 + (aPOFSD / (1 - aPOFSD)) ** accelerationSigmoidCurveShape

    return ((startSleepDelay - finalSleepDelay) / sigmoidDenominator) + finalSleepDelay

deccelerationSigmoidCurveShape = -2
def stepperMotorDecceleration(percentageOfFinalSpeedDelay, startSleepDelay, finalSleepDelay):
    if percentageOfFinalSpeedDelay <= 0:
        return startSleepDelay

    standardisedPercentageOfFinalSpeedDelay = percentageOfFinalSpeedDelay / 100
    aPOFSD = standardisedPercentageOfFinalSpeedDelay
    
    sigmoidDenominator = 1 + (aPOFSD / (1 - aPOFSD)) ** deccelerationSigmoidCurveShape

    return ((startSleepDelay - finalSleepDelay) / sigmoidDenominator) + finalSleepDelay

out1 = 13
out2 = 11
out3 = 15
out4 = 12

def setupGPIOPins():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(out1,GPIO.OUT)
    GPIO.setup(out2,GPIO.OUT)
    GPIO.setup(out3,GPIO.OUT)
    GPIO.setup(out4,GPIO.OUT)

def resetGPIOPins():
    GPIO.output(out1, GPIO.LOW)
    GPIO.output(out2, GPIO.LOW)
    GPIO.output(out3, GPIO.LOW)
    GPIO.output(out4, GPIO.LOW)

oneMillion = 1000000
usleep = lambda sleepTimeMicroSeconds : time.sleep(sleepTimeMicroSeconds / oneMillion)

motorRunTimeInSecs = 10
motorAccelerationTimeSecs = 2
motorDecelerationTimeSecs = 1.5

startSleepDelaySecs = .01

def calculateSleepDelay(startTime, finalSleepDelaySecs):
    # Acceleration
    if not seconds_passed(startTime, motorAccelerationTimeSecs):
        percentageOfFinalSpeedDelay = (motorAccelerationTimeSecs / (startTime - time.time())) * 100
        sleepDelaySecs = stepperMotorAcceleration(percentageOfFinalSpeedDelay, startSleepDelaySecs, finalSleepDelaySecs)
    else:
        sleepDelaySecs = finalSleepDelaySecs
    # else if seconds_passed(startTime, motorRunTimeInSecs - motorDecelerationTimeSecs):
    return sleepDelaySecs

setupGPIOPins()

print("Input steep delay in seconds. And a ramp up factor.")

try:
    while(1):
        resetGPIOPins()

        finalSleepDelaySecs = input()
        sleepDelaySecs = startSleepDelaySecs

        startTime = time.time()
        rampTime = time.time()

        currentStep = 0

        while not seconds_passed(startTime, motorRunTimeInSecs):
            sleepDelaySecs = calculateSleepDelay(startTime)
            print("Calculated sleep delay: ", sleepDelaySecs)

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

            usleep(sleepDelaySecs)

    print("Final sleep delay: ", str(sleepDelaySecs))
      
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
