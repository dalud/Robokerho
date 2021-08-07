#include <Servo.h>
#include <Stepper.h>

// Utils
String command;
boolean led;

// Mouths
Servo mouthL;
Servo mouthR;
// Mouth scalars
int scalarL = 0; // 90 for continuous, 0 for standard 180*d
int scalarR = 90;

// Shoulder
const int stepsPerRevolution = 20000; // 30725 = MAX: 14HS13-0804S-PG19
const int dly = 10;
Stepper shoulder(stepsPerRevolution, 8, 9);

void setup() {
 pinMode(LED_BUILTIN, OUTPUT);
  
 mouthL.attach(2);
 mouthR.attach(3);
 Serial.begin(9600);
 // zero motors
 moveMouth('L', 0);
 moveMouth('R', 0);
 
 shoulder.setSpeed(10); //60: max for 14HS13-0804S-PG19 = 825Hz
}

void loop(){   
  if (Serial.available()) {
    command = Serial.readStringUntil('\n');
  }
  // Serial.println(command);
  String cmd = command.substring(0,2);
  
  if(cmd == "ml") { // Mouth Left
    moveMouth('L', command.substring(2).toInt());
  }
  if(cmd == "mr") { // MOuth Right
    moveMouth('R', command.substring(2).toInt());
  }
  if(cmd == "s") { // Shoulder Right
    moveShoulder();
  }
  delay(dly);
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

void moveShoulder() {
  shoulder.step(stepsPerRevolution);
  delay(dly);
}

void ledOn() {
  digitalWrite(LED_BUILTIN, HIGH);
}

void ledOff() {
  digitalWrite(LED_BUILTIN, LOW);
}
