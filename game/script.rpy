# characters
define c = Character("Connor", image="connor")
define k = Character("Keith", image="keith")

transform same_transform(old, new):
    old
    new with Dissolve(0.2, alpha=True)

define config.side_image_same_transform = same_transform

image keith neutral = "keith_placeholder.jpg"

image side connor happy = "connor_placeholder.png"

label start:
    # cutscene goes here

    scene bedroom_placeholder
    show keith neutral at center
    c happy "Well, good morning to you too, Keith."
    
    "Keith begins to speak, but the sound of his voice is drowned out by a ringing in your ears."

    hide keith neutral with dissolve

    scene black with dissolve

    centered "REMEMBER." with dissolve

    scene bedroom_placeholder with dissolve

    show keith neutral at center with dissolve


    