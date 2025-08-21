#include <Arduino.h>

int middleFinger = 34; // Analog pin where the sensor is connected
int indexFinger = 35;
int ringFinger = 39;
int pinkyFinger = 36;
int middleValue, indexValue, ringValue, pinkyValue;

void setup() {
Serial.begin(115200);
analogReadResolution(12);
//pinMode(middleFinger, INPUT_PULLDOWN);
}

void loop() {
middleValue = analogRead(middleFinger);
indexValue = analogRead(indexFinger);
ringValue = analogRead(ringFinger);
pinkyValue = analogRead(pinkyFinger);
Serial.print(middleValue); // Print the sensor value to the Serial Monitor
Serial.print(",");
Serial.print(indexValue);
Serial.print(",");
Serial.print(ringValue); // Print the sensor value to the Serial Monitor
Serial.print(",");
Serial.println(pinkyValue);
delay(100);
}
