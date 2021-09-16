#include <Servo.h>
#include <AccelStepper.h>

String command;

Servo mouth;
int scalar = 90; // 90 for continuous, 0 for standard 180*d

AccelStepper shoulder_R(1, 8, 9);

int dly = 1; // Universal delay. Scale down to speed motor functions up
float pause = .3; // Audio amplitude interpreted as silence


void setup() {
 mouth.attach(2);
 Serial.begin(9600);
 // zero mouth motors
 moveMouth('L', 0);

 shoulder_R.setMaxSpeed(5000); //SPEED = Steps / second  
 shoulder_R.setAcceleration(1000); //ACCELERATION = Steps /(second)^2    
 shoulder_R.setSpeed(1500);
 delay(500);
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

  if(command.substring(2).toInt() > pause) {
    moveStepper(shoulder_R);
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

void moveStepper(AccelStepper motor) {
  motor.enableOutputs();
  motor.runSpeed();
  // Serial.println(shoulder_R.currentPosition());
  motor.disableOutputs();
}
