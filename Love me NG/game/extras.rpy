
## End Credits Scroll ############################################################
## ATL for scrolling screen object. In this case, credits roll.
## Speed is the time for object to move up from initial ypos to finish ypos.

## Code Source: https://lemmasoft.renai.us/forums/viewtopic.php?t=42667

transform credits_scroll(speed):
    ypos 2000
    linear speed ypos -1800
    ## Adjust these numbers to be the height of your end credits. Both numbers
    ## should be the same.

## Credits screen.

screen credits():

    ## Ensure that the game_menu screens don't appear and interrupt the credits.
    key "K_ESCAPE" action NullAction()
    key "K_MENU" action NullAction()
    key "mouseup_3" action NullAction()

    style_prefix "credits"

    ## If a player has seen the end credits before, this button appears.
    if persistent.credits_seen:

        textbutton _("Skip End Credits") action Jump("skip_credits") xalign 1.0 yalign 1.0

    timer 43.0 action Return()
    ## Adjust this number to control when the Credits screen is hidden and the game
    ## returns to its normal flow.
    ## Ideally, there is some wait time after the the credits reaches the end.

    frame at credits_scroll(45.0):
        ## Adjust this number to control the speed at which the credits scroll.
        background None
        xalign 0.5

        vbox:
            null height -1000
            text "Producer" size 40
            null height 20
            text "ManlyPotato" size 25

            null height 100

            text "Music" size 40
            null height 20 

            hbox:

                xalign 0.5
                spacing 100

                text "CommanderJersey" size 25

                text "Main theme" size 25

            hbox:

                xalign 0.5
                spacing 100

                text "ManlyPotato" size 25

                text "Ending theme" size 25

            null height 100

            text "Writing" size 40
            null height 20
            text "ManlyPotato" size 25
            null height 20
            text "LilSpook" size 25
            null height 20
            text "VoicesByCorey" size 25
            null height 20
            text "mettoretto" size 25
            null height 20
            text "Nek0ai" size 25

            null height 100

            text "Programming" size 40
            null height 20

            text "ManlyPotato" size 25
            null height 20 
            text "CommanderJersey" size 25
            null height 20
            text "Tekkyon" size 25

            null height 100

            text "Voice Acting" size 40
            null height 20

            hbox:

                xalign 0.5
                spacing 100

                text "ManlyPotato" size 25

                text "MC-kun" size 25

            hbox:

                xalign 0.5
                spacing 100

                text "BigDongByCorey " size 25

                text "Steve, Pico, Slimy" size 25

            hbox:

                xalign 0.5
                spacing 100

                text "LilSpook" size 25

                text "Trash-can, Neko, Spook" size 25

            hbox:

                xalign 0.5
                spacing 100

                text "ChromaCee" size 25

                text "Herra, Gloom" size 25

            hbox:

                xalign 0.5
                spacing 100

                text "FineCurry" size 25

                text "Louis" size 25

            hbox:

                xalign 0.5
                spacing 100

                text "MayaLaCookie" size 25

                text "Moxxie" size 25

            null height 100
            
            text "Art & Characters" size 40
            null height 20

            text "An Original Joke - Cat" size 25
            null height 20

            text "Bbii - Bbi" size 25
            null height 20

            text "ChromaCee - Herra" size 25
            null height 20

            text "GloomGorl - Gloom" size 25
            null height 20

            text "FineCurry - Louis" size 25
            null height 20

            text "LilSpook - Spook" size 25
            null height 20

            text "MayaLaCookie - Moxxy" size 25
            null height 20

            text "mettoretto - MJ" size 25
            null height 20

            text "Nek0ai - Neko" size 25
            null height 20

            text "Slimygoo - Slimy" size 25
            null height 100

            text "Special Thanks" size 40
            null height 20 

            text "You!" size 25

style credits_hbox:
    spacing 40
    ysize 30

style credits_label_text:
    xalign 0.5
    size 200
    text_align 0.5

style credits_text:
    xalign 0.5
    size 80
    justify True
    text_align 0.5
    color "#ffffff"

style backercredits_text:
    xalign 0.5
    size 50
    justify True
    text_align 0.5
    color "#ffffff"


## Results Screen ############################################################
## A screen that displays how much of the game the player has seen.

## Code Source: https://lemmasoft.renai.us/forums/viewtopic.php?t=39859
## Official Documentation of function: https://www.renpy.org/doc/html/other.html#renpy.count_dialogue_blocks

# This creates a percentage based on how much of the game the player has seen. 
init python:

    numblocks = renpy.count_dialogue_blocks()

    def percent():

        global readtotal
        readtotal = renpy.count_seen_dialogue_blocks()* 100 / numblocks
        persistent.readtotal = readtotal
        ## This is displayed in our Achievements screen.

default readtotal = 0

screen results():
    
    zorder 200

    vbox:
        xalign .5
        yalign 0.025
        spacing 45

        text "Script Seen: [readtotal]%" color "#fff"

    textbutton _("Main Menu") action Jump("return_to_sender") xalign 1.0 yalign 1.0