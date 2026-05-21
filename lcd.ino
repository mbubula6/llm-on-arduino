#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

// Ustawienia: adres 0x27, 16 kolumn, 2 wiersze
// Jeśli tekst się nie pojawi, spróbuj zmienić adres na 0x3F
LiquidCrystal_I2C lcd(0x27, 16, 2); 

void setup() {
  // Inicjalizacja LCD
  lcd.init();
  
  // Włączenie podświetlenia
  lcd.backlight();
}

void loop() {
  lcd.clear();
  
  // Ustawienie kursora (kolumna, wiersz) - w Arduino liczymy od 0
  lcd.setCursor(0, 0);
  lcd.print("Hi!!!");
  
  lcd.setCursor(0, 1);
  lcd.print("There will be AI"); // Skrócone, bo "There will be an AI" ma 18 znaków (nie zmieści się w 16)

  // Czekaj 4 sekundy (4000 milisekund)
  delay(4000);
}