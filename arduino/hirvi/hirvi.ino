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
int ro = 350; // Right eye open
int rc = 240; // closed
int lo = 240;
int lc = 390;
int trimval;
int switchval = 0;

// Outputs
int suu = 22;


void setup() {
  Serial.begin(9600);

  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);

  pinMode(suu, OUTPUT);
  digitalWrite(suu, LOW);
  
  // Silmät
  pwm.begin();
  pwm.setPWMFreq(60);  // Analog servos run at ~60 Hz updates   
  
  delay(dly);
}


void loop(){  
  if (Serial.available()) {
    command = Serial.readStringUntil('\n');    
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
    trimval = 500;
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

  delay(dly);
}

void moveEyes() {
  // Eye read
  lexpulse = map(xval, 0,1023, 270, 390);
  rexpulse = lexpulse;
    
  leypulse = map(yval, 0,1023, 280, 400);
  reypulse = map(yval, 0,1023, 400, 280);

  pwm.setPWM(0, 0, lexpulse);
  pwm.setPWM(1, 0, leypulse);
  pwm.setPWM(2, 0, rexpulse);
  pwm.setPWM(3, 0, reypulse); 

  // Blink
  if (switchval == LOW) {
    // Oikea silmä
    pwm.setPWM(4, 0, rc);
    pwm.setPWM(5, 0, rc);
    // Vasen
    pwm.setPWM(6, 0, lc);
    pwm.setPWM(7, 0, lc); 
  } else if (switchval == HIGH) {
    // Invers?
    pwm.setPWM(4, 0, ro);
    pwm.setPWM(5, 0, ro);
    pwm.setPWM(6, 0, lo);
    pwm.setPWM(7, 0, lo);
  }      
  delay(dly);
}

void moveOthers() {
  digitalWrite(LED_BUILTIN, HIGH);
  digitalWrite(suu, HIGH);
  delay(dly);
}

void resetOthers() {
  digitalWrite(LED_BUILTIN, LOW);
  digitalWrite(suu, LOW);
  delay(dly);
}
