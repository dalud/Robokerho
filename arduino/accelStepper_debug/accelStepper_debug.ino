#include <AccelStepper.h>

AccelStepper stepper(1, 8, 9);
int speedo = 1500;
int maxi = 2000; // 8000 is full 360*

String command;
bool logita;

void setup()
{
  //Serial Communication
  Serial.begin(9600); //defining some baud rate
  //---------------------------------------------------------------------------
  
  logita = true;
  Serial.println(logita);  

  //Stepper parameters
  //setting up some default values for maximum speed and maximum acceleration
  stepper.setMaxSpeed(5000); //SPEED = Steps / second  
  stepper.setAcceleration(1000); //ACCELERATION = Steps /(second)^2    
  //speedo = 1500;
  stepper.setSpeed(speedo);
  delay(500);
  //---------------------------------------------------------------------------

}

void loop() {
  if (Serial.available()) {
    command = Serial.readStringUntil('\n');
  }

  if(command == "s") {
    /*stepper.runSpeed(); //step the motor (this will step the motor by 1 step at each loop indefinitely)
    if(logita) Serial.println(stepper.currentPosition());
    if(stepper.currentPosition() > maxi) {
      stepper.setSpeed(-speedo);
    } else if(stepper.currentPosition() < 1) stepper.setSpeed(speedo);*/
    // moveStepper(stepper);
    stepper.moveTo(maxi); // Parempi käyttää tätä kalibrointipisteiden kanssa
    stepper.run();
  } else {
    stepper.moveTo(0);
    stepper.run();    
  }
}

// TODO: pointer or whatever as parameter ???
void moveStepper(AccelStepper motor) {
  motor.runSpeed(); //step the motor (this will step the motor by 1 step at each loop indefinitely)
    if(logita) Serial.println(motor.currentPosition());
    if(motor.currentPosition() > maxi) {
      motor.setSpeed(-speedo);
    } else if(motor.currentPosition() < 0) motor.setSpeed(speedo);
}
