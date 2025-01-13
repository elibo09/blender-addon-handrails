import bpy

class BalustradeProperties(bpy.types.PropertyGroup):
    base_length: bpy.props.FloatProperty(
        name="Base Length",
        description="Length of the base",
        default=2.0,
        min=0.5,
        max=10.0
    )
    post_height: bpy.props.FloatProperty(
        name="Post Height",
        description="Height of the posts",
        default=2.0,
        min=0.5,
        max=5.0
    )
    post_width: bpy.props.FloatProperty(
        name="Post Width",
        description="Width of the posts",
        default=0.1,
        min=0.05,
        max=1.0
    )
    array_count: bpy.props.IntProperty(
        name="Array Count",
        description="Number of balustrade sections",
        default=3,
        min=1,
        max=20
    )
    inner_post_count: bpy.props.IntProperty(
        name="Inner Post Count",
        description="Number of inner posts to create",
        default=2,
        min=1,
        max=10
    )
    fence_type: bpy.props.EnumProperty(
        name="Fence Type",
        description="Choose type of fence",
        items=[
            ('SIMPLE', "Simple", "Simple posts"),
            ('ELABORATED', "Elaborated", "Balusters instead of posts")
        ],
        default='SIMPLE'
    )

def register_balustrade_properties():
    bpy.utils.register_class(BalustradeProperties)
    bpy.types.Scene.balustrade_properties = bpy.props.PointerProperty(type=BalustradeProperties)

def unregister_balustrade_properties():
    bpy.utils.unregister_class(BalustradeProperties)
    del bpy.types.Scene.balustrade_properties
