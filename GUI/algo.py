# Import libraries
import psycopg2

# Creates ModifyDataFiles class
class ModifyDataFiles:

    # Constructor for the ModifyDataFiles class
    def __init__(self):

        # Connect to the timetable database
        try:
            self.connectDb = psycopg2.connect(
                database = "timetable_gen",
                host = "localhost",
                user = "postgres",
                password = "ebere",
                port = "5432"
            )

            # Creates a cursor to be used within the timetable database
            self.cursor = self.connectDb.cursor()
        except:
            pass

        self.lineNo = 0

    # Function to iterate through and insert a file into the database
    # def insertFile(self, file):
        
    #     # Opens the file
    #     file = open(file, "r")

    #     # Iterates through each line of the file
    #     for line in file:

    #         # Increments lineNo by 1 and checks the session type
    #         self.lineNo += 1
    #         insertionType = line.lower().split(",")[0]

    #         if insertionType == "module":
    #             self.insertModuleData(line)
    #         elif insertionType == "lecture":
    #             self.insertLectureData(line)
    #         elif insertionType == "lecturer":
    #             self.insertLecturerData(line)
    #         elif insertionType == "room":
    #             self.insertRoomData(line)
    #         elif insertionType == "building":
    #             self.insertBuildingData(line)
    #         else:
    #             raise ValueError(f"Session Type on Line {self.lineNo} is Invalid")

    # Function to insert a lecture into the database
    def insertLectureData(self, data):
        
        # Splits the data into its respective parts
        _, module_name, room_name, lecturer_fname, lecturer_lname, lecture_time = data.split(",")

        try:
            # Selects the required data from the database
            module_id = self.cursor.execute(
                "SELECT module_id from Module WHERE module_name=%s",
                (module_name)
            )

            room_id = self.cursor.execute(
                "SELECT room_id from Room WHERE room_name=%s",
                (room_name)
            )

            lecturer_id = self.cursor.execute(
                "SELECT lecturer_id from Lecturer WHERE lecturer_fname=%s AND lecturer_lname=%s",
                (lecturer_fname, lecturer_lname)
            )

            # Inserts the lecture into the database
            self.cursor.execute(
                "INSERT INTO Lecture (data) VALUES (%s, %s, %s, %s)",
                (module_id, room_id, lecturer_id, lecture_time)
            )
        
        except:
            raise ValueError(f"There was an error when inserting a lecture into the database (line {self.lineNo})")

    # Function to insert a lecturer into the database
    def insertLecturerData(self, data):
        
        # Splits the data into its respective parts
        #_, lecturerFirstName, lecturerLastName, lecturerAvailability = data.split(",")
        lecturerFirstName, lecturerLastName, lecturerAvailability = data.split(",")

        # Inserts the lecturer into the database
        try:
           
            self.cursor.execute(
                 "INSERT INTO Lecturer (lecturer_fname, lecturer_lname, lecturer_availability) VALUES (%s, %s, %s)",
                 (lecturerFirstName, lecturerLastName, lecturerAvailability)
                )
            # Commit the transaction
            self.connectDb.commit()
            return True
        except:
            self.connectDb.rollback()
            raise ValueError(f"There was an error when inserting a lecturer into the database (line {self.lineNo})")
            return False

    # Function to insert a module into the database
    def insertModuleData(self, data):
        
        # Splits the data into its respective parts
        #moduleName, moduleEnrolled, moduleLectures,module_practicals, module_tutorials = data.split("/")
            
        print(data)
        # Inserts the module into the database
        try:
            self.cursor.execute(
                "INSERT INTO modules (mod_name, mod_enrolled, mod_lectures, mod_practicals, mod_tutorials) VALUES (%s, %s, %s, %s, %s)",data)
            
            self.connectDb.commit()
            return True
        except psycopg2.Error as e:
                        raise ValueError(f"There was an error when inserting a module into the database (line {e})")

        except:
            self.connectDb.rollback()
            raise ValueError(f"There was an error when inserting a module into the database (line {self.lineNo})")
            return False
        
        

    # Function to insert a room into the database
    def insertRoomData(self, data):
        
        # Splits the data into its respective parts
        

        try:
            # Gets the buildingID from the database
            # buildingID = self.cursor.execute(
            #     "SELECT building_id from Building WHERE building_name=%s",
            #     (data[0])
            # )
            
            print(data[0])
            # Inserts the lecturer into the database
            self.cursor.execute(
                "INSERT INTO room (room_name, room_capacity, building_id) VALUES (%s, %s, %s)", data)
            self.connectDb.commit()
            return True
        except psycopg2.Error as e:
                        raise ValueError(f"There was an error when inserting a module into the database (line {e})")

        except:
            raise ValueError(f"There was an error when inserting a room into the database (line {self.lineNo})")
   
    def selectBuilding(self):
      try:
        # Execute the SQL query to select building_id from the lecturer table
        self.cursor.execute("SELECT building_id, building_name FROM building")
        
        # Fetch the result of the query
        buildingID = self.cursor.fetchall()
        
        # Return the result
        return buildingID

      except Exception as e:
        # If an error occurs, raise a ValueError with an error message
        raise ValueError(f"There was an error when selecting a lecturer: {str(e)}")
    
    def selectLecturer(self):
      try:
        # Execute the SQL query to select building_id from the lecturer table
        self.cursor.execute("SELECT lecturer_id, lecturer_fname FROM lecturer")
        
        # Fetch the result of the query
        buildingID = self.cursor.fetchall()
        
        # Return the result
        return buildingID

      except Exception as e:
        # If an error occurs, raise a ValueError with an error message
        raise ValueError(f"There was an error when selecting a lecturer: {str(e)}")


    # Function to insert a building into the database
    def insertBuildingData(self, data):
        
        #Splits the data into its respective parts
        _, buildingName = data.split(",")

        # Inserts the building into the database
        try:
            self.cursor.execute(
                "INSERT INTO Building (data) VALUES (%s)",
                (buildingName)
            )

        except:
            raise ValueError(f"There was an error when inserting a building into the database (line {self.lineNo})")

modifyData = ModifyDataFiles()
# modifyData.insertFile("C:/Users/jackb/Desktop/university/Year 2/WorkingArea/dummy_data.txt")