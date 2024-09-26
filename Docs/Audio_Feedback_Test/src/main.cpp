#include <Arduino.h>

int flexPin1 = 34;  // Analog pin where the sensor is connected
int flexPin2 = 35;
int flexValue1, flexValue2;



void setup() {
  Serial.begin(115200);
  analogReadResolution(12);
}

void loop() {
  flexValue1 = analogRead(flexPin1);
  flexValue2 = analogRead(flexPin2);
  Serial.println(flexValue1);  // Print the sensor value to the Serial Monitor
  Serial.println(flexValue2);
  delay(1000);
}