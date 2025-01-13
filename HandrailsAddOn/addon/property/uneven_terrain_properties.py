import bpy

class UnevenTerrainRailingProperties(bpy.types.PropertyGroup):
    scale: bpy.props.FloatProperty(
        name="Scale",
        description="Scale of the instances",
        default=1.0,
        min=0.1,
        max=10.0
    )
    count: bpy.props.IntProperty(
        name="Count",
        description="Number of points along the curve",
        default=10,
        min=1,
        max=100
    )

# Register the properties
def register_terrain_properties():
    bpy.utils.register_class(UnevenTerrainRailingProperties)
    bpy.types.Scene.uneven_terrain_properties = bpy.props.PointerProperty(type=UnevenTerrainRailingProperties)

def unregister_terrain_properties():
    bpy.utils.unregister_class(UnevenTerrainRailingProperties  )
    del bpy.types.Scene.uneven_terrain_properties
