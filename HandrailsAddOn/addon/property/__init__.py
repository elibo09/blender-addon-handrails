from .balustrade_properties import register_balustrade_properties, unregister_balustrade_properties
from .staircase_properties import register_staircase_properties, unregister_staircase_properties
from .glass_panel_properties import register_glass_properties, unregister_glass_properties
from .uneven_terrain_properties import register_terrain_properties, unregister_terrain_properties

def register_properties():
    register_balustrade_properties()
    register_staircase_properties()
    register_glass_properties()
    register_terrain_properties()
    

def unregister_properties():
    unregister_staircase_properties()
    unregister_balustrade_properties()
    unregister_glass_properties()
    unregister_terrain_properties()