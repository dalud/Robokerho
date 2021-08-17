#include <Servo.h>
#include <Stepper.h>
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

// Utils
String command;

// Eyes
int xval;
int yval;
int lexpulse;
int rexpulse;
int leypulse;
int reypulse;
int uplidpulse;
int lolidpulse;
int trimval;
int switchval = 0;

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
 pwm.begin();  
 pwm.setPWMFreq(60);  // Analog servos run at ~60 Hz updates
   
 mouthL.attach(2);
 mouthR.attach(3);
 Serial.begin(9600);
 // zero motors
 moveMouth('L', 0);
 moveMouth('R', 0);
 
 shoulder.setSpeed(10); //60: max for 14HS13-0804S-PG19 = 825Hz

 delay(10);
}

void loop(){   
  if (Serial.available()) {
    command = Serial.readStringUntil('\n');
  }
  // Serial.println(command);
  String cmd = command.substring(0,2);

  // Eyes
  if(cmd == "ex") { // Eye X
    xval = command.substring(2).toInt();
    // 0-1023 (lepo = 500)
    if(xval < 0) xval = 0;
    if(xval > 1023) xval = 1023;
  } else {
    xval = 500;
  }
  if(cmd == "ey") { // Eye Y
    yval = command.substring(2).toInt();
    // 0-1023 (lepo = 500)
    if(yval < 0) yval = 0;
    if(yval > 1023) yval = 1023;
  } else {
    yval = 500;
  }
  if(cmd == "li") { // Lids trimval (0-1023, 0 = auki, 1023 = kiinni)
    trimval = command.substring(2).toInt();
  } else {
    trimval = 1023;
  }
  if(cmd == "b") { // Blink
    switchval = LOW;
  } else {
    switchval = HIGH;
  }
  moveEyes();

  // Mouths
  if(cmd == "ml") { // Mouth Left
    moveMouth('L', command.substring(2).toInt());
  }
  if(cmd == "mr") { // Mouth Right
    moveMouth('R', command.substring(2).toInt());
  }
  if(cmd == "s") { // Shoulder Right
    moveShoulder();
  }
  delay(dly);
}

void moveEyes() {
  // Eye read
  lexpulse = map(xval, 0,1023, 270, 390);
  rexpulse = lexpulse;
    
  leypulse = map(yval, 0,1023, 280, 400);
  reypulse = map(yval, 0,1023, 400, 280);

  trimval=map(trimval, 320, 580, -40, 40);
    uplidpulse = map(yval, 0, 1023, 280, 420);
      uplidpulse += (trimval-40);
        uplidpulse = constrain(uplidpulse, 280, 400);
    lolidpulse = map(yval, 0, 1023, 410, 280);
      lolidpulse += (trimval/2);
        lolidpulse = constrain(lolidpulse, 280, 400);    
    
      pwm.setPWM(0, 0, lexpulse);
      pwm.setPWM(1, 0, leypulse);
      pwm.setPWM(2, 0, rexpulse);
      pwm.setPWM(3, 0, reypulse); 

      // Analog blink
      if (switchval == HIGH) {
      pwm.setPWM(4, 0, 240);
      pwm.setPWM(5, 0, 240);
      }
      else if (switchval == LOW) {
      pwm.setPWM(4, 0, uplidpulse);
      pwm.setPWM(5, 0, lolidpulse);
      }
      
  delay(5); // default 5ms
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
