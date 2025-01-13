# glass_railing_ui.py
import bpy

class GAYA_PT_GlassRailingPanel(bpy.types.Panel):
    bl_idname = "GAYA_PT_GlassRailingPanel"
    bl_label = "Glass Railing Generator"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Handrails"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header_preset(self, context):
        layout = self.layout
        layout.label(text="", icon="SHADING_RENDERED")
    
    def draw(self, context):
        layout = self.layout
        glass_props = context.scene.glass_railing_properties

        layout.prop(glass_props, "post_height")
        layout.prop(glass_props, "post_width")
        layout.prop(glass_props, "glass_length")
        layout.prop(glass_props, "handrail_radius")
        layout.prop(glass_props, "array_count")

        # Button to create the glass railing
        layout.operator("handrail.create_glass_railing")

