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
        # general_layout = BoxLayout(orientation="vertical", size_hint=(None, None), size=(400, 400), spacing=10,
        #                            padding=10, pos_hint={'center_x': 0.5, 'center_y': 0.5})
        # layout = BoxLayout(orientation="vertical", spacing=2, padding=0)
        # module_item = {
        #     'module 1': 'King Charles',
        #     'module 2': 'Anglesea',
        #     'module 3': 'Buckingham',
        #     'module 4': 'FTC'
        # }

        # # Adding a back button
        # back_button = Button(text="Back", size_hint=(None, None), size=(100, 50))
        # back_button.bind(on_press=self.go_back)

        # layout.add_widget(back_button)
        # layout.add_widget(Label(text='Click to select Building:', size_hint=(None, None)))  # widget #1, top left

        # my_dropdown = DropDown()

        # for key, value in module_item.items():  # Corrected variable name
        #     btn = Button(text=value, size_hint_y=None, height=40)
        #     btn.bind(on_release=lambda btn: my_dropdown.select(btn.text))
        #     my_dropdown.add_widget(btn)

        # main_button = Button(text='Select Building', size_hint_y=None, height=40)
        # main_button.bind(on_release=my_dropdown.open)

        # my_dropdown.bind(on_select=lambda instance, x: setattr(main_button, 'text', x))

        # layout.add_widget(main_button)
        # layout.add_widget(Label(text='Room Name:', size_hint_y=None, size_hint_x=None))  # widget #1, top left
        # self.Room_Name = TextInput(multiline=False, size_hint_y=None, size_hint_x=None, height=40, width=300)
        # layout.add_widget(self.Room_Name)
        # layout.add_widget(
        #     Label(text='Lecturer Availability', size_hint_y=None, size_hint_x=None))  # widget #1, top left
        # self.Lecturer_Availability = TextInput(multiline=False, size_hint_y=None, size_hint_x=None, height=40,
        #                                        width=300)
        # layout.add_widget(self.Lecturer_Availability)
        # submit_btn = Button(text='submit', on_press=self.on_submit, height=30, width=60, size_hint_y=None,
        #                     size_hint_x=None, padding=20)
        # layout.add_widget(submit_btn)

        # general_layout.add_widget(layout)
        # self.add_widget(general_layout) 
        general_layout = BoxLayout(orientation="vertical", size_hint=(None, None), size=(500, 500), spacing=10,
                                   padding=10, pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # Top header with back button
        header_layout = BoxLayout(orientation="horizontal", size_hint=(1, None), height=40)
        back_button = Button(text="Back", size_hint=(None, None), width=80, height=40)
        back_button.bind(on_press=self.go_back)
        header_layout.add_widget(back_button)
        header_layout.add_widget(Label(text="Lecture Page", size_hint=(1, None), height=40))
        general_layout.add_widget(header_layout)

        # Main content
        layout = BoxLayout(orientation="vertical", spacing=2, padding=0)
        display_items = {'building 1': 'King Charles', 'building 2': 'Anglesea', 'building 3': 'Buckingham',
                         'building 4': 'FTC'}
        # Dropdown for selecting module
        # Dropdown for selecting module
        module_dropdown = DropDown()
        for key, value in display_items.items():
            btn_module = Button(text=value, size_hint_y=None, height=40)  # Set height to 40
            btn_module.bind(on_release=lambda btn: module_dropdown.select(btn.text))
            module_dropdown.add_widget(btn_module)

        main_module_button = Button(text='Select Module', size_hint_y=None, height=40)
        main_module_button.bind(on_release=module_dropdown.open)
        module_dropdown.bind(on_select=lambda instance, x: setattr(main_module_button, 'text', x))
        
        layout.add_widget(Label(text='Click to select Module:'))
        layout.add_widget(main_module_button)

        # Dropdown for selecting room
        room_dropdown = DropDown()
        for key, value in display_items.items():
            btn_room = Button(text=value, size_hint_y=None, height=40)  # Set height to 40
            btn_room.bind(on_release=lambda btn: room_dropdown.select(btn.text))
            room_dropdown.add_widget(btn_room)

        main_room_button = Button(text='Select Room', size_hint_y=None, height=40)
        main_room_button.bind(on_release=room_dropdown.open)
        room_dropdown.bind(on_select=lambda instance, x: setattr(main_room_button, 'text', x))

        layout.add_widget(Label(text='Click to select Room:'))
        layout.add_widget(main_room_button)
        
         # Dropdown for selecting room
        room_dropdown = DropDown()
        for key, value in display_items.items():
            btn_room = Button(text=value, size_hint_y=None, height=40)  # Set height to 40
            btn_room.bind(on_release=lambda btn: room_dropdown.select(btn.text))
            room_dropdown.add_widget(btn_room)

        main_room_button = Button(text='Select Lecturer', size_hint_y=None, height=40)
        main_room_button.bind(on_release=room_dropdown.open)
        room_dropdown.bind(on_select=lambda instance, x: setattr(main_room_button, 'text', x))

        layout.add_widget(Label(text='Click to select Lecturer:'))
        layout.add_widget(main_room_button)
        layout.add_widget(Label(text='Lecture Start Date:'))  # Label
        Lecture_start = TextInput(multiline=False, height=40, width=300)  # TextInput
        layout.add_widget(Lecture_start)
        layout.add_widget(Label(text='Lecture End Date'))  # Label
        Lecture_end = TextInput(multiline=False, height=40, width=300)  # TextInput
        layout.add_widget(Lecture_end)
        

        submit_btn = Button(text='Submit', on_press=self.on_submit, height=30, width=60)
        submit_btn.bind(on_press=self.on_submit)
        layout.add_widget(submit_btn)

        general_layout.add_widget(layout)
        self.add_widget(general_layout) 

    def on_submit(self, instance):
        pass
        # lecturer_name = self.Room_Name.text  # Changed variable name to Room_Name
        # lecturer_availability = self.Lecturer_Availability.text
        # print(f"Module Name: {lecturer_name}")  # Corrected variable name

    def go_back(self, instance):
        # Navigate back to the main menu
        self.manager.current = 'entry_section' # Implement your functionality to go back here


# if __name__ == "__main__":
#     Module_page().run()