#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>


Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

String command;

#define SERVOMIN  140 // this is the 'minimum' pulse length count (out of 4096)
#define SERVOMAX  520 // this is the 'maximum' pulse length count (out of 4096)

uint8_t servonum = 0;

int xval;
int yval;

int lexpulse;
int rexpulse;

int leypulse;
int reypulse;

int uplidpulse;
int lolidpulse;

int trimval;

const int analogInPin = A0;
int sensorValue = 0;
int outputValue = 0;
int switchval = 0;

void setup() {
  Serial.begin(9600);
  Serial.println("8 channel Servo test!");
  pinMode(analogInPin, INPUT);
  pinMode(2, INPUT);
 
  pwm.begin();  
  pwm.setPWMFreq(60);  // Analog servos run at ~60 Hz updates

  delay(10);
}


void loop() {
  // Serial cmd
  if (Serial.available()) {
    command = Serial.readStringUntil('\n');
  }
  String cmd = command.substring(0,2);
  
  if(cmd == "ex") { // Eye X
    xval = command.substring(2).toInt();
    // 0-1023 (lepo = 500)
    if(xval < 0) xval = 0;
    if(xval > 1023) xval = 1023;
  } else {
    xval = analogRead(A1);
  }
  if(cmd == "ey") { // Eye Y
    yval = command.substring(2).toInt();
    // 0-1023 (lepo = 500)
    if(yval < 0) yval = 0;
    if(yval > 1023) yval = 1023;
  } else {
    yval = analogRead(A0);
  }
  if(cmd == "li") { // Lids trimval (0-1023 0 = auki, 1023 = kiinni)
    trimval = command.substring(2).toInt();
  } else {
    trimval = analogRead(A2);
  }
  if(cmd == "b") { // Blink
    blink();
  }

  // Eye read
  lexpulse = map(xval, 0,1023, 270, 390);
  rexpulse = lexpulse;

  switchval = digitalRead(2); // blink
    
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

// Serial cmd blink
void blink() {
  pwm.setPWM(4, 0, uplidpulse);
  pwm.setPWM(5, 0, lolidpulse);
  delay(200);
  pwm.setPWM(4, 0, 240);
  pwm.setPWM(5, 0, 240);
  delay(1000); // set to proper delay after blink recovery
}
