import bpy
import math

class GAYA_OP_GlassRailing(bpy.types.Operator):
    bl_idname = "handrail.create_glass_railing"
    bl_label = "Create Glass Railing"

    def execute(self, context):
        # Access properties from the UI
        glass_props = context.scene.glass_railing_properties

        post_height = glass_props.post_height
        post_width = glass_props.post_width
        glass_width = 0.02
        glass_height = post_height - 0.2
        glass_length = glass_props.glass_length
        handrail_radius = glass_props.handrail_radius
        array_count = glass_props.array_count

        # Create left post
        bpy.ops.mesh.primitive_cube_add(size=1, location=(-glass_length / 2, 0, post_height / 2))
        left_post = bpy.context.object
        left_post.scale = (post_width, post_width, post_height)

        # Create right post
        bpy.ops.mesh.primitive_cube_add(size=1, location=(glass_length / 2, 0, post_height / 2))
        right_post = bpy.context.object
        right_post.scale = (post_width, post_width, post_height)

        # Create glass panel
        bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, glass_height / 2))
        glass_panel = bpy.context.object
        glass_panel.scale = (glass_length, glass_width, glass_height)

        # Create glass material
        glass_material = bpy.data.materials.new(name="GlassMaterial")
        glass_material.use_nodes = True
        nodes = glass_material.node_tree.nodes
        nodes.clear()  # Clear default nodes

        # Add Glass BSDF
        glass_node = nodes.new(type='ShaderNodeBsdfGlass')
        glass_node.inputs['IOR'].default_value = 1.45  # Index of refraction for glass
        glass_node.inputs['Roughness'].default_value = 0.1  # Slightly rough for realism

        # Add Material Output
        output_node = nodes.new(type='ShaderNodeOutputMaterial')

        # Link Glass BSDF to Output
        glass_material.node_tree.links.new(glass_node.outputs['BSDF'], output_node.inputs['Surface'])

        # Assign the glass material to the glass panel
        if glass_panel.data.materials:
            glass_panel.data.materials[0] = glass_material
        else:
            glass_panel.data.materials.append(glass_material)

        # Create metal material for posts and handrail
        metal_material = bpy.data.materials.new(name="MetalMaterial")
        metal_material.use_nodes = True
        metal_nodes = metal_material.node_tree.nodes
        metal_nodes.clear()  # Clear default nodes

        # Add Principled BSDF for Metal
        metal_node = metal_nodes.new(type='ShaderNodeBsdfPrincipled')
        metal_node.inputs['Metallic'].default_value = 1.0  # Fully metallic
        metal_node.inputs['Roughness'].default_value = 0.1  # Slightly shiny for realism

        # Add Material Output
        metal_output_node = metal_nodes.new(type='ShaderNodeOutputMaterial')

        # Link Metal BSDF to Output
        metal_material.node_tree.links.new(metal_node.outputs['BSDF'], metal_output_node.inputs['Surface'])

        # Assign metal material to posts
        if left_post.data.materials:
            left_post.data.materials[0] = metal_material
        else:
            left_post.data.materials.append(metal_material)

        if right_post.data.materials:
            right_post.data.materials[0] = metal_material
        else:
            right_post.data.materials.append(metal_material)

        # Join all parts (posts, glass, handrail) into one object
        bpy.ops.object.select_all(action='DESELECT')
        left_post.select_set(True)
        right_post.select_set(True)
        glass_panel.select_set(True)

        bpy.context.view_layer.objects.active = left_post  # Set one of the parts as active
        bpy.ops.object.join()  # Join the selected objects into a single object

        railing = bpy.context.object

        # Apply Array Modifier to repeat the structure
        bpy.ops.object.modifier_add(type='ARRAY')
        array_modifier = railing.modifiers[-1]
        array_modifier.count = array_count  # Use the UI property for array count
        array_modifier.relative_offset_displace[0] = 1.1  # Spacing between panels

        # Calculate total handrail length
        total_handrail_length =(glass_length * array_count * array_modifier.relative_offset_displace[0]) + (post_width * (array_count + 1))


        # Create a single handrail that spans the entire length of the railing
        handrail_location = (total_handrail_length / 2 - (glass_length / 2)-(post_width/2), 0, post_height)
        bpy.ops.mesh.primitive_cylinder_add(
            radius=handrail_radius,
            depth=total_handrail_length,
            location=handrail_location,
            rotation=(0, 1.5708, 0)  # Align along X-axis
        )
        handrail = bpy.context.object

        # Assign metal material to handrail
        if handrail.data.materials:
            handrail.data.materials[0] = metal_material
        else:
            handrail.data.materials.append(metal_material)

            

        return {'FINISHED'}
