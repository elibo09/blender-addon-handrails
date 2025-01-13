import bpy

class StaircaseProperties(bpy.types.PropertyGroup):
    step_count: bpy.props.IntProperty(
        name="Step Count",
        description="Number of steps in the staircase",
        default=10,
        min=2,
        max=50
    )
    step_height: bpy.props.FloatProperty(
        name="Step Height",
        description="Height of each step",
        default=0.2,
        min=0.1,
        max=1.0
    )
    step_depth: bpy.props.FloatProperty(
        name="Step Depth",
        description="Depth of each step",
        default=0.3,
        min=0.2,
        max=1.0
    )
    step_width: bpy.props.FloatProperty(
        name="Step Width",
        description="Width of the steps",
        default=2.0,
        min=0.5,
        max=5.0
    )
    post_width: bpy.props.FloatProperty(
        name="Post Width",
        description="Width of the posts for the staircase handrail",
        default=0.05,
        min=0.01,
        max=0.5
    )
    post_height: bpy.props.FloatProperty(
        name="Post Height",
        description="Height of the posts for the handrail",
        default=1.0,
        min=0.5,
        max=3.0
    )
    handrail_left: bpy.props.BoolProperty(
        name="Left Side Handrail",
        description="Add handrail and posts on the left side",
        default=False
    )
    handrail_right: bpy.props.BoolProperty(
        name="Right Side Handrail",
        description="Add handrail and posts on the right side",
        default=True
    )

def register_staircase_properties():
    bpy.utils.register_class(StaircaseProperties)
    bpy.types.Scene.staircase_properties = bpy.props.PointerProperty(type=StaircaseProperties)

def unregister_staircase_properties():
    bpy.utils.unregister_class(StaircaseProperties)
    del bpy.types.Scene.staircase_properties
