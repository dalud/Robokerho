int DIR = 2;
int PUL = 3;

int dly = 2000;

void setup() {
  pinMode(DIR, OUTPUT);
  pinMode(PUL, OUTPUT);
}

void loop() {
  digitalWrite(PUL, HIGH);
  delayMicroseconds(dly);
  digitalWrite(PUL, LOW);
  delayMicroseconds(dly);
}
