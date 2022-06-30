from bpy.types import (Panel, Operator, ThemeTopBar)

def main(context):
    for ob in context.scene.objects:
        print(ob)
        
class GeneratorOperator(Operator):
    """Tooltip"""
    bl_idname = "object.ps3tex_generator"
    bl_label = "Blend PS3Texture Generator"
    
    @classmethod
    def poll(self, context):
        return context.archive_object is not None
    
    def execute(self, context):
        main(context)
        return {'FINISHED'}
    
def menu_func(self, context):
    self.layout.operator(Generator.bl_idname, text=Generator.bl_label)
