#include <ESP8266WiFi.h>
#include <Servo.h>
Servo Servi;
int bled=D4;
WiFiClient p;
WiFiServer  s(80);
void setup() {
  pinMode(bled,OUTPUT);
  pinMode(16,OUTPUT);

WiFi.begin("redtv (NCNTV)","sandeep@123");
Serial.begin(9600);
while(WiFi.status() != WL_CONNECTED){
  digitalWrite(bled,HIGH);
  delay(1000);
  digitalWrite(bled,LOW);
  delay(500);
  s.begin();
  Serial.println();
  Serial.println(WiFi.localIP());
  digitalWrite(16,HIGH);
  Servi.attach(2);
}
}

void loop() {
  p = s.available();
  if (p == 1) {
  String request = p.readStringUntil('\n');
  Serial.println(request);
  request.trim();
  if (request == "GET /1 HTTP/1.1")
  {digitalWrite(16,LOW);
  Servi.write(180);
  }
   if (request == "GET /0 HTTP/1.1")
   {digitalWrite(16,HIGH);
   Servi.write(0);}

  p.println("ok");
  
  }
  


}
