accelerationSigmoidCurveShape = 2
def stepperMotorAcceleration(percentageOfFinalSpeedDelay, startSleepDelay, finalSleepDelay):
    if percentageOfFinalSpeedDelay >= 100:
        return finalSleepDelay

    standardisedPercentageOfFinalSpeedDelay = percentageOfFinalSpeedDelay / 100
    aPOFSD = standardisedPercentageOfFinalSpeedDelay
    
    sigmoidDenominator = 1 + (aPOFSD / (1 - aPOFSD)) ** accelerationSigmoidCurveShape

    return ((startSleepDelay - finalSleepDelay) / sigmoidDenominator) + finalSleepDelay

for i in range(0, 101, 10):
    print(i, ", ", stepperMotorAcceleration(i, .01, .0001))