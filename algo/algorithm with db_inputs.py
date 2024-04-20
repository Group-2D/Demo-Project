import random
import time
from databaseManager import * 

# maximum of 5 days, 9 hour slots, 12 rooms; format days, hour slots, rooms
timetableEntries = [
    [[None for _ in range(8)] for _ in range(9)] for _ in range(5)]
professorTimetable = []
numOfModules = 6


#declare variables
modName = []
lecHours = []
practHours = []
tutHours = []
studentsEnrolled = []
profRequired = []



################################################################################################################################################################
#                    READING IN FROM DB
################################################################################################################################################################

class Module:
    def __init__(self, 
                 moduleName, 
                 lectureHours, 
                 practicalHours, 
                 tutorialHours, 
                 students_enrolled, 
                 moduleProfessorsRequired):
        
        self.modName = moduleName
        self.lecHours = lectureHours
        self.practHours = practicalHours
        self.tutHours = tutorialHours
        self.studentsEnrolled = students_enrolled
        self.profRequired = moduleProfessorsRequired

    def __str__(self):
        return f"Module: {self.modName}, Lecture Hours: {self.lecHours}, Practical Hours: {self.practHours}, Tutorial Hours: {self.tutHours}, Students Enrolled: {self.studentsEnrolled}"
    

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



def createModuleClasses(modules_list, modName, lecHours, practHours, studentsEnrolled, profRequired):
    #   Puts all the values collected from the database into a class.

    for i in range(0, len(modName)):
        mod_name = modName[i]
        lectureHours = lecHours[i]
        pract_hours = practHours[i]
        tutorialHours = tutHours[i]
        students_enrolled = studentsEnrolled[i]
        prof_required = profRequired[i]

        new_module = Module(mod_name, 
                            lectureHours, 
                            pract_hours, 
                            tutorialHours, 
                            students_enrolled, 
                            prof_required
                           )
        
        modules_list.append(new_module)

    return modules_list


def fillModuleLists(session, modules_list):
    # finds the number of entries in the module list table                                                           
    session.count_db_entries("modules", "mod_id")
    length = session.dbCursor.fetchone()[0]
    #print(f"Module: {length}") 

    for i in range(0, length):
        modName.append(str(session.selectOnCondition(["mod_name"], "modules", "mod_id", i+1))[2:-3])
        studentsEnrolled.append(int(session.selectOnCondition(["mod_enrolled"], "modules", "mod_id", i + 1)[0]))
        lecHours.append(int(session.selectOnCondition(["mod_lectures"], "modules", "mod_id", i+1)[0]))
        practHours.append(int(session.selectOnCondition(["mod_practicals"], "modules", "mod_id", i+1)[0]))
        tutHours.append(int(session.selectOnCondition(["mod_tutorials"], "modules", "mod_id", i+1)[0]))
        profRequired.append(int(session.selectOnCondition(["mod_prof_req"], "modules", "mod_id", i+1)[0]))

    modules_list = createModuleClasses(modules_list, modName, lecHours, practHours, studentsEnrolled, profRequired)
    
    return modules_list


def fillRoomLists(session, roomsList):
    # finds the number of entries in the room list table
    session.count_db_entries("room", "room_id")
    length = session.dbCursor.fetchone()[0]

    # Defines the length of the room list array based on the number of entries in the "room" table
    roomsList = [[None for _ in range(4)] for _ in range(length)]

    for i in range (0, length):
        roomsList [i] [0] = str(session.selectOnCondition(["room_name"], 'room', 'room_id', i+1))[2:-3]
        roomsList [i] [1] = int(session.selectOnCondition(["room_capacity"], 'room', 'room_id', i+1)[0])
        roomsList [i] [2] = session.selectOnCondition(["building_id"], 'room', 'room_id', i+1)

    return roomsList


def fillProfessorsLists(session, professorsList):
    # finds the number of entries in the lecturer list table
    session.count_db_entries("lecturer", "lecturer_id")
    length = session.dbCursor.fetchone()[0]
    #print(f"Lecturer: {length}")

    # Determines the length of the professor list based on the number of entries in the 'lecturer' table
    professorsList = [[None for _ in range(5)] for _ in range(length)]

    for i in range (length):
        professorsList [i] [0] = str(session.selectOnCondition(["lecturer_title"], "lecturer", "lecturer_id", i + 1))[2:-3]
        professorsList [i] [1] = str(session.selectOnCondition(["lecturer_fname"], 'lecturer', 'lecturer_id', i + 1))[2:-3]
        professorsList [i] [2] = str(session.selectOnCondition(["lecturer_lname"], 'lecturer', 'lecturer_id', i + 1))[2:-3]
        professorsList [i] [3] = str(session.selectOnCondition(["lecturer_modules"], 'lecturer', 'lecturer_id', i + 1))[2:-3]
        professorsList[i] [4] = str(session.selectOnCondition(["lecturer_availability"], 'lecturer', 'lecturer_id', i + 1))[2:-3]

    return professorsList, length



