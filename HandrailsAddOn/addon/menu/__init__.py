import bpy

# Import all menus
from .balustrade_menu import GAYA_PT_BalustradePanel
from .stair_menu import GAYA_PT_StaircasePanel
from .glass_panel_menu import GAYA_PT_GlassRailingPanel
from .uneven_terrain_menu import GAYA_PT_UnevenTerrainPanel

classes = (GAYA_PT_BalustradePanel, GAYA_PT_StaircasePanel, GAYA_PT_GlassRailingPanel, GAYA_PT_UnevenTerrainPanel)#ADD CLASSES TO REGISTER HERE


def register_menus():
    
    for cls in classes:
       bpy.utils.register_class(cls)

def unregister_menus():
    
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

