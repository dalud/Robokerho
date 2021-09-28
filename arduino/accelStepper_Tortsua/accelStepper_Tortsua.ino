#include <AccelStepper.h>

AccelStepper shoulder(1, 8, 9);
AccelStepper spreader(1, 10, 11);
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
  shoulder.setMaxSpeed(5000); //SPEED = Steps / second  
  shoulder.setAcceleration(1000); //ACCELERATION = Steps /(second)^2    
  shoulder.setSpeed(speedo);
  
  spreader.setMaxSpeed(5000); //SPEED = Steps / second  
  spreader.setAcceleration(1000); //ACCELERATION = Steps /(second)^2    
  spreader.setSpeed(speedo);
  delay(500);
  //---------------------------------------------------------------------------
}

void loop() {
  if (Serial.available()) {
    command = Serial.readStringUntil('\n');
  }

  if(command == "z") {
    zeroMotors();
  }
  
  if(command == "h") { // Hail
    if(logita) Serial.println(shoulder.currentPosition());
    shoulder.moveTo(maxi); // Parempi käyttää tätä kalibrointipisteiden kanssa
    shoulder.run();
  }
  if(command == "s") { // Spread
    if(logita) Serial.println(spreader.currentPosition());
    spreader.moveTo(maxi);
    spreader.run();    
  }
  if(command == "r") { // Go round and around
    if(logita) Serial.println(shoulder.currentPosition());
    shoulder.setSpeed(speedo);
    shoulder.runSpeed();
  }
}

void zeroMotors() {
  shoulder.moveTo(0);
  shoulder.run();
  spreader.moveTo(0);
  spreader.run();  
}
