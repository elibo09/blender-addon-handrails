bl_info = {
    "name": "Handrails Add-On",
    "description": "A tool for creating handrails",
    "author": "Elisa Barba Ortiz",
    "version": (1, 0),
    "blender": (4, 3),
    "location": "View3D",
    "category": "3D View",
}

import bpy

def register():
    from .addon.register import register_addon
    register_addon()
    

    

def unregister():
    from .addon.register import unregister_addon
    unregister_addon()