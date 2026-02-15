go = 0
# Starts the servo

def on_button_pressed_a():
    global go
    go = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

# Stops the servo

def on_button_pressed_b():
    global go
    go = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def on_forever():
    if go == 1:
        servos.P0.set_angle(0)
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            . . . # .
            # # # # #
            . . . # .
            . . . . .
            """)
        servos.P0.set_angle(180)
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            . # . . .
            # # # # #
            . # . . .
            . . . . .
            """)
basic.forever(on_forever)
