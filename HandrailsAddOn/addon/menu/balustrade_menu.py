import bpy

class GAYA_PT_BalustradePanel(bpy.types.Panel):
    bl_idname = "VIEW3D_PT_handrail_panel"
    bl_label = "Balustrade Generator"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Handrails"
    bl_options = {"DEFAULT_CLOSED"}
    
    def draw_header_preset(self, context):
        layout = self.layout
        layout.label(text="", icon="MESH_GRID")

    def draw(self, context):
        layout = self.layout
        handrail_props = context.scene.balustrade_properties
        
        # Add sliders for height, width, handrail height, inner posts and base length
        box = layout.box()
        box.label(text="Balustrade Properties:")
        box.prop(handrail_props, "fence_type")
        box.prop(handrail_props, "post_height")
        box.prop(handrail_props, "post_width")
        box.prop(handrail_props, "inner_post_count")
        box.prop(handrail_props, "base_length")

        # Add Array Count slider
        box.prop(handrail_props, "array_count")

        # Button to create the balustrade
        layout.operator("handrail.create_balustrade_with_array", text="Create Balustrade")