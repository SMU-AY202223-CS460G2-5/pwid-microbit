def on_received_string(receivedString):

    # If string returned is "error", signifies that system was unable to get help
    if receivedString == "error":
        basic.show_icon(IconNames.SAD)
        music.play_melody("E C E C C - - - ", 140)
        
    # Else, display success
    else:
        # Notify user of success with audio and visual
        basic.show_icon(IconNames.YES)
        music.play_melody("F A C5 A C5 - - - ", 140)
        basic.pause(1000)
        
        # Display ICON to match with volunteer
        if receivedString == "HEART" : basic.show_icon(IconNames.Heart)
        elif receivedString == "DUCK" : basic.show_icon(IconNames.Duck)
        elif receivedString == "HOUSE" : basic.show_icon(IconNames.House)
        elif receivedString == "GHOST" : basic.show_icon(IconNames.Ghost)
        elif receivedString == "UMBRELLA" : basic.show_icon(IconNames.Umbrella)
        elif receivedString == "RABBIT" : basic.show_icon(IconNames.Rabbit)
        elif receivedString == "SNAKE" : basic.show_icon(IconNames.Snake)
        elif receivedString == "TARGET" : basic.show_icon(IconNames.Target)
        elif receivedString == "PITCHFORK" : basic.show_icon(IconNames.Pitchfork)
        elif receivedString == "SCISSORS" : basic.show_icon(IconNames.Scissors)
        
radio.on_received_string(on_received_string)

radio.set_group(222)
music.set_volume(175)

def on_forever():
    
    # Implement a press-and-hold for both buttons
    if input.button_is_pressed(Button.AB):
        basic.pause(2000)
        
        #Second check, if AB still pressed, then send signal to Pi Microbit
        if input.button_is_pressed(Button.AB):
            radio.send_number(5)
            
            #Play sound and show LED to signify that SOS has been sent
            basic.show_leds("""
                . . # . .
                . . # . .
                . . # . .
                . . # . .
                . . # . .
            """)
            music.play_melody("F A C5 - - - - - ", 130)
basic.forever(on_forever)
