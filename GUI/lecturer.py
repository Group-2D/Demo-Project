import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout  # one of many layout structures
from kivy.uix.textinput import TextInput  # allow for ...text input.
from kivy.uix.screenmanager import ScreenManager, Screen
from algo import ModifyDataFiles



class Lecturer(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
       
        general_layout = BoxLayout(orientation="vertical", size_hint=(None, None), size=(400, 400), spacing=10,
                                   padding=10, pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # Top header with back button
        header_layout = BoxLayout(orientation="horizontal", size_hint=(1, None), height=40)
        back_button = Button(text="Back", size_hint=(None, None), width=80, height=40)
        back_button.bind(on_press=self.go_back)
        header_layout.add_widget(back_button)
        header_layout.add_widget(Label(text="Lecturer Page", size_hint=(1, None), height=40))
        general_layout.add_widget(header_layout)

        # Main content
        layout = BoxLayout(orientation="vertical", spacing=2, padding=0)
        layout.add_widget(Label(text='Lecturer First Name:'))  # Label
        self.Lecturer_Name = TextInput(multiline=False, height=40, width=300)  # TextInput
        layout.add_widget(self.Lecturer_Name)
        layout.add_widget(Label(text='Lecturer Last Name'))  # Label
        self.Lecturer_lName = TextInput(multiline=False, height=40, width=300)  # TextInput
        layout.add_widget(self.Lecturer_lName)
        layout.add_widget(Label(text='Lecturer Availability'))  # Label
        self.Lecturer_Availability = TextInput(multiline=False, height=40, width=300)  # TextInput
        layout.add_widget(self.Lecturer_Availability)

        submit_btn = Button(text='Submit', on_press=self.validate_form, height=30, width=60)
        submit_btn.bind(on_press=self.on_submit)
        layout.add_widget(submit_btn)

        general_layout.add_widget(layout)
        self.add_widget(general_layout) 

    def on_submit(self, instance):
         lecturer_first_name = self.Lecturer_Name.text
         lecturer_last_name = self.Lecturer_lName.text
         lecturer_availability = self.Lecturer_Availability.text
         data = lecturer_first_name +","+lecturer_last_name+","+lecturer_availability
         try:
            insertdata = ModifyDataFiles()
        #  insertdata.insertLecturerData(data)
            if((insertdata.insertLecturerData(data))):
                print("record submitted") 
            else:
                print("Failed")
         except Exception as e:
            print(f"Error occurred while changing to login screen: {e}")
            print("failed")
        
        #  print(lecturer_first_name +","+lecturer_last_name+","+lecturer_availability)
    def go_back(self, instance):
        # Navigate back to the main menu
        self.manager.current = 'entry_section'

    def validate_form(self, instance):
        Lecturer_Name = self.Lecturer_Name.text.strip()
        Lecturer_lName = self.Lecturer_lName.text.strip()
        Lecturer_Availability = self.Lecturer_Availability.text.strip()

        if not Lecturer_Name or not Lecturer_lName or not Lecturer_Availability:
            print("Please complete form details.")
        else:
          self.on_submit(self)
           
