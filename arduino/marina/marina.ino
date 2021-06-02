#include <Servo.h>

String command;
boolean led;
Servo mouth;

void setup() {
 pinMode(LED_BUILTIN, OUTPUT);
 mouth.attach(9); 
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
  moveMouth(command.toInt());
  delay(25);
}

void moveMouth(int pos) {
  mouth.write(pos);
  if(pos){
    ledOn();
  } else {
    ledOff();
  }
}

void ledOn() {
  digitalWrite(LED_BUILTIN, HIGH);
}

void ledOff() {
  digitalWrite(LED_BUILTIN, LOW);
}
