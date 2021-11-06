#include <AccelStepper.h>

AccelStepper shoulder(1, 8, 9);
AccelStepper spreader(1, 10, 11);
AccelStepper elbow(1, 12, 13);
int speedo = 1500;

String command;

bool logita;
bool debug;
char poses[] = { 'z', 'e', 'h', 's', '1' };
int kiekka = 0;
// unsigned long start = millis();
// unsigned long elapsed;
// char buf[50];
// String stamp = ltoa(millis(), buf, 10);


void setup() {
  Serial.begin(9600); //defining some baud rate

  // Input signal
  pinMode(2, INPUT);
  // Zero switch
  pinMode(3, INPUT);

  // Built in LED
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);
  
  // Logita moottorin asennot?
  logita = false;
  //logita = true;

  // Run in debug mode
  //debug = true;
  debug = false;

  //Stepper parameters
  //setting up some default values for maximum speed and maximum acceleration
  shoulder.setMaxSpeed(5000); //SPEED = Steps / second  
  shoulder.setAcceleration(1000); //ACCELERATION = Steps /(second)^2    
  shoulder.setSpeed(speedo);
  
  spreader.setMaxSpeed(5000); //SPEED = Steps / second  
  spreader.setAcceleration(1000); //ACCELERATION = Steps /(second)^2    
  spreader.setSpeed(-speedo);

  elbow.setMaxSpeed(5000); //SPEED = Steps / second  
  elbow.setAcceleration(1000); //ACCELERATION = Steps /(second)^2    
  elbow.setSpeed(-5000);
  
  delay(500);
  //---------------------------------------------------------------------------
}

void loop() {
  kiekka++;  
  // Debug mode using serial commands
  if(debug) {
    if (Serial.available()) {
      command = Serial.readStringUntil('\n');
    }
  }
  //Serial.println(kiekka);
  //Serial.println(digitalRead(2));
  //Serial.println(command);
  // Auto mode
  if(digitalRead(2)) {
    // kiekka = 0;
    digitalWrite(LED_BUILTIN, HIGH);
    //Serial.println("NYT!!!!");
    // if(kiekka>200) {
    if(kiekka>5000) {  
      command = poses[random(sizeof(poses))];
      kiekka = 0;
    }    
  }
  //Serial.println(kiekka);
  //Serial.println(command);

  // Zero switch
  if(digitalRead(3)) {
    digitalWrite(LED_BUILTIN, LOW);
    //command = "z";
  }

  // Motion
  if(command == "z") {
    zeroMotors();
  }
  
  if(command == "h") { // Hail
    if(logita) Serial.println(shoulder.currentPosition());
    hail();
  }
  if(command == "s") { // Spreader
    if(logita) Serial.println(spreader.currentPosition());
    spreader.moveTo(-3000);
    spreader.run();    
  }
  if(command == "e") { // Elbow
    if(logita) Serial.println(elbow.currentPosition());
    elbow.moveTo(-6000);
    elbow.run();
  }
  if(command == "1") { // Pose1
    pose1();
  }
}

void zeroMotors() {
  shoulder.moveTo(0);
  shoulder.run();
  spreader.moveTo(0);
  spreader.run();
  elbow.moveTo(0);
  elbow.run();
}

void pose1() {
  shoulder.moveTo(4000);
  shoulder.run();
  spreader.moveTo(-3000);
  spreader.run();
  elbow.moveTo(-6000);
  elbow.run();
}

void hail() {
  shoulder.moveTo(4000); // Parempi käyttää tätä kalibrointipisteiden kanssa
  shoulder.run();
  spreader.moveTo(0);
  spreader.run();
  elbow.moveTo(0);
  elbow.run();
}
