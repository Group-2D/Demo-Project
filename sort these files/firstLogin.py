
# function that handles first login 
# when program is installed and run for the first time this will run and create
#   the first admin

# subsequent admins?

import subprocess
import sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

from hashlib import sha256

# ensures pip is installed
subprocess.check_call([sys.executable, 
                        "-m",
                        "ensurepip", 
                        "--upgrade"])

# ensures that all the modules required for the program to run are installed
subprocess.check_call([sys.executable, 
                        "-m", 
                        "pip", 
                        "install", 
                        "-r", 
                        "requirements.txt"])

def firstLogin(userkey):
    
    shaUserkey = sha256()
    shaUserkey.update(userkey.encode('utf-8'))
    encryptedUserkey = shaUserkey.hexdigest()

    with open("userkey.txt","w") as file:
        file.write(encryptedUserkey)
    
    print("admin created")

class createAdminScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.orientation = 'vertical'
        self.padding = [0, 0, 0, 0]
        self.spacing = 20
        self.size_hint = (None, None)
        self.size = (300, 300)
        self.center = Window.center

        # Username Input
        self.username_label = Label(text='Create Username:',
                                    size_hint=(None, None), 
                                    size=(100, 30), 
                                    halign='auto', )
        
        self.username_input = TextInput(size_hint=(None, None), 
                                        size=(300, 50), 
                                        multiline=False, 
                                        halign='auto')

        # Password Input
        self.password_label = Label(text='Create Password:', 
                                    size_hint=(None, None), 
                                    size=(100, 30), 
                                    halign='auto')
        
        self.password_input = TextInput(password=True, 
                                        size_hint=(None, None), 
                                        size=(300, 50), 
                                        halign='auto')

        # Login Button
        self.login_button = Button(text='Create', 
                                   size_hint=(None, None), 
                                   size=(100, 50))
        
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
        
        userkey = str(username) + ":" + str(password)

        firstLogin(userkey)


class CreateAdmin(App):
    def build(self):
        return createAdminScreen()


if __name__ == '__main__':
    CreateAdmin().run()
