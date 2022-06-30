# This is the main file of addon.

bl_info = {
    "name": "Blend PS3Texture",
    "author": "VELD-Dev",
    "version": (0, 0, 1),
    "blender": (3, 2, 0),
    "location": "File > PS3Texture > Generate MTL File",
    "description": "Tool to generate a MTL file for a model, globally for an entire map from a PS3 File. (Work only with PS3 games)",
    "warning": "Work in progress, be careful, the mod may crash Blender, always backup your files !",
    "doc_url": "https://github.com/VELD-Dev/blend-ps3textures",
    "category": "Development",
}

from . import operator
#import bpy
global bpy
from bpy.types import (Panel, Operator, ThemeTopBar)

class PS3TexPanel(Panel):
    """Panel of Blend PS3Texture"""
    bl_label = "Generate"
    bl_idname = "OBJECT_PT_generate_ps3tex"
    bl_space_type = "VIEW3D"
    bl_region_type = "UI"
    bl_context = "object"
    
    def draw(self, context):
        layout = self.layout
        obj = context.object
        row = layout.row()
        row.label(text=bl_label, icon="OUTLINER_OB_LIGHTPROBE")


from bpy.utils import register_class, unregister_class


classes = [
    operator.GeneratorOperator,
    PS3TexPanel
]


def register():
    for cls in classes:
        register_class(cls)

def unregister():
    for cls in classes:
        unregister_class(cls)

#if __name__ == "__main__":
#    print(operator)
#    register()