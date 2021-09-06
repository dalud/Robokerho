#include <Servo.h>

Servo servo;
int scalar = 90; // 90 for continuous, 0 for standard 180*d

String command;

void setup() {
  servo.attach(2);
  Serial.begin(9600);
}

void loop() { 
  if (Serial.available()) {
    command = Serial.readStringUntil('\n');
  }
  if (command && servo.attached()) servo.write(command.toInt() + scalar);
}
