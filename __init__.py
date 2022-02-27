
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
        
