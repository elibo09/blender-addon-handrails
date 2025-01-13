import bpy

class GAYA_OP_Uneven_Terrain_Railing(bpy.types.Operator):
    bl_idname = "object.uneven_terrain_railing"
    bl_label = "Uneven Terrain Railing System"
    bl_description = "Prepares a path and sets up a railing system for uneven terrain"
    
    def execute(self, context):
        # Define the objects by their names
        landscape_name = "Landscape"
        path_name = "Path"
        fence_name = "Fence"
        
        # Check if both objects exist
        landscape = bpy.data.objects.get(landscape_name)
        path = bpy.data.objects.get(path_name)
        
        if not landscape:
            self.report({'ERROR'}, f"Object '{landscape_name}' not found in the scene.")
            return {'CANCELLED'}
        if not path:
            self.report({'ERROR'}, f"Object '{path_name}' not found in the scene.")
            return {'CANCELLED'}
        
        # Add a Shrinkwrap Modifier to the path
        shrinkwrap = path.modifiers.new(name="Shrinkwrap", type='SHRINKWRAP')
        shrinkwrap.target = landscape
        shrinkwrap.wrap_method = 'NEAREST_VERTEX'
        shrinkwrap.use_apply_on_spline = True
        shrinkwrap.offset = 0.5  # Small offset to avoid clipping

        # Ensure the path is selected and active
        bpy.ops.object.select_all(action='DESELECT')  # Deselect all objects
        path.select_set(True)  # Select the path
        bpy.context.view_layer.objects.active = path # Set it as the active object

        # Enter Edit Mode and subdivide
        bpy.ops.object.mode_set(mode='EDIT')  # Enter Edit Mode
        bpy.ops.curve.select_all(action='SELECT')  # Select all control points in Edit Mode
        bpy.ops.curve.subdivide(number_cuts=10)  # Subdivide twice
        bpy.ops.transform.translate(value=(0, 0, 10))  # Move selected vertices along Z-axis
        bpy.ops.object.mode_set(mode='OBJECT')  # Return to Object Mode
        
        #Add Geometry Nodes Modifier
        bpy.ops.node.new_geometry_nodes_modifier()  # Automatically sets up the node tree
        geo_nodes = path.modifiers.get("GeometryNodes")

        # Access the node tree
        node_tree = geo_nodes.node_group
        nodes = node_tree.nodes
        links = node_tree.links

        # Add Instance on Points Node
        instance_node = nodes.new("GeometryNodeInstanceOnPoints")
        instance_node.location = (0, 0)
        
        # Link Instance on Points to Group Input and Output
        group_input = nodes.get("Group Input")
        links.new(group_input.outputs["Geometry"], instance_node.inputs["Points"])
        group_output = nodes.get("Group Output")
        links.new(instance_node.outputs["Instances"], group_output.inputs["Geometry"])

        # Add Object Info Node
        object_info_node = nodes.new("GeometryNodeObjectInfo")
        object_info_node.location = (-200, 0)
        fence = bpy.data.objects.get(fence_name)
        object_info_node.inputs["Object"].default_value = fence

        # Connect Object Info Geometry Output to Instance on Points Instance Input
        links.new(object_info_node.outputs["Geometry"], instance_node.inputs["Instance"])

        # Use Relative Method
        object_info_node.transform_space = 'RELATIVE'  # Ensures local origin for instancing

        # Enable "As Instance"
        object_info_node.inputs[1].default_value = True 

        # Enable "Pick Instance"
        instance_node.inputs["Pick Instance"].default_value = True  # Check "Pick Instance"

        # Add Sample Curve Node
        sample_curve_node = nodes.new("GeometryNodeSampleCurve")
        sample_curve_node.location = (0, -200)

        # Link Sample Curve
        links.new(group_input.outputs["Geometry"], sample_curve_node.inputs["Curves"])
        links.new(sample_curve_node.outputs["Tangent"], instance_node.inputs["Rotation"])

        # Add Align Euler to Vector Node
        align_euler_node = nodes.new(type="FunctionNodeAlignEulerToVector")
        align_euler_node.location = (200, -200)
        # Connect Sample Curve Tangent to Align Euler Vector Input
        links.new(sample_curve_node.outputs["Tangent"], align_euler_node.inputs["Vector"])
        
        # Connect Align Euler Rotation Output to Instance on Points Rotation Input
        links.new(align_euler_node.outputs["Rotation"], instance_node.inputs["Rotation"])

        # Add Resample Curve Node
        resample_node = nodes.new("GeometryNodeResampleCurve")
        resample_node.location = (0, 100)
        resample_node.inputs["Count"].default_value = 30  # Default number of points
        
        # Link Resample Curve to Group Input
        links.new(group_input.outputs["Geometry"], resample_node.inputs["Curve"])
        
        # Link Resample Curve to Sample Curve
        links.new(resample_node.outputs["Curve"], sample_curve_node.inputs["Curves"])
        links.new(resample_node.outputs["Curve"], instance_node.inputs["Points"])

        # Add Spline Parameter Node
        spline_parameter_node = nodes.new("GeometryNodeSplineParameter")
        spline_parameter_node.location = (-200, -300)  # Position it near the Sample Curve Node

        # Access the properties from the scene
        props = context.scene.uneven_terrain_properties
        scale_value = props.scale
        count_value = props.count

        # Connect Spline Parameter Factor to Sample Curve Factor Input
        links.new(spline_parameter_node.outputs["Factor"], sample_curve_node.inputs["Factor"])

        # Add Value Node for Scale
        scale_value_node = nodes.new("ShaderNodeValue")
        scale_value_node.location = (-400, 0)  # Position near the Group Input for clarity
        scale_value_node.label = "Scale"
        scale_value_node.outputs[0].default_value = 1.0  # Default scale value

        # Connect Scale Value Node to Instance on Points Scale Input
        links.new(scale_value_node.outputs["Value"], instance_node.inputs["Scale"])

        # Add Value Node for Count
        count_value_node = nodes.new("ShaderNodeValue")
        count_value_node.location = (-400, 200)  # Position near the Group Input for clarity
        count_value_node.label = "Count"
        count_value_node.outputs[0].default_value = 10  # Default count value

        # Connect Count Value Node to Resample Curve Count Input
        links.new(count_value_node.outputs["Value"], resample_node.inputs["Count"])

        # Update the node inputs with the UI values
        count_value_node.outputs[0].default_value = count_value
        scale_value_node.outputs[0].default_value = scale_value 



        return {'FINISHED'}

