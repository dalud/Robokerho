#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>
#include <Servo.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

String command; // Whole serial read
String cmd; // First 2 chars parsed
int dly = 10;

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

// Servos
Servo mouth;
Servo kaulaV;
Servo kaulaO;

void setup() {
  Serial.begin(9600);
 
  pwm.begin();  
  pwm.setPWMFreq(60);  // Analog servos run at ~60 Hz updates

  mouth.attach(2);
  kaulaO.attach(3);
  kaulaV.attach(4);

  delay(dly);
}


void loop() {
  // Serial cmd
  if (Serial.available()) {
    command = Serial.readStringUntil('\n');
    cmd = command.substring(0,2);
    delay(dly);
  }

  if(cmd == "mm") {
    moveMouth(command.substring(2).toInt());
  }  
  
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
  
  if(cmd == "kv") {
    moveKaula('V', command.substring(2).toInt());
  }

  if(cmd == "ko") {
    moveKaula('O', command.substring(2).toInt());
  }

  moveEyes();      
  delay(dly);
}

void moveMouth(int pos) {
  if(mouth.attached()) mouth.write(pos+90);
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

  // Blink
  if (switchval == LOW) {
    pwm.setPWM(4, 0, uplidpulse);
    pwm.setPWM(5, 0, lolidpulse);
  } else if (switchval == HIGH) {
    pwm.setPWM(4, 0, 240);
    pwm.setPWM(5, 0, 240);
  }
  delay(dly);
}

void moveKaula(char channel, int pos) {  
  switch(channel) {
    case('V'):
      if(kaulaV.attached()) kaulaV.write(pos);
      break;
    case('O'):
      if(kaulaO.attached()) kaulaO.write(pos);
      break;
  }
  delay(dly);
}
