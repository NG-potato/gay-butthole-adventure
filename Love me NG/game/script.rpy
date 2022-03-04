﻿#CODE START!

#Characters
#mc
define mc = Character(_('MC-kun'), color="#f22a19", image="mc", voice_tag="mc")
#pico
define p = Character(_('Pico'), color="#1957BB", image="pico", voice_tag="pico")
#steve
define s = Character(_('Steve'), color="#1957BB", image="steve", voice_tag="steve")

#Classroom
#mj
define mj = Character(_('MJ'), color="#ff0000", image="mj", voice_tag="mj")
#slimy
define slimy = Character(_('Slimy'), color="#1957BB", image="slimy", voice_tag="slimy")
#bbi
define bbi = Character(_('BBi'), color="#FD5DA8", image="bbi", voice_tag="bbi")

#Library
#spook
define spook = Character(_('Spook'), color="#bb7d19", image="spook", voice_tag="spook")
#louis
define louis = Character(_('Louis'), color="#1957BB", image="louis", voice_tag="louis")
#cat
define cat = Character(_('Cat'), color="#FF0066", image="cat", voice_tag="cat")
#gloom
define gloom = Character(_('Gloom'), color="#FF6172", image="gloom", voice_tag="gloom")

#Roof
#moxxy
define moxxy = Character(_('Moxxy'), color="#A117F2", image="moxxy", voice_tag="moxxy")
#neko
define neko = Character(_('Neko, Bancho of NG High'), color="#5c0012", image="neko", voice_tag="neko")
#herra
define herra = Character(_('Herra'), color="#1957BB", image="herra", voice_tag="herra")

#Music
define audio.bgm1 = "music/bgm1.mp3"

#BG scaling fixes
image bg path_fixed = im.Scale("images/bg path.jpg", 1280, 720)
image bg prom_collage_fixed = im.Scale("images/bg prom.png", 1280, 720)
image bg classroom_fixed = im.Scale("images/bg classroom.png", 1280, 720)
image bg dev_fixed = im.Scale("images/bg testbg.jpg", 1280, 720)


#Collage
define collage_pieces_classroom = [0,0,0]
define collage_pieces_roof = [0,0,0]
define collage_pieces_library = [0,0,0,0]
define total = [collage_pieces_classroom, collage_pieces_library, collage_pieces_roof]
define collage = [0,0,0,0,0,0,0,0,0,0]

label start:
    play music bgm1 volume 0.05

    jump devmenu

label devor(x = 0):
    if all(total[x]):
        jump devmenu
    else:
        if x == 0:
            jump cla
        if x == 1:
            jump lib
        if x == 2:
            jump rf

label devmenu:
    scene bg testbg
    with fade

    menu:
        "Where to first...\nPieces: [collage]"

        "Classroom":
            jump cla

        "Roof":
            jump rf

        "Library":
            jump lib

        "wincon":
            $ collage_pieces_classroom = [1,1,1]
            $ collage_pieces_roof = [1,1,1]
            $ collage_pieces_library = [1,1,1,1]
            $ collage = [1,1,1,1,1,1,1,1,1,1]
            jump devmenu

        "The End" if all(collage):
            return

label cla:
    scene bg classroom_fixed
    with fade
    menu:
        "Ah, the good old classroom. An absolute must-have in any school-themed visual novel."
        "Anyways...\nPieces: [collage_pieces_classroom]"

        "MJ":
            jump mj

        "Slimy":
            jump slimy

        "BBi":
            jump bbi

        "Back":
            jump devmenu

label lib:
    scene bg library
    with fade
    menu:
        "I sure wish I could read."
        "Anyways...\nPieces: [collage_pieces_library]"

        "Spook":
            jump spook

        "Louis":
            jump louis

        "Cat":
            jump cat

        "Gloom":
            jump gloom

        "Back":
            jump devmenu

label rf:
    scene bg roof
    with fade
    menu:
        "The delinquents should be hanging out up here, as usual. I hope I won’t get my face kicked in."
        "Anyways...\nPieces: [collage_pieces_roof]"

        "Moxxy":
            jump moxxy

        "Neko":
            jump neko

        "Herra":
            jump herra

        "Back":
            jump devmenu

#Classroom encounters
label mj:
    scene bg classroom_fixed
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
    $ collage[0] = 1

    mc happy "Oh wow! Now I can finally **** **** in my **** with some **** all over ******************! Thank you Michael Jackson!"

    mj point "live 2 love brother"

    call devor(0)

label slimy:
    scene bg classroom_fixed
    show mc nervous at left 
    with fade 

    mc "Hey Slimy so I was maybe wondering if you could possibly maybe"

    show slimy talking at right
    with easeinright

    slimy "Stop."
    slimy "I’m busy right now so I’ll make this quick."
    slimy submit "If I give you this will you piss off?"

    mc happy "Yeah!"

    $ collage_pieces_classroom[1] = 1
    $ collage[1] = 1

    slimy "Good."
    slimy talkingalt "Just keep the weird **** in the broom closet during the dance or whatever."

    call devor(0)

