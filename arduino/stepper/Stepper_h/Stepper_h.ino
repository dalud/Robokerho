#include <Stepper.h>


const int stepsPerRevolution = 30750; // 14HS13-0804S-PG19
const int dly = 500;

Stepper myStepper(stepsPerRevolution, 8, 9);

void setup() {
  myStepper.setSpeed(60); //speed is in RPM;
}

void loop() {
  myStepper.step(stepsPerRevolution);
  delay(dly); //the delay time between turns;

  myStepper.step(-stepsPerRevolution);
  delay(dly);
}
