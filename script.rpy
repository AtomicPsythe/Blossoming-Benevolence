# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Ren = Character("Ren", who_color = "#53302c")
define Aaliyah = Character("Aaliyah", who_color = "#eb9486")
define Ashton = Character("Ashton", who_color = "#534b53")
define Sarah = Character("Sarah", who_color = "#975f3b")
define Waitress = Character("Waitress")

# Images

image Ren happy = "sprite4 happy small.png"
image Ren sad = "sprite4 sad small.png"
image Ren angry = "sprite4 angry small.png"
image Sarah happy = "sprite1 happy small.png"
image Sarah angry = "sprite1 angry small.png"
image Sarah sad = "sprite1 sad small.png"
image Ashton happy = "sprite3 happy small.png"
image Ashton sad = "sprite3 sad small.png"
image Ashton angry = "sprite3 angry small.png"
image Aaliyah happy = "sprite2 happy small.png"
image Aaliyah sad = "sprite2 sad small.png"

# Text Speed (Word by word)

default preferences.text_cps = 20

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show sprite4 happy small with fade

    # Prologue

    "Hi."

    "My name is Ren Lyons."

    Ren "I’m 16 years old, I live in a small-town named Thornwood in the middle of absolutely nowhere with one cat and an ungodly number of books."

    Ren "I have Aaliyah who is my best friend in the whole entire world whom I would never be able to live without and then my family, who are well, my family…"

    Ren "I have very few friends who I adore…"

    show sprite4 sad small

    Ren "But I’m lonely."

    Ren "I think I’m lonely the most at night times, specifically at dusk, that time and moment when you are unsure if you are awake or still dreaming."

    Ren "Those moments when you find yourself wrapped around in your blanket that can feel a little too human like, so you start your days off sad and people constantly wonder why."

    Ren "The feelings creep up behind you at the worst times. During family gatherings, friendly outings, and especially when you’re by yourself."

    Ren "I think I’m lonely all the time."

    Ren "A dark cloud looms above my head whenever I think of not having a person who adores me for me and to spend every moment together to create everlasting memories with each other… I am begging for this."

    Ren "I’m aware another person should not be your only source of happiness, but the absence of another seems to be my only source of unhappiness nowadays."

    show sprite4 happy small

    Ren "So, hi."

    Ren "This is probably the weirdest introduction you have ever heard. But I’m lonely. And this is the story of how I became no longer lonely."

    hide sprite4 happy small

    with fade

    # Scene 1

    show sprite1 happy small at left

    Sarah "Hey Ren! What's up?"

    show sprite4 happy small at right

    Ren "..."

    Ren "Oh, hey Sarah, I was just about to head into class, how about you?"

    Sarah "Perfect then! May I pull you aside for a little bit? I want to talk to you about something."

    Ren "Sure, yea of course, lead the way."

    scene school_hallway_day

    "I follow Sarah deeper down the hallway into a secluded part of the stairs."

    "The sun is not as vibrant here, it appears it has gotten cloudy or maybe a tree is blocking its rays. Nevertheless, I listen to what she has to say."

    show sprite1 happy small at left
    show sprite4 happy small at right

    Ren "Interesting location, so what is it you wanted to tell me?"

    Ren "We should make it quick since class is starting soon."

    Sarah "So, I just wanted to express to you that I’ve loved the way you have been treating me recently and have enjoyed all the time we have spent together. And I’ll just come out and say it…"

    Sarah "I like you! I have a crush on you Ren!"

    Ren "Oh, wow Sarah, I didn’t know you felt this way."

    Ren "I appreciate that you are able to express how you feel towards me, but I don’t think I can accept this sentiment right now…"

    Ren "It has nothing to do with you, it’s just I am in a weird phase of my life right now and all of that, so I think being alone will be the best for me at the moment. I’m sorry it had to come to this."

    Sarah "No no its ok! I totally understand that!"

    hide sprite1 happy small

    "After seeing Sarah run off, I think I royally messed that up. It’s not like what I said was incorrect, I have been feeling… different recently."

    "I have started to think some guys at school are… cute? Only passerby ones though… which I guess doesn’t make a difference."

    "It’s really weird, I need Aaliyah for this because she knows me better than I do myself sometimes, and now is for sure one of those times."

    "Anyways, I can deal with that later, for the time being I should really head back to class, considering I’m probably going to be late."

    scene classroom_day

    "Upon entering class, we are introduced to a new transfer student."

    show sprite3 happy small

    "His name is Ashton Mills, he has black hair with vibrant blue eyes, multiple pieces of jewelry including rings and many piercings."

    "He appears more closed off compared to everyone in the class, which I guess makes sense since he just transferred here. I should introduce myself to him once first period is over, I’m sure it’ll help him feel better."

    scene classroom_day with fade

    "Phew, now that class is over I can introduce myself to him."

    show sprite4 happy small at left
    show sprite3 happy small at right

    Ren "Hey there! You must be the new transfer student, right? I wanted to introduce myself to ease your transition, my name is Ren!"

    Ashton "..."

    Ren "It’s nice to meet you?"

    Ashton "..."

    "I don’t think he can hear me considering he has these giant black headphones on. I begin waving my hand in front of his face and tapping his shoulder, where I finally get his attention."

    Ashton "Oh, hey there! Sorry I couldn’t hear you; I was listening to some music."

    Ren "It’s alright. Let me reintroduce myself, my name is Ren!"

    Ashton "Hey there Ren! I’m Ashton, but you can call me Ash if you prefer."

    Ren "Cool, will do! What’re you up to? What kind of music are you listening to?"

    Ashton "Nothing really, first period was kind of boring so I’m just going to sit here by the window until my next period starts."

    Ashton "As for what music I’m listening to, want to give it a listen? I can lend you, my headphones."

    Ren "Sure!"

    "I put on Ash’s headphones, where I am greeted by something I was not expected to hear. It’s some relaxing guitar lo-fi music."

    "I was expecting something more intense like rock or death metal based off of his appearance and demeanor, that is until I actually talked to him."

    Ren "Wow, I love your music taste, lo-fi is one of my favorite genres to listen to!"

    Ashton "Same here, although many people assume the opposite because of my appearance and demeanor."

    Ren "I don’t get how people can assume things like that, it’s weird."

    Ashton "Right? Anyways, you are super chill and cute, I like your company."

    "DID HE JUST CALL ME CUTE? I’M INTERNALLY FREAKING OUT! I WAS SUPPOSED TO TALK WITH AALIYAH AFTER CLASS BUT I GOT HUNG UP WITH ASH, AND NOW I AM DYING."

    Ren "Why thank you! You are also equally chill and cool, let’s hang out more sometime!"

    Ashton "Of course, I’d love that, let me give you my number and socials so we can chat some more."

    "We exchange contact information and then part ways. Now I REALLY need to find Aaliyah and update her on everything that has happened this morning."

    scene classroom_day with fade

    # Scene 2

    scene school_hallway_day

    "Upon parting ways with Ash, I go and find Aaliyah where I see her chatting with some of her classmates."

    show sprite4 happy small at left

    Ren "Aaliyah!"

    show sprite2 happy small at right

    Aaliyah "Oh, hey Ren! What’s up bestie?"

    hide sprite4 happy small at left

    show sprite4 sad small at left

    Ren "I... uh... need you for some uh school help!"

    Aaliyah "Sure yea! See you later guys, message me if you need anything at all!"

    Ren "Ok, so I don’t actually need school help."

    Aaliyah "That was the easy bit to figure out, please."

    hide sprite4 sad small at left

    show sprite4 happy small at left

    Ren "Anyways, I have A LOT to update you on, something happened with Sarah and the new guy."

    Aaliyah "Sarah? What did she do now? And the new guy? You mean Ashton?"

    Ren "Well… Sarah kind of confessed that she has a crush on me…"

    Aaliyah "OMG! Did you say yes?"

    Ren "Well… that’s also where I need your help."

    Aaliyah "Hm? What do you mean?"

    hide sprite4 happy small at left

    show sprite4 sad small at left

    Ren "You see, I turned her down, and not for the reasons you may be thinking of like she’s not my type or anything."

    Aaliyah "Is it because you may have a thing for guys?"

    hide sprite4 sad small at left

    show sprite4 happy small at left

    Ren "Well you see it's because- WAIT... How do you know?!"

    Aaliyah "Ren... I’ve known you for basically almost all of my life, that was the easy part haha."

    Ren "Fair, I guess? Anyways, I’m not sure as to what to do."

    Aaliyah "Well, you may be feeling these intense feelings right now because you just met him and were on a high of emotions since you instantly clicked."

    Aaliyah "Give it some time, no need to stress out about it, keep it at the back of your mind but don’t put too much pressure on yourself."

    Ren "You’re right, maybe I am just thinking too much into it right now… Thanks for your help bestie again, are you doing anything after school?"

    Aaliyah "Yea, I’m meeting some of the girls later, would you want to join us or nah?"

    Ren "I think I’ll just go home and catch up on some school stuff, maybe re-evaluate this whole situation that happened today. But thanks for the offer and I hope you have fun! You deserve it wholeheartedly!"

    Aaliyah "Aww, alrighty then! If you legit ever need my help, message or call and I’m on my way, don’t care about time or place, got it?"

    Ren "Of course, love you Aali!"

    Aaliyah "Love you too, R!"

    hide sprite4 happy small

    hide sprite2 happy small

    "As per usual, it felt super relieving to talk with Aaliyah about my problems. I don’t mean to overwhelm her of course, but she just gets me on every level."

    "I guess that’s what happens when you’ve been besties from the fetus stages. Looks like it’s time to go home for the time being, have to be a good student and actually do my schoolwork you know."

    scene school_hallway_day with fade

    scene bedroom_night

    "Honestly, today was one of the weirder days I’ve experienced as of recently."

    "From Sarah’s confession to my sudden romance for Ashton, today has tired me out emotionally, but I feel like reflecting upon everything will help to put me at ease."

    "Sarah’s confession wasn’t bad, I just don’t feel the same way about her, so it isn’t her fault, I should probably talk to her about it and apologize next time I see her."

    "As for Ashton, Aaliyah was right, maybe we did just click together instantly, but that won’t change the fact that he called me cute and that I genuinely felt something after hearing his words."

    "But I shouldn’t jump to conclusions yet, spending more time with him may be a good idea just to wager how I really feel about him, if it’s a crush or just an emotional reaction to those words. Only time will tell I guess, but for now it is time to sleep."

    show bedroom_night with fade

    # Scene 3

    scene bedroom_day

    "Waking up today, I feel excited for school? Which is not a feeling I get very often, only when there are special events or the food options for the day are my favorites."

    "But today, I was excited for neither reason… well equally excited and nervous to be exact."

    "I want to spend time with both Sarah and Ashton today, but I only have enough time for one since it’s a shorter school day today."

    "I guess if I spend time with Sarah, I can explain myself from yesterday and all will be well between us hopefully."

    "But if I spend time with Ashton, I can get to know him better and potentially see where our acquaintanceship evolves into."

    menu:
        "Hmm who to go with?"

        "Sarah":
            scene school_hallway_day with fade

            "Finally arrived at school, time to find Sarah. Knowing her she’s probably either in the library or at her locker. I’ll check both just to make sure."

            "Upon finding Sarah, I muster up the courage to talk to her about what happened the other day."

            show sprite4 happy small at left

            Ren "Hey Sarah, are you busy? I wanted to explain myself after what happened the other day."

            show sprite1 happy small at right

            Sarah "Oh, hey Ren. I’m free, what do you want?"

            hide sprite4 happy small

            show sprite4 sad small at left

            Ren "Listen, I just wanted to apologize for the way I may have acted or reacted. I still like you as a friend and a person, but I’m just undergoing some personal changes right now so I don’t think I can be in a relationship."

            Ren "Again, I am sorry it resulted like this but please forgive me."

            Sarah "First of all, I appreciate your concern in how I feel and thank you for reaching out to apologize. Second, I’m fine, Ren. Yes, it does hurt to be rejected, but it’s not the end of the world, I’ll live trust me."

            Ren "I know that, I just wanted to ensure that you were alright and were not sad and or mad at me for how I handled it."

            Sarah "No, you’re fine, it will for sure take some adjusting to go back to how I felt towards you pre-crush, but that’s normal."

            hide sprite4 sad small

            show sprite4 happy small at left

            Ren "Very valid if you need help you know where to find me!"

            Sarah "Yes, I do, but I think something like this is better dealt with alone rather than with the person who just rejected you, no offense."

            hide sprite4 happy small

            show sprite4 sad small at left

            Ren "Ahh right my bad, I didn’t think of that, sorry."

            Sarah "It’s ok Ren, well I have to leave for now to study for a test I have coming up, so see you later!"

            hide sprite4 sad small

            show sprite4 happy small at left

            Ren "Bye Sarah, good luck with your test!"

            "Well, I would say that worked out successfully, seems like things are officially cleared up between Sarah and me. All there is to do now is to give her the space she needs, which is fine. But now, it is my time to head to class and then go home."

            hide sprite4 happy small

            hide sprite1 happy small

            scene bedroom_night with fade

            "Today was a fulfilling day, I finally got to clear things up with Sarah and it seems like we are back to normal now… well somewhat back to normal."

            "But honestly, I’ll take what I can get, I just want my friend back that’s all. I do feel kind of bad that I didn’t get to see Ashton or Aaliyah today though…"

            "I can probably see them both tomorrow and spend some time with them since Sarah needs her space. But that’s tomorrow me’s problem, for now current me’s problem is finding a way to fall asleep and not stay up reading fanfiction until midnight."

            # Scene 4: Sarah Version

            scene school_hallway_day with fade

            "Surging with energy, I am ready to conquer today, and that is starting with talking with Aaliyah."

            "As I walk through the hallways looking for her, I find her at her locker talking with this girl I’ve never seen before. I await until their conversation is over then I head over to talk to her."

            show sprite2 happy small at left

            Aaliyah "Oh, hey Ren!"

            show sprite4 happy small at right

            Ren "Hey Aaliyah, who was that girl you were talking to?"

            Aaliyah "Oh, she’s some girl from my class that asked to hang out together sometime this weekend~"

            Ren "Oh? Look at you miss smooth moves! What’s she like?"

            Aaliyah "She’s super cool, kind of like Ashton now that I think about it in terms of style, but her personality to me is what really caught my attention. She’s super loving and appreciative of everything and everybody, so I really hope we have a good time this weekend!"

            Ren "I hope so as well! Well, it looks like we are both swoon for some people!"

            Aaliyah "So that means you and Ashton are getting along well, right?"

            Ren "Yea, we are getting along well, I haven’t spoken to him since the last time I talked to you. I confronted Sarah yesterday about the whole confession thing and we are all good now! I was planning on seeing him today just to see how he is doing."

            Aaliyah "That’s amazing, I’m glad everything is cleared up with Sarah! And for sure go spend some time with your man!"

            show sprite4 sad small at right

            Ren "He’s not “my man” … well at least not right now. With the end of our senior year coming up soon, I may want to reassess you know… who I am interested in and make some actions if you know what I mean."

            Aaliyah "Yes for sure! This may sound weird but do some research on what it’s like being queer? You know like watch some YouTube videos, do some of those “am I gay” quizzes, you never know they could be really helpful. Heck I’m even thinking of doing it myself!"

            show sprite4 happy small at right

            Ren "Oh, that’s awesome, I’ll for sure do that! We can keep each other updated on what results we get and experience this together!"

            Aaliyah "Like we say, forever and always, till death do us part bestie!"

            Ren "You know it! Oh, I hate to leave abruptly but it looks like my class is starting in 5 minutes and I have to head to another building for that, ugh I hate it."

            Aaliyah "No worries, RUN GO RUN DON’T BE LATE!"

            Ren "YES YES, OK I’LL TALK WITH YOU LATER BYEEE!"

            Aaliyah "BYEE!"

            hide sprite4 happy small

            hide sprite2 happy small

            "As always, talking with Aaliyah is a breath of fresh air, and I’m happy to find out that I’m not the only one who’s exploring their sexuality."

            "Yes, it does feel weird since it’s a lot of change, but I’m glad I have someone by my side who is going through a similar thing as I am."

            "As soon as class is over, I should probably head home and take some time to reflect on everything Aaliyah told me… plus I need to seriously catch up on some schoolwork."

            show bedroom_night with fade

            "Upon talking with Aaliyah today, some much needed reflection about myself should be put in place."

            "First of all, I should look into what Aaliyah said about those sexuality quizzes, maybe they will finally give me the answers I need. I found a pretty good quiz on this website FeedBuzz, seems like it’ll do the job."

            "..."

            "After going through the quiz, the results were pretty clear… it says I am a homosexual based on my emotional responses and reactions to being around men… specifically the nervous ticks and constantly thinking about another guy."

            "I guess that makes sense… I can’t believe I did not notice and accept this sooner. I need to let Aaliyah know about this. For now, I rest on this information."

        "Ashton":
            scene school_hallway_day with fade

            "Finally arrived at school, time to find Ashton. I don’t know too much about him yet, but he did say he likes some alone time to listen to his music. So maybe I can find him in an empty classroom or by one of the windowsills near the lockers."

            "I’ll check both just to make sure I find him."

            show classroom_day with fade

            "Upon finding Ashton, I muster up the courage to talk to him about what happened the other day."

            show sprite4 happy small at left

            Ren "Hey Ashton, what are you doing over here?"

            show sprite3 happy small at right

            Ashton "..."

            show sprite4 angry small at left

            Ren "Ashton?"

            "I tap his shoulder, just like last time."

            Ashton "Oh, my bad… Ren, was it?"

            show sprite4 happy small at left

            Ren "Yep, that’s me and no worries it’s all good!"

            Ashton "So, what’s up how have you been?"

            Ren "I was just about to ask you the same question, but I am doing fine, just wanted to hang out with you some more after yesterday to get you more accustomed to the school and all."

            Ashton "Oh, thanks I appreciate it, well first of all come sit next to me, just for ease of conversation."

            Ren "S-sure yea I can do that!"

            Ren "So, how do you find life in Thornwood? Is it different from your old town and stuff?"

            Ashton "Well, so far everything is good, the people I’ve met, like yourself, have all been super kind and welcoming to me and the environment of the town feels good so it’s better yea… but the adapting process has been a bit challenging."

            Ren "I’m glad your transition is going well! And I feel you, I struggle myself with adapting to new situations too, but I can help you out in any way you may need!"

            Ashton "Thanks, I really appreciate that! My old town was pretty toxic to my family and I so starting anew is definitely refreshing."

            Ren "Oh? What happened if you don’t mind me asking."

            hide sprite3 happy small

            show sprite3 sad small at right

            Ashton "See, it was specifically my old school. I got bullied a lot from the other guys in my class for “looking and acting gay” which doesn’t make sense because at the time I wasn’t even queer myself."

            Ashton "It happened a lot during and after physical education classes in the gym and bathrooms where we would change from our gym uniforms to our school uniforms."

            Ashton "It got so bad to a point where I unable to attend some classes and had to be excused from them to avoid the hate I would receive."

            Ashton "However, after the end of that school year, my family and I made the decision to move to another town since it became so toxic, which is why I’m here now…"

            Ashton "Also sorry for just dumping that onto you, it was hard keeping it in for so long."

            hide sprite4 happy small

            show sprite4 sad small at left

            Ren "Oh my gosh, Ashton I’m so sorry to hear that. No one deserves to be bullied for “looking or acting gay” whether they are queer themselves or not, that’s just straight up homophobic."

            Ren "Those guys are terrible and probably have some internalized problems or homophobia they are dealing with themselves."

            hide sprite4 sad small

            show sprite4 happy small at left

            Ren "I’m glad you were able to get out of there and start anew though! It must feel refreshing! Besides, I got to become friends with you so I’m happy you're here!"

            hide sprite3 sad small

            show sprite3 happy small at right

            Ashton "Aww thank you thank you! It was also amazing to meet you and become your friend! You’ve treated me so kindly and with a lot of respect and care, so again thank you for that!"

            Ren "Of course, forever and always. Also, you can confide in me in anything, if you feel comfortable, I’ll help you with the best of my abilities!"

            Ashton "Thanks again, well now that all of the sappy stuff are over with, would you want to maybe share headphones and listen to some music together?"

            Ashton "I remembered you said you liked lo-fi music, so I made a playlist of some of my favorite songs."

            Ren "Yes! I’d absolutely love to!"

            "Upon being offered to listen to music with Ashton, I quickly accept, and we spend the rest of the afternoon listening to music together whilst talking about miscellaneous topics."

            "This has truly been an amazing day and I feel the butterflies in my stomach growing each time I talk with Ashton. Eventually, we parted ways to head to our final classes of the day and we each head home."

            hide sprite3 happy small

            hide sprite4 happy small

            scene bedroom_night with fade

            "Today was an amazing day, I got to spend some more time with Ashton, which I loved and wanted."

            "I learned more about his old town and all of the terrible things he had to experience. I hope all of those bullies get what they deserve and receive a rude awakening."

            "But I digress, listening to his custom made playlist together all afternoon was truly a blessing and I couldn’t have asked for a better way to spend my afternoon."

            "Well… I could have cleared things up with Sarah and maybe hung out with Aaliyah some more."

            "I’ll do that tomorrow; they deserve some attention as well. But that’s tomorrow me’s problem, for now current me’s problem is finding a way to fall asleep and not stay up reading fanfiction until midnight."

            # Scene 4: Ashton Version

            scene school_hallway_day with fade

            "Surging with energy, I am ready to conquer today, and that is starting with talking with Aaliyah."

            "As I walk through the hallways looking for her, I find her at her locker talking with this girl I’ve never seen before. I await until their conversation is over then I head over to talk to her."

            show sprite2 happy small at left

            Aaliyah "Oh, hey Ren!"

            show sprite4 happy small at right

            Ren "Hey Aaliyah, who was that girl you were talking to?"

            Aaliyah "Oh, she’s some girl from my class that asked to hang out together sometime this weekend~"

            Ren "Oh? Look at you miss smooth moves! What’s she like?"

            Aaliyah "She’s super cool, kind of like Ashton now that I think about it in terms of style, but her personality to me is what really caught my attention. She’s super loving and appreciative of everything and everybody, so I really hope we have a good time this weekend!"

            Ren "I hope so as well! Well, it looks like we are both swoon for some people!"

            Aaliyah "So that means you and Ashton are getting along well, right?"

            Ren "Extremely well, we spent the whole the whole afternoon yesterday together, where he opened up to me about his old town and life and we listened to some music together! It was pure bliss truly!"

            Aaliyah "Ooohh, you get ‘em tiger! Strut your stuff and keep up the good pace!"

            Ren "That’s ultimately the goal, I mean with the end of our senior year coming up soon, I may want to reassess you know… who I am interested in and make some actions if you know what I mean."

            Aaliyah "Yes for sure! This may sound weird but do some research on what it’s like being queer? You know like watch some YouTube videos, do some of those “am I gay” quizzes, you never know they could be really helpful. Heck I’m even thinking of doing it myself!"

            Ren "Oh, that’s awesome, I’ll for sure do that! We can keep each other updated on what results we get and experience this together!"

            Aaliyah "Like we say, forever and always, till death do us part bestie!"

            Ren "You know it! Oh, I hate to leave abruptly but it looks like my class is starting in 5 minutes and I have to head to another building for that, ugh I hate it."

            Aaliyah "No worries, RUN GO RUN DON’T BE LATE!"

            Ren "YES YES, OK I’LL TALK WITH YOU LATER BYEEE!"

            Aaliyah "BYEE!"

            hide sprite4 happy small

            hide sprite2 happy small

            "As always, talking with Aaliyah is a breath of fresh air, and I’m happy to find out that I’m not the only one who’s exploring their sexuality."

            "Yes, it does feel weird since it’s a lot of change, but I’m glad I have someone by my side who is going through a similar thing as I am."

            "As soon as class is over, I should probably head home and take some time to reflect on everything Aaliyah told me… plus I need to seriously catch up on some schoolwork."

            show bedroom_night with fade

            "Upon talking with Aaliyah today, some much needed reflection about myself should be put in place."

            "First of all, I should look into what Aaliyah said about those sexuality quizzes, maybe they will finally give me the answers I need. I found a pretty good quiz on this website FeedBuzz, seems like it’ll do the job."

            "..."

            "After going through the quiz, the results were pretty clear… it says I am a homosexual based on my emotional responses and reactions to being around men… specifically the nervous ticks and constantly thinking about another guy."

            "I guess that makes sense… I can’t believe I did not notice and accept this sooner. I need to let Aaliyah know about this. For now, I rest on this information."



    # Scene 5

    scene school_hallway_day with fade

    "Waking up this morning felt weird, obviously after seeing the quiz results from the other night. I just feel shocked yet also not at the same time."

    "Like, I equally expected those results as I also didn’t expect the results. It’s a weird feeling to say the least, but the one person who I know could help me with this is, of course, Aaliyah."

    "She knows me inside and out so maybe she can make some sense of these results and calm my nerves and confusions."

    show sprite4 happy small at left

    Ren "Aaliyah! Finally, I found you, I need your help… again."

    show sprite2 happy small at right

    Aaliyah "Why hello again my bestie, what brings you to Aaliyah’s advice emporium today?"

    Ren "Well, you see, I did the quiz you recommended for me to try the other day."

    Aaliyah "The “am I gay” one?"

    Ren "Yes, an-"

    Aaliyah "Well, what did it say? Oh wait, you were going to say that. My bad, carry on now."

    Ren "As I was saying, the results told me that I am gay and, to be honest, I’m not sure how to process that information."

    Aaliyah "Ren, you don’t necessarily need to embrace that now. Sure, some silly little quiz told you that you may be gay, but if you aren’t ready to accept that yet then no worries."

    Ren "So, I can just keep this information to myself and just think back to it in certain situations?"

    Aaliyah "Like with Ashton, yes."

    Ren "I wasn’t going there!"

    Aaliyah "Yes, you were you just had a hard time saying it that’s all!"

    Ren "Ok, fine you may be right but that’s not the point now!"

    Aaliyah "Well, it is MY point."

    Ren "Huh, what do you mean?"

    Aaliyah "You see, I was ALSO looking for you today because my parents gave me these two tickets to an orchestra event this weekend."

    Aaliyah "They couldn’t go because of work responsibilities, and since I don’t like that type of music, I decided to give them to you!"

    Ren "Oh wow, thanks, I guess? I’m not sure who to go with though."

    Aaliyah "I’ll leave that to you to think about, but your welcome for the tickets and I must be skedaddling to my next class now so, byeeee!"

    hide sprite2 happy small

    Ren "Aaliyah wait I-…"

    "And just like that Aaliyah is gone in a flash, and I am left with much confusion. It was very thoughtful of her to give me these tickets and all but I’m not sure who I’d want to even go with."

    "Well… there are two people I can think of… it’s really either Sarah or Ashton."

    menu:
        "Let me think, who would I want to really go with and get to know better?"

        "Sarah":
            "I think I’m going to go with Sarah, I mean she’s a nice girl and I still feel bad about the whole confession thing, so this may be a way to make it up to her about it all. I’ll go look for her later to ask her myself."

            hide sprite4 happy small

            scene cafeteria_day with fade

            show sprite4 happy small at left

            Ren "Hey Sarah!"

            show sprite1 happy small at right

            Sarah "Oh, Ren, hey there. What’s up?"

            Ren "I was looking for you because I wanted to ask you something."

            Sarah "Oh? What did you need?"

            Ren "Well, you see, Aaliyah gave me these two tickets to an orchestral concert this weekend and I was wondering if you’d want to go with me?"

            Sarah "Oh my, yes! Of course, I’d go with you! I personally love orchestral music, so this is right up my alley!"

            Ren "Oh wow, that’s amazing then! Funny enough, its tomorrow, is that still fine?"

            Sarah "Yes, it should be! I’m just going to let my parents know and all, but it should work out!"

            Ren "Lovely, amazing! I’ll hold onto the tickets, and I’ll message you the details of the event later today, yea?"

            Sarah "Perfect, that works for me! Thanks Ren!"

            Ren "My pleasure, thanks for accepting!"

            hide sprite1 happy small

            hide sprite4 happy small

            "Believe it or not, that worked out much better than it did in my head. I’m glad she said yes, now I just await until tomorrow to experience the event to its fullest!"

            "Gosh, I’m so excited I’m going to have a hard time concentrating in class!"

            "I should probably put that on the backburner though so I can focus on the one single class I have left for today. Then I go home and rush all of my homework so that tomorrow is a free day!"

            # Scene 6

            scene bedroom_day with fade

            "Alas, it is finally the day to go to the orchestra concert. Not going to lie I’m a bit nervous for it, but I also have the rest of the day to mentally prepare myself for it."

            "I just need to remember to stay calm, cool, and collected and all should go well! I’ll confirm with Sarah that all is well still and that she can still attend the concert."

            scene street_summer_night with fade

            "Upon arriving to the venue, I see Sarah waiting at the entrance already. Guess I must be fashionably late, or maybe she’s just early. Whatever the case may be I go up to talk to her."

            show sprite4 happy small at left

            Ren "Hey Sarah! You look nice this evening!"

            show sprite1 happy small at right

            Sarah "Oh, hey Ren, didn’t see you there, and thanks you look handsome as well!"

            Ren "It’s alright, shall we head inside?"

            Sarah "Yes lets!"

            scene orchestra with fade

            "We head inside the venue and get seated in a secluded balcony, as the show begins. As the show goes on, we sit in silence until Sarah says something to me."

            Sarah "Wow this concert is amazing! All of these musicians are so talented, and the music is so intense yet soothing, I kind of love it!"

            Ren "Same, there’s a reason why I love this kind of music!"

            Sarah "I definitely see what you mean now!"

            Ren "Hey Sarah, do you mind if I ask you something?"

            Sarah "Yes of course, anything."

            "As she responds, she puts her hand atop of mine and begins to intertwine her fingers with mine."

            Ren "So, uh, it’s about the confession, just one last thing to confirm. Can we still be friends like we were before, even if I someday do have a crush on you myself?"

            Ren "I feel like it would ruin our dynamic and history that we have and I don’t want mess that up and lose you forever."

            Sarah "Aww Ren, of course we can be friends still! Yes, while I did develop more deeper feelings for you that I would like to admit, whether we ended up in a relationship or not I would still want you in my life and still want to be friends with you still no matter what."

            Ren "Ok good, promise?"

            Sarah "I promise, like you always say, forever and always!"

            "She holds out her pinky and I do the same as we interlock pinky fingers, sealing our promise."

            Ren "Good, I’m glad we can agree on that, now let’s just enjoy the rest of the sh-"

            "As I am mid setence, I look down into the audience and notice a familiar face. One I did not expect nor want to see tonight at this particular concert."

            show sprite4 sad small at left

            Ren "Oh no, oh no no no no no no no..."

            Sarah "Ren, what’s wrong? Talk to me."

            Ren "A-Ashton is down in the audience, and I think he saw us together, no no no no no..."

            show sprite1 angry small at right

            Sarah "What’s wrong with that?"

            Ren "See, the thing is I think he likes me and I’m not sure if I like him and all and I think him seeing us may have given him the wrong idea an-"

            show sprite1 sad small at right

            Sarah "Ren. Slow down. Calm down. Breathe, everything is going to be ok. You’re going to be ok; you just need to explain yourself to him that’s all."

            Ren "Right yea, you’re right, everything is going to be ok… right. Let’s just enjoy the rest of the concert, I’ll talk to him when I see him in school next…"

            Sarah "Alright, if you insist."

            "Needless to say, after that, my stress levels soared through the roof, and I don’t think I was able to concentrate on the concert nor think clearly for the rest of that evening."

            "Sure, to any other person, seeing someone from school in a crowd can either result in one of two things, one you interact with the other person and have small talk, or two you avoid them at all costs."

            "Now, I would’ve done this if it was anyone BUT Ashton to not give him the wrong idea… oh my I think I messed up… again."

            "I seriously need to talk to him, but through text would be so awkward and weird, it has to be at school for sure. I have to search for him next week and hope to explain that what he saw isn’t what he thought he saw… if that makes sense?"

            # Scene 7

            scene school_hallway_day with fade

            "It has been about a week since the whole concert incident with Sarah and Ashton, and yet I’m still unsure on what to do and how to feel about what happened."

            "Like I still want to talk with him to clarify what he may have seen just so he doesn’t get the wrong idea."

            "But I also feel as though, after seeing that, he may want to avoid me at all costs, which is valid, but I can’t not clear things up, that’s the right thing to do. Just as I am stuck in thought about this a familiar face approaches me."

            show sprite2 happy small at left

            Aaliyah "Hey Ren! You have to tell me all about that concert last weekend! How did it go?"

            show sprite4 sad small at right

            Ren "Hey Aaliyah..."

            show sprite2 sad small at left

            Aaliyah "Oh my, that’s a “Ren doesn’t feel good hey”. What’s wrong?"

            Ren "See… it’s about the concert…"

            Aaliyah "Oh no what happened?"

            Ren "So, uh, I decided to ask Sarah, you know to make it up to her and all, and I was about finished clearing things up with her."

            Ren "But she then places her hand upon mine and then I looked down into the crowd, since we were seated on one of the balconies, and I see Ashton looking up at me with his face crumpled."

            Ren "From there on out, I was not able to think or act clearly for the rest of the evening and have been trying to find a way to gain the courage to talk to him to explain everything… but I just haven’t."

            Aaliyah "I see what happened, it sounds like one big misunderstanding clearly."

            Aaliyah "Unless I interpreted things incorrectly myself, but we all know the resolution to misinterpretations, and that’s just talking. So go and find Ashton and just talk to him about it, it’ll clear things up instantly."

            Ren "I guess you’re right; I was just overthinking everything as per usual."

            show sprite2 happy small at left

            Aaliyah "And we love you for that, but right now overthinking is not the answer, talking is."

            Ren "That’s true, I’ll go do that. Wait, before I do, how was your date with that girl?"

            Aaliyah "That’s irrelevant right now, I’ll tell you more about that once this is settled with."

            show sprite4 happy small at right

            Ren "Fine if you say so. I’ll see you later!"

            Aaliyah "Bye bye, good luck!"

            hide sprite2 happy small

            hide sprite4 happy small

            "Once I part ways with Aaliyah, I scout the school for Ashton."

            "Since he could literally be anywhere, I try to remember the places where we used to hang out a lot together, it would either be by the windowsills in the halls or in the classroom where we first met, which is now emptied and no longer being used."

            "I’ll check the classroom first… I have a feeling he would be in a secluded area to spend some time alone."

            show classroom_day with fade

            "And to no one’s surprise, I find him sitting in the far-left desk next to an open window staring outside as he is now wearing his old big black headphones again… that doesn’t feel like a good thing to me. Nonetheless, I go up to talk to him."

            show sprite4 sad small at left

            Ren "Hey Ashton… I know you may not want to see but can we talk?"

            show sprite3 angry small at right

            Ashton "..."

            Ren "Ashton? Hello?"

            Ashton "..."

            Ren "Listen, I know I messed up but please talk to me… please."

            "As I am saying this, I tap his shoulder to get his attention. Wait, this feels familiar..."

            Ashton "Oh, I didn’t see or hear you there. Hey Ren… what do you want to do with me now."

            Ren "Finally! Your attention please!"

            Ashton "What is it? Wasn’t last weekend enough awkwardness already?"

            Ren "I can explain myself."

            menu:
                Ashton "Dude really? You know we made eye contact at the theatre and we both know you were there with your girlfriend, so what is there to even talk about and or clarify."

                "Sarah is my girlfriend":

                    Ren "Well, I thought that I’d just let you know that I am beginning to be interested in Sarah…"

                    Ren "I know this may hurt considering we may have had something going on, but something sparked within me that night with her… I’m sorry it had to turn out this way."

                    Ashton "You know what, whatever Ren, I don’t really care anymore. If you want to be with this Sarah chick, then go ahead, but I really thought we had something together."

                    Ashton "The times we hung out and shared deep conversations with each other, the shared playlist, and songs… I guess it was all one sided after all."

                    Ren "Listen, I did enjoy that time with you and I wouldn’t take it back for the world, but I don’t know, I just got swoon for her."

                    Ashton "Well congratulations Ren, I hope all goes well for you two. Now if you will excuse me, I have somewhere else to be right now."

                    Ren "Ashton wait I-"

                    hide sprite3 angry small

                    "And just like that… Ashton was gone. Low and behold that would be one of the last times I see him again."

                    "I tried my best to confront him, but I guess it wasn’t enough. I guess royally messing up things seems to be my shtick. I’ll just head home early for the day… I really don’t feel like attending class anymore."

                    # Scene 8

                    scene school_hallway_day with fade

                    "It has been a couple of days now since the whole Ashton incident, where I confronted him about the concert a couple weeks ago. Not going to lie, it has been kind of hard to deal with… like yes, I was honest, but having to lose a friend over it hurt."

                    "Having lost Ashton and distanced myself from Sarah, because of the whole situation, the only real person I have left is Aaliyah."

                    "But anyways the festival preparations must continue as today is the final day of the festival. Once I’m done with my duties I can go and find Aaliyah and see how she’s doing."

                    "Just need to hang up some flyers and posters, while also passing out some to students when I see them about the fireworks event to close off the event and I am free to go. Let’s do this thing, I guess."

                    show school_hallway_day with fade

                    "Phew, now having finished completing my duties, it seems like it went on for longer than anticipated since its now dark outside. I check my watch and see that it is now 6:50 PM and that the fireworks event will be starting in 10 minutes."

                    "As I am walking towards the school’s exit to go the fireworks event meeting point, I hear some crying around a corner. I go to check who it may be, and I find Aaliyah crumpled up in a ball in tears."

                    show sprite4 sad small at left

                    Ren "Oh my god Aaliyah, what are you doing here?"

                    show sprite2 sad small at right

                    Aaliyah "Oh Ren, hi."

                    Ren "What’s wrong, why are you crying, who hurt you?"

                    Aaliyah "Well, you see, you know the girl I was talking to you about and hanging out with a lot? Well, she kind of broke up with me a couple of minutes ago, because I was “too boring” to her."

                    Ren "What the hell? She’s so stupid for letting someone like you go!"

                    Ren "You are literally perfect in every way, you’re considerate, funny, welcoming, loving, and overall, a ray of positivity in everyone’s day! Like, this girl must’ve lost some brain cells or something, I fear…"

                    show sprite2 happy small at right

                    Aaliyah "Thanks Ren, I really value your kind words to me, and am eternally thankful for having you in life. I’d choose you over her any day of the week, month, and year."

                    show sprite4 happy small at left

                    Ren "Likewise, bestie! Would you like to head over to the fireworks event with me? It should be starting any minute now and I think spending these last few moments of high school together would be the perfect way to end it before graduation, don’t you think?"

                    Aaliyah "I agree, let’s do it!"

                    hide sprite2 happy small

                    hide sprite4 happy small

                    "After cheering up Aaliyah, we head to the fireworks event hand in hand and take in these last few moments of our high school experience."

                    "As I gaze up at the fireworks, I see a silhouette of a figure that resembles that of Ashton’s, as noticed by his big headphones, on the second floor of the school through a window."

                    "A saddened expression takes over my being, as the two of us lock eyes and Ashton leaves my sight for the last time."

                    # Epilogue - Bad Ending

                    scene city_morning with fade

                    "It has now been 4 years since I graduated high school."

                    "For some reason this thought popped into my head as I was entering the train station to head out to lunch with some friends for my birthday."

                    "As the train arrives in front of me, I enter it and find a place to sit down near the back of the train, when I suddenly see a man with dual colored hair walk towards me with a boy linked around her arm."

                    "Low and behold it is Ashton Mills from high school, coming to torment me with his happy relationship. We have a bit of small talk before he eagerly exits the train to go on a date for his upcoming birthday."

                    "I proceed to sit down in my seat, bitterly, thinking about how I could have ended up with Ashton back in high school, but I fluked it."

                    "In moments like these I think about a specific quote that makes me teary eyed every time: “the world breaks everyone… and afterward, some are strong at the broken places, why does this make me sad?”."

                    "With that being said, I put in my earphones and listen to some orchestral music as the train rides off and brings me into another day."

                    "The end!" with fade



                "Sarah is not my girlfriend":

                    Ren "What? No? Sarah is not my girlfriend at all, what are you talking about?"

                    show sprite3 happy small at right

                    Ashton "Really? Then who is she to you then? I saw you two holding hands while watching that orchestra."

                    show sprite4 happy small at left

                    Ren "Relax, I just invited her to the concert because I wanted to clear something up between us."

                    Ashton "And what may that be huh?"

                    Ren "Basically, if you want a basic rundown, a couple weeks ago she confessed her feelings to me and I politely rejected her."

                    Ren "Ever since then, I’ve wanted to clear things up between us properly to reestablish our friendship again. I swear we have nothing going on, it was just a way to clarify our situation I promise you."

                    Ashton "Well, did it get resolved?"

                    Ren "Yes, it did, we agreed that even if we catch feelings for one another that we would always remain friends no matter what so that we don’t ruin or disrupt the dynamic we have going on already."

                    Ashton "Oh, well I’m happy for you two then."

                    Ren "So please, I’m sorry if it may have given you the wrong idea, but again there is nothing going on between me and her I promise. Do you accept my apology?"

                    Ashton "Yes, I do. I’m also sorry for assuming the worst and questioning your trust. But now that this is cleared up, I also have something to tell you."

                    Ren "Go for it."

                    Ashton "Ok so let me be blunt, I really like you Ren and I hope the feeling is mutual. You don’t need to answer right now with how you feel, but I want you to be honest and genuine with me and your answer."

                    Ashton "So, when you are ready with your answer, you can meet me in this classroom next Friday, on the last day of the school’s summer festival before graduation. I’ll be ready with my answer, and you can come ready with yours. Does that work?"

                    Ren "Oh wow, yes for sure yea totally that can work yea."

                    Ashton "Sweet, perfect in fact! Now this happened and ended at the perfect time, since I have to head to my last class of the day but thanks for clearing things up for me, and I’ll see you around sometime yea?"

                    Ren "Yep, for sure! Good luck with class!"

                    Ashton "Thanks, see ya!"

                    hide sprite3 happy small

                    hide sprite4 happy small

                    "And just like that… Ashton was gone. I’m glad we got to clear things up but wow I did not expect him to subtly confess how he feels about me."

                    "I mean I kind of liked that he asserted himself… I found it kind of attractive."

                    "But nevertheless, he told me to reflect on how I truly feel and give him a proper answer, on the last day of the summer festival nonetheless, what a romantic he is."

                    "After this, I feel as though class may be hard to get through, considering my excitement and emotional overload… I think going home is the best and safest option here so I’m just going to do that."

                    # Scene 8

                    scene school_hallway_day with fade

                    "It has been a couple of days now since the whole Ashton incident, where I confronted him about the concert a couple weeks ago. I’ve been thinking about what he said to me that day every day going forward."

                    "Not going to lie, it has been kind of hard to deal with, but I think I’M ready to confront him one last time!"

                    "But first I have some festival preparations that I must deal with first before meeting with Ashton later. Just need to hang up some flyers and posters, while also passing out some to students when I see them about the fireworks event to close off the event and I am free to go."

                    "Let’s do this thing!"

                    show school_hallway_day with fade

                    "Phew, that took way longer than anticipated, but alas it is finally done. And it seems like I finished at just the right time, seeing as I got a message from Ashton confirming as to when I will be arriving at the designated room."

                    "I tell him that I will be there in 10 minutes, which is also very convenient seeing as the fireworks event begins in 10 minutes as well, talk about perfect timing!"

                    "I climb up the two flights of stairs to arrive at the classroom, where I see Aaliyah waiting for me in front of the room."

                    show sprite2 happy small at left

                    Aaliyah "Ren! There you are! I wanted to see you before you went to see Ashton!"

                    show sprite4 happy small at right

                    Ren "Bestie hey! You found me at the perfect time I was about to head in, what’s up?"

                    Aaliyah "Well, I just wanted to give you a pep talk and wish you good luck before heading in."

                    Ren "Aww you’re too kind to me!"

                    Aaliyah "But you deserve it! You’ve experienced so many hardships as of recently from dealing with the Sarah confession, to discovering your own sexuality, to even getting to know Ashton better."

                    Aaliyah "All equally scary stuff to do, yet you have overcome them all flawlessly. And now this is the final chapter to seal everything together and end high school on the right foot."

                    Ren "Aww Aaliyah, you’re going to make me cry."

                    Aaliyah "No no no! No crying allowed here, because if you start crying then I will too."

                    Ren "Ok ok fine, no crying, maybe a bit of happy tears but no crying!"

                    Aaliyah "Right yes. Ok enough of me babbling, you have your man waiting for you in there!"

                    Ren "He isn’t “my man”."

                    Aaliyah "Well, not yet…"

                    Ren "Fair point, but that is still to be determined."

                    Aaliyah "Very true, now go on now! Don’t keep him waiting!"

                    Ren "Alright alright, wish me luck!"

                    Aaliyah "Good luck, you got this!"

                    hide sprite4 happy small

                    hide spirte2 happy small

                    "Alright, now is the moment we have all been waiting for. I enter the classroom and see Ashton sitting by one of the classroom’s windowsills with his smaller headphones on just gazing up at the stars, when he suddenly turns towards me upon hearing the door open."

                    show street_summer_stars with fade

                    show sprite3 happy small at left

                    Ashton "Ren! You’ve arrived!"

                    show sprite4 happy small at right

                    Ren "Of course, I wouldn’t miss this for the world!"

                    Ashton "I’m flattered and glad you came!"

                    Ren "Likewise!"

                    Ashton "What’s wrong Ren, you seem a bit flustered?"

                    Ren "N-nothing’s w-wrong!"

                    Ashton "Fair enough, come sit up here with me so we can get a better view of the fireworks together."

                    Ren "O-ok if you i-insist. Also, uh, how can you tell I’m flustered?"

                    Ashton "I can just tell…"

                    Ren "How can you?"

                    Ashton "Do you want me to say it out loud? I’ll tell you if you answer my one question."

                    Ren "And w-what may that be?"

                    Ashton "Well, for instance, your adorable stuttering kind of gave it away. That and playing with your hands and nails is an adorable habit I’ve caught on since we first met. You like to do that when you are nervous and want to express something."

                    Ren "How did you figure all of this out?"

                    Ashton "Even though I may have my headphones on all the time, I am very observant of my surroundings, especially the people, and I like to adapt my habits to each person I interact with. You know to ensure everyone is comfortable."

                    Ren "That’s s-so thoughtful wow."

                    Ashton "Indeed, and now I must say one last thing."

                    Ren "Mhm?"

                    Ashton "Ren Lyons, I like you. I really like you, and I would like for us to be more than friends!"

                    Ashton "I know it may be challenging and weird at times, since it’s something new for us both, but I am willing to go through all of the hardships with you and work through everything together to become the best versions of ourselves. What do you say?"

                    Ren "Yes! Of course, yes! However, I am not fully sure of my sexuality yet as I am still exploring that myself, you know after doing some quizzes and all. But nonetheless, even if I am unsure of what I am and who I am attracted to, I still want to try with you! Will you do that with me?"

                    Ashton "Forever and always Ren, we can go as slow or as fast as you would like, no pressure at all."

                    Ren "Yay, then it settled then!"

                    Ashton "Indeed, it is, we are officially a couple now! Man, that feels great to say out loud."

                    Ren "SO good!"

                    Ashton "Now then, as our first official date, would you like to watch the fireworks with me as we listen to some music together?"

                    Ren "I would want nothing more than to do that with you now Ashton!"

                    Ashton "Gosh I like you so much!"

                    Ren "I like you too!"

                    hide sprite4 happy small

                    hide spriet3 happy small

                    "We spend the rest of the evening together cuddled up on the windowsill watching the fireworks event as we listen to some shared music together."

                    "The moment I have dreamed of for years has finally come to fruition! And it feels so good!"

                    "Ashton was so kind and gentle with his declaration of his feelings and how he would progress our relationship going forward which I loved."

                    "So now, the only thing to do is to enjoy this moment to the fullest and bid adieu to high school!"

                    # Epilogue - Good Ending

                    scene city_morning with fade

                    "It has now been 4 years since I graduated high school."

                    "For some reason this thought popped into my head as I was entering the train station to head out to lunch with some friends for my birthday."

                    "I was told Ashton and Aaliyah would meet me here, but as always, he’s late… again! But it’s fine, he’s cute so he has an excuse and Aaliyah… well she’s fine."

                    "As the train arrives in front of me, I feel someone tapping my shoulder behind me and low and behold its Ashton and Aaliyah… I greet them with a hug, and we enter the train together."

                    "As I am sitting down however, I see a lady with a short brown bobbed haircut and some cozy looking clothes on exit the train with a boy linked around her arm."

                    "I know that is Sarah Westlake from high school, I just know it, so I chase after her and yell out “SARAH!”. She looks back at me with a smile on her face and waves back at me."

                    "She looks happy and I’m glad she got to find someone who is perfect for her like I did for myself, and Aaliyah did for her and her girlfriend."

                    "In moments like these I am reminded of how grateful I am for having supportive friends to get me through my toughest of moments and I always remember this quote from a musical I cherish deeply: “all you have to do is just believe, you can be who you want to be”."

                    "With that being said, I clutch onto Ashton’s arm the train begins to depart leading us into a new day together."

                    "The end!" with fade


        "Ashton":

            "I think I’m going to go with Ashton, I really enjoy our time spent together and based on his music taste, I’m sure he would have a blast at a concert like this."

            "I’ll go look for him later to ask him myself."

            hide sprite4 happy small

            scene cafeteria_day with fade

            show sprite4 happy small at left

            Ren "Hey Ash!"

            show sprite3 happy small at right

            Ashton "Hey Ren! It’s been a while, how have you been?"

            Ren "I’ve been doing great thanks for asking, I like your new headphones, what happened to your big ones?"

            Ashton "Thanks, I usually switch between then depending on my moods, so today I’m feeling especially happy, so I decided to use these!"

            Ren "Ohhh that’s really cool actually, I’m glad you’re feeling good! Also, there was something I wanted to ask you."

            Ashton "Sure, hit me, what’s up R?"

            Ren "Well, you see, Aaliyah gave me these two tickets to an orchestral concert this weekend and I was wondering if you’d want to go with me?"

            Ashton "Oh my god, YES! I love orchestras, they are my favorite type of concerts and I used to be in one back in my old town!"

            Ren "Yay, I’m happy you can come with me! I’m interested to hear about your time in an orchestra, if you’d want to share that is, and to just spend time together and enjoy the concert."

            Ashton "Of course, I’ll talk about it, anything for you R! And likewise, I’m really looking forward to it! When is the event?"

            Ren "It’s, ironically enough, tomorrow, does that work?"

            Ashton "Oh yes it does, I wasn’t planning on doing much tomorrow anyways, but now I do haha!"

            Ren "Lovely, amazing! I’ll send you the details of everything later, yea?"

            Ashton "Yep, that works for me! Can’t wait for it!"

            Ren "Same here! Now as much as I’d love to chat more I have to head to class for now, but I just wanted to stop by to ask you."

            Ashton "I’m glad you did, now head off to your class so you aren’t late you little rascal, don’t forget to text me later!"

            Ren "Haha, thanks, and don’t worry I won’t forget!"

            hide sprite4 happy small

            hide sprite3 happy small

            "Believe it or not, that worked out much better than it did in my head. I’m glad he said yes, now I just await until tomorrow to experience the event to its fullest!"

            "Gosh, I’m so excited I’m going to have a hard time concentrating in class! I should probably put that on the backburner though so I can focus on the one single class I have left for today. Then I go home and rush all of my homework so that tomorrow is a free day!"

            # Scene 6

            scene bedroom_day with fade

            "Alas, it is finally the day to go to the orchestra concert. Not going to lie I’m a bit nervous for it, but I also have the rest of the day to mentally prepare myself for it."

            "I just need to remember to stay calm, cool, and collected and all should go well! I’ll confirm with Ashton that all is well still and that he can still attend the concert."

            scene street_summer_night with fade

            "Upon arriving to the venue, I see Ashton waiting at the entrance already. Guess I must be fashionably late, or maybe he’s just early. Whatever the case may be I go up to talk to him."

            show sprite4 happy small at left

            Ren "Hey Ashton! Wow, you look really good tonight, I’m blown away."

            show sprite3 happy small at right

            Ashton "Oh, hey R, you look quite handsome yourself there!"

            Ren "Why thank you good sir, shall we head inside to be blown away by the incredible orchestra?"

            Ashton "I believe we shall!"

            scene orchestra with fade

            "We head inside the venue and get seated in a secluded balcony, as the show begins. As the show goes on, we sit in silence until Ashton says something to me."

            show sprite3 happy small at left

            Ashton "Wow this concert is amazing! It’s like everything I’ve dreamed of and more all at once! I recognize some songs even which is a shocker, besides all of these musicians are so talented so only the best is to be expected."

            show sprite4 happy small at right

            Ren "Same, my favorites have been the two songs following the opening one, I listen to those all the time!"

            Ashton "Ayy same here, I started listening to those recently as well and I was instantly hooked!"

            Ren "Well, that’s perfect timing, a quality I admire and love about you!"

            Ashton "Hey now, don’t make me blush haha!"

            Ren "That’s how I feel when I’m around you silly… now you know what it feels like HUH?"

            Ashton "Haha, you got me there!"

            "This evening is truly splendid, I feel as though I am on cloud 9. Nothing in the world can ruin this moment."

            "As I am thinking this, I see Ashton approach me with his eyes closed leaning his head into me. Putting all of this together, I notice he is leaning in to kiss me, so I mimic his actions and do the same thing. That is until we get suddenly interrupted..."

            Waitress "Would any of you like some water, juice, or champagne to drink while you enjoy the orchestra’s performance?"

            Ashton "Oh no I’m fine but thank you for offering! How about you Ren?"

            Ren "Oh, uh well uh I think I’m also fine yea, t-thank you for offering as well."

            Waitress "My pleasure!"

            "Needless to say, after that, my stress levels soared through the roof, and I don’t think I was able to concentrate on the concert nor think clearly for the rest of that evening."

            "Sure, to any other person, almost being kissed by someone you kind of have a crush on is no big deal, but for me this would’ve been my very first kiss EVER!"

            "But it got interrupted by a random waitress, ugh what a way to ruin the perfect moment. The rest of the evening progressed as normal, now featuring small talk about the event itself, instead of in-depth conversations like before… but that’s partially my fault."

            "I don’t know after that interrupted kiss; I just felt awkward and uncomfortable around Ashton and don’t know what to do. That combined with the recent quiz results has my brain all foggy and messed up."

            "I think I need some time away from Ashton to get my thoughts and feelings in order, that may be the best remedy for the time being."

            # Scene 7

            scene school_hallway_day with fade

            "It has been about a week since the whole concert incident with Ashton, and yet I’m still unsure on what to do and how to feel about what happened."

            "Like I still want to talk with him to clarify what he may have seen just so he doesn’t get the wrong idea."

            "But I also feel as though, after seeing that, he may want to avoid me at all costs, which is valid, but I can’t not clear things up, that’s the right thing to do. Just as I am stuck in thought about this a familiar face approaches me."

            show sprite2 happy small at left

            Aaliyah "Hey Ren! You have to tell me all about that concert last weekend! How did it go?"

            show sprite4 sad small at right

            Ren "Hey Aaliyah…"

            Aaliyah "Oh my, that’s a “Ren doesn’t feel good hey”. What’s wrong?"

            Ren "See… it’s about the concert…"

            show sprite2 sad small at left

            Aaliyah "Oh no what happened?"

            Ren "So, uh, I decided to ask Ashton, you know to deepen our relationship further, and we were talking about the concert and all and all of a sudden, he leans in to kiss me… but a waitress interrupted it."

            Ren "It got awkward after that, and we just remained silent."

            Ren "From there on out, I was not able to think or act clearly for the rest of the evening and I’ve been avoiding him since then since I’m too scared to confront that situation… like what if he hates me or something I don’t know."

            Aaliyah "I see what happened, it sounds like one big misunderstanding clearly."

            Aaliyah "Unless I interpreted things incorrectly myself, but we all know the resolution to misinterpretations, and that’s just talking."

            Aaliyah "So go and find Ashton and just talk to him about it, it’ll clear things up instantly."

            Ren "I guess you’re right; but I don’t know if I’m ready."

            show sprite2 happy small at left

            Aaliyah "I know you’re ready, yes confrontation is scary but it’s better to tackle it head on then to have it linger around for days on end."

            show sprite4 happy small at right

            Ren "That’s true, I guess I’ll reconsider my options again. Wait, I forgot to ask, how was your date with that girl?"

            Aaliyah "That’s irrelevant right now, I’ll tell you more about that once this is settled with. Until then, I have to rush to class now, so I’ll be checking up on you at a later date bestie!"

            Ren "Fine if you say so. I’ll see you later!"

            Aaliyah "Bye bye, good luck!"

            hide sprite2 happy small

            hide sprite4 happy small

            scene cafeteria_day with fade

            "Once I part ways with Aaliyah, I try to find an empty place to reflect on everything. As I am scouting for a place, Sarah bumps into me and sparks a bit of conversation."

            show sprite1 happy small at left

            Sarah "Ren! I’ve been meaning to look for you, seems like we found each other!"

            show sprite4 sad small at right

            Ren "Oh, uh hey Sarah."

            Sarah "Sooo how was the concert with Ashton?"

            Ren "It was good and all, but I really have to go for now."

            show sprite1 angry small at left

            Sarah "Wait wait no before you rush off again, I need you to answer my question, it’s the least you can do right?"

            show sprite4 angry small at right

            Ren "Fair enough, you’re right. It went great, we had a splendid time talking about the music and orchestra itself, we really bonded together over a variety of topics and deepened our friendship to a greater level. There is that what you wanted to hear?"

            Sarah "Yes, but you can tone it down on the sass and attitude, geez I was just trying to be nice."

            show sprite4 sad small at right

            Ren "You’re right, my bad, I’m sorry I’m just a bit caught up at the moment."

            show sprite1 sad small at left

            Sarah "What's wrong?"

            Ren "I didn’t want to express this portion, but I guess it would be more helpful if I did…"

            Ren "So basically Ashton and I almost kissed during the orchestra but got interrupted by a waitress and now I feel really awkward being around him and I need to reflect on everything before confronting him, or even if I will, myself."

            Ren "I didn’t want to say anything to you because of the whole confession thing."

            Sarah "Oh wow, that’s equally exciting as it sounds awkward, I’m sorry you had to have that moment interrupted like that."

            show sprite1 happy small at left

            Sarah "Also, no need to worry about the whole confession dilemma, I’m chill about it now, I’ve done some self-reflection myself and I’ve come to terms with it, so no need to worry."

            Ren "Are you sure? I didn’t want to make you uncomfortable with anything or make anything awkward between us."

            Sarah "Yes, I’m sure, we are fine Ren trust me, I’ve gotten over it."

            show sprite4 happy small at right

            Ren "Ok that’s good I’m proud of you!"

            Sarah "Thank you, well I’m glad I bumped into you, but I must head off to the library to study, so I’ll see you around! Good luck with Ashton again!"

            Ren "Thanks Sarah if you ever need anything don’t hesitate to let me know!"

            Sarah "Will do! See ya!"

            hide sprite4 happy small

            hide sprite1 happy small

            "Upon leaving Sarah at the library, I wander around trying to find an empty room, when I stumble onto the room where Ashton and I met on his first day transferring here."

            show classroom_day with fade

            "As soon as I enter the room, I hear a familiar voice behind me."

            show sprite3 happy small at left

            Ashton "Ren! Finally, I found you! I’ve been looking for you all week!"

            show sprite4 sad small at right

            Ren "Oh, uh hey there Ashton…"

            show sprite3 sad small at left

            Ashton "So, uh, can we talk about last week? If you don’t mind that is?"

            Ren "Sure, I guess… what is there to talk about?"

            Ashton "Well, you see, I’m sorry for how I spontaneously wanted to kiss you, it was my bad and it was in the heat of the moment and I’m sorry if it may have made you uncomfortable."

            Ren "It’s fine that’s whatever…sure it did make me a bit uncomfortable, but I didn’t necessarily mind it, I’ve been just worried if you were mad at me because I stayed silent afterwards for the evening."

            Ashton "No no no, I was worried you were mad at me for the kiss, so I also remained silent as a result too!"

            Ren "Oh my, look at us, both worried about the other."

            Ashton "Yea… but just to clarify, you do forgive me for the impromptu kiss, right?"

            Ren "Yea that’s not a problem at all, and you forgive me for reacting silently, right?"

            show sprite3 happy small at left

            Ashton "Of course, always!"

            show sprite4 happy small at right

            Ren "Ok phew that’s good to hear."

            Ashton "Now that this is cleared up, I also have something to tell you."

            Ren "Go for it."

            Ashton "Ok so let me be blunt, I really like you Ren and I hope the feeling is mutual. You don’t need to answer right now with how you feel, but I want you to be honest and genuine with me and your answer."

            Ashton "So, when you are ready with your answer, you can meet me in this classroom next Friday, on the last day of the school’s summer festival before graduation. I’ll be ready with my answer, and you can come ready with yours. Does that work?"

            Ren "Oh wow, yes for sure yea totally that can work yea."

            Ashton "Sweet, perfect in fact! Now this happened and ended at the perfect time, since I have to head to my last class of the day but thanks for clearing things up for me, and I’ll see you around sometime yea?"

            Ren "Yep, for sure! Good luck with class!"

            Ashton "Thanks, see ya!"

            hide sprite4 happy small

            hide sprite3 happy small

            "And just like that… Ashton was gone. I’m glad we got to clear things up but wow I did not expect him to subtly confess how he feels about me. I mean I kind of liked that he asserted himself… I found it kind of attractive."

            "But nevertheless, he told me to reflect on how I truly feel and give him a proper answer, on the last day of the summer festival nonetheless, what a romantic he is."

            "After this, I feel as though class may be hard to get through, considering my excitement and emotional overload… I think going home is the best and safest option here so I’m just going to do that."

            # Scene 8

            scene school_hallway_day with fade

            "It has been a couple of days now since the whole Ashton incident, where I confronted him about the concert a couple weeks ago. I’ve been thinking about what he said to me that day every day going forward."

            "Not going to lie, it has been kind of hard to deal with, but I think I’M ready to confront him one last time!"

            "But first I have some festival preparations that I must deal with first before meeting with Ashton later."

            "Just need to hang up some flyers and posters, while also passing out some to students when I see them about the fireworks event to close off the event and I am free to go."

            "Let’s do this thing!"

            show school_hallway_day with fade

            "Phew, that took way longer than anticipated, but alas it is finally done. And it seems like I finished at just the right time, seeing as I got a message from Ashton confirming as to when I will be arriving at the designated room."

            "I tell him that I will be there in 10 minutes, which is also very convenient seeing as the fireworks event begins in 10 minutes as well, talk about perfect timing!"

            "I climb up the two flights of stairs to arrive at the classroom, where I see Aaliyah waiting for me in front of the room."

            show sprite2 happy small at left

            Aaliyah "Ren! There you are! I wanted to see you before you went to see Ashton!"

            show sprite4 happy small at right

            Ren "Bestie hey! You found me at the perfect time I was about to head in, what’s up?"

            Aaliyah "Well, I just wanted to give you a pep talk and wish you good luck before heading in."

            Ren "Aww you’re too kind to me!"

            Aaliyah "But you deserve it! You’ve experienced so many hardships as of recently from dealing with the Sarah confession, to discovering your own sexuality, to even getting to know Ashton better."

            Aaliyah "All equally scary stuff to do, yet you have overcome them all flawlessly. And now this is the final chapter to seal everything together and end high school on the right foot."

            Ren "Aww Aaliyah, you’re going to make me cry."

            Aaliyah "No no no! No crying allowed here, because if you start crying then I will too."

            Ren "Ok ok fine, no crying, maybe a bit of happy tears but no crying!"

            Aaliyah "Right yes. Ok enough of me babbling, you have your man waiting for you in there!"

            Ren "He isn’t “my man”."

            Aaliyah "Well, not yet…"

            Ren "Fair point, but that is still to be determined."

            Aaliyah "Very true, now go on now! Don’t keep him waiting!"

            Ren "Alright alright, wish me luck!"

            Aaliyah "Good luck, you got this!"

            hide sprite4 happy small

            hide sprite2 happy small

            "Alright, now is the moment we have all been waiting for. I enter the classroom and see Ashton sitting by one of the classroom’s windowsills with his smaller headphones on just gazing up at the stars."

            "He turns towards me upon hearing the door open."

            show street_summer_stars with fade

            show sprite3 happy small at left

            Ashton "Ren! You’ve arrived!"

            show sprite4 happy small at right

            Ren "Of course, I wouldn’t miss this for the world!"

            Ashton "I’m flattered and glad you came!"

            Ren "Likewise!"

            Ashton "What’s wrong Ren, you seem a bit flustered?"

            Ren "N-nothing’s w-wrong!"

            Ashton "Fair enough, come sit up here with me so we can get a better view of the fireworks together."

            Ren "O-ok if you i-insist. Also, uh, how can you tell I’m flustered?"

            Ashton "I can just tell…"

            Ren "How can you?"

            Ashton "Do you want me to say it out loud? I’ll tell you if you answer my one question."

            Ren "And w-what may that be?"

            Ashton "Well, for instance, your adorable stuttering kind of gave it away. That and playing with your hands and nails is an adorable habit I’ve caught on since we first met. You like to do that when you are nervous and want to express something."

            Ren "How did you figure all of this out?"

            Ashton "Even though I may have my headphones on all the time, I am very observant of my surroundings, especially the people, and I like to adapt my habits to each person I interact with. You know to ensure everyone is comfortable."

            Ren "That’s s-so thoughtful wow."

            Ashton "Indeed, and now I must say one last thing."

            Ren "Mhm?"

            Ashton "Ren Lyons, I like you. I really like you, and I would like for us to be more than friends!"

            Ashton "I know it may be challenging and weird at times, since it’s something new for us both, but I am willing to go through all of the hardships with you and work through everything together to become the best versions of ourselves. What do you say?"

            Ren "Yes! Of course, yes! However, I am not fully sure of my sexuality yet as I am still exploring that myself, you know after doing some quizzes and all."

            Ren "But nonetheless, even if I am unsure of what I am and who I am attracted to, I still want to try with you! Will you do that with me?"

            Ashton "Forever and always Ren, we can go as slow or as fast as you would like, no pressure at all."

            Ren "Yay, then it settled then!"

            Ashton "Indeed, it is, we are officially a couple now! Man, that feels great to say out loud."

            Ren "SO good!"

            Ashton "Now then, as our first official date, would you like to watch the fireworks with me as we listen to some music together?"

            Ren "I would want nothing more than to do that with you now Ashton!"

            Ashton "Gosh I like you so much!"

            Ren "I like you too!"

            hide sprite4 happy small

            hide sprite3 happy small

            "We spend the rest of the evening together cuddled up on the windowsill watching the fireworks event as we listen to some shared music together."

            "The moment I have dreamed of for years has finally come to fruition! And it feels so good!"

            "Ashton was so kind and gentle with his declaration of his feelings and how he would progress our relationship going forward which I loved."

            "So now, the only thing to do is to enjoy this moment to the fullest and bid adieu to high school!"

            # Epilogue - Good Ending

            scene city_morning with fade

            "It has now been 4 years since I graduated high school."

            "For some reason this thought popped into my head as I was entering the train station to head out to lunch with some friends for my birthday."

            "I was told Ashton and Aaliyah would meet me here, but as always, he’s late… again! But it’s fine, he’s cute so he has an excuse and Aaliyah… well she’s fine."

            "As the train arrives in front of me, I feel someone tapping my shoulder behind me and low and behold its Ashton and Aaliyah… I greet them with a hug, and we enter the train together."

            "As I am sitting down however, I see a lady with a short brown bobbed haircut and some cozy looking clothes on exit the train with a boy linked around her arm."

            "I know that is Sarah Westlake from high school, I just know it, so I chase after her and yell out “SARAH!”. She looks back at me with a smile on her face and waves back at me."

            "She looks happy and I’m glad she got to find someone who is perfect for her like I did for myself, and Aaliyah did for her and her girlfriend."

            "In moments like these I am reminded of how grateful I am for having supportive friends to get me through my toughest of moments."

            "I always remember this quote from a musical I cherish deeply: “all you have to do is just believe, you can be who you want to be”."

            "With that being said, I clutch onto Ashton’s arm the train begins to depart leading us into a new day together."

            "The end!" with fade

    # This ends the game.

    return
