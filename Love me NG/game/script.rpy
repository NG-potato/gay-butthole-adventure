#CODE START!

init python:
    def new_char(name, col, tag):
        return Character(_(name), color=col, image=tag, voice_tag=tag, callback=name_callback, cb_name=tag)

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
define fv = new_char("A Familiar Voice", "#1957BB", "t")

#mc
define mc = new_char("MC-kun", "#f22a19", "mc")
#pico
define p = new_char("Pico", "#1957BB", "pico")
#steve
define s = new_char("Steve", "#1957BB", "steve")
#pico & steve
define ps = new_char("Pico & Steve", "#1957BB", "steve")
#trash
define t = new_char("Trash-can", "#1957BB", "t")

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
image bg prom_collage_fixed = im.Scale("images/bg promcollage.webp", 1280, 720)
image bg dev_fixed = im.Scale("images/bg testbg.webp", 1280, 720)

image bg dream_classroom = Transform("bg classroom", matrixcolor=SaturationMatrix(0.0)*BrightnessMatrix(0.7))

#Collage
default collage_pieces_classroom = [0,0,0]
default collage_pieces_roof = [0,0,0]
default collage_pieces_library = [0,0,0,0]
default total = [collage_pieces_classroom, collage_pieces_library, collage_pieces_roof]

screen map:
    imagemap:
        ground 'images/map/schoolmap.png'
        hover 'images/map/schoolmap_hover.png'
        hotspot (0,0,200,200) action Return("devmenu")
        if not all(collage_pieces_roof):
            hotspot (581, 338, 126, 60) action Return("rf") #roof
        if not all(collage_pieces_classroom):
            hotspot (501, 454, 130, 60) action Return("cla") #classroom
        if not all(collage_pieces_library):
            hotspot (721, 404, 88, 74) action Return("lib") #library

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

        "Map":
            jump school_map

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

label school_map:
    window hide
    scene black with dissolve
    call screen map with fade
    if _return == 'rf':
        jump rf
    elif _return == 'cla':
        jump cla
    elif _return == 'lib':
        jump lib
    else:
        jump devmenu

label dream:
    show bg dream_classroom
    with fade
    
    show p placeholder at left with dissolve
    p "I’ll make sure to tell you not to come to school tomorrow~"
    
    hide p placeholder with dissolve
    
    pause(0.5)
    
    show s placeholder at right
    with dissolve
    s "It’s not a pretty pink birthday cake with your face on it, but take this you scrumptious son of a bitch~"
    
    hide s placeholder
    with dissolve
    
    pause(0.5)
    
    show p placeholder at left
    show s placeholder at right
    ps "Happy Valentines day!" with dissolve
    
    scene black
    #heres where it jumps to morning with the window smash

label morning:
    
    scene black
    with fade
    
    #insert window smash sound effect here
    "*SMASH*" with vpunch

    u "JESUS CHRIST WHAT THE HELL"
    
    fv "Wakey-wakey~"
    
    show bg bedroom
    with fade
    
    #Incase we show the MC before the name input
    #show mc worried at left
    #with easeinleft
    
    u "What?"
    
    #Does trashcan have a portrait?
    #show t nervous at right
    #with easeinright
    
    fv "Don’t tell me you forgot! That Ligma must’ve really messed you up. It’s White Day!"

    #shock sound effect
    
    #Incase we show the MC before the name input
    #show mc nervous at left
    u "WH-WHITE DAY!? That’s today?!"

    fv "Of course it is, you f**king baka! Now c'mon! If you don’t get dressed now, we’re gonna be late for class!"

    #-how should we insert this part from the script?-
    "You rush to put on your clothes, and get a glance of yourself in the mirror. All you see is a blur."
    
    u "Aw crap, I nearly forgot to put on my contacts again. Now where could they be…"
    
    #Rummaging sound
    
    $ renpy.input("What is your name?", length=32)
    
    #Rummaging sound (again)
    
    show mc happy at left
    with easeinleft
    mc "There we go! I better get going..."

