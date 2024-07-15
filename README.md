# 💡 micro:bit LED controller

This Python script uses a micro:bit as a controller to send signals to an LED strip. The micro:bit display is used to show a preview of the mode and color.

This LED strip was recieved as an arcade prize and came with a cheap remote. The janky IR remote didn't have ambient color-fading abilities and I wanted better pre-defined colors. I use this LED strip around my desk for ambiance. A micro:bit is an inexpensive controller and provides a 5x5 LED matrix display to show a preview of the selected theme, along with two buttons that are used to toggle the theme. The touch-capacative logo is used for enabling the rainbow mode, similar to what is seen as the "fade" setting on the remote. *(not finished)*

## 🔨 How to use

My LED strip has 4 pins for R, G, and B input and a single (3V?) power input.

Connect pin0 (micro:bit) to the R pin (LED strip), pin1 to G pin, pin2 to B pin, and 3V (micro:bit) to the "+" (power input for the LED strip). Use the micro:bit's left & right buttons to switch between presets.

The micro:bit acts like the controller: it writes data out through the pins to tell the LED strip what color it should display.

If you want a permanent setup, you can use gator clips, pins, and electrical tape to attach the wires to the microbit (or solder it) 

This is **NOT** written in Makecode Python as it has slightly different syntax. For modification and flashing, please use the [Microbit Python Editor](python.microbit.org)
