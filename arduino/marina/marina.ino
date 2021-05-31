// #include <LiquidCrystal.h>
#include <Servo.h>

String command;
boolean led;
Servo myservo;

void setup() {
 pinMode(LED_BUILTIN, OUTPUT);
 myservo.attach(9); 
 Serial.begin(9600);
}

void loop(){
  if (Serial.available()) {
    command = Serial.readStringUntil('\n');
  }
  /*if(command == "on") ledOn();
  if(command == "off") ledOff();
  if(command == "clr") {
    // lcd.clear();
    command = "";
  }*/
  
  // Serial.println("command:" + command);
  sout(command.toInt());
  delay(100);
}

void sout(int pos) {
  myservo.write(pos+90);
  if(pos){
    ledOn();
  } else {
    ledOff();
  }
  // delay(100);
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
