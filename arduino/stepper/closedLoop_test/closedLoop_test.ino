int dly = 100;
int x = 0;
int max = 6400;

void setup() { 
  // Polvi
  pinMode(6, OUTPUT);
  pinMode (7, OUTPUT);

  digitalWrite(6, HIGH);
 }
 
void loop() {
  
}

void movePolvi() {
  digitalWrite(7, HIGH);
  delayMicroseconds(dly);
  digitalWrite(7, LOW);
  delayMicroseconds(dly); 
  x++;

  if(x > max) {
    digitalWrite(6, LOW);
    x = 0;
  }  
}
