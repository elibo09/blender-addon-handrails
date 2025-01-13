import bpy

# Import all operators
from .balustrade_operators import GAYA_OP_Balustrade
from .stair_handrail_operator import GAYA_OP_StaircaseRailing
from .glass_panels_handrail import GAYA_OP_GlassRailing
from .uneven_terrain_railing import GAYA_OP_Uneven_Terrain_Railing

classes =(GAYA_OP_Balustrade, GAYA_OP_StaircaseRailing, GAYA_OP_GlassRailing, GAYA_OP_Uneven_Terrain_Railing)

# Register all your operators here
def register_operators():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister_operators():
    for cls in classes:
        bpy.utils.unregister_class(cls)


