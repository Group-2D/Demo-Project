from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window

class TimetableSchedule(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size = Window.size  # Use the window size to ensure the layout fills the screen

        # Create a back button
        back_button = Button(text="Back", size_hint=(None, None), size=(100, 50))
        back_button.bind(on_press=self.on_back_button_press)

        # Add the back button at the top of the screen
        self.add_widget(back_button)

        # Create a label for "Room 1" above the timetable
        room_label = Label(text="Room 1", size_hint=(None, None), size=(100, 50))
        self.add_widget(room_label)

        # Timetable header
        header = GridLayout(cols=8, size_hint_y=None, height=30)
        days = ['Time', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        for day in days:
            header.add_widget(Label(text=day, size_hint_y=None, height=30))

        self.add_widget(header)

        # Timetable body with explicit minimum height to ensure visibility
        self.timetable_body = GridLayout(cols=8, size_hint_y=None, spacing=2)
        self.timetable_body.bind(minimum_height=self.timetable_body.setter('height'))  # Bind height to minimum_height

        self.populate_timetable()
        self.add_widget(self.timetable_body)

    def populate_timetable(self):
        times = ['8-9', '9-10', '10-11', '11-12', '12-1', '1-2', '2-3', '3-4']
        for time in times:
            self.timetable_body.add_widget(Label(text=time, size_hint_y=None, height=60))  # Adjusted height for visibility
            for _ in range(7):  # For each day
                self.timetable_body.add_widget(Label(text='Class', size_hint_y=None, height=60))  # Added dummy text for visibility

    def on_back_button_press(self, instance):
        # Define the behavior when the back button is pressed
        print("Back button pressed")

class TimetableApp(App):
    def build(self):
        return TimetableSchedule()

if __name__ == '__main__':
    TimetableApp().run()
