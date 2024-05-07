import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout  # one of many layout structures
from kivy.uix.textinput import TextInput  # allow for ...text input.
from kivy.uix.screenmanager import ScreenManager, Screen
from algo import ModifyDataFiles


# An actual app is likely to consist of many different
# "pages" or "screens." Inherit from GridLayout
# Arg for gridlayout GridLayout
class Lecturer(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # runs on initialization
        # def __init__(self, **kwargs):
        # we want to run __init__ of both ConnectPage AAAAND GridLayout (understanding_super.py)
        # super().__init__(**kwargs)

        # self.cols = 2  # used for our grid
        # general_layout = BoxLayout(orientation="vertical", size_hint=(None, None), size=(400, 400), spacing=10,
        #                            padding=10, pos_hint={'center_x': 0.5, 'center_y': 0.5})
        # layout = BoxLayout(orientation="vertical", spacing=2, padding=0)
        # # widgets added in order, so mind the order.
        # layout.add_widget(Label(text='Lecturer Name:', size_hint_y=None, size_hint_x=None))  # widget #1, top left
        # Lecturer_Name = TextInput(multiline=False, size_hint_y=None, size_hint_x=None, height=40,
        #                           width=300)  # defining self.ip...
        # layout.add_widget(Lecturer_Name)  # widget #2, top right
        # layout.add_widget(Label(text='Lecturer Last Name:', size_hint_y=None, size_hint_x=None))  # widget #1, top left
        # Lecturer_lName = TextInput(multiline=False, size_hint_y=None, size_hint_x=None, height=40,
        #                           width=300)  # defining self.ip...
        # layout.add_widget(Lecturer_Name)  # widget #2, top
        # layout.add_widget(
        #     Label(text='Lecturer AVailability', size_hint_y=None, size_hint_x=None))  # widget #1, top left
        # Lecturer_Availability = TextInput(multiline=False, size_hint_y=None, size_hint_x=None, height=40,
        #                                   width=300)  # defining self.ip...
        # layout.add_widget(Lecturer_Availability)
        # submit_btn = Button(text='submit', on_press=self.on_submit, height=30, width=60, size_hint_y=None,
        #                     size_hint_x=None)
        # layout.add_widget(submit_btn)
        # general_layout.add_widget(layout)
        # self.add_widget(general_layout)
        general_layout = BoxLayout(orientation="vertical", size_hint=(None, None), size=(400, 400), spacing=10,
                                   padding=10, pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout = BoxLayout(orientation="vertical", spacing=2, padding=0)

        # Username Input
        self.lecturer_firstname = TextInput(size_hint=(None, None), size=(300, 50), multiline=False, halign='left')
        layout.add_widget(Label(text='Lecturer First Name:', size_hint=(None, None), size=(100, 30), halign='left'))
        layout.add_widget(self.lecturer_firstname)

        # Password Input
        self.lecturer_lastname = TextInput(size_hint=(None, None), size=(300, 50), multiline=False, halign='left')
        layout.add_widget(Label(text='Lecturer last Name:', size_hint=(None, None), size=(100, 30), halign='left'))
        layout.add_widget(self.lecturer_lastname)
        
        self.lecturer_availability = TextInput(size_hint=(None, None), size=(300, 50), multiline=False, halign='left')
        layout.add_widget(Label(text='Lecturer availability:', size_hint=(None, None), size=(100, 30), halign='left'))
        layout.add_widget(self.lecturer_availability)

        # Login Button
        login_button = Button(text='Submit', size_hint=(None, None), size=(100, 50))
        login_button.bind(on_press=self.on_submit)
        layout.add_widget(login_button)

        # Add widgets to the layout
        general_layout.add_widget(layout)
        self.add_widget(general_layout)

    def on_submit(self, instance):
         lecturer_first_name = self.lecturer_firstname.text
         lecturer_last_name = self.lecturer_lastname.text
         lecturer_availability = self.lecturer_availability.text
         data = lecturer_first_name +","+lecturer_last_name+","+lecturer_availability
         try:
            insertdata = ModifyDataFiles()
        #  insertdata.insertLecturerData(data)
            insertdata.insertLecturerData(data)
         except Exception as e:
            print(f"Error occurred while changing to login screen: {e}")
            print("failed")
        
        #  print(lecturer_first_name +","+lecturer_last_name+","+lecturer_availability)


# class Setap2DApp(App):
#     def build(self):
#         return ConnectPage()


# if __name__ == "__main__":
#     Module_page().run()