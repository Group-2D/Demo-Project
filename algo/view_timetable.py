import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

# Define the TimetableSchedule layout
class TimetableSchedule(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size = Window.size
        #self.screen_manager = screen_manager

        # Back button
        back_button = Button(text="Back", size_hint=(None, None), size=(100, 50))
        back_button.bind(on_press=self.go_back)
        self.add_widget(back_button)

        # Timetable header
        header = GridLayout(cols=8, size_hint_y=None, height=30)
        days = ['Time', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        for day in days:
            header.add_widget(Label(text=day, size_hint_y=None, height=30))

        self.add_widget(header)

        # Timetable body
        self.timetable_body = GridLayout(cols=8, size_hint_y=None, spacing=2)
        self.timetable_body.bind(minimum_height=self.timetable_body.setter('height'))

        self.populate_timetable()
        self.add_widget(self.timetable_body)

    def populate_timetable(self):
        times = ['8-9', '9-10', '10-11', '11-12', '12-1', '1-2', '2-3', '3-4']
        for time in times:
            self.timetable_body.add_widget(Label(text=time, size_hint_y=None, height=60))
            for _ in range(7):
                self.timetable_body.add_widget(Label(text='Class', size_hint_y=None, height=60))

    def go_back(self, instance):
        # Navigate back to the main menu
        self.manager.current = 'main_menu'
