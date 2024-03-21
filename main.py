from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window


# Define the TimetableSchedule layout
class TimetableSchedule(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size = Window.size

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


# Main Menu Screen
class MainMenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'main_menu'

        main_layout = BoxLayout(orientation='vertical', spacing=10, padding=(50, 50))
        label = Label(text="Generate Timetable", font_size=20, size_hint_y=None, height=50)
        buttons_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)

        view_button = Button(text="View Timetable")
        view_button.bind(on_press=self.change_to_timetable)

        generate_button = Button(text="Generate New Timetable")
        generate_button.bind(on_press=self.buttonPressTemp)

        buttons_layout.add_widget(view_button)
        buttons_layout.add_widget(generate_button)

        main_layout.add_widget(Label())
        main_layout.add_widget(label)
        main_layout.add_widget(Label())
        main_layout.add_widget(buttons_layout)
        main_layout.add_widget(Label())

        self.add_widget(main_layout)

    def change_to_timetable(self, instance):
        self.manager.current = 'timetable_schedule'
    
    def buttonPressTemp(self, instance):
        print("Button pressed")


# Timetable Screen
class TimetableScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'timetable_schedule'
        timetable_layout = TimetableSchedule()
        self.add_widget(timetable_layout)


# App Initialization
class TimetableApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenuScreen())
        sm.add_widget(TimetableScreen())
        return sm


if __name__ == '__main__':
    TimetableApp().run()
