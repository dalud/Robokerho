#include <Servo.h>

String command;

Servo mouth;
int scalar = 90; // 90 for continuous, 0 for standard 180*d

int dly = 30; // Scale down to speed motor functions up


void setup() {
 mouth.attach(2);
 Serial.begin(9600);
 // zero motors
 moveMouth('L', 0);
}

void loop(){
  if (Serial.available()) {
    command = Serial.readStringUntil('\n');
  }
  // Serial.println(command);
  String cmd = command.substring(0,2);
  
  if(cmd == "ml") {
    moveMouth('L', command.substring(2).toInt());
  }
  
  delay(dly);
}

void moveMouth(char channel, int pos) {  
  switch(channel) {
    case('L'):
      if(mouth.attached()) mouth.write(pos+scalar);
      break;
  }
}

