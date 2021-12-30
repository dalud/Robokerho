String command;

int dly = 10; // Universal delay. Scale down to speed motor functions up
float pause = 10; // Audio amplitude interpreted as silence
int amp;
// Kädet
int ko = 10;
int kv = 11;


void setup() {
 Serial.begin(9600);
 
 pinMode(LED_BUILTIN, OUTPUT);
 // pinMode(8, OUTPUT); // Niskat
 // pinMode(9, OUTPUT); // Polvi
 pinMode(ko, OUTPUT);
 pinMode(kv, OUTPUT);
 digitalWrite(ko, LOW);
 digitalWrite(kv, LOW);
 
 delay(500);
}

void loop(){
  if (Serial.available()) {
    command = Serial.readStringUntil('\n');
  }
  // Serial.println(command);
  String cmd = command.substring(0,2);
  
  if(cmd == "mo") { // Move Others
    // movePolvi();
    moveKadet();
    
    // Move niskat only when speaking
    amp = command.substring(2).toInt();
    if (amp > pause) {
      // moveNiskat();
    }
  } else {
    resetAll();
  }

  delay(dly);
}

void resetAll() {
  digitalWrite(LED_BUILTIN, LOW);
  // digitalWrite(8, LOW);
  // digitalWrite(9, LOW);
  digitalWrite(ko, LOW);
  digitalWrite(kv, LOW);
}

void movePolvi() {
  digitalWrite(LED_BUILTIN, HIGH);
  digitalWrite(9, HIGH);
}

void moveNiskat() {
  digitalWrite(8, HIGH);
}

void moveKadet() {
  digitalWrite(ko, HIGH);
  digitalWrite(kv, HIGH);
}
