#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

const char* ssid = "ssid";
const char* password = "pass";

const char* serverURL = "http://<PC_IP>:5000/button";

void setup() {
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) delay(500);
}

void loop() {
  while (WiFi.status() == WL_CONNECTED){
    digitalWrite(D4,HIGH);
    delay(500);
    digitalWrite(D4,LOW);
  }
}
