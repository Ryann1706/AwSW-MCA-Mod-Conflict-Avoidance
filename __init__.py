
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
        ml.find_label("adinegoodending") \
            .search_say("I don't know.", depth=400) \
            .hook_to("ryann_mca_adine_good_ending") 

    
        ml.find_label("annagoodending") \
            .search_say("But at least I'm not alone.", depth=250) \
            .hook_to("ryann_mca_anna_good_ending") 

    
         ml.find_label("a4romance") \
            .search_menu("If you say so.").branch() \
            .search_say("Not like that! You'll ruin them. I'll do it.") \
            .hook_to("ryann_mca_anna4_romance", condition="persistent.nsfwtoggle == True") 


    def mod_complete(self):
        pass

    
