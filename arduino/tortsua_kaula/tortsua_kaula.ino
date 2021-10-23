#include <Servo.h>

// Utils
String command;
int dly = 200;
bool debug = false;
//bool debug = true;

// Kaula
Servo kaula_L;
Servo kaula_R;


void setup() {
  Serial.begin(9600);

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
  if (Serial.available()) {
    command = Serial.readStringUntil('\n');    
  }
  // Serial.println(command);
    moveKaula(command.toInt());
  }
  // Auto mode
  else {
    if(digitalRead(2)) moveKaula(random(0, 180));
  }
  kaula_L.write(0);
  kaula_R.write(0);
  delay(dly);
}

void moveKaula(int pos) {
  kaula_L.write(pos);
  kaula_R.write(pos);
  delay(dly);
}
