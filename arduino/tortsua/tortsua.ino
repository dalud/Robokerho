//  #include <Stepper.h>

// Utils
String command; // The whole serial read
String cmd; // First 2 chars parsed
const int dly = 10;

// Outputs
int suu = 8;
int niskat = 9;
int kasi_o = 10;
int kasi_v = 11;
int silmat = 12;


void setup() {
  Serial.begin(9600);

  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);

  pinMode(suu, OUTPUT);
  digitalWrite(suu, LOW);
  pinMode(niskat, OUTPUT);
  digitalWrite(niskat, LOW);
  pinMode(kasi_o, OUTPUT);
  digitalWrite(kasi_o, LOW);
  pinMode(kasi_v, OUTPUT);
  digitalWrite(kasi_v, LOW);
  pinMode(silmat, OUTPUT);
  digitalWrite(silmat, LOW);
 
  delay(dly);
}


void loop(){  
  if (Serial.available()) {
    command = Serial.readStringUntil('\n');    
    //Serial.println(command);
    //delay(10);
    cmd = command.substring(0,2);
  }

  if(cmd == "z") {
    resetOthers();
  }
  if(cmd == "mo") { // Move others
    moveOthers();
  }

  delay(dly);
}

void moveOthers() {
  digitalWrite(LED_BUILTIN, HIGH);
  digitalWrite(suu, HIGH);
  digitalWrite(niskat, HIGH);  
  digitalWrite(kasi_o, HIGH);
  digitalWrite(kasi_v, HIGH);
  digitalWrite(silmat, HIGH);
  delay(dly);
}

void resetOthers() {
  digitalWrite(LED_BUILTIN, LOW);
  digitalWrite(suu, LOW);
  digitalWrite(niskat, LOW);
  digitalWrite(kasi_o, LOW);
  digitalWrite(kasi_v, LOW);
  digitalWrite(silmat, LOW);
  delay(dly);
}
  
