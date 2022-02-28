
from modloader import modast, modinfo
from modloader.modclass import Mod, loadable_mod
import jz_magmalink as ml

@loadable_mod
class AWSWMod(Mod):
    name = "Mod Conflict Avoidance"
    version = "0.0"
    author = "Ryann1706"
    dependencies = ["MagmaLink"]

    def mod_load(self):
        pass

    def mod_complete(self):
        pass


    ml.find_label("adinegoodending") \
        .search_say("I don't know.", depth=400) \
        .hook_to("ryann_mca_adine_good_ending") \
        .search_scene("black", depth=400) \
        .link_from("ryann_mca_adine_return")
        

    ml.find_label("annagoodending") \
        .search_say("Both of us were seemingly unharmed, and by the time Reza was reloading his gun, Anna was already up again and running towards him.") \
        .hook_call_to("ryann_mca_anna_good_ending_check")
    
    ml.find_label("annagoodending") \
        .search_say("But at least I'm not alone.", depth=250) \
        .hook_call_to("ryann_mca_anna_good_ending", condition="ryann_mca_annagoodends == True") \
