#  TEMP RULES:
#  All practs for a module will be in the same room.

# how do we associate a professor with a lecture and multiple with the 
#   practicals?
# how to make professors unavailable once they have been assigned to a lecture
# how to end the program if not spaces or availabilities can be found

import random
from databaseManager import * 

# maximum of 5 days, 9 hour slots, 12 rooms; format days, hour slots, rooms
timetableEntries = [
    [[None for _ in range(8)] for _ in range(9)] for _ in range(5)]
professorTimetable = [
    [[None for _ in range(9)] for _ in range(5)] for _ in range(7)]
numOfModules = 6


modules_list = []

module = Module()
professor = Professor()

class Module:
    def __init__(self, 
                 moduleName=None, 
                 lectureHours=None, 
                 practicalHours=None, 
                 tutorialHours=None, 
                 students_enrolled=None):
        
        self.modName = moduleName
        self.lecHours = lectureHours
        self.practHours = practicalHours
        self.tutHours = tutorialHours
        self.studentsEnrolled = students_enrolled

    @classmethod
    def fillModuleLists(self, cls, session, modules_list):
        # finds the number of entries in the module list table                                                           
        session.count_db_entries("modules", "mod_id")
        length = session.dbCursor.fetchone()[0]
        print(f"Module: {length}") 

        for i in range(length):
            #mod_info = session.selectOnCondition(["mod_name, mod_enrolled, mod_lectures, mod_practicals, mod_tutorials"], "modules", "mod_id", i+1)
            modName = session.selectOnCondition(["mod_name"], "modules", "mod_id", i+1)
            lecHours = session.selectOnCondition(["mod_enrolled"], "modules", "mod_id", i+1)
            practHours = session.selectOnCondition(["mod_lectures"], "modules", "mod_id", i+1)
            tutHours = session.selectOnCondition(["mod_practicals"], "modules", "mod_id", i+1)
            studentsEnrolled = session.selectOnCondition(["mod_tutorials"], "modules", "mod_id", i+1)
            module = cls(modName, lecHours, practHours, tutHours, studentsEnrolled)
            modules_list.append(module)

            


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

    def fillProfessorsLists(session):
        # finds the number of entries in the lecturer list table
        session.count_db_entries("lecturer", "lecturer_id")
        length = session.dbCursor.fetchone()[0]
        print(f"Lecturer: {length}")

        professorsList = [[None for _ in range(5)] for _ in range(length)]

        #professorsList = [[] for _ in range(length + 1)]

        for i in range (length):
            #professorsList [i] [0] = session.selectOnCondition(["lecturer_title", 'lecturer_fname', 'lecturer_lname'], "lecturer", "lecturer_id", i)
            professorsList [i] [0] = session.selectOnCondition(["lecturer_title"], "lecturer", "lecturer_id", i + 1)
            print(i)
            print(professorsList[i][0])
            professorsList [i] [1] = session.selectOnCondition(["lecturer_fname"], 'lecturer', 'lecturer_id', i + 1)
            professorsList [i] [2] = session.selectOnCondition(["lecturer_lname"], 'lecturer', 'lecturer_id', i + 1)
            professorsList [i] [3] = session.selectOnCondition(["lecturer_modules"], 'lecturer', 'lecturer_id', i + 1)
            professorsList [i] [4] = session.selectOnCondition(["lecturer_availability"], 'lecturer', 'lecturer_id', i + 1)
        
        print(professorsList)
        print()

        return professorsList


#declare variables
modName = []
lecHours = []
practHours = []
tutHours = []
studentsEnrolled = []
roomsList = []
professorsList = []
modules_list = []
#tidy variables/arrays
modsCompleted = []


module = Module()


def fillRoomLists(session):
    # finds the number of entries in the room list table
    session.count_db_entries("room", "room_id")[0]
    length = session.dbCursor.fetchone()[0]
    print(f"Room: {length}")   

    roomsList = [[None for _ in range(4)] for _ in range(length)]

    for i in range (0, length):
        roomsList [i] [0] = session.selectOnCondition(["room_name"], 'room', 'room_id', i+1)
        roomsList [i] [1] = session.selectOnCondition(["room_capacity"], 'room', 'room_id', i+1)
        roomsList [i] [2] = session.selectOnCondition(["building_id"], 'room', 'room_id', i+1)
        roomsList [i] [3] = session.selectOnCondition(["room_type"], 'room', 'room_id', i+1)


def fillProfessorsLists(session):
    # finds the number of entries in the lecturer list table
    session.count_db_entries("lecturer", "lecturer_id")
    length = session.dbCursor.fetchone()[0]
    print(f"Lecturer: {length}")

    professorsList = [[None for _ in range(5)] for _ in range(length)]

    #professorsList = [[] for _ in range(length + 1)]

    for i in range (length):
        #professorsList [i] [0] = session.selectOnCondition(["lecturer_title", 'lecturer_fname', 'lecturer_lname'], "lecturer", "lecturer_id", i)
        professorsList [i] [0] = session.selectOnCondition(["lecturer_title"], "lecturer", "lecturer_id", i + 1)
        print(i)
        print(professorsList[i][0])
        professorsList [i] [1] = session.selectOnCondition(["lecturer_fname"], 'lecturer', 'lecturer_id', i + 1)
        professorsList [i] [2] = session.selectOnCondition(["lecturer_lname"], 'lecturer', 'lecturer_id', i + 1)
        professorsList [i] [3] = session.selectOnCondition(["lecturer_modules"], 'lecturer', 'lecturer_id', i + 1)
        professorsList [i] [4] = session.selectOnCondition(["lecturer_availability"], 'lecturer', 'lecturer_id', i + 1)
    
    print(professorsList)
    print()

    return professorsList



