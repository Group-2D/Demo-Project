import copy
import time
import random
from databaseManager import * 

# Maximum of 5 days, 9 hour slots, 12 rooms; format days, hour slots, rooms
timetableEntries = [
    [[None for _ in range(8)] for _ in range(9)] for _ in range(5)]
professorTimetable = []

modules_list = []

# Declare variables
modName = []
lecHours = []
practHours = []
tutHours = []
studentsEnrolled = []
profRequired = []
newTimetableEntries = []

# All the list of days
dayList = ["MON",
           "TUE",
           "WED",
           "THU",
           "FRI"]

'''
    This is the list of all of the classes that are used within the algorithm
'''
class Module:
    def __init__(self, 
                 moduleName, 
                 lectureHours, 
                 practicalHours, 
                 tutorialHours, 
                 students_enrolled, 
                 prof_required):
        
        self.modName = moduleName

        self.lecHours = lectureHours
        self.practHours = practicalHours
        self.tutHours = tutorialHours
        self.studentsEnrolled = students_enrolled
        self.profRequired = prof_required

        self.room = ""
        self.day = ""
        self.time = 0
        self.professors = []
        self.classType = ""

    def __str__(self) -> str:
        
        mystring = f"""Module Name: {self.modName}
                    On: {self.day} at: {self.time} in room: {self.room}
                    Professors: {self.professors}, 
                    Type: {self.classType}
                    """
        return mystring


class Room:
    def __init__(self, 
                 room_name, 
                 building, 
                 room_type, 
                 capacity):
        self.roomName = room_name
        self.buildingName = building
        self.roomType = room_type
        self.roomcapacity = capacity


class Professor:
    def __init__(self, 
                 professor_name, 
                 modules):
        self.professorName = professor_name
        self.modulesTaught = modules

'''
    This function creates instances of the module class to be used elsewhere for comparing and storing modules.
'''
def createModuleClasses(modules_list, 
                        modName, lecHours, 
                        practHours, studentsEnrolled, 
                        profRequired):
    
    for i in range(0, len(modName)):
        mod_name = modName[i]
        lectureHours = lecHours[i]
        pract_hours = practHours[i]
        tutorialHours = tutHours[i]
        students_enrolled = studentsEnrolled[i]
        prof_required = profRequired [i]

        new_module = Module(mod_name, 
                            lectureHours, 
                            pract_hours, 
                            tutorialHours, 
                            students_enrolled, 
                            prof_required)
        
        modules_list.append(new_module)
    
    return modules_list


'''
    This function fills the module lists with data from the database. It uses the selectOnCondition and count_db_entries functions from database_manager to pull the information in.
'''
def fillModuleLists(session, modules_list):
    # Finds the number of entries in the module list table                                                           
    session.count_db_entries("modules", "mod_id")
    length = session.dbCursor.fetchone()[0]

    # Brings in [variable name, table, by mod_id, at position] e.g. SELECT mod_name FROM modules WHERE mod_id = i+1
    for i in range(0, length):
        modName.append(str(session.selectOnCondition(["mod_name"], "modules", "mod_id", i+1))[2:-3])
        studentsEnrolled.append(int(session.selectOnCondition(["mod_enrolled"], "modules", "mod_id", i + 1)[0]))
        lecHours.append(int(session.selectOnCondition(["mod_lectures"], "modules", "mod_id", i+1)[0]))
        practHours.append(int(session.selectOnCondition(["mod_practicals"], "modules", "mod_id", i+1)[0]))
        tutHours.append(int(session.selectOnCondition(["mod_tutorials"], "modules", "mod_id", i+1)[0]))
        profRequired.append(int(session.selectOnCondition(["mod_prof_req"], "modules", "mod_id", i+1)[0]))

    modules_list = createModuleClasses(modules_list, modName, lecHours, practHours, studentsEnrolled, profRequired)
    
    return modules_list


'''
    This function fills the rooms lists with data from the database. It uses the selectOnCondition and count_db_entries functions from database_manager to pull the information in.
'''
def fillRoomLists(session, roomsList):
    # Finds the number of entries in the room list table
    session.count_db_entries("room", "room_id")
    length = session.dbCursor.fetchone()[0]

    # Defines the length of the room list array based on the number of entries in the "room" table
    roomsList = [[None for _ in range(4)] for _ in range(length)]

    # For the number of rooms in the database.
    for i in range (length):
        roomsList [i] [0] = str(session.selectOnCondition(["room_name"], 'room', 'room_id', i+1))[2:-3]
        roomsList [i] [1] = int(session.selectOnCondition(["room_capacity"], 'room', 'room_id', i+1)[0])
        roomsList [i] [2] = session.selectOnCondition(["building_id"], 'room', 'room_id', i+1)

    return roomsList


