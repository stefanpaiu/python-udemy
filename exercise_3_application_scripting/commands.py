# Those commands were run in Blender

bpy.data.objects

list(bpy.data.objects)

cube = bpy.data.objects["Cube"]
cube.location

# After you move the visualisation of the cube you will have changed the position of it, therefore the location variables will have different values

import mathutils
cube.location += mathutils.Vector((1,1,1))