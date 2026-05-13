
void setup() {
pinMode(D7,OUTPUT);
Serial.begin(9600);
pinMode(D4,OUTPUT);
digitalWrite(D4,HIGH);
}

void loop() {
  Serial.println();
  Serial.println("Ok");
 digitalWrite(D7,LOW);
 digitalWrite(D4,LOW);

 delay(2000);

  digitalWrite(D7,HIGH);
   digitalWrite(D4,HIGH);
delay(2000);
}
