# glass_railing_properties.py
import bpy

class GlassRailingProperties(bpy.types.PropertyGroup):
    post_height: bpy.props.FloatProperty(
        name="Post Height",
        description="Height of the posts",
        default=1.0,
        min=0.05,
        max=5.0
    )
    
    post_width: bpy.props.FloatProperty(
        name="Post Width",
        description="Width of the posts",
        default=0.05,
        min=0.01,
        max=0.5
    )
    
    glass_length: bpy.props.FloatProperty(
        name="Glass Length",
        description="Length of each glass panel",
        default=0.5,
        min=0.05,
        max=2.5
    )
    
    handrail_radius: bpy.props.FloatProperty(
        name="Handrail Radius",
        description="Radius of the handrail",
        default=0.05,
        min=0.01,
        max=0.2
    )
    
    array_count: bpy.props.IntProperty(
        name="Array Count",
        description="Number of glass panels to create",
        default=5,
        min=1,
        max=50
    )
    
# Register the properties
def register_glass_properties():
    bpy.utils.register_class(GlassRailingProperties)
    bpy.types.Scene.glass_railing_properties = bpy.props.PointerProperty(type=GlassRailingProperties)

def unregister_glass_properties():
    bpy.utils.unregister_class(GlassRailingProperties)
    del bpy.types.Scene.glass_railing_properties
