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
define endcards = ["bg steveendcard", "bg picoendcard", "bg trashendcard"]
define engingbgs = ["bg steveend", "bg picoend", "bg trashend"]
define choice = 0

#Characters
#???
define u = new_char("???", "#f22a19", "mc")
#familiar voice
define fv = new_char("A Familiar Voice", "#999999", "t")

#mc
define mc = new_char("MC-kun", "#f22a19", "mc")
#pico
define p = new_char("Pico", "#f94907", "p")
#steve
define s = new_char("Steve", "#000000", "s")
#pico & steve
define ps = new_char("Pico & Steve", "#a20c3d", "steve")
#trash
define t = new_char("Trash-can", "#999999", "t")

#Classroom
#mj
define mj = new_char("MJ", "#2a108a", "mj")
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

#alt bg manipulations
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
            hotspot (544, 356, 148, 68) action Return("rf") #roof
        if not all(collage_pieces_classroom):
            hotspot (510, 440, 121, 102) action Return("cla") #classroom
        if not all(collage_pieces_library):
            hotspot (694, 382, 128, 115) action Return("lib") #library

#this is mainly used to play music and stuff at the beginning
label start:
    play music bgm1
    jump dream

label devmenu:
    scene bg path
    with fade

    menu:
        "Pieces: [total]"

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
            jump the_end

label school_map:
    call screen map(_with_none=False) with dissolve
    with fade
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
    
    show p happy_uniform at left with dissolve
    p "I’ll make sure to tell you not to come to school~"
    
    hide p happy_uniform with dissolve
    
    pause(0.5)
    
    show s flirt_uniform at right
    with dissolve
    s "It’s not a pretty pink birthday cake with your face on it, but take this you scrumptious son of a bitch~"
    
    hide s flirt_uniform
    with dissolve
    
    pause(0.5)
    
    show p happy_uniform at left
    show s flirt_uniform at right
    ps "Happy Valentine's day!" with dissolve
    
    scene black
    #heres where it jumps to morning with the window smash

label morning:
    
    scene black
    with fade
    
    #insert window smash sound effect here
    "The sound of a rock flying through your window wakes you up with a start." with vpunch

    u "JESUS CHRIST WHAT THE HELL"
    
    fv "Wakey-wakey~"
    
    show bg bedroom
    with fade
    
    u "What?"
    
    fv "Don’t tell me you forgot! That Ligma must’ve really messed you up. It’s White Day!"

    #shock sound effect
    
    u "WH-WHITE DAY!? That’s today?!"

    fv "Of course it is, you f**king baka! Now c'mon! If you don’t get dressed now, we’re gonna be late for class!"

    #clothing sounds
    "You rush to put on your clothes, and get a glance of yourself in the mirror. All you see is a blur."
    
    u "Nearly forgot to put on my contacts again. Now where could they be..."
    
    #Rummaging sound
    
    $ renpy.input("What is your name?", length=32)
    
    #Rummaging sound (again)
    
    show mc neutral at left
    mc "There we go! Better meet up with her outside..." with easeinleft

label walking:
    scene bg path
    with fade

    show t talking at right
    with easeinright
    t "Sooo... did you ask anyone to go to the White Day Promdancestravaganza(tm) yet?"
    
    show mc nervous at left
    mc "Aw nuts! I totally forgot..." with easeinleft
    
    t "Well, at least you have a gift to give, right?"
    
    mc bashful "..." 
    
    t "Right?"
    
    mc "Uhhhhhhhhhh"
    
    t angry "So, you don’t have anything to give anyone!?"

    mc worried "Oh man! If Pico or Steve find out that I don’t have a gift, I’m ruined! You gotta help me Trash-can, you’re my only hope!"

    t "Fine! If you can’t come up with something yourself, then I’m sure our classmates would be willing to help."

    mc bashful "What do you mean?"
    
    t talking "Well, we’ve all been working on an end-of-year project. I’m sure that if you ask nicely, they’ll help you out." 
    
    t "Here, you’ll need this." 
    
    #Script says that a video could go here, for now it's just a description box
    "Trash-can hands you a crumpled up piece of paper with a shittily scribbled map of the school."
    
    show mc shy at left
    mc "Wow... thanks Trash-can, I don’t know what to say..."
    
    t "You’ll just have to owe me hehe~"
    
    #footsteps *2 sound, pause
    scene bg entrance
    show t talking at center
    with fade

    t "Ah, here we are! Remember to meet me back here when you’re done so I can help you put it together, ok?"

    #Maybe show a "Where to first?" selection with the locations

    scene black
    with fade

    jump school_map