def importFromDatabase(session, modules_list, rooms_list, professors_list, profLength):
    modules_list = fillModuleLists(session, modules_list)
    rooms_list = fillRoomLists(session, rooms_list)
    professors_list, profLength = fillProfessorsLists(session, professors_list)

    return modules_list, rooms_list, professors_list, profLength





################################################################################################################################################################
#                    ALGORITHM
################################################################################################################################################################


def determineAvailableProfessors(
    module_info, 
    availableProfessors, 
    randDay, 
    randHour, professorsList, professorTimetable):

    #makes sure the correct index for professor availability is selected
    index = (9*randDay) + randHour

    for i in range(len(professorsList)):

        if (module_info.modName in professorsList [i][3]) and (
            professorTimetable [i] [randDay] [randHour] is None) and (
            professorsList [i][4][index] == '0'):
            
            availableProfessors.append(
                [professorsList[i][0], 
                 professorsList[i][1], 
                 professorsList[i][2]])


    #time.sleep(50)

    return availableProfessors


def checkConstraints(
    module_info, type, 
    randPotentialRoom, 
    studentsUnassigned, 
    room, professors_list, prof_timetable):

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
                randHour, professors_list, prof_timetable)

            if len(availableProfessors) == 0:
                return False
            
            else:
                # generate a random number x amount of times where x is the 
                #   number of professors required to take each practical
                # this will be used to pick one or more of the professors who 
                #   are available at this time
                if (type == 'pract'):
                    for i in range(module_info.profRequired):
                        randProfessors.append(
                            random.randint(0, len(availableProfessors) - 1))
                        
                        chosenProfessors.append(
                            availableProfessors[randProfessors[i]])
                else: 
                    randProfessors.append(
                        random.randint(0, len(availableProfessors) - 1))
                        
                    chosenProfessors.append(
                        availableProfessors[randProfessors[0]])

                #populate the timetableEntry at the randDay randHour index
                timetableEntries[randDay][randHour][randPotentialRoom] = (
                    [module_info.modName, type, chosenProfessors, room])


                # reduce the number of studentUnassigned to reflect the session 
                #   just generated
                studentsUnassigned = studentsUnassigned - room [1] 
                
        else:
            return False
        
    return True
    


def insertIntoTimetable(module_info, modType, roomsList, professorsList, profTimetable):
    room = ""
    studentsUnassigned = module_info.studentsEnrolled
    moduleInserted = False

    while not moduleInserted:
        correctRoomType = False

        while not correctRoomType:
            randPotentialRoom = random.randint(0, len(roomsList) - 1)

            # checks that the room is the correct modType for the sessions being 
            #   assigned to
            if modType == 'lec' or modType == 'tut':
                if roomsList[randPotentialRoom][1] > 100:
                    room = roomsList[randPotentialRoom]
                    correctRoomType = True 
            else:
                if roomsList[randPotentialRoom][1] < 100:
                    room = roomsList[randPotentialRoom]
                    correctRoomType = True 

        

        # inserts the requirements of the module into the timetable
        moduleInserted = checkConstraints(
            module_info, 
            modType, 
            randPotentialRoom, 
            studentsUnassigned, 
            room, professorsList, profTimetable)


def main():
    #declare variables
    modulesCompleted = []
    session = dbManager()

    modules_list = []
    rooms_list = []
    professors_list = []
    profLength = 0

    modules_list, rooms_list, professors_list, profLength = importFromDatabase(session, modules_list, rooms_list, professors_list, profLength)

    professorTimetable = [[[None for _ in range(9)] for _ in range(5)] for _ in range(profLength)]

    for i in range(numOfModules):
        moduleInserted = False 

        while moduleInserted == False:
            randMod = random.randint(0, numOfModules-1) 

            if randMod not in modulesCompleted:
                if modules_list[randMod].lecHours > 0:
                    for i in range(lecHours [randMod]):
                        insertIntoTimetable(modules_list[randMod], 'lec', rooms_list, professors_list, professorTimetable)

                if modules_list[randMod].practHours > 0:
                    for i in range(practHours [randMod]):
                        insertIntoTimetable(modules_list[randMod], 'pract', rooms_list, professors_list, professorTimetable)

                if modules_list[randMod].tutHours > 0:
                    for i in range(tutHours [randMod]):
                        insertIntoTimetable(modules_list[randMod], 'tut', rooms_list, professors_list, professorTimetable)

                moduleInserted = True
            
        #adds to this array to ensure the same module does not get added to the 
        #   timetable again.
        modulesCompleted.append(randMod) 

    session.dbClose()

    displayTimetable()



def displayTimetable():
    for i in range(len(timetableEntries)):
        for j in range(len(timetableEntries[i])):
            for k in range(len(timetableEntries[i][j])):
                if timetableEntries [i] [j] [k] is not None:
                    print(f"Value at ({i}, {j}, {k}): {timetableEntries [i] [j] [k]}")

                    #i represents days [0-4], [0] = Monday, [1] = Tuesday, etc
                    #j represents days [0-4], []

main()