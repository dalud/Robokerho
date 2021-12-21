#include <Servo.h>

// Utils
String command;
int dly = 100;
bool debug = false;
//bool debug = true;


void setup() {
  Serial.begin(9600);
  
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);   

  // Input signal
  pinMode(2, INPUT);
    
  // Kaula
  pinMode(6, OUTPUT);
  digitalWrite(6, LOW);   
  pinMode(7, OUTPUT);
  digitalWrite(7, LOW);   


  delay(dly);
}

void loop() {
  // Debug using serial commands
  if(debug) {
    if (Serial.available()) {
      command = Serial.readStringUntil('\n');    
  }
  // Serial.println(command);
  // moveKaula(command.toInt());
  }
  // Auto mode
  else {
    if(digitalRead(2)) {
      digitalWrite(LED_BUILTIN, HIGH);
      moveKaula();
      // moveKaesi();
    } else {
      digitalWrite(LED_BUILTIN, LOW);
      resetKaula();
    }
    
  }
  delay(dly);
}

void moveKaula() {
  digitalWrite(6, HIGH);
  digitalWrite(7, HIGH);
}

void resetKaula() {
  digitalWrite(6, LOW);
  digitalWrite(7, LOW);
}
