#CODE START!

init python:
    def new_char(name, col, tag):
        return Character(_(name), color=col, image=tag, voice_tag=tag)

transform flip:
    xzoom -1.0

transform unflip:
    xzoom 1.0

# this code decreases variable time by 0.01 until time hits 0, at which point, 
# the game jumps to label timer_jump (timer_jump is another variable that will be defined later)
define timer_jump = 0
define time = 0
screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Jump(timer_jump)]) 

# for mutable scenes like running into pico and steve, we need a scene variable instead of hardcoding it
define in_between_scene = ""

#Characters
#???
define u = new_char("???", "#f22a19", "mc")
#familiar voice
define fv = new_char("A Familiar Voice", "#1957BB", "trash")

#mc
define mc = new_char("MC-kun", "#f22a19", "mc")
#pico
define p = new_char("Pico", "#1957BB", "pico")
#steve
define s = new_char("Steve", "#1957BB", "steve")
#trash
define t = new_char("Trash-can", "#1957BB", "trash")

#Classroom
#mj
define mj = new_char("MJ", "#eef3ff", "mj")
#slimy
define slimy = new_char("Slimy", "#1957BB", "slimy")
#bbi
define bbi = new_char("BBi", "#FD5DA8", "bbi")

#Library
#spook
define spook = new_char("Spook", "#bb7d19", "spook")
#louis
define louis = new_char("Louis", "#1957BB", "louis")
#cat
define cat = new_char("Cat", "#FF0066", "cat")
#gloom
define gloom = new_char("Gloom", "#FF6172", "gloom")

#Roof
#moxxy
define moxxy = new_char("Moxxy", "#A117F2", "moxxy")
#neko
define neko = new_char("Neko", "#5c0012", "neko")
#herra
define herra = new_char("Herra", "#1957BB", "herra")

#Music
define audio.bgm1 = "music/bgm1.mp3"
define audio.gay = "music/I'm gay btw not sure if that matters.mp3"

#BG scaling fixes
image bg path_fixed = im.Scale("images/bg path.webp", 1280, 720)
image bg prom_collage_fixed = im.Scale("images/bg promcollage.webp", 1280, 720)
image bg classroom_fixed = im.Scale("images/bg classroom.webp", 1280, 720)
image bg dev_fixed = im.Scale("images/bg testbg.webp", 1280, 720)

image bg dream_classroom = Transform("bg classroom_fixed", matrixcolor=SaturationMatrix(0.0)*BrightnessMatrix(0.7))

#Collage
default collage_pieces_classroom = [0,0,0]
default collage_pieces_roof = [0,0,0]
default collage_pieces_library = [0,0,0,0]
default total = [collage_pieces_classroom, collage_pieces_library, collage_pieces_roof]

#this is mainly used to play music and stuff at the beginning
label start:
    play music bgm1 volume 0.05

label devmenu:
    scene bg testbg
    with fade

    menu:
        "Where to first...\nPieces: [total]"

        "Dream":
            jump dream

        "Morning":
            jump morning

        "To school":
            jump walking

        "Classroom":
            jump cla

        "Roof":
            jump rf

        "Library":
            jump lib

        "wincon":
            $ for i, x in enumerate(collage_pieces_library): collage_pieces_library[i] = 1
            $ for i, x in enumerate(collage_pieces_roof): collage_pieces_roof[i] = 1
            $ for i, x in enumerate(collage_pieces_classroom): collage_pieces_classroom[i] = 1
            jump devmenu

        "reset":
            $ for i, x in enumerate(collage_pieces_library): collage_pieces_library[i] = 0
            $ for i, x in enumerate(collage_pieces_roof): collage_pieces_roof[i] = 0
            $ for i, x in enumerate(collage_pieces_classroom): collage_pieces_classroom[i] = 0
            jump devmenu

        "The End" if all([1 if all(i) else 0 for i in total]):
            jump second_part

