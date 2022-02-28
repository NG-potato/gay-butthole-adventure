#CODE START!

#Characters
#mc
define mc = Character(_('MC-kun'), color="#f22a19", image="mc", voice_tag="mc")

#mj
define mj = Character(_('MJ'), color="#ff0000", image="mj", voice_tag="mj")

#spook
define spook = Character(_('Spook'), color="#bb7d19", image="spook", voice_tag="spook")

#Music
define audio.bgm1 = "music/bgm1.mp3"

#BGs
image bg to_school = im.Scale("images/bg school_path.png", 1280, 720)
image bg prom_fixed = im.Scale("images/bg prom.png", 1280, 720)

#Collage
define collage_pieces_classroom = [0,0]

label start:
    play music bgm1 volume 0.05

    $ collage_pieces_classroom = [0,0]

    jump devmenu

label devmenu:
    scene bg testbg
    with fade

    menu:

        "Pieces = [collage_pieces_classroom]"

        "MJ":

            jump mj

        "Spook":

            jump spook

        "The End" if all(collage_pieces_classroom):

            return

label mj:
    
    scene bg prom_fixed
    show mc neutral at left
    with fade

    show mj suntalk at right
    with easeinright

    mj "hi kid im Michael Jackson how can i help you today"

    mc @ nervous "Erm… hi."

    mc "Well you know White Day is today right? I don’t have any gift prepared yet."

    mc happy "But I heard that you were part of the school project! Could I have your piece?"

    mj confused "id k what you are talking about dude i have not been to school since 2009 you must be tripping from the Ligma"

    mc nervous "Where did your glasses go?"

    mj submit "ok im just messing with you my buddy pal guy dude friend check this out"

    $ collage_pieces_classroom[0] = 1

    mc happy "Oh wow! Now I can finally **** **** in my **** with some **** all over ******************! Thank you Michael Jackson!"

    mj point "live 2 love brother"

    jump devmenu

label spook:

    scene bg to_school
    show mc neutral at left
    with fade

    show spook talking at right
    with easeinright

    spook "Hey, MC-kun! I haven’t seen you in almost a month. You had me worried sick!"

    mc bashful "I feel way better but.. I have no gift for white day..."

    spook talking alt "That’s terrible! Is there anything I can do?"

    mc happy "Could I have your piece of the school project? I need it for love!"

    spook submit "If it’s for love, no cost is too great! Here you go."

    $ collage_pieces_classroom[1] = 1

    spook talking "Remember to keep yourself hydrated!"

    jump devmenu