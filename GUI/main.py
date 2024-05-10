import kivy
from kivy import Config
Config.set('graphics', 'multisamples', '0')
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
#from lecture import Module_page  # Import the Module_page class from your file
from login_second import LoginScreen
from loginpage_new import LoginScreen_new
from homepage_new import HomePage
from generate_timetable_page import MainMenuScreen
from view_timetable import TimetableSchedule
from four_buttons import EntrySection
from lecturer import Lecturer
from module import Module_page
from room import Room
from lecture import Lecture
#from algo import ModifyDataFile
from kivy.core.window import Window


class MyApp(App):
    def build(self):
         sm = ScreenManager()
         homePage = HomePage(name='homepage')
         actual_login = LoginScreen_new(name='actual_login')
         main_menu = MainMenuScreen(name='main_menu')
         view_timetable = TimetableSchedule(name='view_timetable')
         entry_section = EntrySection(name='entry_section')
         module = Module_page(name='module')
         lecturer = Lecturer(name='lecturer')
         lecture = Lecture(name='lecture')
         room = Room(name='room')
         sm.add_widget(homePage)
         sm.add_widget(actual_login)
         sm.add_widget(main_menu)
         sm.add_widget(view_timetable)
         sm.add_widget(entry_section)
         sm.add_widget(lecturer)
         sm.add_widget(room)
         sm.add_widget(lecture)
         sm.add_widget(module)
         return sm
       

if __name__ == "__main__":
    #Window.size = (400, 600)  # Set the window size
    MyApp().run()
