void setup() {
  Serial.begin(9600);
  
  pinMode(2, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);

}

void loop() {
    if(!digitalRead(2)) {
      Serial.println(1);
      digitalWrite(LED_BUILTIN, HIGH);
    } else {
      Serial.println(0);
      digitalWrite(LED_BUILTIN, LOW);
    }
}
