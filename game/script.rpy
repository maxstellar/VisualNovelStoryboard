# characters
define c = Character("Connor", image="connor")
define g = Character("Grace", image="grace")

transform same_transform(old, new):
    old
    new with Dissolve(0.2, alpha=True)

define config.side_image_same_transform = same_transform

image grace neutral = "keith_placeholder.webp"

image side connor happy = "connor_placeholder.png"

label start:
    # cutscene goes here

    scene bedroom_placeholder
    show grace neutral at center
    c happy "Well, good morning to you too, Grace."
    
    "(Grace begins to speak, but the sound of her voice is drowned out by a ringing in my ears.)"

    hide grace neutral with dissolve

    scene black with dissolve

    centered "{size=+40}REMEMBER." with dissolve

    show grace neutral at center with dissolve

    scene bedroom_placeholder with dissolve

    g neutral "...eggs got cold and you don't even care!"

    g "...what are you-{w} Are you good?"
    