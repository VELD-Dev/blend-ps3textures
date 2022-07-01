from bpy.types import (Panel, Operator, ThemeTopBar)

def main(context):
    for ob in context.scene.objects:
        print(ob)
        
class PS3TexGeneratorOperator(Operator):
    """PS3 Texture Generator Operator class"""
    bl_idname = "object.ps3tex_generator"
    bl_label = "Generate Materials"
    
    @classmethod
    def poll(self, context):
        return context.archive_object is not None
    
    def execute(self, context):
        main(context)
        return {'FINISHED'}
    
def menu_func(self, context):
    self.layout.operator(PS3TexGeneratorOperator.bl_idname, text=PS3TexGeneratorOperator.bl_label)
