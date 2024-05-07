from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
#from algo import ModifyDataFiles


class Module_page(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        general_layout = BoxLayout(orientation="vertical", size_hint=(None, None), size=(400, 400), spacing=10,
                                   padding=10, pos_hint={'center_x': 0.5, 'center_y': 0.5})

        layout = BoxLayout(orientation="vertical", spacing=2, padding=0)

        # Back button above the module text
        back_btn = Button(text='Back', on_press=self.go_back, height=30, width=60, size_hint_y=None, size_hint_x=None)
        layout.add_widget(back_btn)

        layout.add_widget(Label(text='Module:', size_hint_y=None, size_hint_x=None))
        self.module_name_input = TextInput(multiline=False, size_hint_y=None, size_hint_x=None, height=40, width=300)
        layout.add_widget(self.module_name_input)
        submit_btn = Button(text='Submit', on_press=self.on_submit, height=30, width=60, size_hint_y=None,
                            size_hint_x=None)
        layout.add_widget(submit_btn)

        general_layout.add_widget(layout)
       
        

    def on_submit(self, instance):
        # module_name = self.module_name_input.text
        # enter_module = ModifyDataFiles()
        print("I can hear you")

    def go_back(self, instance):
        self.stop()  # Stops the current application instance, effectively going back


# if __name__ == '__main__':
#     Module_page().run()
