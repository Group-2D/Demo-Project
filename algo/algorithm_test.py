#  TEMP RULES:
#  All practs for a module will be in the same room.

# how do we associate one professor with the lecture and more than one with the practicals?
# how to make professors unavailable once they have been assigned to a lecture
# how to end the program if not spaces or availabilities can be found

import random

# maximum of 5 days, 9 hour slots, 12 rooms; format days, hour slots, rooms
timetableEntries = [
    [[None for _ in range(8)] for _ in range(9)] for _ in range(5)]
professorTimetable = [
    [[None for _ in range(9)] for _ in range(5)] for _ in range(7)]
numOfModules = 6


modules_list = []
modName = ["Architecture & Operating Systems", 
           "Comp Tutorial 4", 
           "Core Computing Concepts", 
           "Database Systems Development", 
           "Networks", 
           "Programming"]

lecHours = [1, 0, 1, 1, 1, 1] 
practHours = [2, 0, 1, 2, 1, 2] 
tutHours = [0, 1, 0, 0, 0, 0]
studentsEnrolled = [200, 200, 200, 200, 200, 150]
hoursRequiredForPract = [1, 1, 1, 1, 1, 1]


roomsList = [["A2.03", "Anglesea", 40, "pract"],
            ["FTC_Floor1", "Future Technology Centre", 80, "pract"], 
            ["FTC_Floor2", "Future Technology Centre", 80, "pract"], 
            ["FTC_Floor1", "Future Technology Centre", 50, "tut"],
            ["L0.14a", "LionGate", 67, "tut"],
            ["RLT1", "Richmond Building", 330, "lec"], 
            ["RLT2", "Richmond Building", 160, "lec"], 
            ["R1.03", "Richmond Building", 24, "pract"]]


professorsList = [['Dr', 
                  'John',
                  'Smith', 
                  'Architecture & Operating Systems, Comp Tutorial 4', 
                  '000000100000000100000000100000000100000000100'],
                ['Dr', 
                 'Lisa',
                 'Franklin', 
                 'Core Computing Concepts', 
                 '000000000000000000000000000000000000000000000'],
                ['Dr', 
                 'Herbert',
                 'Jones', 
                 'Core Computing Concepts', 
                 '000000000000000000000000000000000000000000000'],
                ['Dr', 
                 'Richard',
                 'Johnson', 
                 'Database Systems Development', 
                 '000010000000000010000000000000010000000000000'],
                ['Dr', 
                 'Hugh',
                 'Piper',
                 'Programming', 
                 '000000000000000000000000000000000000000000000'],
                ['Dr',
                 'Javier',
                 'Rodriguez', 
                 'Networks', 
                 '000000000000000000000000000000000000000000000'],
                ['Dr', 
                 'Kathlyn',
                 'Ferguson', 
                 'Networks', 
                 '000000000000001000000000000100000000000000001']]

#tidy variables/arrays
modsCompleted = []


class Module:
    def __init__(self, 
                 moduleName, 
                 lectureHours, 
                 practicalHours, 
                 tutorialHours, 
                 students_enrolled, 
                 hours_required_for_pract):
        
        self.modName = moduleName
        self.lecHours = lectureHours
        self.practHours = practicalHours
        self.tutHours = tutorialHours
        self.studentsEnrolled = students_enrolled
        self.hoursRequiredForPract = hours_required_for_pract


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



def createModuleClasses():
    for i in range(0, len(modName)):
        mod_name = modName[i]
        lectureHours = lecHours[i]
        pract_hours = practHours[i]
        tutorialHours = tutHours[i]
        students_enrolled = studentsEnrolled[i]
        hours_required_for_pract = hoursRequiredForPract [i]

        new_module = Module(mod_name, 
                            lectureHours, 
                            pract_hours, 
                            tutorialHours, 
                            students_enrolled, 
                            hours_required_for_pract)
        
        modules_list.append(new_module)


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


def main():
    #declare variables
    modulesCompleted = []

    #create class for the module which takes in mod information.
    createModuleClasses() 

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

    displayTimetable()