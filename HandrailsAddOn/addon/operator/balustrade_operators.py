import bpy

class GAYA_OP_Balustrade(bpy.types.Operator):
    bl_idname = "handrail.create_balustrade_with_array"
    bl_label = "Create Balustrade with Array Modifier"

    def create_base(self, length, width, height):
        # Create a base (a long rectangular platform)
        bpy.ops.mesh.primitive_cube_add(location=(length / 2, 0, height / 2))
        base = bpy.context.active_object
        base.scale = (length / 2, width / 2, height)
        return base

    def create_post(self, location, size, height):
        # Create a post (basic cube)
        bpy.ops.mesh.primitive_cube_add(location=location)
        post = bpy.context.active_object
        post.scale = (size, size, height + (height * 1 / 5))  # Add extra height for the first and last posts
        return post

    def create_rail(self, length, width, height):
        # Create a rail (horizontal, connecting posts)
        bpy.ops.mesh.primitive_cube_add(location=(length / 2, 0, height))
        rail = bpy.context.active_object
        rail.scale = (length / 2, width / 2, 0.1)  # Default height for rail is 0.1
        return rail

    def create_inner_post(self, location, size, height):
        # Create an inner post (basic cube)
        bpy.ops.mesh.primitive_cube_add(location=location)
        inner_post = bpy.context.active_object
        inner_post.scale = (size, size, height)
        return inner_post

    def apply_array_modifier(self, object, count, spacing):
        # Apply the Array Modifier to the entire fence structure
        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.view_layer.objects.active = object

        # Add Array Modifier
        array_modifier = object.modifiers.new(name="Array", type='ARRAY')
        array_modifier.count = count
        array_modifier.relative_offset_displace[0] = spacing / object.scale[0]  # Set duplication along the X-axis

    def execute(self, context):
        handrail_props = context.scene.balustrade_properties

        # Use the values from the sliders
        base_length = handrail_props.base_length
        post_height = handrail_props.post_height
        post_width = handrail_props.post_width
        rail_height = 2 * post_height  # Rail height will be set at the top of the posts
        array_count = handrail_props.array_count
        inner_post_count = handrail_props.inner_post_count  # Number of inner posts to create
        inner_post_spacing = base_length / (inner_post_count + 1)

        # Create base
        base = self.create_base(base_length, 0.5, 0.1)

        # Create first post
        first_post = self.create_post(location=(0, 0, post_height), size=post_width, height=post_height)

        # Create last post
        last_post = self.create_post(location=(base_length, 0, post_height), size=post_width, height=post_height)
        # Create a list to store all inner posts or balusters
        inner_posts = []

        # Check if elaborated fence is selected
        if handrail_props.fence_type == 'ELABORATED':
            # Get the external baluster model from the scene (replace with inner posts)
            baluster = bpy.context.scene.objects.get("ExternalBaluster")  # Ensure the name matches

            if baluster:
                # Get the original height of the baluster (before scaling)
                original_height = baluster.dimensions.z
                new_height = 2*post_height-0.2

                # Calculate the scaling factor based on the post height and original baluster height
                scale_factor = new_height / original_height  # Adjust scaling factor based on post height

                # Create multiple balusters based on user input
                for i in range(inner_post_count):
                    location = ((i + 1) * inner_post_spacing, 0, post_height)
                    baluster_instance = baluster.copy()
                    baluster_instance.dimensions = (
                        scale_factor * baluster.dimensions.x,
                        scale_factor * baluster.dimensions.y,
                        new_height
                    )
                    baluster_instance.location = location
                    bpy.context.collection.objects.link(baluster_instance)
                    inner_posts.append(baluster_instance)

            else:
                self.report({'ERROR'}, "External baluster model not found!")
                return {'CANCELLED'}

        else:
            # Create inner posts (if simpler fence is selected)
            for i in range(inner_post_count):
                location = ((i + 1) * inner_post_spacing, 0, post_height)
                inner_post=self.create_inner_post(location=location, size=post_width / 2, height=post_height)
                inner_posts.append(inner_post)

        # Create rail (handrail) – fixed at the top of the posts
        rail = self.create_rail(length=base_length, width=0.2, height=rail_height)

        # Join all the objects (base, posts, rails) into a single object
        bpy.ops.object.select_all(action='DESELECT')
        base.select_set(True)
        first_post.select_set(False)
        last_post.select_set(True)
        rail.select_set(True)

        # Select all inner posts or balusters
        for inner_post in inner_posts:
            inner_post.select_set(True)

        bpy.context.view_layer.objects.active = base
        bpy.ops.object.join()  # Join the selected objects into a single object

        # Apply Array Modifier to the entire structure (posts, inner posts, and rails)
        self.apply_array_modifier(bpy.context.view_layer.objects.active, array_count, (base_length / 2) - post_width)

        first_post.select_set(True)
        base.select_set(True)

        bpy.context.view_layer.objects.active = base
        bpy.ops.object.join()  # Join the selected objects into a single object


        return {'FINISHED'}
