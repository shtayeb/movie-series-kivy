# # from kivy.uix.modalview import ModalView
# # from kivy.lang import Builder

# # from kivymd import images_path
# # from kivymd.app import MDApp
# # from kivymd.uix.card import MDCard

# # Builder.load_string(
# #     '''
# # <Card>:
# #     elevation: 10

# #     FitImage:
# #         id: bg_image
# #         source: "../icons/pose.png"
# #         size_hint:0,0.9
# #         pos_hint: {"right": 1}
# #         radius: [0, 0, 0, 0, ]
# # ''')


# # class Card(MDCard):
# #     pass


# # class Example(MDApp):
# #     def build(self):
# #         modal = ModalView(
# #             size_hint=(0.8, 0.4),
# #             background=f"{images_path}/transparent.png",
# #             overlay_color=(0, 0, 0, 0),
# #         )
# #         modal.add_widget(Card())
# #         modal.open()


# # Example().run()


# from kivy.lang import Builder

# from kivymd.app import MDApp

# KV = '''

# <MyTile@SmartTileWithStar>
#     size_hint_y: None
#     height: "240dp"

# Screen:

#     MDCard:
#         orientation: "vertical"
#         padding: "8dp"
#         size_hint: 1, 0.3
#         size: "280dp", "180dp"
#         pos_hint: {"center_x": .5, "center_y": .5}

#         FitImage:
#             id: bg_image
#             source: "../icons/pose.png"
#             size_hint:0.5,0.9
#             pos_hint: {"left": 1}
#             radius: [0, 0, 0, 0, ]
            
#         MyTile:
#             stars: 5
#             source: "../icons/muscle.png"
            
#         MDLabel:
#             text: "Title"
#             theme_text_color: "Secondary"
#             size_hint: 
#             height: self.texture_size[1]

#         MDSeparator:
#             height: "1dp"

#         MDLabel:
#             text: "Body"
# '''


# class TestCard(MDApp):
#     def build(self):
#         return Builder.load_string(KV)


# TestCard().run()



from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
<MyTile@SmartTileWithLabel>
    size_hint_y: None
    height: "240dp"


ScrollView:

    MDGridLayout:
        cols: 3
        adaptive_height: True
        padding: dp(5), dp(4)
        spacing: dp(5)

        MyTile:
            source: "../icons/fitness.png"
         
            text : "Hello"
        MyTile:
            source: "../icons/fitness.png"
           
            #tile_text_color: app.theme_cls.accent_color
            text : "Hello"
        MyTile:
            source: "../icons/fitness.png"
           
            #tile_text_color: app.theme_cls.accent_color
            text : "Hello"
''' 


class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


MyApp().run()