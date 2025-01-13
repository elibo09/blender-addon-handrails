import bpy
class GAYA_PT_UnevenTerrainPanel(bpy.types.Panel):
    
    bl_idname = "GAYA_PT_uneven_terrain_railing"
    bl_label = "Uneven Terrain Railing"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Handrails"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header_preset(self, context):
        layout = self.layout
        layout.label(text="", icon="RNDCURVE")
    
    def draw(self, context):
        layout = self.layout
        props = context.scene.uneven_terrain_properties
        
        layout.prop(props, "scale")
        layout.prop(props, "count")
        layout.operator("object.uneven_terrain_railing", text="Apply Railing")
