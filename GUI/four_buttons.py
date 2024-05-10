#code for page B
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class EntrySection(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Main layout - vertical BoxLayout
        main_layout = BoxLayout(orientation='vertical', spacing=10, padding=(50, 50))

        # Back Button
        back_button = Button(text="Back", size_hint=(None, None), size=(100, 50))  # Adjust the size here
        back_button.bind(on_press= self.go_back)
        # "Generate Timetable" label
        label = Label(text="CONSTRUCT FRESH TIMETABLE", font_size=20, size_hint_y=None, height=50)

        # Buttons layout - horizontal BoxLayout
        buttons_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)

        # Login Button
        lecturer = Button(text="LECTURER")
        lecturer.bind(on_press= self.go_to_lecturer)

        # Sign up Button
        btn_module = Button(text="MODULE")
        btn_module.bind(on_press= self.go_to_module)

        # Extra Buttons
        btn_room = Button(text="ROOM")
        btn_room.bind(on_press= self.go_to_room)
        
        btn_lecture = Button(text="LECTURE")
        btn_lecture.bind(on_press= self.go_to_lecture)

        # Adding buttons to the buttons layout
        buttons_layout.add_widget(lecturer)
        buttons_layout.add_widget(btn_module)
        buttons_layout.add_widget(btn_room)
        buttons_layout.add_widget(btn_lecture)

        # Adding label and buttons layout to the main layout
        main_layout.add_widget(back_button)
        main_layout.add_widget(Label())
        main_layout.add_widget(label)
        main_layout.add_widget(Label())
        main_layout.add_widget(buttons_layout)
        main_layout.add_widget(Label())

        self.add_widget(main_layout)
    def go_back(self, instance):
        # Navigate back to the main menu
        self.manager.current = 'main_menu'
        # lecturer
    def go_to_lecturer(self, instance):
        # Navigate back to the lecturer
        self.manager.current = 'lecturer'
    def go_to_module(self, instance):
        # Navigate back to the module
        self.manager.current = 'module'
    def go_to_room(self, instance):
        # Navigate back to the module
        self.manager.current = 'room'
    def go_to_lecture(self, instance):
        # Navigate back to the module
        self.manager.current = 'lecture'
# if __name__ == '__main__':
#     TimetableApp().run()