#Classroom encounters
label cla:
    if all(collage_pieces_classroom):
        $ in_between_scene = "bg classroom"
        jump surprise_meeting

    scene bg classroom
    with fade

    menu:
        "Ahhh, the good old classroom. An absolute must-have in any school-themed visual novel."

        "MJ" if not collage_pieces_classroom[0]:
            jump mj

        "Slimy" if not collage_pieces_classroom[1]:
            jump slimy

        "BBi" if not collage_pieces_classroom[2]:
            jump bbi

label mj:
    scene bg classroom

    show mj suntalk at right
    with easeinright

    mj "hi kid im Michael Jackson how can i help you today"

    show mc nervous at left

    mc "Erm... hi." with easeinleft
    mc "Well you know White Day is today right? I don’t have any gift prepared yet."
    mc happy "But I heard that you were part of the school project! Could I have your piece?"

    mj confused "id k what you are talking about dude i have not been to school since 2009 you must be tripping from the Ligma"

    mc nervous "Where did your glasses go?"

    mj submit "ok im just messing with you my buddy pal guy dude friend check this out"

    $ collage_pieces_classroom[0] = 1

    mc happy "Oh wow! Now I can finally get to the good ****! Thank you Michael Jackson!"

    mj point "live 2 love brother"

    jump cla

label slimy:
    scene bg classroom
    show mc nervous at left 
    with easeinleft

    mc "Hey Slimy so I was maybe wondering if you could possibly maybe"

    show slimy talking at right

    slimy "Stop." with easeinright
    slimy "I’m busy right now so I’ll make this quick."
    slimy submit "If I give you this will you piss off?"

    mc happy "Yeah!"

    $ collage_pieces_classroom[1] = 1

    slimy "Good."
    slimy talkingalt "Just keep the weird **** in the broom closet during the dance or whatever."

    jump cla

label bbi:
    scene bg classroom
    show mc happy at left

    mc "Sleeping during school hours again? Get off the Doxylamine already."

    show bbi sleepy at right

    bbi "what the hell MC bro that was my NASA nap whats your deal ??" with easeinright

    mc bashful "Well I heard you took part in the collab."

    bbi talking "eeh i think so, yea, so what ???"

    mc worried "I just REALLY need it now for an emergency present for White Day, can you please let me have it?"

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
        "I sure wish I could read..."
        "Spook" if not collage_pieces_library[0]:
            jump spook

        "Louis" if not collage_pieces_library[1]:
            jump louis

        "Cat" if not collage_pieces_library[2]:
            jump cat

        "Gloom" if not collage_pieces_library[3]:
            jump gloom

label spook:
    scene bg library
    show spook talking at right
    with easeinright

    spook "Hey, MC-kun! I haven’t seen you in almost a month. You had me worried sick!"

    show mc happy at left
    mc "I feel way better but.." with easeinleft
    mc bashful "I have no gift for white day..."

    spook talking alt "That’s terrible! Is there anything I can do?"

    mc happy "Could I have your piece of the school project? I need it for love!"

    spook submit "If it’s for love, no cost is too great! Here you go."

    $ collage_pieces_library[0] = 1

    spook talking "Remember to keep yourself hydrated!"

    jump lib

label louis:
    scene bg library

    show louis talking at right
    with easeinright

    louis "Oh hey man what’s up?"

    show mc neutral at left
    mc "Hand it over. That thing. Your art piece." with easeinleft

    louis "My project entry? But I’ve been working on this all month!"

    mc angry "And this is my game! You wouldn’t deny someone their win con, would you?"

    louis "Am I at least gonna get credited?"

    mc neutral "No."

    $ collage_pieces_library[1] = 1

    louis submit "Okay..."

    jump lib

