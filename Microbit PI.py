def on_received_number(receivedNumber):
	# When ID is received from the ID Microbit, send ID to Pi
    basic.show_string("" + str((receivedNumber)))
    serial.write_number(receivedNumber)
radio.on_received_number(on_received_number)

def on_data_received():

	# When data is received from the pi, check for further action
    logo_code = serial.read_string()
	
	# if data received is 0, means pi is connected successfully
    if logo_code == "0\r":
	
		# Play sound and display tick to inform user of successful connection
        basic.show_icon(IconNames.YES)
        music.play_melody("F A C5 A C5 - - - ", 140)
        basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
		
	# else, send data to ID Microbit
    else:
        basic.show_leds("""
            . . # . .
            # # # # #
            . . # . .
            . . # . .
            . . # . .
        """)
		radio.send_string(logo_code)
serial.on_data_received(serial.delimiters(Delimiters.CARRIAGE_RETURN), on_data_received)

radio.set_group(222)