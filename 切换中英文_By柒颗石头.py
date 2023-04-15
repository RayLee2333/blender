import bpy

bl_info = {
    "name": "中英文切换助手",
    "author": "柒颗石头",
    "version": (1, 0),
    "blender": (3, 4, 0),
    "location": "3D Viewport Sidebar",
    "description": "帮助您在Blender中切换中英文语言",
    "category": "Language",
}

class SwitchLanguagePanel(bpy.types.Panel):
    bl_label = "中英文切换助手"
    bl_idname = "VIEW3D_PT_switch_language"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tools"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Blender语言切换:")

        row = layout.row()
        row.operator("wm.switch_language", text="翻译中文").language = 'zh_CN'

        row = layout.row()
        row.operator("wm.switch_language", text="翻译英文").language = 'en_US'


class SwitchLanguageOperator(bpy.types.Operator):
    bl_idname = "wm.switch_language"
    bl_label = "Switch Language"

    language: bpy.props.StringProperty()

    def execute(self, context):
        bpy.context.preferences.view.use_translate_interface = True
        bpy.context.preferences.view.language = self.language
        return {'FINISHED'}

def register():
    bpy.utils.register_class(SwitchLanguagePanel)
    bpy.utils.register_class(SwitchLanguageOperator)


def unregister():
    bpy.utils.unregister_class(SwitchLanguagePanel)
    bpy.utils.unregister_class(SwitchLanguageOperator)


if __name__ == "__main__":
    register()
