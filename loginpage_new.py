from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [100, 0, 100, 0]
        self.spacing = 20
        self.size_hint = (None, None)
        self.size = (300, 300)
        self.center = Window.center

        # Username Input
        self.username_label = Label(text='Username:', size_hint=(None, None), size=(100, 30), halign='left')
        self.username_input = TextInput(size_hint=(None, None), size=(300, 50), multiline=False, halign='left')

        # Password Input
        self.password_label = Label(text='Password:', size_hint=(None, None), size=(100, 30), halign='left')
        self.password_input = TextInput(password=True, size_hint=(None, None), size=(300, 50), halign='left')

        # Login Button
        self.login_button = Button(text='Login', size_hint=(None, None), size=(100, 50))
        self.login_button.bind(on_press=self.login)

        # Add widgets to the layout
        self.add_widget(self.username_label)
        self.add_widget(self.username_input)
        self.add_widget(self.password_label)
        self.add_widget(self.password_input)
        self.add_widget(self.login_button)

    def login(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        # Implement your login logic here


class LoginApp(App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    LoginApp().run()
