import os
import time
import serial
from groq import Groq
import dotenv

dotenv.load_dotenv()

# --- PORT CONFIGURATION ---
# Enter the port where your Arduino Uno is visible on the system.
# Check it in the Arduino IDE (e.g. 'COM3' on Windows or '/dev/ttyACM0' on Linux/Mac)
PORT_ARDUINO = 'COM6' 

try:
    arduino = serial.Serial(port=PORT_ARDUINO, baudrate=9600, timeout=1)
    time.sleep(2) # Short pause to establish the connection
    print("Connected to Arduino!")
except Exception as e:
    print(f"Error connecting to port {PORT_ARDUINO}: {e}")
    exit()

# --- GROQ QUERY ---
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

print("Sending request to Groq...")

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are an assistant connected to a tiny 16x2 LCD screen. Your response MUST be under 32 characters total, short and concise. Do not use punctuation if not needed."
        },
        {
            "role": "user",
            "content": "say something nice to the user on the LCD screen1",
        }
    ],
    model="llama-3.3-70b-versatile",
)

ai_text = chat_completion.choices[0].message.content
print(f"AI response: {ai_text}")

# --- SENDING TO ARDUINO ---
# Send the text encoded in ASCII with '\n' appended so Arduino knows where the end is
formatted_text = f"{ai_text}\n"
arduino.write(formatted_text.encode('ascii', errors='ignore'))

print("Sent to Arduino!")
arduino.close()