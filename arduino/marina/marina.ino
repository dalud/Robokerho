// #include <LiquidCrystal.h>
#include <Servo.h>

String command;
boolean led;
Servo myservo;
// int pos = 0;

// LiquidCrystal lcd(2,3,4,5,6,7);


void setup() {
 /*lcd.begin(16, 2);
 lcd.setCursor(0,0);*/
 
 pinMode(LED_BUILTIN, OUTPUT);
 myservo.attach(9); 
 Serial.begin(9600);
}

void loop(){
  if (Serial.available()) {
    command = Serial.readString();
  }
  if(command == "on") ledOn();
  if(command == "off") ledOff();
  if(command == "clr") {
    // lcd.clear();
    command = "";
  }
  
  sout(command.toInt());
  
  // lcd.setCursor(0,1);
  // lcd.print(millis());   
}

void sout(int pos) {
  myservo.write(pos+90);
  if(pos){
    ledOn();
  } else {
    ledOff();
  }
  delay(15)
}

void ledOn() {
  digitalWrite(LED_BUILTIN, HIGH);
}

void ledOff() {
  digitalWrite(LED_BUILTIN, LOW);
}
/*void loop() {
  for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
                  // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
}*/
