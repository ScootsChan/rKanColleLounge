# The start of the code, I presume.

define sc = Character("Scoots")
define me = Character("Me")
define wolf = Character("Ashigara")

# everything actually starts here, i guess.

label start:

    scene kure-naval-headquarters
    
    me "Today is the start of a new life."
    
    me "I prepare to enter the large building in front of me, clearly the main area of operations in this base."
    
    me "however, before I can pass through the doors, a person dressed in an officer's uniform bumps into me on the way out."
    
    show scoots
    with easeinbottom
    
    sc "Oh! Hello! Didn't see you there!"
    
    sc "You seem new 'round these parts, what's your name?"


menu:
    "Who am I?" #decides on which kanmusu you shall be
    
    "Ashigara.": #you become ashigara
        wolf "I'm Ashigara, the third Myoukou!"
        jump ashigarastart


# Ashigara's start
label ashigarastart:
    sc "Ashi... gara?"
    sc "Is that really you?"
    sc "No.. It can't be.."
    sc "Ah, sorry. Had a moment there. My name's Admiral Scoots, and I manage the tech side of things around here."
    wolf "Nice to meet you!"
    wolf "Where can I chat with a higher level admiral around here?"
    sc "Oh, uh, try Astraph. Down the hallway, his door is on the right."
    "He points toward a door."
    wolf "Thank you!"
    sc "No problem."
    
    hide scoots
    with easeoutbottom

return