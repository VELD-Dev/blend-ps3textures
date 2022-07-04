# This is the main file of addon.

bl_info = {
    "name": "Blend PS3Texture",
    "author": "VELD-Dev",
    "version": (0, 0, 21),
    "blender": (3, 2, 0),
    "location": "File > PS3Texture > Generate Materials",
    "description": ("Tool to generate all the materials for a model, mostly for an entire map from "
                    "a PS3 exported .obj map file. (Work only with PS3 games) "                     ),
    "warning": "Work in progress, be careful, the mod may crash Blender, always backup your files !",
    "doc_url": "https://github.com/VELD-Dev/blend-ps3textures",
    "category": "Reverse-Engineering",
}

print("hello world")


if "bpy" in locals():
    import importlib
    importlib.reload(ps3tex_operator)
else:
    from . import ps3tex_operator

import bpy
from bpy.types import (Panel, Operator, ThemeTopBar)

class PS3TexPanel(Panel):
    """Panel of Blend PS3Texture"""
    bl_label = "Blend PS3Texture"
    bl_idname = "HEADER_PT_generate_ps3tex"
    bl_space_type = "TOPBAR"
    bl_region_type = "HEADER"
    
    def draw(self, context):
        layout = self.layout
        obj = context.object
        row = layout.row()
        row.operator(ps3tex_operator.PS3TexGeneratorOperator.bl_idname, text=ps3tex_operator.PS3TexGeneratorOperator.bl_label, icon="OUTLINER_OB_LIGHTPROBE")
        #ICON: OUTLINER_OB_LIGHTPROBE


from bpy.utils import register_class, unregister_class


classes = [
    PS3TexPanel,
    ps3tex_operator.PS3TexGeneratorOperator
]


def register():
    for cls in classes:
        register_class(cls)
    bpy.types.TOPBAR_MT_file.append(PS3TexPanel.draw()) #ps3tex_operator.menu_func)

def unregister():
    for cls in classes:
        unregister_class(cls)
    bpy.types.VIEW3D_MT_object.remove(ps3tex_operator.menu_func)
        
if __name__ == "__main__":
    register()
    bpy.ops.object.ps3tex_generator()