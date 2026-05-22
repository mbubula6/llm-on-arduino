# LLM on Arduino (C++)

I used my code from [main.py](https://github.com/mbubula6/llm-on-arduino/blob/main/main.py) and changed it to C++ using ekhem Gemini.

Rewritten code got updated and we have working API connection, but we also need another file.

## Structure

Code for Arduino UNO without MicroPython got segmented into two: [lcd.ino](https://github.com/mbubula6/llm-on-arduino/blob/main/lcd.ino) for handling LCD and [python_api.py](https://github.com/mbubula6/llm-on-arduino/blob/main/python_api.py). I couldn't use MicroPython  because UNO doesn't have enough RAM, but Groq library works on Python only. That is why we separated our code.

### lcd.ino
In this file we use LiquidCrystal_I2C.h library for handling the LCD with I2C adapter. We need Wire.h for the same reason.

We set the sreen in `setup()` and then in `loop()` we listen if anything is sent using `Serial.available`, then we read first line.

If respnse is a two-liner, we slice it to two rows, either way we display it using `lcd.print()`.

### python_api.py

That is the more complicated file - we handle API here. 