label walking:
    show bg path
    with fade

    show t talking at right
    with easeinright
    t "Sooo… did you ask anyone to go to the White Day Promdancestravaganza™ yet?"
    
    show mc nervous at left
    with easeinleft
    mc "Aw nuts! I totally forgot…"
    
    t "Well, at least you have a gift to give, right?"
    
    show mc bashful at left
    mc "..." with dissolve
    
    t "Right?"
    
    mc "Uhhhhhhhhhh"
    
    t angry "So, you don’t have anything to give anyone." with dissolve
    
    show mc worried at left
    with dissolve
    mc "Oh man! If Pico or Steve find out that I don’t have a gift, I’m ruined! You gotta help me Trash-can, you’re my only hope!"

    t "Fine! If you can’t come up with something yourself, then I’m sure our classmates would be willing to help."

    show mc bashful at left
    with dissolve
    mc "What do you mean?"
    
    t talking "Well, we’ve all been working on an end-of-year project. I’m sure that if you ask nicely, they’ll help you out." with dissolve
    
    t "Here, you’ll need this. It’s a list of everyone working on the project." 
    
    #Script says that a video could go here, for now it's just a description box
    "Trash-can hands you a crumpled up piece of paper, with a shittily scribbled list of people on it."
    
    show mc shy at left
    with dissolve
    mc "Wow... thanks Trash-can, I- I don’t know what to say..."
    
    t "You’ll just have to owe me hehe~"
    
    #footsteps *2 sound, pause
    scene bg entrance
    show t talking at center
    with fade

    t "Ah, here we are, made it to school. Remember to meet me back here when you’re done so I can help you put the project together, ok?"

    #Maybe show a "Where to first?" selection with the locations

    scene black
    with fade

    jump devmenu

#Classroom encounters
label cla:
    if all(collage_pieces_classroom):
        $ in_between_scene = "bg classroom"
        jump surprise_meeting

    scene bg classroom
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
    scene bg classroom

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
    scene bg classroom
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
    scene bg classroom
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
    with easeinleft
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
    with easeinleft

    show louis talking at right
    with easeinright

    louis "Oh hey man what’s up?"

    mc "Give it to me. That thing. Your art piece"

    louis "My project entry? But I’ve been working on this all month!"

    mc angry "And this is my game! You wouldn’t deny someone their win con, would you?"

    louis "Am I at least gonna get credited?"

    mc neutral "No."

    $ collage_pieces_library[1] = 1

    louis submit "Okay..."

    jump lib

label cat:
    scene bg library
    show mc neutral at left
    with easeinleft

    show cat submit at right
    with easeinright

    $ collage_pieces_library[2] = 1

    cat @ submitalt "Sup MC-kun, here’s the project piece."

    mc worried "Wait, what? I didn’t even ask you for it yet."

    cat talkingalt "You ran through the hall screaming \"Oh god I need a White Day present\" several times before walking up to me."
    cat talking "Wasn’t exactly subtle."

    mc shy "Well, uh, thanks, I guess."

    cat @ talkingalt "Anytime."

    jump lib

label gloom:
    scene bg library
    show mc neutral at left
    with easeinleft
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
    moxxy "!!" with vpunch
    moxxy talkingalt "Next time you're gonna sneak up on me don't do it when I'm eating, it's a real choking hazard you know."
    moxxy talking "So what's up?"

    mc happy "Can I have your piece of the big project? Without it I’ll never find true love!"

    $ collage_pieces_roof[0] = 1

    moxxy talkingalt "Well if it helps you find true love at that lousy dance tonight then sure."
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

    neko happy "{b}Yeah, what of it? Come to see my masterpiece?{/b}" with dissolve

    mc bashful "Y-yeah, totally, totally… I’ve heard rumors from the other third years that it’s the strongest piece of art in the region." with dissolve
    mc shy "I’d be honored if you let me share it for you, if that’s true of course." with dissolve

    $ collage_pieces_roof[1] = 1

    neko threaten "{b}OF COURSE IT IS! THOSE ****S ARE FINALLY GONNA SEE HENTAI AS ART!{/b}" with dissolve
    neko submit "{b}Take good care of it or you’ll be sucking burgers through a straw ‘til graduation.{/b}" with dissolve

    jump rf

label herra:
    scene bg roof
    show herra spooked at right

    herra "Wait it’s not what it looks lik-" with vpunch

    show mc happy at left
    with easeinleft

    herra talking "Oh it’s just you MC-kun. What are you doing up here?" with dissolve

    mc "Well Steve and Pico got me these imported chocolates for Valentines Day!" 
    mc worried "I know you were part of the big art project, can I preeeeetty please have your piece? It’s for love..." with dissolve

    herra confused "Imported... Those sound like the chocolates I got Pico for Valentines Day." with dissolve

    mc shy "Haha not really sure what you mean by that but can I have the picture?" with dissolve

    $ collage_pieces_roof[2] = 1

    herra submit "Sure, it might have a little spray paint on it though..." with dissolve

    jump rf

