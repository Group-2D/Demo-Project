#  TEMP RULES:
#  All practs for a module will be in the same room.

# how do we associate a professor with a lecture and multiple with the 
#   practicals?
# how to make professors unavailable once they have been assigned to a lecture
# how to end the program if not spaces or availabilities can be found

import copy
import random

# maximum of 5 days, 9 hour slots, 12 rooms; format days, hour slots, rooms
timetableEntries = [
    [[None for _ in range(8)] for _ in range(9)] for _ in range(5)]
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
                 'Core Computing Concepts, Comp Tutorial 4', 
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


newTimetableEntries = []
dayList = ["MON",
           "TUE",
           "WED",
           "THU",
           "FRI"]

class Module:
    def __init__(self, 
                 moduleName, 
                 lectureHours, 
                 practicalHours, 
                 tutorialHours, 
                 students_enrolled, 
                 hoursRequiredForPract):
        
        self.modName = moduleName

        self.lecHours = lectureHours
        self.practHours = practicalHours
        self.tutHours = tutorialHours
        self.studentsEnrolled = students_enrolled
        self.hoursRequiredForPract = hoursRequiredForPract

        self.room = ""
        self.day = ""
        self.time = 0
        self.professors = []
        self.classType = ""

    def __str__(self) -> str:
        
        mystring = f"""Module Name: {self.modName}
On: {self.day} at: {self.time} in room: {self.room}
Professors: {self.professors}
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


def createModuleClasses():
    for i in range(0, len(modName)):

        # temp code that pulls module information from temp lists
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

    # #makes sure the correct index for professor availability is selected
    # index = (9*randDay) + randHour

    if len(newTimetableEntries) == 0:
        for i in range(0, len(professorsList)):
            if (module_info.modName in professorsList [i][3]):
                availableProfessors.append(
                    [professorsList[i][0], 
                    professorsList[i][1], 
                    professorsList[i][2]])

    else:

        for i in range(0, len(professorsList)):
            for checkModule in newTimetableEntries:
                if ([professorsList[i][0], 
                     professorsList[i][1], 
                     professorsList[i][2]]) in checkModule.professors and checkModule.day == randDay and checkModule.time == randHour:
                        pass

                else:
                    availableProfessors.append(
                        [professorsList[i][0], 
                        professorsList[i][1], 
                        professorsList[i][2]])

    return availableProfessors



def checkProfessorAvailability(checkTime,
                               checkDay,
                               module_info):
    
    timeSlotBit = checkTime * dayList.index(checkDay)
    availableProfessors = []

    for checkProfessor in professorsList:
        if module_info.modName in checkProfessor[3]:
            if int((checkProfessor[4])[timeSlotBit]) == 0:
                availableProfessors.append(checkProfessor[2])

    return availableProfessors


def checkConstraints(
    module_info, 
    classType, 
    randPotentialRoom, 
    studentsUnassigned, 
    room):

    # continue generating new practicals until all students have been assigned 
    #   a practical if need be
    while studentsUnassigned > 0: 
        randDay = random.choice(dayList)
        randHour = random.randint(0, 8)
        randProfessors = []
        chosenProfessors = []
        # print("C")

        unavailable = False

        for checkModule in newTimetableEntries:
            if checkModule.day == randDay and checkModule.time == randHour and checkModule.room == randPotentialRoom:
                unavailable = True

        if unavailable == False: 
            availableProfessors = checkProfessorAvailability(randHour,
                                                             randDay,
                                                             module_info)

            if len(availableProfessors) == 0:
                return False
            
            else:
                # generate a random number x amount of times where x is the 
                #   number of professors required to take each practical
                # this will be used to pick one or more of the professors who 
                #   are available at this time
                for i in range(module_info.hoursRequiredForPract):
                    chosenProfessors.append(random.choice(availableProfessors))
            
                entryModule = copy.deepcopy(module_info)

                entryModule.day = randDay
                entryModule.time = randHour
                entryModule.room = randPotentialRoom
                entryModule.professors = chosenProfessors
                entryModule.classType = classType

                newTimetableEntries.append(entryModule)

                studentsUnassigned = studentsUnassigned - room [2] 

    return True
    


def insertIntoTimetable(module_info, modType):
    room = ""
    studentsUnassigned = module_info.studentsEnrolled
    moduleInserted = False

    while not moduleInserted:
        correctRoomType = False
        # print(newTimetableEntries)

        while not correctRoomType:
            randPotentialRoom = random.randint(0, len(roomsList) - 1)

            # checks that the room is the correct modType for the sessions being 
            #   assigned to
            if roomsList[randPotentialRoom] [3] == modType:
                room = roomsList[randPotentialRoom]
                correctRoomType = True 

        # inserts the requirements of the module into the timetable
        moduleInserted = checkConstraints(module_info,
                                          modType, 
                                          randPotentialRoom, 
                                          studentsUnassigned, 
                                          room)


def displayTimetable():
    for lesson in newTimetableEntries:

        print(lesson)


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

main()