#include <Servo.h>

Servo FrontControl;

void setup() {
  FrontControl.attach(2,500,2400);
  Serial.begin(9600);



}

void loop() {
  if (Serial.available() == 1){
  Serial.println();
  Serial.println("ENTER ANGLE");
  int inp = Serial.parseInt();
  int inu = map(inp,0,180,500,2400);
  FrontControl.write(inu);}
 
  

}
