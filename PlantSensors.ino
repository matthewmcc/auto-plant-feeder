
#include <C:\Users\matth\Documents\Arduino\libraries\DHTLibrary\dht.h>
#include <C:\Users\matth\Documents\Arduino\libraries\DHTLibrary\dht.cpp>

unsigned long timeToPowerSensorsOnMs = 2000;
unsigned long oneSecondInMs = 1000;
unsigned long oneMinuteInMs = 60 * oneSecondInMs;
unsigned long tenMinutesInMs = oneMinuteInMs * 10;
unsigned long timeBetweenReads = tenMinutesInMs;

unsigned long timeToTurnTempSensorOnBeforeRead = 10000;

bool tempSensorIsOn = false;

unsigned long lastReadTime = 0;
bool timeResetCaught = true;

uint8_t SEN_MOISTURE_PWD = 3;
uint8_t SEN_MOISTURE_READ = A0;
unsigned int moistureValue;

dht DHT;
uint8_t SEN_TEMP_HUMDITIY_READ = 2;
uint8_t SEN_TEMP_HUMDITIY_PWD = 12;

void setup() {
  Serial.begin(9600);

    pinMode(SEN_MOISTURE_PWD, OUTPUT);
    pinMode(SEN_TEMP_HUMDITIY_PWD, OUTPUT);

  lastReadTime = millis();
}   

void turnOnTempSensor() {
    digitalWrite(SEN_TEMP_HUMDITIY_PWD, HIGH);

    tempSensorIsOn = true;
}

void turnMoistureSensorsOn() {
    digitalWrite(SEN_MOISTURE_PWD, HIGH);
}

void turnSensorsOff() {
    digitalWrite(SEN_MOISTURE_PWD, LOW);
    digitalWrite(SEN_TEMP_HUMDITIY_PWD, LOW);

    tempSensorIsOn = false;
}

void loop() {
    // Temp is turned on before read to allow time to calibrate
    if (not tempSensorIsOn and 
        lastReadTime + timeBetweenReads - timeToTurnTempSensorOnBeforeRead < millis()) {
      turnOnTempSensor();
    }
  
    if (lastReadTime + timeBetweenReads < millis()) {
        lastReadTime = millis();
      
        turnMoistureSensorsOn();
        delay(timeToPowerSensorsOnMs);

        int errorDHT = DHT.read11(SEN_TEMP_HUMDITIY_READ);
        moistureValue = analogRead(SEN_MOISTURE_READ);
        
        Serial.print("Moisture: ");
        Serial.print(moistureValue);
        Serial.print(", Temperature: ");
        Serial.print(DHT.temperature);
        Serial.print(", Humidity: ");
        Serial.println(DHT.humidity);

        turnSensorsOff();

        timeResetCaught = false;
    }

    // Checked for when millis() time wraps around
    if (not timeResetCaught and millis() < lastReadTime) {
      lastReadTime = millis();
      timeResetCaught = true;
    }
}
