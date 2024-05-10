from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'login_screen'

        layout = BoxLayout(orientation='vertical', spacing=20)

        self.username_label = Label(text='Username:', size_hint=(None, None), size=(100, 30), halign='left',
                                    pos_hint={'center_x': 0.5})
        self.username_input = TextInput(size_hint=(None, None), size=(300, 50), multiline=False, halign='left',
                                        pos_hint={'center_x': 0.5})

        self.password_label = Label(text='Password:', size_hint=(None, None), size=(100, 30), halign='left',
                                    pos_hint={'center_x': 0.5})
        self.password_input = TextInput(password=True, size_hint=(None, None), size=(300, 50), halign='left',
                                        pos_hint={'center_x': 0.5})

        self.login_button = Button(text='Login', size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.5})
        self.login_button.bind(on_press=self.login)

        layout.add_widget(Label())
        layout.add_widget(self.username_label)
        layout.add_widget(self.username_input)
        layout.add_widget(self.password_label)
        layout.add_widget(self.password_input)
        layout.add_widget(Label())
        layout.add_widget(self.login_button)
        layout.add_widget(Label())

        self.add_widget(layout)

    def login(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        # Implement your login logic here


class MainMenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'main_menu'

        main_layout = BoxLayout(orientation='vertical', spacing=10, padding=(50, 50))
        label = Label(text="Generate Timetable", font_size=20, size_hint_y=None, height=50)
        buttons_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)

        login_button = Button(text="Login Here")
        login_button.bind(on_press=self.change_to_login)

        buttons_layout.add_widget(login_button)

        main_layout.add_widget(Label())
        main_layout.add_widget(label)
        main_layout.add_widget(Label())
        main_layout.add_widget(buttons_layout)
        main_layout.add_widget(Label())

        self.add_widget(main_layout)

    def change_to_login(self, instance):
        self.manager.current = 'login_screen'


class TimetableApp(App):
    def build(self):
        sm = ScreenManager()
        main_menu_screen = MainMenuScreen()
        login_screen = LoginScreen()
        sm.add_widget(main_menu_screen)
        sm.add_widget(login_screen)
        return sm


# if __name__ == '__main__':
#     Window.size = (400, 600)  # Set the window size
#     TimetableApp().run()