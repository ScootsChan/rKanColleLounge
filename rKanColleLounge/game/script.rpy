# The start of the code, I presume.

define sc = Character("Scoots")
define wolf = Character("Ashigara")
define unknown = Character("??")

# everything actually starts here, i guess.

label start:

    scene kure-naval-headquarters
    
    "Today is the start of a new life."
    
    "I prepare to enter the large building in front of me, clearly the main area of operations in this base."
    
    "However, before I can pass through the doors, a person dressed in an officer's uniform bumps into me on the way out."
    
    show scoots
    with easeinbottom
    
    unknown "Oh! Hello! Didn't see you there!"
    
    unknown "You seem new 'round these parts, what's your name?"


menu:
    "Who am I?" #decides on which kanmusu you shall be
    
    "Ashigara.": #you become ashigara
        wolf "I'm Ashigara, the third Myoukou!"
        jump wolfstart


# Ashigara's start
label wolfstart:
    unknown "Ashi... gara?"
    unknown "Is that really you?"
    unknown "No.. It can't be.."
    sc "Ah, sorry. Had a moment there. My name's Admiral Scoots, and I manage the tech side of things around here."
    wolf "Nice to meet you!"
    wolf "Where can I chat with a higher level admiral around here?"
    sc "Oh, uh, try Astraph. Down the hallway, his door is on the right."
    "He points toward a door."
    wolf "Thank you!"
    sc "No problem."
    
    hide scoots
    with easeoutbottom

    jump wolfastraphintroduction #jumps to astraph's introduction

#scene where astraph is introduced
label wolfastraphintroduction:
    scene hallway
    with wipeleft

    "I head towards Astraph's office. He is sure to recognize me."
    "I push open the door into his room."
	
    scene office
    with wipeleft
return