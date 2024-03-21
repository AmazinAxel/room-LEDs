# 💡 micro:bit LED controller

This Python script uses a micro:bit as a controller to send signals to an LED strip. The micro:bit display is used to show a preview of the mode and color.

## Background history (why?)

I got this inexpensive LED strip as an arcade prize, but didn't like the limited functionality of the janky IR remote. It didn't have ambient color-fading abilities and I didn't like the pre-defined colors. I use this LED strip around my bed backboard for ambiance to make the atmosphere cozier. A micro:bit is an inexpensive controller and provides a 5x5 LED matrix display to show a preview of the selected theme, along with two buttons that are used to toggle the theme. The touch-capacative logo is used for enabling the rainbow fade mode, similar to what is seen on the remote.

## ❓ How it works / how to set it up

My LED strip has 4 pins for R, G, and B input and a single (3V?) power input.

To set it up, connect pin0 (micro:bit) to the R pin (LED strip), pin1 to G pin, pin2 to B pin, and 3V (micro:bit) to the + (LED strip). Use the micro:bit left & right buttons to switch between presets.

The micro:bit just writes data out through the pins to tell the LED strip what color it should display.

If you want a permanent LED setup, you can use gator clips, pins, and electrical tape to attach the wires to the microbit, like this: 

(attach image here)