label dream:
    show bg dream_classroom
    with fade
    "dream"

label morning:
    show bg bedroom
    with fade

    "morning scene"
    jump devmenu

label walking:
    show bg path_fixed
    with fade

    "walking to school"
    jump devmenu

#Classroom encounters
label cla:
    if all(collage_pieces_classroom):
        $ in_between_scene = "bg classroom_fixed"
        jump surprise_meeting

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

label mj:
    scene bg classroom_fixed

    show mj suntalk at right
    with easeinright

    mj "hi kid im Michael Jackson how can i help you today"

    show mc nervous at left
    with easeinleft

    mc "Erm… hi."
    mc "Well you know White Day is today right? I don’t have any gift prepared yet."
    mc happy "But I heard that you were part of the school project! Could I have your piece?"

    mj confused "id k what you are talking about dude i have not been to school since 2009 you must be tripping from the Ligma"

    mc nervous "Where did your glasses go?"

    mj submit "ok im just messing with you my buddy pal guy dude friend check this out"

    $ collage_pieces_classroom[0] = 1

    mc happy "Oh wow! Now I can finally **** **** in my **** with some **** all over ******************! Thank you Michael Jackson!"

    mj point "live 2 love brother"

    jump cla

label slimy:
    scene bg classroom_fixed
    show mc nervous at left 
    with easeinleft

    mc "Hey Slimy so I was maybe wondering if you could possibly maybe"

    show slimy talking at right
    with easeinright

    slimy "Stop."
    slimy "I’m busy right now so I’ll make this quick."
    slimy submit "If I give you this will you piss off?"

    mc happy "Yeah!"

    $ collage_pieces_classroom[1] = 1

    slimy "Good."
    slimy talkingalt "Just keep the weird **** in the broom closet during the dance or whatever."

    jump cla

label bbi:
    scene bg classroom_fixed
    show mc worried at left

    mc "Sleeping during school hours again? Get off the Doxylamine already."

    show bbi sleepy at right
    with easeinright

    bbi "what the hell MC bro that was my NASA nap whats your deal ??"

    mc bashful "Well I heard you took part in the collaboration project."

    bbi talking "eeh i think so, yea, so what ???"

    mc shy "I just REALLY need it now for an emergency present for White Day, can you please let me have it?"

    $ collage_pieces_classroom[2] = 1

    bbi talkingalt "awww baby girl forgot their present for the white day ?? you suck lol"
    bbi submit "here ya go pal it got washed couple of times with my sweater but i hope itll still get you nice and penetrated hehe <33"

    jump cla

#Library encounters
label lib:
    if all(collage_pieces_library):
        $ in_between_scene = "bg library"
        jump surprise_meeting

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

label spook:
    scene bg library
    show mc neutral at left

    show spook talking at right
    with easeinright

    spook "Hey, MC-kun! I haven’t seen you in almost a month. You had me worried sick!"

    mc bashful "I feel way better but.. I have no gift for white day..."

    spook talking alt "That’s terrible! Is there anything I can do?"

    mc happy "Could I have your piece of the school project? I need it for love!"

    spook submit "If it’s for love, no cost is too great! Here you go."

    $ collage_pieces_library[0] = 1

    spook talking "Remember to keep yourself hydrated!"

    jump lib

label louis:
    scene bg library
    show mc neutral at left

    show louis placeholder at right
    with easeinright

    louis "Oh hey man what’s up?"

    mc "Give it to me. That thing. Your art piece"

    louis "My project entry? But I’ve been working on this all month!"

    mc angry "And this is my game! You wouldn’t deny someone their win con, would you?"

    louis "Am I at least gonna get credited?"

    mc neutral "No."

    $ collage_pieces_library[1] = 1

    louis "Okay..."

    jump lib

