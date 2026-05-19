# LLM on Arduino (technically)

This project's main idea is not to install a LLM on Arduino locally (my Arduino too small T-T) but to call the API and show communication on the 16x2 LCD I2C. I hadn't figured out yet how to comminicate with it rather than just display answers but we'll get there. (Maybe using a rotary encoder and a button? (I mean those I have))

## Introduction (tools)

Okay, so I have used Arduino IDE and programmed C# already, but since I work with AI and people do AI in Python we will be switching sides. I mean, broadening my skills. So we will be using:
- **Arduino UNO** microcontroller (I'll check the number later)
- **Python** (duh)
- **MicroPython** Python implementation for microcontrollers
- **Arduino IDE** for installing MicroPython on da device
- **Thonny IDE** as the main IDE
- **DIYables_MicroPython_LCD_I2C** library for LCD screen use

And here I would like to spare a minute for DIYables and this repo [DIYables_MicroPython_LCD_I2C](https://github.com/DIYables/DIYables_MicroPython_LCD_I2C). I mostly learned from that and their tutorials linked.

## Setup (virtual)

Okay we need to start with installing MicroPython on da board. Again, a full tutorial is provided here: [Arduino MicroPython Getting Started](https://newbiely.com/tutorials/arduino-micropython/arduino-micropython-getting-started) (at least this the one I've been using)

1. Installing MicroPython on Arduino

Open Arduino IDE, connect your board, install Giga Board Package on it (using Boards Manager).

Get the [MicroPython installer](https://github.com/arduino/lab-micropython-installer/releases/tag/v1.4.0) for your operating system and run it while your board is connected.

You have MicroPython on your Arduino!

2. Install Thonny and setup

*I guess you can do it using casual VSC but I don't know how yet.*

You can find Thonny [here](https://thonny.org/), again install for your operating system. (I mean You can install it for different one but why for)

Open the IDE and in Tools > Options > Interpreter choose MicroPython (generic) and then Port, it should look something like: Giga Virtual Common Port something (smart people say COM33 for Windows, /dev/tty/ACM0 for Linux).

You have place to work with MicroPython on your Arduino!

3. Okay I thought the setup will be longer nvm.

## Coding

## No lol

## Physical setup

I mean - connect GND on your LCD with GND on your board, then 5V, then SDA and SCL. (They are labeled You're gonna be fine)

You have your screen connected to your Arduino with which you can work using Thonny and on which you have MicroPython! Congrats!

And connect it to your PC/Laptop/whatever you code on if You haven't already (that would be concerning).

## Coding

Finally! Right? But setup first.

### Coding setup

We will need libraries. The important ones are there already, but the most important one we need to install. Install DIYables-MicroPython-LCD-I2C using Tools > Manage packages in Thonny or in other preffered way.

We need also: I2C, Pin, utime, so:

```
from machine import I2C, Pin
from DIYables_MicroPython_LCD_I2C import LCD_I2C
import utime
```

And now we're done!
If you know how to use it, go straight to code here.
If not, we will work through this together and I will explain things. But the main problems are over.

*explanation*
<sup>*will happen after the code*</sup>

The main code is pretty self-explanatory, it is commented in the [main.py](https://github.com/mbubula6/llm-on-arduino/blob/main/main.py) file. However we have the library functions for setting up the LCD, I2C and displaying text on screen there (all labeled and in first few rows).

## Coding AI

### Setup again?

Okay, so as You know, one has to have an API key to call the given LLM. Some companies are giving some tokens for free to have fun in personal projects. When I first made an AI chatbot in C#, I used Groq (not to confuse with Grok) so I will use it here as well.

You shall go to [groq.com](https://groq.com/) and log in, then go to API keys > create API key. That is pretty much it.

Copy the key and best You can do is put it in the `.env` file in a telling variable (like `API_KEY = "..."`). DO NOT FORGET TO PUT .ENV IN .GITIGNORE. So yeah, if You don't know it yet, to make sure that your API key (and other private stuff) is not public on GitHub, You shall use `.gitignore` file and mention private stuff there e.g.:
```.env #.env file with secrecy will be ignored while pushing to GitHub```

### Using the API key

For Groq specifically, documentation for us this page: [Groq Quickstart](https://console.groq.com/docs/quickstart).

But so far all we need is this:
```
from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama-3.3-70b-versatile",
)
```
 
 Replace the GROQ_API_KEY with your key or with the name of the variable we created in the `.env` file (API_KEY) and then we work.



Martyna Bubula github.com/mbubula6