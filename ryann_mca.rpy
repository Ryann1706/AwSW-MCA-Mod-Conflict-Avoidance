
# Adine's good ending: 
# Freefall, Adine Romantic Ending and Adine Shopping

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
    

#==================================================================================================================================

# Anna good ending:
# w/ 4 dates and impressed, and 3 Adine dates and impressed, Not So Tragic Hero, and Adine and Anna beter ending

# I'm removing the requirement for Adine to be impressed for NSTH, because it's much more convenient to just be able to skip the 3 dates

init python:
    ryann_mca_annagoodends = False

label ryann_mca_anna_good_ending_check:

if renpy.has_label("eck_annashappyend") and renpy.has_label("wyv_betterannaending"):
    $ ryann_mca_annagoodends = True

return


label ryann_mca_anna_good_ending:

if annastatus == "good" and annascenesfinished == 4 and adinescenesfinished == 3 and adinedead == False:
    scene black with dissolveslow
    $ renpy.pause (3.0)
    s "Multiple Anna good ending mods detected. Jump to which one?"
    menu:
        "Not-so-Tragic Hero":
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
            $ renpy.pause (3.0)
            $ adinestatus = "good"
            jump eck_common_anna

        "Anna and Adine ending":
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
            $ renpy.pause (3.0)
            jump wyv_betterannaending

else:
    return

