# Room-LEDs by AmazinAxel (Alec) 2024
# Licensed under the GNU GPLv3 license (do whatever u want)

from microbit import *
from time import sleep

# 0 means it's on full-bright
# 1023 means its basically off

# TODO: Finish rainbow mode

theme, screenTimeout = 0, 0
totalThemes = 9 # Total amount of themes
red, green, blue = 1023, 1023, 1023
rainbowMode = False 


def changeTheme(goForward):
    global theme, screenTimeout, rainbowMode
    if screenTimeout != -1:
        if goForward == True:
            if theme == totalThemes: # Rollback to the first theme
                theme = 0
            theme += 1
        else:
            if theme == 1: # Rollback to the last theme
                theme = totalThemes + 1
            theme -= 1
        fadeOutLEDs()
        sleep(0.1) # Wait for fade out to be done
    rainbowMode = False

    screenTimeout = 250 # 1.5 second screen timeout
    # Unfortunately the m:b python version doesn't support match case statements
    # so we have to use if else statements for now :(
    
    if theme == 1: # Ocean Blue
        # Image of a wave
        fadeInLEDs('00000:'
                   '07700:'
                   '50880:'
                   '00099:'
                   '99999')

        fadeToColor([0, 500, 1023])
        
    elif theme == 2: # Sunny Yellow
        # Image of a sun
        fadeInLEDs('60606:'
                   '07770:'
                   '67976:'
                   '07770:'
                   '60606')

        fadeToColor([1023, 300, 0])
        
    elif theme == 3: # Dreary Gray
        # Image of a cloud
        fadeInLEDs('00000:'
                   '00033:'
                   '05577:'
                   '77889:'
                   '99999')

        fadeToColor([0, 0, 0])
        
    elif theme == 4: # Sandy White
        # Image of a sandy beach
        fadeInLEDs('05000:'
                   '79700:'
                   '89800:'
                   '09036:'
                   '99999')

        fadeToColor([500, 200, 500])

    
    elif theme == 5: # Fiery Red
        # Image of a flame
        fadeInLEDs('05000:'
                   '06605:'
                   '67766:'
                   '78980:'
                   '08980')

        fadeToColor([0, 1023, 1023])
        
    elif theme == 6: # Maroon Red
        # Image of an apple
        fadeInLEDs('00060:'
                   '07800:'
                   '78987:'
                   '88988:'
                   '07070')

        fadeToColor([0, 200, 200])
        
    elif theme == 7: # Lucky Green
        # Image of a 4-leaf clover
        fadeInLEDs('77077:'
                   '77377:'
                   '03830:'
                   '77377:'
                   '77077')

        fadeToColor([300, 0, 600])

    elif theme == 8: # Chill Blue
        # Image of a cool looking thing
        fadeInLEDs('07070:'
                   '50905:'
                   '00000:'
                   '07070:'
                   '50905')

        fadeToColor([900, 0, 900])
        
    elif theme == 9: # Electric Blue
        # Image of an electric bolt
        fadeInLEDs('00060:'
                   '00800:'
                   '09990:'
                   '00800:'
                   '06000')

        fadeToColor([1023, 0, 1023])

    print(theme)        

def fadeToColor(colors):
    global red, green, blue
    while True:
        if red < colors[0]:
            red += 1
        elif red > colors[0]:
            red -= 1
            
        if green < colors[1]:
            green += 1
        elif green > colors[1]:
            green -= 1
            
        if blue < colors[2]:
            blue += 1
        elif blue > colors[2]:
            blue -= 1
        
        pin0.write_analog(green) # Green
        pin1.write_analog(red) # Red
        pin2.write_analog(blue) # Blue
        if red == colors[0] and green == colors[1] and blue == colors[2]:
            return
        sleep(0.0001)
        
def fadeOutLEDs():
    # Iterate over each pixel and set its brightness
    for i in range(9):
        for x in range(5):
            for y in range(5):
                pxBrightness = display.get_pixel(x, y)
                if pxBrightness > 0:
                    display.set_pixel(x, y, pxBrightness - 1)
            sleep(0.003)

def fadeInLEDs(screen):
    pixels = {} 
    screen = Image(screen) # Optimization

    # Create a dictionary of the LEDs
    for x in range(5):
        for y in range(5):
            pxBrightness = screen.get_pixel(x, y)
            #if pxBrightness > 0: # Pixel is not empty
            pixels["%s%s" % (x, y)] = pxBrightness


    # Now loop all stored LED's and slowly fade it in 
    for i in range(9):
        for x in range(5):
            for y in range(5):
                pxBrightness = display.get_pixel(x, y)
                #if pixels["%s%s" % (x, y)] in locals(): # If pixel isn't blank
                if pxBrightness < pixels["%s%s" % (x, y)]:
                    display.set_pixel(x, y, pxBrightness + 1)
        
def toggleRainbowMode():
    global rainbowMode, screenTimeout
    rainbowMode = True
    screenTimeout = 200

    # Animate screen in
    pixels = [
        (2, 2, 9), # Center dot
        (3, 1, 9),
        (2, 0, 9),
        (1, 0, 8),
        (0, 1, 8),
        (0, 2, 8),
        (0, 3, 7),
        (1, 4, 7),
        (2, 4, 7),
        (3, 4, 6),
        (4, 3, 5)
    ]

    # Loop all predefined pixels to place, and then fade in the pixel
    for x, y, brightness in pixels:
        for brightness in range(brightness):
            display.set_pixel(x, y, brightness)
            sleep(0.01)
    
    while rainbowMode == True:
        return # TODO
        # Change the colors rapidly!

# Start up screen & LEDs
changeTheme(True)

while True:
    if button_a.is_pressed():
        changeTheme(False)
        while button_a.is_pressed():
            sleep(0.01) # Wait for button to stop being pressed
    elif button_b.is_pressed():
        changeTheme(True)
        while button_b.is_pressed():
            sleep(0.01) # Wait for button to stop being pressed
            
    elif pin_logo.is_touched():
        if rainbowMode == False:
            fadeOutLEDs()
            sleep(0.1)
            rainbowMode = True
            toggleRainbowMode()

            # Unfinished confirm button code
            # Doesn't work due to thread-blocking
            # Might just give up on the idea if I can't emulate
            # multi-threading
            
            #fadeInLEDs('00000:'
            #   '00000:'
            #   '00900:'
            #   '00000:'
            #   '00000')
            #while pin_logo.is_touched():
            #    sleep(0.01) # Wait for pin to stop being pressed
                
            #for i in range(100): # 1 second
            #    if pin_logo.is_touched():
            #        toggleRainbowMode()
            #        break
            #    sleep(0.01)

            #if pin_logo.is_touched(): # Fixes bug
            #    if rainbowMode == "confirm": # Hasn't confirmed, turn off screen
            #        fadeOutLEDs()
            #        sleep(0.1) # Wait for fade out to be done
            #        display.clear() # Then, clear display

        elif rainbowMode == "confirm":
            toggleRainbowMode()
        while pin_logo.is_touched():
            sleep(0.01) # Wait for pin to stop being pressed

    if screenTimeout == 0:
        fadeOutLEDs()
        screenTimeout -= 1 # Don't repeatedly clear screen
        sleep(0.1) # Wait for fade out to be done
        display.clear() # Then, clear display
    elif screenTimeout > 0:
        screenTimeout -= 1
    
    sleep(0.01)
