from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from hashlib import sha256

class LoginScreen_new(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.center = Window.center
        general_layout = BoxLayout(orientation="vertical", size_hint=(None, None), size=(400, 400), spacing=10,
                                   padding=10, pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout = BoxLayout(orientation="vertical", spacing=2, padding=0)

        # Username Input
        self.username_input = TextInput(size_hint=(None, None), size=(300, 50), multiline=False, halign='left')
        layout.add_widget(Label(text='Username:', size_hint=(None, None), size=(100, 30), halign='left'))
        layout.add_widget(self.username_input)

        # Password Input
        self.password_input = TextInput(password=True, size_hint=(None, None), size=(300, 50), halign='left')
        layout.add_widget(Label(text='Password:', size_hint=(None, None), size=(100, 30), halign='left'))
        layout.add_widget(self.password_input)

        # Login Button
        login_button = Button(text='Login', size_hint=(None, None), size=(100, 50))
        login_button.bind(on_press=self.login)
        layout.add_widget(login_button)

        # Add widgets to the layout
        general_layout.add_widget(layout)
        self.add_widget(general_layout)




    def login(self, instance):
        try:
         username = self.username_input.text
         password = self.password_input.text
        
         print("Username:", username)
         print("Password:", password)

         # Implement your login logic here
         userkey = username +' '+ password
         shaUserkey = sha256()
         shaUserkey.update(userkey.encode('utf-8'))
         encryptedUserkey = shaUserkey.hexdigest()
         print("login successful")
         self.change_to_main()

        except Exception as e:
            print(f"Error occurred while changing to login screen: {e}")
            print("login failed")
    




    def change_to_main(self):
        try:
           self.manager.current = 'main_menu'
        except Exception as e:
            print(f"Error occurred while changing to login screen: {e}")

    
       

# class LoginApp(App):
#     def build(self):
#         return LoginScreen()


# if __name__ == '__main__':
#     LoginApp().run()

