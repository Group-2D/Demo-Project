import kivy
from kivy import Config
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout  # one of many layout structures
from kivy.uix.textinput import TextInput  # allow for ...text input.
from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import ScreenManager, Screen

from algo import ModifyDataFiles

#kivy.require("1.10.1")


# An actual app is likely to consist of many different
# "pages" or "screens." Inherit from GridLayout
# Arg for gridlayout GridLayout
class Room(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # runs on initialization
       
        # general_layout = BoxLayout(orientation="vertical", size_hint=(None, None), size=(400, 400), spacing=10,
        #                            padding=10, pos_hint={'center_x': 0.5, 'center_y': 0.5})
        # layout = BoxLayout(orientation="vertical", spacing=2, padding=0)
        # display_items = {
        #     'building 1': 'King Charles',
        #     'building 2': 'Anglesea',
        #     'building 3': 'Buckingham',
        #     'building 4': 'FTC'
        # }

        # my_dropdown = DropDown()
        # layout.add_widget(Label(text='Click to select Building:', size_hint=(None, None)))  # widget #1, top left

        # for key, value in display_items.items():
        #     btn = Button(text=value, size_hint_y=None, height=40)
        #     btn.bind(on_release=lambda btn: my_dropdown.select(btn.text))
        #     my_dropdown.add_widget(btn)

        # main_button = Button(text='Select Building', size_hint_y=None, height=40)
        # main_button.bind(on_release=my_dropdown.open)

        # my_dropdown.bind(on_select=lambda instance, x: setattr(main_button, 'text', x))

        # layout.add_widget(main_button)
        # # widgets added in order, so mind the order.
        # layout.add_widget(Label(text='Room Name:', size_hint_y=None, size_hint_x=None))  # widget #1, top left
        # Room_Name = TextInput(multiline=False, size_hint_y=None, size_hint_x=None, height=40,
        #                       width=300)  # defining self.ip...
        # layout.add_widget(Room_Name)  # widget #2, top right
        # layout.add_widget(
        #     Label(text='Lecturer AVailability', size_hint_y=None, size_hint_x=None))  # widget #1, top left
        # Room_Capacity = TextInput(multiline=False, size_hint_y=None, size_hint_x=None, height=40,
        #                           width=300)  # defining self.ip...
        # layout.add_widget(Room_Capacity)
        # submit_btn = Button(text='submit', on_press=self.on_submit, height=30, width=60, size_hint_y=None,
        #                     size_hint_x=None, padding=20)
        # layout.add_widget(submit_btn)
        # general_layout.add_widget(layout)
        # self.add_widget(general_layout) 
        general_layout = BoxLayout(orientation="vertical", size_hint=(None, None), size=(400, 400), spacing=10,
                                   padding=10, pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # Top header with back button
        header_layout = BoxLayout(orientation="horizontal", size_hint=(1, None), height=40)
        back_button = Button(text="Back", size_hint=(None, None), width=80, height=40)
        back_button.bind(on_press=self.go_back)
        header_layout.add_widget(back_button)
        header_layout.add_widget(Label(text="Room Page", size_hint=(1, None), height=40))
        general_layout.add_widget(header_layout)

        # Main content
        layout = BoxLayout(orientation="vertical", spacing=2, padding=0)
        display_items = {'building 1': 'King Charles', 'building 2': 'Anglesea', 'building 3': 'Buckingham',
                         'building 4': 'FTC'}
        my_dropdown = DropDown()

        layout.add_widget(Label(text='Click to select Building:'))  # Label
        for key, value in display_items.items():
            btn = Button(text=key+"-"+value, size_hint_y=None, height=40)
            btn.bind(on_release=lambda btn: my_dropdown.select(btn.text))
            my_dropdown.add_widget(btn)

        main_button = Button(text='Select Building', size_hint_y=None, height=40)
        main_button.bind(on_release=my_dropdown.open)
        my_dropdown.bind(on_select=self.on_dropdown_select)

        layout.add_widget(main_button)
        layout.add_widget(Label(text='Room Name:'))  # Label
        self.Room_Name = TextInput(multiline=False, height=40, width=300)  # TextInput
        layout.add_widget(self.Room_Name)
        layout.add_widget(Label(text='Lecturer Capacity'))  # Label
        self.Room_Capacity = TextInput(multiline=False, height=40, width=300)  # TextInput
        layout.add_widget(self.Room_Capacity)

        submit_btn = Button(text='Submit', on_press=self.on_submit, height=30, width=60)
        layout.add_widget(submit_btn)

        general_layout.add_widget(layout)
        self.add_widget(general_layout) 
    def on_dropdown_select(self, instance, selected_value):
        
        print("Selected:", selected_value)
        return selected_value
    def on_submit(self, instance):
        Room_Name = self.Room_Name.text
        Room_Capacity = self.Room_Capacity.text
        my_dropdown_building = self.on_dropdown_select
        data = (Room_Name, int(Room_Capacity), 1)
         #print(data)
        try:
            insertdata = ModifyDataFiles()
        #  insertdata.insertLecturerData(data)
            if((insertdata.insertRoomData(data))):
                print("record submitted") 
            else:
                
                print("Failed")
        except Exception as e:
            print(f"Error occurred while changing to login screen: {e}")
            print("failed")

    
    def go_back(self, instance):
        # Navigate back to the main menu
        self.manager.current = 'entry_section'


