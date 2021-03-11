# from kivy.lang import Builder

# from kivymd.toast import toast
# from kivymd.uix.bottomsheet import MDListBottomSheet
# from kivymd.app import MDApp

# KV = '''
# Screen:

#     MDToolbar:
#         title: "Example BottomSheet"
#         pos_hint: {"top": 1}
#         elevation: 10

#     MDRaisedButton:
#         text: "Open list bottom sheet"
#         on_release: app.show_example_list_bottom_sheet()
#         pos_hint: {"center_x": .5, "center_y": .5}
# '''


# class Example(MDApp):
#     def build(self):
#         return Builder.load_string(KV)

#     def callback_for_menu_items(self, *args):
#         toast(args[0])

#     def show_example_list_bottom_sheet(self):
#         bottom_sheet_menu = MDListBottomSheet()
#         for i in range(1, 11):
#             bottom_sheet_menu.add_item(
#                 f"Standart Item {i}",
#                 lambda x, y=i: self.callback_for_menu_items(
#                     f"Standart Item {y}"
#                 ),
#             )
#         bottom_sheet_menu.open()


# Example().run()


from kivy.lang import Builder

from kivymd.app import MDApp
import kivymd_extensions.akivymd

KV = """
<NavigationButton@Button_Item>
    icon_color: app.theme_cls.text_color
    text_color: app.theme_cls.text_color
    button_bg_color: app.theme_cls.primary_color
    mode: 'color_on_active'
    badge_disabled: True


MDScreen:

    AKBottomNavigation2:
        bg_color: app.theme_cls.bg_darkest

        NavigationButton:
            text: 'Alert'
            icon: 'bell-outline'

        NavigationButton:
            text: 'Bank'
            icon: 'bank-outline'

        NavigationButton:
            text: 'Download'
            icon: 'arrow-down-bold-outline'
"""


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()