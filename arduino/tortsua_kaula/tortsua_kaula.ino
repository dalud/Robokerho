#include <Servo.h>

// Utils
String command;
int dly = 250;
bool debug = false;
//bool debug = true;

// Kaula moottorit
Servo kaula_L;
Servo kaula_R;


void setup() {
  Serial.begin(9600);

  // Debug LED
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);

  // Input signal
  pinMode(2, INPUT);
    
  kaula_L.attach(3);
  kaula_R.attach(4);
  kaula_L.write(0);
  kaula_R.write(0);

  delay(dly);
}

void loop() {
  // Debug using serial commands
  if(debug) {
    // Monitor input
    // Serial.println(digitalRead(2));
    if (Serial.available()) {
      command = Serial.readStringUntil('\n');    
    }
    // Serial.println(command);
    moveKaula(command.toInt());
  }
  // Auto mode
  else {
    if(digitalRead(2)) {
      digitalWrite(LED_BUILTIN, HIGH);
      moveKaula(random(0, 180));
    } else {
      digitalWrite(LED_BUILTIN, LOW);
      kaula_L.write(0);
      kaula_R.write(0);   
    }    
  }
  delay(dly);
}

void moveKaula(int pos) {
  kaula_L.write(pos);
  kaula_R.write(pos);
  delay(dly);
}
