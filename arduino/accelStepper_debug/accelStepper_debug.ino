#include <AccelStepper.h>

AccelStepper stepper(1, 8, 9);
int speedo = 1500;
int maxi = 4000;

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
  stepper.setMaxSpeed(5000); //SPEED = Steps / second  
  stepper.setAcceleration(1000); //ACCELERATION = Steps /(second)^2    
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
    stepper.moveTo(maxi); // Parempi käyttää tätä kalibrointipisteiden kanssa
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
