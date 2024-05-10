import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
# from WorkingArea_up939395.loginpage_new import LoginScreen
from kivy.uix.screenmanager import ScreenManager, Screen


class HomePage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size = Window.size
        # self.name = 'timetableapp'
        # Create a ScreenManager instance and store it as an attribute
        # self.sm = ScreenManager()
        # self.add_widget(self.sm)  # Add the ScreenManager to the TimetableApp

        # Main layout - vertical BoxLayout
        main_layout = BoxLayout(orientation='vertical', spacing=10, padding=(50, 50))

        # "Generate Timetable" label
        label = Label(text="Generate Timetable", font_size=20, size_hint_y=None, height=50)

        # Buttons layout - horizontal BoxLayout
        buttons_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)

        # Login Button
        login_button = Button(text="Login")
        login_button.bind(on_press=self.change_to_timetable)  # Bind the event to the method

        # Adding login button to the buttons layout
        buttons_layout.add_widget(login_button)

        # Adding label and buttons layout to the main layout
        main_layout.add_widget(Label())
        main_layout.add_widget(label)
        main_layout.add_widget(Label())
        main_layout.add_widget(buttons_layout)
        main_layout.add_widget(Label())

        self.add_widget(main_layout)  # Add the main_layout to the TimetableApp widget
    
    def change_to_timetable(self, instance):
        try:
           self.manager.current = 'actual_login'
        except Exception as e:
            print(f"Error occurred while changing to login screen: {e}")