label cat:
    scene bg library
    show mc neutral at left

    show cat talking at right
    with easeinright

    $ collage_pieces_library[2] = 1

    cat submitalt "Sup MC-kun, here’s the project piece."

    mc worried "Wait, what? I didn’t even ask you for it yet."

    cat talkingalt "You ran through the hall screaming \"Oh god I need a White Day present\" several times before walking up to me."
    cat talking "Wasn’t exactly subtle."

    mc shy "Well, uh, thanks, I guess."

    cat talkingalt "Anytime."

    jump lib

label gloom:
    scene bg library
    show mc neutral at left

    show gloom placeholder at right
    with easeinright

    $ collage_pieces_library[3] = 1

    gloom "Nothing written yet."

    mc happy "Shame. Nice style though, you do something with your hair?"

    gloom "Yeah I've decided to pivot to trad."

    mc "Nice, nice. Okay thanks for the piece Gloom!"

    gloom "No worries, have a good one."

    jump lib

#Roof encounters
label rf:
    if all(collage_pieces_roof):
        $ in_between_scene = "bg roof"
        jump surprise_meeting

    scene bg roof
    with fade

    menu:
        "The delinquents should be hanging out up here, as usual. I hope they won't be any trouble."
        "Anyways...\nPieces: [collage_pieces_roof]"

        "Moxxy":
            jump moxxy

        "Neko":
            jump neko

        "Herra":
            jump herra

        "Back":
            jump devmenu

label moxxy:
    scene bg roof
    show mc neutral at left
    with easeinleft

    mc "Moxxy."
    mc "Moxxy?"
    mc "Moxxy!"

    show moxxy surprised at right 
    with vpunch
    with easeinright

    moxxy "!!"
    moxxy talking "Next time you're gonna sneak up on me don't do it when I'm eating, it's a real choking hazard you know."
    moxxy talkingalt "So what's up?"

    mc happy "Can I have your piece of the big project? Without it I’ll never find true love!"

    $ collage_pieces_roof[0] = 1

    moxxy "Well if it helps you find true love at that lousy dance tonight then sure."
    moxxy submit "If it doesn't... at least you'll have a cool doodle from your friend Mox right?"

    mc "Thanks, you're the best!"

    jump rf

label neko:
    scene bg roof
    show mc worried at left

    mc "{i}It’s the bancho of NG High! I better be respectful or I’ll get my teeth kicked in...{/i}"

    show neko talkingalt at right 
    with easeinright

    neko "{b}What do you want, runt?{/b}"

    mc "I have a small favour to ask, you’re working on the big project right?"

    neko happy "{b}Yeah, what of it? Come to see my masterpiece?{/b}"

    mc bashful "Y-yeah, totally, totally… I’ve heard rumors from the other third years that it’s the strongest piece of art in the region."
    mc shy "I’d be honored if you let me share it for you, if that’s true of course."

    $ collage_pieces_roof[1] = 1

    neko threaten "{b}OF COURSE IT IS! THOSE ****S ARE FINALLY GONNA SEE HENTAI AS ART!{/b}"
    neko submit "{b}Take good care of it or you’ll be sucking burgers through a straw ‘til graduation.{/b}"

    jump rf

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

    herra submit "Sure, it might have a little spray paint on it though..."

    jump rf

label surprise_meeting:
    $ renpy.scene()
    $ renpy.show(in_between_scene)
    with fade

    $ finished_rooms = sum([1 if all(i) else 0 for i in total])

    if finished_rooms == 1:
        "pico scene"
    elif finished_rooms == 2:
        "steve scene"
    elif finished_rooms == 3:
        "pico & steve scene"

    "end of surprise scene"

    jump devmenu

label second_part:
    scene bg hallway
    show mc neutral at left
    show trash at right
    with fade
    mc "Man, some of the places in this school are really poorly made"

    trash "Yeah they must’ve spent most of their time setting up the gym"

    "Collage get!"

    trash "But that’s not important right now! Here, I’ve put it back together for you"
    trash "Well, what are you standing around here for? Get in there!"

    mc worried "But what do I say? What should I do?"

    mc yiiking "Oh man I’m YIIKING OUT RIGHT NOW"

    trash """
    I think you just need to get out there and speak from the heart. 

    When you stay true to yourself MC-kun it doesn’t matter who you talk to, they’ll understand.
    """

