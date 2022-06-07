String command; // Whole serial read
String cmd; // First 2 chars parsed
int dly = 10;

// Outputs
int kaula = 3;
int ko = 8; // Kädet
int kv = 9;
int silmat = 10;

void setup() {
  Serial.begin(9600);
 
  // Kaula
  pinMode(kaula, OUTPUT);
  digitalWrite(kaula, LOW);

  // Kädet
  pinMode(ko, OUTPUT);
  digitalWrite(ko, LOW);
  pinMode(kv, OUTPUT);
  digitalWrite(kv, LOW);

  // Silmät
  pinMode(silmat, OUTPUT);
  digitalWrite(silmat, LOW);
  
  delay(dly);
}


void loop() {
  // Serial cmd
  if (Serial.available()) {
    command = Serial.readStringUntil('\n');
    cmd = command.substring(0,2);
    delay(dly);
  }

  if(cmd == "z") {
    resetMotors();
  }

  if(cmd == "mm") {
    moveArms();
    moveSilmat();
  }  
  
  if(cmd == "kv") {
    moveKaula();
  }

  delay(dly);
}

void resetMotors() {
  digitalWrite(kaula, LOW);
  digitalWrite(ko, LOW);
  digitalWrite(kv, LOW);
  digitalWrite(silmat, LOW);
  delay(dly);
}

void moveArms() {
  digitalWrite(ko, HIGH);
  digitalWrite(kv, HIGH);
  delay(dly);
}

void moveKaula() {
  digitalWrite(kaula, HIGH);
  delay(dly);
}

void moveSilmat() {
  digitalWrite(silmat, HIGH);
  delay(dly);
}