label surprise_meeting:
    $ finished_rooms = sum([1 if all(i) else 0 for i in total])

    if finished_rooms == 1:
        scene black
        "You suddenly find yourself running into someone"
        #sfx, oof!
        $ renpy.scene()
        $ renpy.show(in_between_scene)
        with fade

        show mc neutral at left
        show p placeholder at right
        p "Oof, Watch where you’re... Oh MC-kun you’re back! I was worried you were gonna miss the Promdancestravaganza™" with vpunch

        mc "Oh, hi Pico.. I wouldn’t miss it for the world."

        p "Funny running into you right now, I was just on my way to target practice. Care to join?"

        mc "(If I don’t come up with something fast {i}I’ll{/i} be the target!) OH yeah would love to but I uhh"
        mc "I gotta go to the optometrist for my teeth whitening appointment! I mean..."
        mc "I left my oven outside! Or uhh what I was trying to say was..."
        mc "Gotta take out the trash!"
        hide mc
        mc "WOAH would you look at the time gotta scoot see you later okay bye!" with easeoutleft

        p ""
        p "What?"

    elif finished_rooms == 2:
        scene black
        "You suddenly find yourself running into someone else"
        #sfx, oof!
        $ renpy.scene()
        $ renpy.show(in_between_scene)
        with fade
        show mc neutral at left
        with easeinleft

        mc "Oh shit I’m sorry"

        show s placeholder at right
        with easeinright

        s "Sorry for what?"

        mc "For bumping into you."

        s "Oh you know you can bump into me any time. With your cock."

        mc nervous "Oh, you mean like a rooster?"

        s "Yeah, right, like a rooster."

        mc shy "Heh, scared me there for a sec."

        s "Yep..."

        mc bashful "..."

        mc "I should get going now."

        s "Yyyeah. See you at the Promdancestravaganza™"

    elif finished_rooms == 3:
        $ renpy.scene()
        $ renpy.show(in_between_scene)
        show mc neutral at center
        with ease

        mc "My mc-senses are tingling..."

        show p placeholder at right 
        show s placeholder at left 
        with vpunch

        "MC-kun!"

        hide mc neutral
        mc "(Stupid, Insipid, Startled Sounds)" with easeoutright

        p "What gives? Do you think he’s mad at us?"

        s "I don’t think so… Wait, did you brush your teeth today?"

        p "Yeah of course. You must have that nasty swamp-ass today."

        s "Ugh, I know! It’s only natural in a sub-tropical climate like this. Anyway, I should probably change before the Promdancestravagnza™"

        p "Ditto. I can feel it coming on too…"

    jump devmenu

label second_part:
    scene bg entrance
    show t talking at right
    with fade

    t "Took you long enough MC-kun!"
    t @ threaten "It's almost time."

    show mc shy at left
    mc "Haha, yeah I'm pretty slow sometimes" with easeinleft

    t "You’ve got that right, now hand over the pieces."
    t "I’ll put it together while you go get ready and we’ll meet back at the hallway outside of the gym."
    #sfx unzip, clothes ruffle, pissing

    scene bg hallway
    show mc neutral at left
    show t talking at right
    with fade
    mc "Man, some of the places in this school are really poorly made"

    t "Yeah they must’ve spent most of their time setting up the gym"

    t angry "But that’s not important right now! Here, I’ve put it back together for you" with dissolve

    "Collage get!"

    t talking "Well, what are you standing around here for? Get in there!" with dissolve

    mc worried "But what do I say? What should I do?" with dissolve
    mc yiiking "Oh man I’m YIIKING OUT RIGHT NOW" with dissolve

    t unu "I think you just need to get out there and speak from the heart." with dissolve
    t "When you stay true to yourself MC-kun it doesn’t matter who you talk to, they’ll understand."

    mc shy "You really mean that?" with dissolve

    t talking "I mean kinda I guess."
    t "Now get that dick!" with vpunch

    mc neutral "What?"

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
    show mc:
        flip
    s "Shut up Pico, do you know how much that dates the game!?" with easeinleft
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

    "WHAT?!" with vpunch

    s placeholder "Who the fuck is Trash-Can?! I'm so confused..."

    p placeholder "Forget this, you two deserve each-other, you ARE Trash!"

    hide s placeholder
    hide p placeholder
    with dissolve

    show mc neutral at left
    with ease

    show t at right
    with easeinright
    t "Is.. Is that how you really feel MC-kun?"

    mc "Yes, Trash-Can, you've always been there for me when I've needed help."

    mc happy "You complete me!"

    t "Oh MC-kun, Kiss me!"

    jump the_end

label the_end:

    scene bg prom_collage_fixed
    with fade

    $ ui.text("The End", size=40, xpos=400, ypos=340, color="#ffffff")

    $renpy.pause(10)

    return