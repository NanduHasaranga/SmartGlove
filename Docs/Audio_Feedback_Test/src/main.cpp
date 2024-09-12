#include <Arduino.h>

int flexPin = 34;  // Analog pin where the sensor is connected
int flexValue;

void setup() {
  Serial.begin(115200);
  analogReadResolution(12);
}

void loop() {
  flexValue = analogRead(flexPin);
  Serial.println(flexValue);  // Print the sensor value to the Serial Monitor
  delay(100);
}