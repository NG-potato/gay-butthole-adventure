# The script of the game goes in this file.

##label character_tut:
# Declare characters used by this game. The color argument colorizes the
# name of the character.
#to define the label use "define".
#color defines the color of all of their text
#A working example is below
#define Zone = Character("Zone", color="#e03888")

# The game starts here.
#sprites need to be named "character attribute"
##label start_tut:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

##label sprites_tut:
#this is basic way to show dialogue per scene.
#    "character" "dialogue goes here"
#    show #character #modifier
#this defines a basic line.
#"show" displays the sprite
# a working example would be the below 2 lines
#   "Zone" "I Love tentacles!"
#   show zone excited

##label scene_tut:
#scene is defined by keyword "scene"
#"bg" designates the background image for it. uses same naming convention as sprite
#with defines actions for the label. Can be used with fade, fadeout, and wipe
#"play" defines what audio should be played for the base audio.
#"fadein" or "fadeout" can be defined by adding after. add a numerical value to define time.
#"volume" defines the overall volume of the audio. it is defined with 1 being max.
#"stop music" can be used to stop audio otherwise it will loop
#"queue music" can be used to add multiple audio files back to back with "filename" added after to set them
#a working example is below
#   play music "audio/bgm_gym.mp3" fadein 1.0 volume 0.5
#   scene bg gym
#   with fade

##label sounds_tut:
#"play sound "filelocation"" can be used to add sound effects.
#unlike music will not loop.

##label choices_tut:
#choices are defined by adding under "menu:" doing a break, then adding choices in ""s
#"jump" defines where to move next after a choice is made. It will poiunt to the label.
#an example is below

#label: choice1
#   "Zone" "Do you like tentacles?"
#menu:
#   "take blue pill":
#   jump choice1a
#   "take red pill":
#   jump choice1b

#label: choice1a
#   "Zone" "Boo! Not tentacles!"
#   jump newscene
#label: choice1b
#   "Zone" "Yay! Tentacles"
#   jump newscene
#label: newscene

#CODE START!

#Characters
define mc = Character(_('MC-kun'), color="#ffffff")
define steve = Character(_('Steve'), color="#ff0000")
define pico = Character(_('Pico'), color="#0000ff")
define test = Character(_('\"The Dev\"'), color="#1951BB")

#Music
define audio.bgm1 = "music/bgm1.mp3"

label start:
    play music bgm1 volume 0.05
    scene bg testbg
    show dev1
    with fade
    voice "voice/test_1.mp3"
    test "Hey buddy! If you can see this right now then the game's prototype is working. Hooray!"
    hide dev1
    show dev2
    voice "voice/test_2.mp3"
    test "We don't have much going on besides conversational capabilities..."
    show dev2 at left
    with move 
    show mc1 at right
    with moveinright
    voice "voice/test_4r.mp3"
    mc "I'm a huge faggot!"
    hide dev2
    show dev3 at left
    voice "voice/test_3.mp3"
    test "You said it."
    hide mc1 at right
    with moveoutright
    show dev3 at center
    with move
    hide dev3
    show dev2
    voice "voice/test_5.mp3"
    test "This has been your captain speaking. Until then!"