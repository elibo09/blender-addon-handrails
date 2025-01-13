import bpy
import math

class GAYA_OP_StaircaseRailing(bpy.types.Operator):
    bl_idname = "handrail.create_staircase_with_posts_handrail"
    bl_label = "Create Staircase with Posts and Handrail"

    def execute(self, context):
        handrail_props = context.scene.staircase_properties

        # Use the values from the sliders
        num_steps = handrail_props.step_count
        step_height = handrail_props.step_height
        step_depth = handrail_props.step_depth
        step_width = handrail_props.step_width
        post_height = handrail_props.post_height
        post_width = handrail_props.post_width

        # Determine which sides to add the handrail and posts
        add_left = handrail_props.handrail_left
        add_right = handrail_props.handrail_right

        # Create staircase steps
        steps = []

        for i in range(num_steps):
            # Calculate the height from the base level to the current step's top
            current_step_height = (i + 1) * step_height

            # Calculate the position of the step so they stack properly
            step_location = (i * step_depth / 2, 0, current_step_height / 4)

            # Add a step at the calculated location
            bpy.ops.mesh.primitive_cube_add(size=1, location=step_location)

            # Set the dimensions of each step
            step = bpy.context.object
            step.scale = (step_depth / 2, step_width / 2, current_step_height / 2)
            # Store each step in a list for joining
            steps.append(step)

        # Create posts at each step (left, right, or both)
        posts = []

        for i in range(num_steps):
            x_position = i * step_depth / 2
            z_position = (i * step_height) + (post_height / 2)

            # Create posts on the right side if selected
            if add_right:
                bpy.ops.mesh.primitive_cube_add(size=1, location=(x_position, (-step_width / 4) + (post_width / 2), (z_position / 2) + step_height / 2))
                post = bpy.context.object
                post.scale = (post_width / 2, post_width / 2, post_height / 2)
                posts.append(post)

            # Create posts on the left side if selected
            if add_left:
                bpy.ops.mesh.primitive_cube_add(size=1, location=(x_position, (step_width / 4) - (post_width / 2), (z_position / 2) + step_height / 2))
                post = bpy.context.object
                post.scale = (post_width / 2, post_width / 2, post_height / 2)
                posts.append(post)

        # Create the handrails and join with posts
        handrails = []

        # Create handrail for right side if selected
        if add_right and len(posts) >= 2:
            handrail = self.create_handrail(posts, step_width, num_steps, step_depth, step_height, post_height, post_width, side='right')
            handrails.append(handrail)

        # Create handrail for left side if selected
        if add_left and len(posts) >= 2:
            handrail = self.create_handrail(posts, step_width, num_steps, step_depth, step_height, post_height, post_width, side='left')
            handrails.append(handrail)

        # Join all parts (steps, posts, handrails) into one object
        bpy.ops.object.select_all(action='DESELECT')
        all_parts = steps + posts + handrails

        # Select and join all parts
        for obj in all_parts:
            obj.select_set(True)

        bpy.context.view_layer.objects.active = all_parts[0]  # Set one of the parts as active
        bpy.ops.object.join()

        # Apply curve modifier to the entire structure
        curve_name = "StaircasePath"  # Replace with the name of the user's curve
        curve = bpy.data.objects.get(curve_name)

        if curve is None:

            return {'CANCELLED'}

        # Add curve modifier to the joined structure
        bpy.ops.object.modifier_add(type='CURVE')
        modifier = bpy.context.object.modifiers[-1]
        modifier.object = curve
        modifier.deform_axis = 'POS_X'

        return {'FINISHED'}

    def create_handrail(self, post_locations, step_width, num_steps, step_depth, step_height, post_height, post_width, side='right'):
        # Create the handrail as a single object
        first_post_loc = post_locations[0].location
        last_post_loc = post_locations[-1].location

        # Calculate the midpoint between the first and last posts
        mid_x = (first_post_loc.x + last_post_loc.x) / 2
        mid_z = ((first_post_loc.z + last_post_loc.z) / 2) + (post_height / 4) + (post_width / 2)
        y_position = (-step_width / 4) + (post_width / 2) if side == 'right' else (step_width / 4) - (post_width / 2)

        # Calculate the length of the handrail
        total_depth = (num_steps) * step_depth
        total_height = (num_steps) * step_height
        handrail_length = math.hypot(total_depth, total_height)

        # Calculate the rotation angle for the handrail
        angle = math.atan2(total_height, total_depth)

        # Create the handrail (a long cube)
        bpy.ops.mesh.primitive_cube_add(size=1, location=(mid_x, y_position, mid_z))
        handrail = bpy.context.object
        handrail.scale = (handrail_length / 2, post_width / 2, post_width / 2)

        # Rotate the handrail to match the incline
        handrail.rotation_euler = (0, -angle, 0)

        # Subdivide the handrail to add more geometry for bending
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.subdivide(number_cuts=20)
        bpy.ops.object.mode_set(mode='OBJECT')

        return handrail