'''
    This function fills the professors lists with data from the database. It uses the selectOnCondition and count_db_entries functions from database_manager to pull the information in.
'''
def fillProfessorsLists(session, professorsList):
    # Finds the number of entries in the lecturer list table
    session.count_db_entries("lecturer", "lecturer_id")
    length = session.dbCursor.fetchone()[0]

    # Determines the length of the professor list based on the number of entries in the 'lecturer' table
    professorsList = [[None for _ in range(5)] for _ in range(length)]

    # For the number of professors in the database
    for i in range (length):
        professorsList [i] [0] = str(session.selectOnCondition(["lecturer_title"], "lecturer", "lecturer_id", i + 1))[2:-3]
        professorsList [i] [1] = str(session.selectOnCondition(["lecturer_fname"], 'lecturer', 'lecturer_id', i + 1))[2:-3]
        professorsList [i] [2] = str(session.selectOnCondition(["lecturer_lname"], 'lecturer', 'lecturer_id', i + 1))[2:-3]
        professorsList [i] [3] = str(session.selectOnCondition(["lecturer_modules"], 'lecturer', 'lecturer_id', i + 1))[2:-3]
        professorsList[i] [4] = str(session.selectOnCondition(["lecturer_availability"], 'lecturer', 'lecturer_id', i + 1))[2:-3]

    return professorsList


'''
    This function is used to pool together the fillLists functions for convenience.
'''
def importFromDatabase(session, modules_list, rooms_list, professors_list):
    modules_list = fillModuleLists(session, modules_list)
    rooms_list = fillRoomLists(session, rooms_list)
    professors_list = fillProfessorsLists(session, professors_list)

    return modules_list, rooms_list, professors_list


'''
    This function is reponsible for checking whether the professor can work at a particular time and day.
'''
def checkProfessorAvailability(checkTime,
                               checkDay,
                               module_info,
                               professorsList):
    
    timeSlotBit = checkTime * dayList.index(checkDay)
    availableProfessors = []

    for checkProfessor in professorsList:
        if module_info.modName in checkProfessor[3]:
            if int((checkProfessor[4])[timeSlotBit]) == 0:
                availableProfessors.append(checkProfessor[:3])

    return availableProfessors

'''
    This function is responsible for applying constraints to potential timetable entries, attempting to find a suitable time that a specified number of lecturers can teach in. 
        When it finds a time where all the constraints can be applied, then it adds all the information into an array called TimetableEntries, which stores all of the times.
        
'''
def checkConstraints(
    module_info, 
    classType, 
    randPotentialRoom, 
    studentsUnassigned, 
    room,
    professorsList):

    unavailable_combinations = []

    # Calculate the total number of possible combinations
    total_combinations = 45  # Assuming 9 hours per day

    # continue generating new practicals until all students have been assigned 
    #   a practical if need be
    while studentsUnassigned > 0:
        if len(unavailable_combinations) >= total_combinations:
            print("No available times for this room.")
            return False

        randDay = random.choice(dayList)
        randHour = random.randint(0, 8)
        dayHourComb = (randDay, 
                       randHour)

        # Restarts the loop if the combination has already been used
        if dayHourComb in unavailable_combinations:
            continue

        chosenProfessors = []

        unavailable = False

        for checkModule in newTimetableEntries:
            if checkModule.day == randDay and checkModule.time == randHour and checkModule.room == randPotentialRoom:
                unavailable = True
                # Add to a lists of day hour combinations that cannot be used so they aren't checked again.
                unavailable_combinations.append(randDay, 
                                                randHour) 

        if unavailable == False: 
            # Fills the availableProfessors array with the list of professors that can work at the specific day and time.
            availableProfessors = checkProfessorAvailability(randHour,
                                                             randDay,
                                                             module_info,
                                                             professorsList)

            # Get out of the checkConstraints file and try and find another day and time.
            if len(availableProfessors) == 0:
                return False
            
            else:
                # Generates a random number x amount of times where x is the 
                #   number of professors required to take each practical
                # This will be used to pick one or more of the professors who 
                #   are available at this time
                for i in range(module_info.profRequired):
                    chosenProfessors.append(random.choice(availableProfessors))
            
                entryModule = copy.deepcopy(module_info)
                entryModule.day = randDay
                entryModule.time = randHour
                entryModule.room = room [0]
                entryModule.professors = chosenProfessors
                entryModule.classType = classType

                # Puts the information into the timetableEntries array.
                newTimetableEntries.append(entryModule)

                studentsUnassigned = studentsUnassigned - room [1] 

    return True
    

