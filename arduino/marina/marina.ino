#include <Servo.h>

boolean continuous = true;
int scalar;
String command;
boolean led;
Servo mouthL;
Servo mouthR;

void setup() {
  if(continuous) {
    scalar = 90;
  } else {
    scalar = 0;
  }
 pinMode(LED_BUILTIN, OUTPUT);
 mouthL.attach(2);
 mouthR.attach(3);
 Serial.begin(9600);
 // zero motors
 moveMouth('L', 0);
 moveMouth('R', 0);
}

void loop(){
  if (Serial.available()) {
    command = Serial.readStringUntil('\n');
  }
  Serial.println(command);
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
      if(mouthL.attached()) mouthL.write(pos+scalar);
      break;
    case('R'):
      if(mouthR.attached()) mouthR.write(pos+scalar);
      break;
  }
}

void ledOn() {
  digitalWrite(LED_BUILTIN, HIGH);
}

void ledOff() {
  digitalWrite(LED_BUILTIN, LOW);
}
