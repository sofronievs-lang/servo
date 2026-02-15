let go = 0
// Starts the servo
input.onButtonPressed(Button.A, function () {
    go = 1
})
// Stops the servo
input.onButtonPressed(Button.B, function () {
    go = 0
})
basic.forever(function () {
    if (go == 1) {
        servos.P0.setAngle(0)
        basic.pause(100)
        basic.showLeds(`
            . . . . .
            . . . # .
            # # # # #
            . . . # .
            . . . . .
            `)
        servos.P0.setAngle(180)
        basic.pause(100)
        basic.showLeds(`
            . . . . .
            . # . . .
            # # # # #
            . # . . .
            . . . . .
            `)
    }
})
