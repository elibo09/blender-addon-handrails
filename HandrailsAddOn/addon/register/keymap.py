import bpy

keys = []

def register_keymap():

    wm = bpy.context.window_manager
    addon_keyconfig = wm.keyconfigs.addon
    kc = addon_keyconfig

    km = kc.keymaps.new(name = "3D View", space_type = "VIEW_3D")
    kmi = km.keymap_items.new("wm.call_menu_pie","F","PRESS", ctrl = False, shift = False)
    kmi.properties.name = "OBJECT_MT_simple_pie_menu"
    keys.append((km,kmi))

def unregister_keymap():
    for km,kmi in keys:
        km.keymap_items.remove(kmi)
    keys.clear()