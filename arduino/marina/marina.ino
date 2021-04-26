#include <LiquidCrystal.h>

String command;
boolean led;

LiquidCrystal lcd(2,3,4,5,6,7);


void setup() {
 lcd.begin(16, 2);
 lcd.setCursor(0,0);
 
 pinMode(LED_BUILTIN, OUTPUT);
 
 Serial.begin(9600);
}

void loop(){
  if (Serial.available()) {
    command = Serial.readString();
  }
  if(command == "on") ledOn();
  if(command == "off") ledOff();
  if(command == "clr") {
    lcd.clear();
    command = "";
  }
  
  sout(command);
  
  lcd.setCursor(0,1);
  // lcd.print(millis());  
}

void sout(String message) {
  lcd.setCursor(0,0);
  if(message.length() > 16) {
    String scd = message.substring(16);
    lcd.print(message);
    lcd.setCursor(0,1);
    lcd.print(scd);
  } else lcd.print(message);
}

void ledOn() {
  digitalWrite(LED_BUILTIN, HIGH);
}

void ledOff() {
  digitalWrite(LED_BUILTIN, LOW);
}
