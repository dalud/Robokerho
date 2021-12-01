#include <AccelStepper.h>

AccelStepper stepper(1, 8, 9);
int speedo = 20;
int maxi = 100;

String command;
bool logita;

void setup()
{
  //Serial Communication
  Serial.begin(9600); //defining some baud rate
  //---------------------------------------------------------------------------
  
  logita = false;

  //Stepper parameters
  //setting up some default values for maximum speed and maximum acceleration
  //stepper.setMinPulseWidth(15);
  stepper.setMaxSpeed(100); //SPEED = Steps / second  
  stepper.setAcceleration(10); //ACCELERATION = Steps /(second)^2    
  stepper.setSpeed(speedo);
  delay(500);
  //---------------------------------------------------------------------------
}

void loop() {
  if (Serial.available()) {
    command = Serial.readStringUntil('\n');
  }

  if(command == "h") { // Hail
    if(logita) Serial.println(stepper.currentPosition());
    stepper.moveTo(maxi);
    stepper.run();
  } else {
    stepper.moveTo(0);
    stepper.run();    
  }
  if(command == "r") { // Go round and around
    if(logita) Serial.println(stepper.currentPosition());
    stepper.setSpeed(speedo);
    stepper.runSpeed();
  }
}
