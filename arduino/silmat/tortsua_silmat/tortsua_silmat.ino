// Tortsua eyes (USB from Rasp)

#include <Stepper.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

// Utils
String command;
const int dly = 10;

// Eyes
int xval = 500;
int yval = 500;
int lexpulse;
int rexpulse;
int leypulse;
int reypulse;
int uplidpulse;
int lolidpulse;
int trimval;
int switchval = 0;


void setup() {
  Serial.begin(9600);

  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);
 
  // Silmät
  pwm.begin();
  pwm.setPWMFreq(60);  // Analog servos run at ~60 Hz updates   
  
  delay(dly);
}


void loop(){  
  if (Serial.available()) {
    command = Serial.readStringUntil('\n');    
  }
  //Serial.println(command);
  delay(10);
  String cmd = command.substring(0,2);

  // Eyes
  if(cmd == "ex") { // Eye X
    digitalWrite(LED_BUILTIN, HIGH);
    xval = command.substring(2).toInt();
    // 0-1023 (lepo = 500)
    if(xval < 0) xval = 0;
    if(xval > 1023) xval = 1023;
  }
  if(cmd == "ey") { // Eye Y
    digitalWrite(LED_BUILTIN, HIGH);
    yval = command.substring(2).toInt();
    // 0-1023 (lepo = 500)
    if(yval < 0) yval = 0;
    if(yval > 1023) yval = 1023;
  }
  if(cmd == "li") { // Lids trimval (0-1023, 0 = auki, 1023 = kiinni)
    digitalWrite(LED_BUILTIN, HIGH);
    trimval = command.substring(2).toInt();
  } else {
    trimval = 1023;
  }
  if(cmd == "b") { // Blink
    digitalWrite(LED_BUILTIN, HIGH);
    switchval = LOW;
  } else {
    switchval = HIGH;
  }
  moveEyes();
  digitalWrite(LED_BUILTIN, LOW);

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
      } 
      else if (switchval == HIGH) {
        pwm.setPWM(4, 0, 240);
        pwm.setPWM(5, 0, 240);      
      }
      
  delay(dly);
}
