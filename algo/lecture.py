from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
import kivy
from kivy.uix.screenmanager import ScreenManager, Screen


class Lecture(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        general_layout = BoxLayout(orientation="vertical", size_hint=(None, None), size=(400, 400), spacing=10,
                                   padding=10, pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout = BoxLayout(orientation="vertical", spacing=2, padding=0)
        module_item = {
            'module 1': 'King Charles',
            'module 2': 'Anglesea',
            'module 3': 'Buckingham',
            'module 4': 'FTC'
        }

        # Adding a back button
        back_button = Button(text="Back", size_hint=(None, None), size=(100, 50))
        back_button.bind(on_press=self.go_back)

        layout.add_widget(back_button)
        layout.add_widget(Label(text='Click to select Building:', size_hint=(None, None)))  # widget #1, top left

        my_dropdown = DropDown()

        for key, value in module_item.items():  # Corrected variable name
            btn = Button(text=value, size_hint_y=None, height=40)
            btn.bind(on_release=lambda btn: my_dropdown.select(btn.text))
            my_dropdown.add_widget(btn)

        main_button = Button(text='Select Building', size_hint_y=None, height=40)
        main_button.bind(on_release=my_dropdown.open)

        my_dropdown.bind(on_select=lambda instance, x: setattr(main_button, 'text', x))

        layout.add_widget(main_button)
        layout.add_widget(Label(text='Room Name:', size_hint_y=None, size_hint_x=None))  # widget #1, top left
        self.Room_Name = TextInput(multiline=False, size_hint_y=None, size_hint_x=None, height=40, width=300)
        layout.add_widget(self.Room_Name)
        layout.add_widget(
            Label(text='Lecturer Availability', size_hint_y=None, size_hint_x=None))  # widget #1, top left
        self.Lecturer_Availability = TextInput(multiline=False, size_hint_y=None, size_hint_x=None, height=40,
                                               width=300)
        layout.add_widget(self.Lecturer_Availability)
        submit_btn = Button(text='submit', on_press=self.on_submit, height=30, width=60, size_hint_y=None,
                            size_hint_x=None, padding=20)
        layout.add_widget(submit_btn)

        general_layout.add_widget(layout)
        self.add_widget(general_layout) 

    def on_submit(self, instance):
        lecturer_name = self.Room_Name.text  # Changed variable name to Room_Name
        lecturer_availability = self.Lecturer_Availability.text
        print(f"Module Name: {lecturer_name}")  # Corrected variable name

    def go_back(self, instance):
        print("Back button pressed")  # Implement your functionality to go back here


# if __name__ == "__main__":
#     Module_page().run()