label cat:
    scene bg library

    show cat submit at right
    with easeinright

    $ collage_pieces_library[2] = 1

    cat @ submitalt "Sup MC-kun, here’s the project piece."

    show mc nervous at left
    mc "Wait, what? I didn’t even ask you for it yet." with easeinleft

    cat talkingalt "You ran through the hall screaming \"Oh god I need a White Day present\" several times before walking up to me."
    cat talking "Wasn’t exactly subtle."

    mc shy "Well, uh, thanks, I guess."

    cat @ talkingalt "Anytime."

    jump lib

label gloom:
    scene bg library
    show gloom talking at right
    with easeinright

    gloom "Hey MC-kun! What’s up?"

    show mc happy at left
    mc "Trash-can told me that you worked on the big project, is it okay if I use it?" with easeinleft

    gloom talkingalt "Sure thing, I’ve been waiting to show this off for ages!"
    gloom submit "Sorry if it’s a little sticky, mini gloom here has a drooling problem"
    $ collage_pieces_library[3] = 1

    mc "Thanks!"

    mc shy "By the way did you do something with your hair?"

    gloom talking "Been trying out a more traditional approach, how’s it look?"

    mc happy "Looks good, see you at the dance!"

    jump lib

#Roof encounters
label rf:
    if all(collage_pieces_roof):
        $ in_between_scene = "bg roof"
        jump surprise_meeting

    scene bg roof
    with fade

    menu:
        "The delinquents should be hanging out up here, as usual. I hope they won't be any trouble..."

        "Moxxy" if not collage_pieces_roof[0]:
            jump moxxy

        "Neko" if not collage_pieces_roof[1]:
            jump neko

        "Herra" if not collage_pieces_roof[2]:
            jump herra

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

    mc worried "Can I have your piece of the big project? Without it I’ll never find true love!"

    $ collage_pieces_roof[0] = 1

    moxxy talkingalt "Well if it helps you find true love at that lousy dance tonight then sure."
    moxxy submit "If it doesn't... at least you'll have a cool doodle from your friend Mox right?"

    mc happy "Thanks, you're the best!"

    jump rf

label neko:
    scene bg roof
    show mc worried at left

    mc "{i}It’s the bancho of NG High! I better be respectful or I’ll get my teeth kicked in...{/i}"

    show neko talkingalt at right 

    neko "{b}What do you want, runt?{/b}" with easeinright

    mc "I have a small favour to ask, you’re working on the big project right?"

    neko happy "{b}Yeah, what of it? Come to see my masterpiece?{/b}" 

    mc bashful "Y-yeah, totally, totally... I’ve heard rumors from the other third years that it’s the strongest piece of art in the region."
    mc shy "I’d be honored if you let me share it for you, if that’s true of course."

    $ collage_pieces_roof[1] = 1

    neko threaten "{b}OF COURSE IT IS! THOSE ****S ARE FINALLY GONNA SEE HENTAI AS ART!{/b}"
    neko submit "{b}Take good care of it or you’ll be sucking burgers through a straw ‘til graduation.{/b}"

    jump rf

label herra:
    scene bg roof
    show herra spooked at right

    herra "Wait it’s not what it looks like!" with vpunch

    show mc happy at left
    with easeinleft

    herra talking "Oh it’s just you MC-kun. What are you doing up here?"

    mc "Well Steve and Pico got me these imported chocolates for Valentines Day!" 
    mc worried "I know you were part of the big art project, can I preeeeetty please have your piece? It’s for love..."

    herra confused "Imported... Those sound like the chocolates I got Pico for Valentines Day." 

    mc shy "Haha not really sure what you mean by that can I have the picture?"

    $ collage_pieces_roof[2] = 1

    herra submit "Sure, it might have a little spray paint on it though..."

    jump rf