label at_prom:
    play music gay volume 0.5
    $ time = 3                                        ### set variable time to 3
    $ timer_jump = 'lovemenu_slow'                    ### set where you want to jump once the timer runs out
       
    scene bg prom 
    show mc nervous at center
    with fade

    mc "Ouch... What a bit-{w=1}{nw}"
    show mc worried
    show p placeholder at right
    p "Are you alright MC-kun? We’ve been trying to reach you about your car’s extended warranty." with easeinright

    show s placeholder at left
    s "Shut up Pico, do you know how much that dates the game!?" with easeinleft
    show mc:
        flip
    s "We’ve been trying to corner your tight ass all day."

    mc "({i}Oh Crap{/i}) Hi Pico, Hi Steve"

    s "You really went all out for this Promdancestravaganza™ huh."
    
    show mc:
        unflip
    p "Well now that you’re here we can finally get to our dance."
    
    show mc: 
        flip
    s "Hate to shatter your sad, naive delusions, but MC-kun is obviously here to ask yours truly."
    
    show mc:
        unflip
    p "In your dreams, why would they ever want to dance with a *cock joke* like you?"

    mc "Um..."

label lovemenu:
    show screen countdown

    menu:
        "Pico":
            hide screen countdown
            jump choose_pico

        "Steve":
            hide screen countdown
            jump choose_steve

label lovemenu_slow:
    hide screen countdown
    menu:
        "Pico":
            jump choose_pico

        "Steve":
            jump choose_steve

        "Trash-can":
            jump choose_trash

label choose_steve:
    "Steve ending"

    hide p placeholder
    p "You'll regret this!" with dissolve

    s "Oh.. This looks... Great.. Thanks"

    show s placeholder at right
    with easeinright

    show mc happy at left
    with easeinleft

    mc "That's not all"

    s placeholder "Is that... A pretty pink birthday cake with my face on it? You didn't do this because I referenced it at the beginning of the game.. Did you?"

    mc bashful "No Steve, I did it because I care."

    show s placeholder at center

    s "Just kiss me you black and white son of a gun!"

    jump the_end

label choose_pico:
    "Pico ending"

    p "Don't do this... I have a dark secret"

    show mc bashful at left
    with easeinleft

    mc "I know what you are..."

    p placeholder "Then say it. Out loud."

    mc nervous "..."

    mc "... A character in a wildly popular rhythm game"

    mc worried "But I love every part of you! From the edgy flash game you to the freaky on a friday night you! You make me feel warm inside"
    show mc bashful at left

    p placeholder "MC-kun...  Would you like me to make you feel warm on the outside?"

    scene bg testbg
    with fade

    jump the_end

label choose_trash:
    "Trash ending"

    "WHAT?!"

    s placeholder "Who the fuck is Trash-Can?! I'm so confused..."

    p placeholder "Forget this, you two deserve each-other, you ARE Trash!"

    show steve placeholder at left
    with easeoutright

    show pico placeholder at right
    with easeoutright

    scene bg prom

    show trash placeholder at center
    with easeinright

    t "Is.. Is that how you really feel MC-kun?"

    scene bg prom

    show trash placeholder at right

    show mc bashful at left

    mc "Yes, Trash-Can, you've always been there for me when I've needed help."

    mc happy "You complete me!"

    show trash placeholder at right

    t "Oh MC-kun, Kiss me!"

    scene bg testbg
    with fade

    jump the_end

label the_end:

    scene bg prom_collage_fixed
    with fade

    $ ui.text("The End", size=40, xpos=400, ypos=340, color="#ffffff")

    $renpy.pause(10)

    return