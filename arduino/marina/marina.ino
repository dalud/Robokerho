#include <Servo.h>

String command;
boolean led;
Servo mouthL;
Servo mouthR;
int scalarL = 0; // 90 for continuous, 0 for standard 180*d
int scalarR = 90;

void setup() {
 pinMode(LED_BUILTIN, OUTPUT);
 pinMode(4, OUTPUT);
 mouthL.attach(3);
 // mouthR.attach(3);
 Serial.begin(9600);
 // zero motors
 moveMouth('L', 0);
 moveMouth('R', 0);
}

void loop(){
  if (Serial.available()) {
    command = Serial.readStringUntil('\n');
  }
  
  //  Serial.println(command);
  String cmd = command.substring(0,2);
  
  if(cmd == "mL") {
    moveMouth('L', command.substring(2).toInt());
  }
  if(cmd == "mR") {
    moveMouth('R', command.substring(2).toInt());
  }
  
  delay(30);
}

void moveMouth(char channel, int pos) {  
  switch(channel) {
    case('L'):
      if(mouthL.attached()) mouthL.write(pos+scalarL);
      break;
    case('R'):
      if(mouthR.attached()) mouthR.write(pos+scalarR);
      break;
  }
}

void ledOn() {
  digitalWrite(LED_BUILTIN, HIGH);
}

void ledOff() {
  digitalWrite(LED_BUILTIN, LOW);
}