label bbi:
    scene bg classroom_fixed
    show mc worried at left
    with fade

    mc "Sleeping during school hours again? Get off the Doxylamine already."

    show bbi sleepy at right
    with easeinright

    bbi "what the hell MC bro that was my NASA nap whats your deal ??"

    mc bashful "Well I heard you took part in the collaboration project."

    bbi talking "eeh i think so, yea, so what ???"

    mc shy "I just REALLY need it now for an emergency present for White Day, can you please let me have it?"

    $ collage_pieces_classroom[2] = 1
    $ collage[2] = 1

    bbi talkingalt "awww baby girl forgot their present for the white day ?? you suck lol"
    bbi submit "here ya go pal it got washed couple of times with my sweater but i hope itll still get you nice and penetrated hehe <33"

    call devor(0)

#Library encounters
label spook:
    scene bg library
    show mc neutral at left
    with fade

    show spook talking at right
    with easeinright

    spook "Hey, MC-kun! I haven’t seen you in almost a month. You had me worried sick!"

    mc bashful "I feel way better but.. I have no gift for white day..."

    spook talking alt "That’s terrible! Is there anything I can do?"

    mc happy "Could I have your piece of the school project? I need it for love!"

    spook submit "If it’s for love, no cost is too great! Here you go."

    $ collage_pieces_library[0] = 1
    $ collage[3] = 1

    spook talking "Remember to keep yourself hydrated!"

    call devor(1)

label louis:
    scene bg library
    show mc neutral at left
    with fade

    show louis placeholder at right
    with easeinright

    louis "Oh hey man what’s up?"

    mc "Give it to me. That thing. Your art piece"

    louis "My project entry? But I’ve been working on this all month!"

    mc angry "And this is my game! You wouldn’t deny someone their win con, would you?"

    louis "Am I at least gonna get credited?"

    mc neutral "No."

    $ collage_pieces_library[1] = 1
    $ collage[4] = 1

    louis "Okay..."

    call devor(1)

label cat:
    scene bg library
    show mc neutral at left
    with fade

    show cat talking at right
    with easeinright

    $ collage_pieces_library[2] = 1
    $ collage[5] = 1

    cat submitalt "Sup MC-kun, here’s the project piece."

    mc worried "Wait, what? I didn’t even ask you for it yet."

    cat talkingalt "You ran through the hall screaming \"Oh god I need a White Day present\" several times before walking up to me."
    cat talking "Wasn’t exactly subtle."

    mc shy "Well, uh, thanks, I guess."

    cat talkingalt "Anytime."

    call devor(1)

label gloom:
    scene bg library
    show mc neutral at left
    with fade

    show gloom placeholder at right
    with easeinright

    $ collage_pieces_library[3] = 1
    $ collage[6] = 1

    gloom "Nothing written yet."

    mc happy "Shame. Nice style though, you do something with your hair?"

    gloom "Yeah I've decided to pivot to trad."

    mc "Nice, nice. Okay thanks for the piece Gloom!"

    gloom "No worries, have a good one."

    call devor(1)

#Roof encounters
label moxxy:
    scene bg roof
    show mc neutral at left
    with fade

    mc "Moxxy."
    mc "Moxxy?"
    mc "Moxxy!"

    show moxxy talking at right 
    with vpunch
    with easeinright

    moxxy "!!"
    moxxy "Next time you're gonna sneak up on me don't do it when I'm eating, it's a real choking hazard you know."
    moxxy talkingalt "So what's up?"

    mc happy "Can I have your piece of the big project? Without it I’ll never find true love!"

    $ collage_pieces_roof[0] = 1
    $ collage[7] = 1

    moxxy "Well if it helps you find true love at that lousy dance tonight then sure."
    moxxy submit "If it doesn't... at least you'll have a cool doodle from your friend Mox right?"

    mc "Thanks, you're the best!"

    call devor(2)

label neko:
    scene bg roof
    show mc worried at left
    with fade

    mc "{i}It’s the bancho of NG High! I better be respectful or I’ll get my teeth kicked in...{/i}"

    show neko talkingalt at right 
    with easeinright

    neko "{b}What do you want, runt?{/b}"

    mc "I have a small favour to ask, you’re working on the big project right?"

    neko happy "{b}Yeah, what of it? Come to see my masterpiece?{/b}"

    mc bashful "Y-yeah, totally, totally… I’ve heard rumors from the other third years that it’s the strongest piece of art in the region."
    mc shy "I’d be honored if you let me share it for you, if that’s true of course."

    $ collage_pieces_roof[1] = 1
    $ collage[8] = 1

    neko threaten "{b}OF COURSE IT IS! THOSE ****S ARE FINALLY GONNA SEE HENTAI AS ART!{/b}"
    neko submit "{b}Take good care of it or you’ll sucking burgers through a straw ‘til graduation.{/b}"

    call devor(2)

label herra:
    scene bg roof
    show herra spooked at right
    with vpunch
    with easeinright

    herra "Wait it’s not what it looks lik-"

    show mc happy at left
    with easeinleft

    herra talking "Oh it’s just you MC-kun. What are you doing up here?"

    mc "Well Steve and Pico got me these imported chocolates for Valentines Day!"
    mc worried "I know you were part of the big art project, can I preeeeetty please have your piece? It’s for love..."

    herra confused "Imported... Those sound like the chocolates I got Pico for Valentines Day."

    mc shy "Haha not really sure what you mean by that but can I have the picture?"

    $ collage_pieces_roof[2] = 1
    $ collage[9] = 1

    herra submit "Sure, it might have a little spray paint on it though..."

    call devor(2)