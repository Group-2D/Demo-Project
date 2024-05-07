import tkinter
import customtkinter
from tkinter import filedialog
from databaseManager import *
import algorithm_with_db_functionality as timetable

class main:

    def __init__(self):

        # Initial Setup of the Window
        self.main_window = tkinter.Tk()
        self.main_window.geometry("950x650")
        self.main_window.resizable(False, False)
        self.main_window.title("Timetable Generator Main")
        
        # Adds Buttons and Labels to main Window
        self.setup_main_window()

    def setup_main_window(self):
        # Creates the Overall Title        
        overall_title = customtkinter.CTkLabel(master=self.main_window, text="Timetable Generator", font=("Calibre", 25), corner_radius=10)
        overall_title.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

        # Set a fixed width and height for buttons
        button_width = 250
        button_height = 50

        # Creates buttons with fixed size
        insert_file_button = customtkinter.CTkButton(master=self.main_window, text="INSERT FILE", font=("Calibre", 20), corner_radius=10, fg_color="black", command=self.insert_file_window, width=button_width, height=button_height)
        insert_file_button.place(relx=0.25, rely=0.25, anchor=tkinter.CENTER)

        alter_data_button = customtkinter.CTkButton(master=self.main_window, text="ADD/DELETE DATA", font=("Calibre", 20), corner_radius=10, fg_color="black", command=self.alter_data_window, width=button_width, height=button_height)
        alter_data_button.place(relx=0.25, rely=0.5, anchor=tkinter.CENTER)

        get_data_button = customtkinter.CTkButton(master=self.main_window, text="GET DATA", font=("Calibre", 20), corner_radius=10, fg_color="black", command=self.get_data_window, width=button_width, height=button_height)
        get_data_button.place(relx=0.75, rely=0.25, anchor=tkinter.CENTER)

        generate_timetable_button = customtkinter.CTkButton(master=self.main_window, text="GENERATE TIMETABLE", font=("Calibre", 20), corner_radius=10, fg_color="black", command=self.generate_timetable_window, width=button_width, height=button_height)
        generate_timetable_button.place(relx=0.75, rely=0.5, anchor=tkinter.CENTER)

        quit_button = customtkinter.CTkButton(self.main_window, text="QUIT", font=("Calibre", 20), corner_radius=10, fg_color="black", command=self.quit_button_command, width=button_width, height=button_height)
        quit_button.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)

        # Runs the main window
        self.main_window.mainloop()

    def quit_button_command(self):
        self.main_window.destroy()

    def insert_file_window(self):
        
        insert_window = tkinter.Toplevel(self.main_window)
        insert_window.title("Insert Data From File")
        insert_window.geometry("650x450")
        insert_window.resizable(False, False)
        insert_window.attributes("-topmost", True)

        open_button = customtkinter.CTkButton(master=insert_window, text="Select File", font=("Calibre", 20), corner_radius=10, fg_color="black", command=self.open_file_dialog)
        open_button.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

        selected_file_label = customtkinter.CTkLabel(insert_window, text="Selected File:", font=("Calibre", 20), corner_radius=10)
        selected_file_label.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

        self.file_name = customtkinter.CTkLabel(insert_window, text="", corner_radius=10)
        self.file_name.place(relx=0.1, rely=0.3, anchor=tkinter.W)

        insert_button = customtkinter.CTkButton(insert_window, text="Insert Into Database", font=("Calibre", 20), corner_radius=10, text_color="white", fg_color="black")
        insert_button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


    def open_file_dialog(self):
        # Selects a file and puts the directory of that file on `insert_window`
        file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            self.file_name.configure(text=file_path)

    def alter_data_window(self):

        def add_data():
            pass

        def delete_data():
            pass
        
        alter_data = tkinter.Toplevel(self.main_window)
        alter_data.title("Add/Delete Data")
        alter_data.geometry("650x450")
        alter_data.resizable(False, False)
        alter_data.attributes("-topmost", True)

        title = customtkinter.CTkLabel(alter_data, text="Add/Delete Data", font=("Calibre", 20), corner_radius=10)
        title.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

        tbl_name_label = customtkinter.CTkLabel(alter_data, text="Table Name (String):", font=("Calibre", 16), corner_radius=10)
        tbl_name_label.place(relx=0.1, rely=0.2, anchor=tkinter.W)
        tbl_name_entry = customtkinter.CTkEntry(alter_data)
        tbl_name_entry.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

        tbl_column_label = customtkinter.CTkLabel(alter_data, text="Column Name (String):", font=("Calibre", 16), corner_radius=10)
        tbl_column_label.place(relx=0.1, rely=0.3, anchor=tkinter.W)
        tbl_column_entry = customtkinter.CTkEntry(alter_data)
        tbl_column_entry.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        values_label = customtkinter.CTkLabel(alter_data, text="Values (Any):", font=("Calibre", 16), corner_radius=10)
        values_label.place(relx=0.1, rely=0.4, anchor=tkinter.W)
        values_entry = customtkinter.CTkEntry(alter_data)
        values_entry.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

        note_label = customtkinter.CTkLabel(alter_data, text="*Seperate each values with a ',' e.g., value1,value2", font=("Calibre", 12), corner_radius=10)
        note_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        add_button = customtkinter.CTkButton(alter_data, text="Add Data", font=("Calibre", 20), fg_color="black")
        add_button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

        delete_button = customtkinter.CTkButton(alter_data, text="Delete Data", font=("Calibre", 20), fg_color="black", command=delete_data)
        delete_button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

    def get_data_window(self):
        """
        Select all
        DROPDOWN FOR TABLE NAMES
        """
        get_data = tkinter.Toplevel(self.main_window)
        get_data.title("Get Data")
        get_data.geometry("650x450")
        get_data.resizable(False, False)
        get_data.attributes("-topmost", True)

        title = customtkinter.CTkLabel(get_data, text="Get Data", font=("Calibre", 20), corner_radius=10)
        title.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
        

    def generate_timetable_window(self):
        generate_timetable = tkinter.Toplevel(self.main_window)
        generate_timetable.title("Generate Timetable")
        generate_timetable.geometry("650x450")
        generate_timetable.resizable(False, False)
        generate_timetable.attributes("-topmost", True)

        gt_button = customtkinter.CTkButton(generate_timetable, text="Generate Timetable", font=("Calibre", 20), fg_color="black", command=timetable.main)
        gt_button.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

        error_label = customtkinter.CTkLabel(generate_timetable, text="", font=("Calibre", 20))
        error_label.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        download_button = customtkinter.CTkButton(generate_timetable, text="Download Timetable (AFTER GENERATING)", font=("Calibre", 20), fg_color="black")
        download_button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)


run = main()