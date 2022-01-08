//int reverseSwitch =   2;  // Push button for reverse
int driverPUL = 12;    // PUL- pin
int driverDIR = 13;    // DIR- pin
//int spd = A0;     // Potentiometer
 
// Variables
 
int pd = 100;       // Pulse Delay period
boolean setdir = LOW; // Set Direction
 
// Interrupt Handler
 
/*void revmotor (){
  setdir = !setdir;
}*/
 
 
void setup() { 
   pinMode(LED_BUILTIN, OUTPUT);
   digitalWrite(LED_BUILTIN, LOW);
   
  // Input signal
  pinMode(2, INPUT);

  // Polvi
  pinMode (driverPUL, OUTPUT);
  pinMode (driverDIR, OUTPUT);
  //attachInterrupt(digitalPinToInterrupt(reverseSwitch), revmotor, FALLING);
}
 
void loop() {
  //if(1 == 1) {
  if(digitalRead(2)) {
    digitalWrite(LED_BUILTIN, HIGH);
    movePolvi();

  } else {
    digitalWrite(LED_BUILTIN, LOW); 
    resetMotors();
  }
}

void movePolvi() {  
  //pd = map((analogRead(spd)),0,1023,2000,50);
  digitalWrite(driverDIR,setdir);
  digitalWrite(driverPUL,HIGH);
  delayMicroseconds(pd);
  digitalWrite(driverPUL,LOW);
  delayMicroseconds(pd); 
}

void resetMotors() {
  digitalWrite(9, LOW);
  digitalWrite(10, LOW);
}
