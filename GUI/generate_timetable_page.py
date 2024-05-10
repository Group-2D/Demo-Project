#code for Page A
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window


# Define the TimetableSchedule layout
# class TimetableSchedule(Screen):
#     def __init__(self, screen_manager, **kwargs):
#         super().__init__(**kwargs)
#         self.orientation = 'vertical'
#         self.size = Window.size
#         self.screen_manager = screen_manager

#         # Back button
#         back_button = Button(text="Back", size_hint=(None, None), size=(100, 50))
#         back_button.bind(on_press=self.go_back)
#         self.add_widget(back_button)

#         # Timetable header
#         header = GridLayout(cols=8, size_hint_y=None, height=30)
#         days = ['Time', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#         for day in days:
#             header.add_widget(Label(text=day, size_hint_y=None, height=30))

#         self.add_widget(header)

#         # Timetable body
#         self.timetable_body = GridLayout(cols=8, size_hint_y=None, spacing=2)
#         self.timetable_body.bind(minimum_height=self.timetable_body.setter('height'))

#         self.populate_timetable()
#         self.add_widget(self.timetable_body)

#     def populate_timetable(self):
#         times = ['8-9', '9-10', '10-11', '11-12', '12-1', '1-2', '2-3', '3-4']
#         for time in times:
#             self.timetable_body.add_widget(Label(text=time, size_hint_y=None, height=60))
#             for _ in range(7):
#                 self.timetable_body.add_widget(Label(text='Class', size_hint_y=None, height=60))

#     def go_back(self, instance):
#         # Navigate back to the main menu
#         self.screen_manager.current = 'main_menu'


# Main Menu Screen
class MainMenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.name = 'main_menu'

        main_layout = BoxLayout(orientation='vertical', spacing=10, padding=(50, 50))
        label = Label(text="Generate Timetable", font_size=20, size_hint_y=None, height=50)
        buttons_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)

        view_button = Button(text="View Timetable")
        view_button.bind(on_press=self.view_timetable)

        generate_button = Button(text="Make Entries")
        generate_button.bind(on_press=self.change_to_page_b)

        buttons_layout.add_widget(view_button)
        buttons_layout.add_widget(generate_button)

        main_layout.add_widget(Label())
        main_layout.add_widget(label)
        main_layout.add_widget(Label())
        main_layout.add_widget(buttons_layout)
        main_layout.add_widget(Label())

        self.add_widget(main_layout)

    def view_timetable(self, instance):
        self.manager.current = 'view_timetable'

    def change_to_page_b(self, instance):
        self.manager.current = 'entry_section'


# # Timetable Screen
# class TimetableScreen(Screen):
#     def __init__(self, screen_manager, **kwargs):
#         super().__init__(**kwargs)
#         self.name = 'timetable_schedule'
#         timetable_layout = TimetableSchedule(screen_manager)
#         self.add_widget(timetable_layout)


# # Page B
# class PageB(Screen):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.name = 'page_b'
#         main_layout = BoxLayout(orientation='vertical', spacing=10, padding=(50, 50))

#         back_button = Button(text="Back", size_hint=(None, None), size=(100, 50))
#         back_button.bind(on_press=self.go_back)

#         label = Label(text="CONSTRUCT FRESH TIMETABLE", font_size=20, size_hint_y=None, height=50)

#         main_layout.add_widget(back_button)
#         main_layout.add_widget(Label())
#         main_layout.add_widget(label)
#         main_layout.add_widget(Label())

#         self.add_widget(main_layout)

#     def go_back(self, instance):
#         self.manager.current = 'main_menu'


# App Initialization
# class TimetableApp(App):
#     def build(self):
#         sm = ScreenManager()
#         main_menu_screen = MainMenuScreen()
#         timetable_screen = TimetableScreen(sm)
#         page_b = PageB()
#         sm.add_widget(main_menu_screen)
#         sm.add_widget(timetable_screen)
#         sm.add_widget(page_b)
#         return sm


# if __name__ == '__main__':
#     TimetableApp().run()