def createModuleClasses():
    print("Hello")

    modules_list = [len (modName)]

    print(len(modName))

    for i in range(0, len(modName)):
        print(f"Mod_name(i): {modName[i]}")
        mod_name = modName[i]
        print(f"Mod_name: {mod_name}")
        lectureHours = lecHours[i]
        pract_hours = practHours[i]
        tutorialHours = tutHours[i]
        students_enrolled = studentsEnrolled[i]

        new_module = Module(mod_name, 
                            lectureHours, 
                            pract_hours, 
                            tutorialHours, 
                            students_enrolled, 
                           )
        
        modules_list.append(new_module)

        print(f"createModuleClasses {modules_list}") 


def determineAvailableProfessors(
    module_info, 
    availableProfessors, 
    randDay, 
    randHour):

    #makes sure the correct index for professor availability is selected
    index = (9*randDay) + randHour

    for i in range(0, len(professorsList)):
        if (module_info.modName in professorsList [i][3]) and (
            professorTimetable [i] [randDay] [randHour] is None) and (
            professorsList [i][4][index] == '0'):

            availableProfessors.append(
                [professorsList[i][0], 
                 professorsList[i][1], 
                 professorsList[i][2]])

    return availableProfessors


def checkConstraints(
    module_info, type, 
    randPotentialRoom, 
    studentsUnassigned, 
    room):

    # continue generating new practicals until all students have been assigned 
    #   a practical if need be
    while studentsUnassigned > 0: 
        # 5 days, 9 hour slots
        randDay = random.randint(0, 4) 
        randHour = random.randint(0, 8)
        availableProfessors = []
        randProfessors = []
        chosenProfessors = []

        if timetableEntries [randDay] [randHour] [randPotentialRoom] is None:
            # finds which professors who teach the module can teach at 
            #   the specific time.
            availableProfessors = determineAvailableProfessors(
                module_info, 
                availableProfessors, 
                randDay, 
                randHour)

            if len(availableProfessors) == 0:
                return False
            
            else:
                # generate a random number x amount of times where x is the 
                #   number of professors required to take each practical
                # this will be used to pick one or more of the professors who 
                #   are available at this time
                for i in range(module_info.hoursRequiredForPract):
                    randProfessors.append(
                        random.randint(0, len(availableProfessors) - 1))
                    
                    chosenProfessors.append(
                        availableProfessors[randProfessors[i]])

                #populate the timetableEntry at the randDay randHour index
                timetableEntries[randDay][randHour][randPotentialRoom] = (
                    [module_info.modName, type, chosenProfessors, room])


                # reduce the number of studentUnassigned to reflect the session 
                #   just generated
                studentsUnassigned = studentsUnassigned - room [2] 
                
        else:
            return False
        
    return True
    


def insertIntoTimetable(module_info, modType):
    room = ""
    studentsUnassigned = module_info.studentsEnrolled
    moduleInserted = False

    while not moduleInserted:
        correctRoomType = False

        while not correctRoomType:
            randPotentialRoom = random.randint(0, len(roomsList) - 1)

            # checks that the room is the correct modType for the sessions being 
            #   assigned to
            if roomsList[randPotentialRoom] [3] == modType:
                room = roomsList[randPotentialRoom]
                correctRoomType = True 

        # inserts the requirements of the module into the timetable
        moduleInserted = checkConstraints(
        module_info, 
        modType, 
        randPotentialRoom, 
        studentsUnassigned, 
        room)


def displayTimetable():
    for i in range(len(timetableEntries)):
        for j in range(len(timetableEntries[i])):
            for k in range(len(timetableEntries[i][j])):
                if timetableEntries [i] [j] [k] is not None:
                    print(f"Value at ({i}, {j}, {k}): {timetableEntries [i] [j] [k]}")

                    #i represents days [0-4], [0] = Monday, [1] = Tuesday, etc
                    #j represents days [0-4], []


def importFromDatabase(session):

    module.fillModuleLists(Module, session, modules_list)
    #fillRoomLists(session)
    fillProfessorsLists(session)

    return modules_list

def main():
    #declare variables
    modulesCompleted = []
    session = dbManager()

    importFromDatabase(session)

    #create class for the module which takes in mod information.
    modules_list = createModuleClasses() 

    print(f"Modules list: {modules_list}")

    for i in range(numOfModules):
        #displayTimetable()

        moduleInserted = False 

        while moduleInserted == False:
            randMod = random.randint(0, numOfModules-1) 

            if randMod not in modulesCompleted:
                if modules_list[randMod].lecHours > 0:
                    for i in range(lecHours [randMod]):
                        insertIntoTimetable(modules_list[randMod], 'lec')

                if modules_list[randMod].practHours > 0:
                    for i in range(practHours [randMod]):
                        insertIntoTimetable(modules_list[randMod], 'pract')

                if modules_list[randMod].tutHours > 0:
                    for i in range(tutHours [randMod]):
                        insertIntoTimetable(modules_list[randMod], 'tut')

                moduleInserted = True
            
        #adds to this array to ensure the same module does not get added to the 
        #   timetable again.
        modulesCompleted.append(randMod) 

    session.dbClose()

    displayTimetable()

main()