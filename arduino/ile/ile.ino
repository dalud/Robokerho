// Tortsua eyes (USB from Rasp)

#include <Stepper.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

// Utils
String command; // The whole serial read
String cmd; // First 2 chars parsed
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

// Outputs
int suu = 8;
int niskat = 9;
int kasi_o = 10;
int kasi_v = 11;
int eyes = 12;


void setup() {
  Serial.begin(9600);

  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);

  pinMode(suu, OUTPUT);
  digitalWrite(suu, LOW);
  pinMode(niskat, OUTPUT);
  digitalWrite(niskat, LOW);
  pinMode(kasi_o, OUTPUT);
  digitalWrite(kasi_o, LOW);
  pinMode(kasi_v, OUTPUT);
  digitalWrite(kasi_v, LOW);
  pinMode(eyes, OUTPUT);
  digitalWrite(eyes, LOW);
 
  // Silmät
  pwm.begin();
  pwm.setPWMFreq(60);  // Analog servos run at ~60 Hz updates   
  
  delay(dly);
}


void loop(){  
  if (Serial.available()) {
    command = Serial.readStringUntil('\n');    
    //Serial.println(command);
    //delay(10);
    cmd = command.substring(0,2);
  }

  if(cmd == "z") {
    resetOthers();
  }

  // Eyes
  if(cmd == "ex") { // Eye X    
    xval = command.substring(2).toInt();
    // 0-1023 (lepo = 500)
    if(xval < 0) xval = 0;
    if(xval > 1023) xval = 1023;
  }
  if(cmd == "ey") { // Eye Y
    yval = command.substring(2).toInt();
    // 0-1023 (lepo = 500)
    if(yval < 0) yval = 0;
    if(yval > 1023) yval = 1023;
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
  if(cmd == "mo") { // Move others
    moveOthers();
  }
  moveEyes();
  // resetOthers();

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

void moveOthers() {
  digitalWrite(LED_BUILTIN, HIGH);
  digitalWrite(suu, HIGH);
  digitalWrite(niskat, HIGH);  
  digitalWrite(kasi_o, HIGH);
  digitalWrite(kasi_v, HIGH);
  digitalWrite
  delay(dly);
}

void resetOthers() {
  digitalWrite(LED_BUILTIN, LOW);
  digitalWrite(suu, LOW);
  digitalWrite(niskat, LOW);
  digitalWrite(kasi_o, LOW);
  digitalWrite(kasi_v, LOW);
  delay(100);
}
