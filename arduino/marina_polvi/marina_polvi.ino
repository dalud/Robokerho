int reverseSwitch =   2;  // Push button for reverse
int driverPUL = 7;    // PUL- pin
int driverDIR = 6;    // DIR- pin
int spd = A0;     // Potentiometer
 
// Variables
 
int pd = 500;       // Pulse Delay period
boolean setdir = LOW; // Set Direction
 
// Interrupt Handler
 
void revmotor (){
  setdir = !setdir;
}
 
 
void setup() { 
   pinMode(LED_BUILTIN, OUTPUT);
   digitalWrite(LED_BUILTIN, LOW);
   
  // Input signal
  pinMode(8, INPUT);

  // Polvi
  pinMode (driverPUL, OUTPUT);
  pinMode (driverDIR, OUTPUT);
  attachInterrupt(digitalPinToInterrupt(reverseSwitch), revmotor, FALLING);

  // Kaula
  pinMode(9, OUTPUT);
  digitalWrite(9, LOW);
  pinMode(10, OUTPUT);
  digitalWrite(10, LOW);
}
 
void loop() {
  if(digitalRead(8)) {
    digitalWrite(LED_BUILTIN, HIGH);
    movePolvi();
    moveKaula();
  } else {
    digitalWrite(LED_BUILTIN, LOW); 
    resetMotors();
  }
    
}

void movePolvi() {  
  pd = map((analogRead(spd)),0,1023,2000,50);
  digitalWrite(driverDIR,setdir);
  digitalWrite(driverPUL,HIGH);
  delayMicroseconds(pd);
  digitalWrite(driverPUL,LOW);
  delayMicroseconds(pd); 
}

void moveKaula() {
  digitalWrite(9, HIGH);
  digitalWrite(10, HIGH);
}

void resetMotors() {
  digitalWrite(9, LOW);
  digitalWrite(10, LOW);
}