'''
    This function creates a random number representing a potential room from roomslist and determines if it is suitable capacity wise for the type of session (lec, pract, tut) that is to take place.
'''
def insertIntoTimetable(module_info, classType, roomsList, professorsList):
    room = ""
    studentsUnassigned = module_info.studentsEnrolled
    moduleInserted = False

    # Test checking invalid values
    valid_classTypes = ['lec', 'pract', 'tut']  # Define valid classType values
    if classType not in valid_classTypes:
        raise ValueError("Invalid classType. Supported classTypes are 'lec', 'pract', and 'tut'.")


    while not moduleInserted:
        correctRoomType = False

        while not correctRoomType:
            # Generates a random number to represent a room
            randPotentialRoom = random.randint(0, len(roomsList) - 1)

            # Checks that the room is the correct classType for the sessions being 
            # assigned to
            if classType == 'lec' or classType == 'tut':
                if roomsList[randPotentialRoom][1] >= 100:
                    room = roomsList[randPotentialRoom]
                    correctRoomType = True 
            else:
                if roomsList[randPotentialRoom][1] < 100:
                    room = roomsList[randPotentialRoom]
                    correctRoomType = True 

        # Inserts the requirements of the module into the timetable
        moduleInserted = checkConstraints(module_info,
                                          classType, 
                                          randPotentialRoom, 
                                          studentsUnassigned, 
                                          room, 
                                          professorsList)


'''
This function displays all the newly generated timetable entries.
'''
def displayTimetable():
    for lesson in newTimetableEntries:
        print(lesson.day)
        print(lesson)


'''
This function inserts the timetableEntry information into the database.
'''
def insertIntoDatabase(session):
    for i in range(len(newTimetableEntries)):
        timetableEntry = newTimetableEntries[i]  # Index 4 corresponds to the fifth entry

        module = timetableEntry.modName
        day = timetableEntry.day
        time = timetableEntry.time
        room = timetableEntry.room
        professors = timetableEntry.professors
        classType = timetableEntry.classType
        
        # Finds the module id and room id from the database
        modId = int(session.selectOnCondition(["mod_id"], "modules", "mod_name", module)[0])
        roomId = int(session.selectOnCondition(["room_id"], "room", "room_name", room)[0])

        # string : tbl_name, tbl_cols = array / list of strings List[str], values either a string (1 item) or a list[]
        session.insertIntoDb("lecture", 
                            ["mod_id", "room_id", "lecture_type", "lecture_day", "lecture_start"], 
                            (modId, roomId, classType, day, time))
    
def main():
    # Connects to the dbManager
    session = dbManager()

    # Declare variables
    modulesCompleted = []

    modules_list = []
    rooms_list = []
    professors_list = []

    # Read values in from the database to fill lists
    modules_list, rooms_list, professors_list = importFromDatabase(session, 
                                                                   modules_list, 
                                                                   rooms_list,
                                                                   professors_list,)

    # For every module
    for i in range(len(modules_list)):
        moduleInserted = False 

        while moduleInserted == False:
            ## Generates a random number to determine which module gets timetableentries created first. This is to prevent any inherent bias towards the first alphabetical
            # module name if the program has many modules
            randMod = random.randint(0, len(modules_list)-1) 

            if randMod not in modulesCompleted:
                # Add sessions if the lecture hours is greater than 0.
                if modules_list[randMod].lecHours > 0:
                    for i in range(lecHours [randMod]):
                        insertIntoTimetable(modules_list[randMod], 'lec', rooms_list, professors_list)

                # Add sessions if the practical hours is greater than 0.
                if modules_list[randMod].practHours > 0:
                    for i in range(practHours [randMod]):
                        insertIntoTimetable(modules_list[randMod], 'pract', rooms_list, professors_list)

                # Add sessions if the tutor hours is greater than 0.
                if modules_list[randMod].tutHours > 0:
                    # For the number of 
                    for i in range(tutHours [randMod]):
                        insertIntoTimetable(modules_list[randMod], 'tut', rooms_list, professors_list)

                # This module no longer needs sessions added to it.
                moduleInserted = True
            
        ## Adds to this array to ensure the same module does not get added to the 
        #  timetable again.
        modulesCompleted.append(randMod) 

    # Displays the timetable and inserts the new entries into the database
    displayTimetable()
    insertIntoDatabase(session)

if __name__ == '__main__':
    main()