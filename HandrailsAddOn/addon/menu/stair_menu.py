import bpy
class GAYA_PT_StaircasePanel(bpy.types.Panel):
    bl_idname = "GAYA_PT_StaircasePanel"
    bl_label = "Staircase Handrail Generator"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Handrails"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header_preset(self, context):
        layout = self.layout
        layout.label(text="", icon="IPO_ELASTIC")
    
    def draw(self, context):
        layout = self.layout
        handrail_props = context.scene.staircase_properties


        # Staircase Properties
        box = layout.box()
        box.label(text="Staircase Parameters:")
        box.prop(handrail_props, "step_count")
        box.prop(handrail_props, "step_height")
        box.prop(handrail_props, "step_depth")
        box.prop(handrail_props, "step_width")

        layout.separator()
        box = layout.box()
        box.label(text="Posts Parameters:")
        box.prop(handrail_props, "post_width")
        box.prop(handrail_props, "post_height")  
         # Draw handrail placement options
        layout.label(text="Handrail Placement:")
        layout.prop(handrail_props, "handrail_left")
        layout.prop(handrail_props, "handrail_right")

        layout.operator("handrail.create_staircase_with_posts_handrail", text="Create Staircase Handrail")
