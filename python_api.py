import os
import time
import serial  # biblioteka pyserial
from groq import Groq
import dotenv

dotenv.load_dotenv()

# --- KONFIGURACJA PORTU ---
# Musisz wpisać port, pod którym widoczne jest Twoje Arduino Uno w systemie.
# Sprawdź go w Arduino IDE (np. 'COM3' na Windowsie lub '/dev/ttyACM0' na Linux/Mac)
PORT_ARDUINO = 'COM3' 

try:
    arduino = serial.Serial(port=PORT_ARDUINO, baudrate=9600, timeout=1)
    time.sleep(2) # Krótka pauza na ustanowienie połączenia
    print("Połączono z Arduino!")
except Exception as e:
    print(f"Błąd połączenia z portem {PORT_ARDUINO}: {e}")
    exit()

# --- ZAPYTANIE DO GROQ ---
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

print("Wysyłam zapytanie do Groq...")

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are an assistant connected to a tiny 16x2 LCD screen. Your response MUST be under 30 characters total, short and concise. Do not use punctuation if not needed."
        },
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama-3.3-70b-versatile",
)

ai_text = chat_completion.choices[0].message.content
print(f"Odpowiedź z AI: {ai_text}")

# --- WYSYŁANIE DO ARDUINO ---
# Wysyłamy tekst zakodowany w ASCII z dopiskiem '\n', żeby Arduino wiedziało, gdzie jest koniec
formatted_text = f"{ai_text}\n"
arduino.write(formatted_text.encode('ascii', errors='ignore'))

print("Wysłano do Arduino!")
arduino.close()