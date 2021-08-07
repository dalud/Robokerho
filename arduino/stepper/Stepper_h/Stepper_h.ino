#include <Stepper.h>


const int stepsPerRevolution = 20000; // 30725 = MAX: 14HS13-0804S-PG19
const int dly = 500;

Stepper myStepper(stepsPerRevolution, 8, 9);

void setup() {
  myStepper.setSpeed(10); //60: max for 14HS13-0804S-PG19 = 825Hz
}

void loop() {
  myStepper.step(stepsPerRevolution);
  delay(dly);

  myStepper.step(-stepsPerRevolution);
  delay(dly);
}
