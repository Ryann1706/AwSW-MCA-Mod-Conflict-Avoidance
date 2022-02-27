
init python:
    mca_adinegoodends = 0


label ryann_mca_adine_good_ending:

if renpy.has_label("cm_freefall1"):
    $ mca_adinegoodends += 1

if renpy.has_label("adine_romance_end"):
    $ mca_adinegoodends += 1

if renpy.has_label("adine_shopping"):
    $ mca_adinegoodends += 1


if mca_adinegoodens > 1:
    stop music fadeout 2.0
    scene black with dissolveslow
    $ renpy.pause (3.0)
    play sound "fx/system3.wav"
    s "Multiple Adine good ending mods detected. Jump to which one?"
    menu:
        "Freefall" if renpy.has_label("cm_freefall1"):
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
            scene black with dissolveslow
            $ renpy.pause (3.0)
            jump cm_freefall1

        "Adine Romantic Ending" if renpy.has_label("adine_romance_end"):
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
            scene black with dissolveslow
            $ renpy.pause (3.0)
            jump thn_common_adine

        "Adine Shopping" if renpy.has_label("adine_shopping"):
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
            scene black with dissolveslow
            $ renpy.pause (3.0)
            jump adine_shopping


else:
    jump ryann_mca_adine_return
    
