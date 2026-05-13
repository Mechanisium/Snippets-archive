#include <Servo.h>
Servo Servi;


void setup() {
Servi.attach(D4,500,2400);


}

void loop() {
  Servi.write(500);
  delay(500);
  Servi.write(1000);
  delay(500);
  Servi.write(1500);
  delay(500);
  Servi.write(2400);
  delay(500);


}
