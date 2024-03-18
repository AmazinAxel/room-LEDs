# 💡 Desk LED controller

This Python script uses a micro:bit as a controller to send signals to an LED strip. The micro:bit display is used to show a preview of the mode and color.

# Background history (why?)

I got this inexpensive LED strip as an arcade prize, but didn't like the limited functionality of the funky IR remote. I use this LED strip around my desk for ambiance to make my atmosphere cozier depending on the type of vibe I'm trying to create, like a focus vibe, gaming vibe, or a chill vibe. I had a micro:bit laying around so I decided to use it as an easy way to change the LED colors using the micro:bit display.

# ❓ How it works / how to set it up

My LED strip has 4 pins for R, G, and B input and a single (3V?) power input.

To set it up, connect pin0 (micro:bit) to the R pin (LED strip), pin1 to G pin, pin2 to B pin, and 3V (micro:bit) to the + (LED strip). Use the micro:bit left & right buttons to switch between presets.

The micro:bit just writes data out through the pins to tell the LED strip what color it should display.

# ⛰️ What it looks like

Insert image here (not finished)
