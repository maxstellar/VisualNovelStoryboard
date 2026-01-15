# characters
define c = Character("Connor")

# transitions
define dissolve1 = Dissolve(1.0)

label start:
    scene black
    pause 1

    centered "Remember." with dissolve1
    pause 1

    scene bedroom_day with blinds
    play sound "alarmclock.wav"
    pause 3
    "Random Friend" "Wake up, Connor."

    # This ends the game.

    return