label surprise_meeting:
    $ finished_rooms = sum([1 if all(i) else 0 for i in total])

    if finished_rooms == 1:
        scene black
        "You suddenly find yourself running into someone." with hpunch
        #sfx, oof!
        $ renpy.scene()
        $ renpy.show(in_between_scene)

        show mc nervous at left
        show p angry_uniform at right
        p angryalt_uniform "Oof, Watch where you’re..."
        p happy_uniform "MC-kun you’re back! I was worried you were gonna miss the Promdancestravaganza(tm)"

        mc shy "Oh, hi Pico.. I wouldn’t miss it for the world."

        p "Funny running into you right now!" 
        p @ gremlin "I was just on my way to target practice."
        p "Care to join?"

        mc "{i}If I don’t come up with something fast I’ll be the target!{/i}"
        mc worried "OH yeah would love to but I uhh"
        mc "I gotta go to the optometrist for my teeth whitening appointment! I mean..." with hpunch 
        mc "I left my oven outside! Or uhh what I was trying to say was..." with hpunch
        mc nervous "Gotta take out the trash!" with vpunch
        hide mc
        mc "WOAH would you look at the time gotta scoot see you later okay bye!" with easeoutleft

        p talking_uniform ""
        p sideeye_uniform "What?"
        scene black with fade

    elif finished_rooms == 2:
        scene black
        "You suddenly find yourself running into someone. Again." with hpunch
        #sfx, oof!
        $ renpy.scene()
        $ renpy.show(in_between_scene)
        with fade
        show mc worried at left
        with easeinleft

        mc "Oh shit I’m sorry"

        show s talking_uniform at right
        with easeinright

        s "Sorry for what?"

        mc neutral "For bumping into you."

        s "Oh you know you can bump into me any time." 
        s flirt_uniform "With your cock."

        mc nervous "Oh, you mean like a rooster?"

        s "Yeah, right, like a rooster."

        mc shy "Heh, scared me there for a sec."

        s talking_uniform "Yep..."

        mc bashful "..."

        hide mc
        mc "I should get going now." with easeoutleft

        s "Yyyeah. See you at the Promdancestravaganza(tm)"
        scene black with fade

    elif finished_rooms == 3:
        $ renpy.scene()
        $ renpy.show(in_between_scene)

        show mc worried at center
        with ease

        mc worried "My mc-senses are tingling..."

        show p confused_uniform at right 
        show s confused_uniform at left 
        with vpunch

        ps "MC-kun!"

        hide mc worried
        mc "Insipid startled sounds." with easeoutright

        p confusedalt_uniform "What gives? Do you think he’s mad at us?"

        s "I don’t think so..."
        s talking_uniform "Wait, did you brush your teeth today?"

        p happy_uniform "Yeah of course. You must have that nasty swamp-ass today."

        s "Ugh, I know! It’s only natural in a sub-tropical climate like this. Anyway, I should probably change before the Promdancestravagnza(tm)"

        p sideeye_uniform "Ditto. I can feel it coming on too..."

        jump second_part

    jump school_map

label second_part:
    scene bg entrance
    show t talking at right
    with fade

    t "Took you long enough MC-kun!"
    t @ threaten "It's almost time." with dissolve

    show mc shy at left
    mc "Haha, yeah I'm pretty slow sometimes." with easeinleft

    t "You’ve got that right, now hand over the pieces."
    t "I’ll put it together while you go get ready and we’ll meet back at the hallway outside of the gym."
    #sfx unzip, clothes ruffle, pissing

    scene black with fade

    scene bg hallway
    show mc nervous at left
    show t talking at right
    with fade
    mc "Man, some of the places in this school are really poorly made"

    t "Yeah they must’ve spent most of their time setting up the gym"

    t angry "But that’s not important right now! Here, I’ve put it back together for you"

    #triumph sfx!
    "Collage get!"

    t talking "Well, what are you standing around here for? Get in there!"

    mc worried "But what do I say? What should I do?"
    mc @ yiiking "Oh man I’m YIIKING OUT RIGHT NOW"

    t unu "I think you just need to get out there and speak from the heart."
    t "When you stay true to yourself MC-kun it doesn’t matter who you talk to, they’ll understand."

    mc shy "You really mean that?"

    t talking "I mean kinda I guess."
    t "Now get that dick!" with vpunch

    mc nervous "What?"

    #scene cut to black, sfx scene of tumbling, skidding, doors swinging open, the works
    scene black with hpunch
    "You suddenly find yourself pushed through the doors, skidding across the gym floor on your face."
