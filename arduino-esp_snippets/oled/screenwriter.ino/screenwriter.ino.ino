#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define OLED_RESET -1
#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);




void setup() {
 display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
 display.clearDisplay();
delay(100);
}

void loop() {
  display.setTextSize(2.75);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0,0);
  display.println("BULLSHIT");
  display.display();
  delay(500);
}
