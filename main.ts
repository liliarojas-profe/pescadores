radio.onReceivedNumber(function (receivedNumber) {
    num_peces += -1 * receivedNumber
    dias += 1
    if (num_peces <= 0) {
        basic.showLeds(`
            . # # # .
            # . # . #
            # # # # #
            # # # # #
            # . # . #
            `)
    } else {
        basic.showLeds(`
            # . # # .
            # # # # #
            # # # # #
            # . # # .
            . . . . .
            `)
        basic.showString("Quedan")
        basic.showNumber(num_peces)
        basic.showString("peces")
    }
})
input.onButtonPressed(Button.A, function () {
    num_peces = 100
    dias = 0
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    basic.showString("días pesca")
    basic.showNumber(dias)
})
let num_peces = 0
let dias = 0
dias = 0
num_peces = 100
radio.setGroup(1)
