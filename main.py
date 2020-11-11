def on_received_number(receivedNumber):
    global num_peces, dias
    num_peces += -1 * receivedNumber
    dias = 1 + dias
    if num_peces <= 0:
        basic.show_leds("""
            . # # # .
            # . # . #
            # # # # #
            # # # # #
            # . # . #
            """)
    else:
        basic.show_leds("""
            # . # # .
            # # # # #
            # # # # #
            # . # # .
            . . . . .
            """)
        basic.show_number(num_peces)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global num_peces, dias
    num_peces = 100
    dias = 0
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_string("d")
    basic.show_number(dias)
input.on_button_pressed(Button.B, on_button_pressed_b)

num_peces = 0
dias = 0
dias = 0
num_peces = 100
radio.set_group(1)