label at_prom:

    play music gay volume 0.5
    $ time = 3                                        ### set variable time to 3
    $ timer_jump = 'lovemenu_slow'                    ### set where you want to jump once the timer runs out
       
    scene bg prom 
    show mc nervous at center
    with fade

    mc "Man, I hate it when that happens..."
    show mc worried
    show p talking_formal at right
    p "Are you alright MC-kun? We’ve been trying to reach you about your car’s extended warranty." with easeinright

    show s who_formal at left
    show mc:
        flip
    s "Shut up Pico, do you know how much that dates the game!?" with easeinleft
    s flirt_formal "We’ve been trying to corner your tight ass all day."

    mc "{i}Oh Crap{/i}"
    mc "Hi Pico, Hi Steve"

    s "You really went all out for this Promdancestravaganza(tm) huh."
    
    show mc:
        unflip
    p happy_formal "Well now that you’re here we can finally get to our dance."
    
    show mc: 
        flip
    s confused_formal "Hate to shatter your sad, naive delusions, but MC-kun is obviously here to ask yours truly."
    
    show mc:
        unflip
    p angry_formal "In your dreams, why would they ever want to dance with a *cock joke* like you?"

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
    show p heartbroken
    $ choice = 0
    $ endingbg = "bg steveend"
    play sound "sfx/no regerts.mp3"
    hide p with dissolve


    show s at right
    with ease
    s who_formal "Oh.. This looks... Great.. Thanks"

    show mc shy at left
    mc "I kinda figured you'd say that, so I also got you this." with ease

    s shockedalt_formal "Is that... A pretty pink birthday cake with my face on it? You didn't do this because I referenced it at the beginning of the game.. Did you?"

    show s confused_formal at right 
    mc bashful "No Steve, I did it because I care."

    show s at center
    with ease

    s love "Just kiss me you black and white son of a gun!"

    jump the_end

label choose_pico:
    show s heartbroken
    $ choice = 1
    $ endingbg = "bg picoend"
    play sound "sfx/stevecry.mp3"
    hide s with dissolve

    p sideeye_formal "Don't do this... I have a dark secret"

    show mc bashful at left
    mc "I know what you are..." with ease

    show p talking_formal

    p @ angry_formal "Then say it. Out loud."

    mc nervous "..."

    mc "... A character in a wildly popular rhythm game"

    mc worried "But I love every part of you! From the edgy flash game you to the freaky on a friday night you! You make me feel warm inside"
    show mc bashful at left

    show p at center 
    with ease
    p love "MC-kun...  Would you like me to make you feel warm on the outside?"

    jump the_end

label choose_trash:
    $ choice = 2
    $ endingbg = "bg trashend"
    show s whoalt_formal
    show p flabbergasted_formal
    ps "WHAT?!" with vpunch

    s who_formal "Who the **** is Trash-Can?!"

    p angry_formal "Forget this, you two deserve each-other, you ARE Trash!"

    hide s 
    hide p 
    with dissolve

    show mc worried at left
    with ease

    show t unu at right
    with easeinright
    t "Is.. Is that how you really feel MC-kun?"

    mc "Yes, Trash-Can, you've always been there when I've needed help."

    mc happy "You complete me!"

    t talking "Oh MC-kun, Kiss me!"

    jump the_end

label the_end:
    # End Credits

    ## We hide the quickmenu for the End Credits so they don't appear at the bottom.
    $ quick_menu = False

    ## We hide the textbox as well so it doesn't mess with things
    window hide
    $ renpy.scene()
    $ renpy.show(engingbgs[choice])
    with fade

    ## Find "End Credits Scroll" in extras.rpy to change text.
    call screen credits

    $ persistent.credits_seen = True
    
    # Players can skip the credits in subsequent playthroughs of the game.
    label skip_credits:
 
        pass

    ## We re-enable the quickscreen as the credits are over.

    $ quick_menu = True

    ## Makes [result] work. This needs to be near the end of the game
    ## for it to work properly.
    $ percent()

    ## We display a screen that shows how much the player has seen and played of the game.

    $ renpy.scene()
    $ renpy.show(endcards[choice])
    with fade
    show screen results
    
    centered ""

    hide screen results

    pass

label return_to_sender:
    # This ends the game.
    return