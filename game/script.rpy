# characters
define c = Character("Connor", image="connor")
define g = Character("Grace", image="grace")

label start:
    # cutscene goes here

    scene bedroom_placeholder
    show grace neutral at center
    c happy "Well, good morning to you too, Grace."
    
    "(Grace begins to speak, but the sound of her voice is drowned out by a ringing in my ears.)"

    window hide None
    show black zorder 100 with dissolve

    centered "{cps=0}{size=+40}{b}REMEMBER." with dissolve

    show grace annoyed
    hide black with dissolve
    window auto

    g annoyed "{cps=50}...eggs got cold and you don't even care!"

    g neutral "...what are you-{w} Are you good?"
    
    c embarassed "I-I'm fine. Just... got up too quickly, I think."

    g "Well, then, did you hear anything I just said?"

    menu:
        c "{cps=0}You were talking about..."

        "Eggs":
            c "Eggs! You were talking about eggs."
            g annoyed "...I'm baffled that *that's* what you're focusing on."
            g "It's not about the eggs, Connor."
        "My attitude":
            c "You were talking about my attitude."
            g annoyed "Oh, so you can listen, and you've just been purposefully not doing so for the last few days?"
        "Outer space":
            c "You were talking about... outer space?"
            g annoyed "It's always about space with you. Is that what you've been daydreaming about?"

    g neutral "*sighs* Well, it doesn't matter. The point is, you have really got to lock in, man."

    g "Your new job starts tomorrow and you're... {i}spacing out{/i} on me every few seconds."

    g tired "Staying in bed all day isn't doing you any favors."

    g neutral "It's been like this since you got back from uni. Why don't you go out and... do something?"

    c embarassed "I don't know... like what?"

    g "Well, why don't you start with helping me clean the attic? I'm trying to put some of the stuff we unpacked away."

    c "Fine."

    # transition to attic