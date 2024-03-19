#  TEMP RULES:
#  All practs for a module will be in the same room.

# how do we associate one lecturer with the lecture and more than one with the practicals?
# how to make lecturers unavailable once they have been assigned to a lecture
# how to end the program if not spaces or availabilities can be found


#############################################################
#                                                            #
#      CHECK WHY PROGRAM IS SAYING LECTURERS UNAVAILABLE     #
#                                                            #
#############################################################


import random
from .databaseManger import selectOnCondition

#global variables

# maximum of 5 days, 9 hour slots, 12 rooms
timetableEntries = [[[None for _ in range(8)] for _ in range(9)] for _ in range(5)] #days, hour slots, rooms
lecturerTimetable = [[[None for _ in range(9)] for _ in range(5)] for _ in range(7)] #days, hour slots, rooms
numOfModules = 6

# modules variables
modules_list = []
modName = ["Architecture & Operating Systems", "Comp Tutorial 4", "Core Computing Concepts", "Database Systems Development", "Networks", "Programming"]
lecHours = [1, 0, 1, 1, 1, 1] 
practHours = [2, 0, 1, 2, 1, 2] 
tutHours = [0, 1, 0, 0, 0, 0]
studentsEnrolled = [200, 200, 200, 200, 200, 150]
hoursRequiredForPract = [1, 1, 1, 1, 1, 1]

# rooms variables
#room name, building name, capacity, type
roomsList = [
                ["A2.03", "Anglesea", 40, "pract"],
                ["FTC_Floor1", "FutureTechnologyCentre", 80, "pract"], ["FTC_Floor2", "FutureTechnologyCentre", 80, "pract"], ["FTC_Floor1", "FutureTechnologyCentre", 50, "tut"],
                ["L0.14a", "LionGate", 67, "tut"],
                ["RLT1", "Richmond Building", 330, "lec"], ["RLT2", "Richmond Building", 160, "lec"], ["R1.03", "Richmond Building", 24, "pract"],
            ]

# lecturer variables
lecturersList = [
                    ['Dr', 'John','Smith', 'Architecture & Operating Systems, Programming, Comp Tutorial 4', '000000100000000100000000100000000100000000100'], #000000100 000000100 000000100 000000100 000000100
                    ['Dr', 'Lisa','Franklin', 'Core Computing Concepts', '000000000000000000000000000000000000000000000'], #000000000 000000000 000000000 000000000 000000000
                    ['Dr', 'Herbert','Jones', 'Core Computing Concepts', '000000000000000000000000000000000000000000000'], #000000000 000000000 000000000 000000000 000000000
                    ['Dr', 'Richard','Johnson', 'Database Systems Development', '000010000000000010000000000000010000000000000'], #000010000 000000010 000000000 000010000 000000000
                    ['Dr', 'Hugh','Piper','Programming', '000000000000000000000000000000000000000000000'], #000000000 000000000 000000000 000000000 000000000
                    ['Dr', 'Javier','Rodriguez', 'Networks', '000000000000000000000000000000000000000000000'], #000000000 000000000 000000000 000000000 000000000
                    ['Dr', 'Kathlyn','Ferguson', 'Networks', '000000000000001000000000000100000000000000001'] #000000000 000001000 000000000 100000000 000000001
                ]

#tidy variables/arrays
modsCompleted = []

class ModuleInfo:
    def __init__(self, mod_name, lec_hours, pract_hours, tut_hours, students_enrolled, hours_required_for_pract):
        self.modName = mod_name
        self.lecHours = lec_hours
        self.practHours = pract_hours
        self.tutHours = tut_hours
        self.studentsEnrolled = students_enrolled
        self.hoursRequiredForPract = hours_required_for_pract
        
class Room:
    def __init__(self, room_name, building, room_type, capacity):
        self.roomName = room_name
        self.buildingName = building
        self.roomType = room_type
        self.roomcapacity = capacity

class Lecturer:
    def __init__(self, lecturer_name, modules):
        self.lecturerName = lecturer_name
        self.modulesTaught = modules



def createModuleClasses():
    for i in range(0, len(modName)):
        mod_name = modName[i]
        lec_hours = lecHours[i]
        pract_hours = practHours[i]
        tut_hours = tutHours[i]
        students_enrolled = studentsEnrolled[i]
        hours_required_for_pract = hoursRequiredForPract [i]

        new_module = ModuleInfo(mod_name, lec_hours, pract_hours, tut_hours, students_enrolled, hours_required_for_pract)
        modules_list.append(new_module)


def determineAvailableLecturers(module_info, availableLecturers, randDay, randHour):
    #makes sure the correct index for lecturer availability is selected
    index = (9*randDay) + randHour

    #print(f"randDay {randDay}, randHour {randHour}, index: {index}")

    for i in range(0, len(lecturersList)):
        if module_info.modName in lecturersList [i][3] and lecturerTimetable [i] [randDay] [randHour] is None and lecturersList [i][4][index] == '0' :
            #print(f"Lecturer {lecturersList [i][0]} {lecturersList [i][1]} {lecturersList [i][2]}")
            availableLecturers.append([lecturersList[i][0], lecturersList[i][1], lecturersList[i][2]])

    return availableLecturers


def checkConstraints(module_info, type, randPotentialRoom, studentsUnassigned, room):
    while studentsUnassigned > 0: #continue generating new practicals until all students have been assigned a practical if need be
        # 5 days, 9 hour slots
        randDay = random.randint(0, 4) 
        randHour = random.randint(0, 8)
        availableLecturers = []
        randLecturers = []
        chosenLecturers = []

        if timetableEntries [randDay] [randHour] [randPotentialRoom] is None:
            #finds which lecturers who teach the module can teach at the specific time.
            availableLecturers = determineAvailableLecturers(module_info, availableLecturers, randDay, randHour)
            #print(f"available lecturers: {availableLecturers}")

            #time.sleep(100)

            if len(availableLecturers) == 0:
                print("No lecturers available")

                return False
            else:
                #generate a random number x amount of times where x is the number of lecturers required to take each practical
                #this will be used to pick one or more of the lecturers who are available at this time
                for i in range(module_info.hoursRequiredForPract):
                    randLecturers.append(random.randint(0, len(availableLecturers) - 1))
                    #print(f"Random lecs [i]: {randLecturers[i]}")
                    chosenLecturers.append(availableLecturers[randLecturers[i]])
                    #print(f"Chosen lecturers [i]: {chosenLecturers [i]}")

                #populate the timetableEntry at the randDay randHour index
                timetableEntries[randDay][randHour][randPotentialRoom] = [module_info.modName, type, chosenLecturers, room]
                #print(f"TimetableEntries {randDay} {randHour} {randPotentialRoom} = ModuleName = {module_info.modName}, type = {type}, chosenLecturers = {chosenLecturers}, room = {room}")

                #reduce the number of studentUnassigned to reflect the session just generated
                studentsUnassigned = studentsUnassigned - room [2] 
                
                #print(f"Students unassigned: {studentsUnassigned} ")     
            print("Session inserted")
        else:
            print("No availability for this time for this room.")

            return False
    return True
    


def insertIntoTimetable(module_info, type):
    room = ""
    studentsUnassigned = module_info.studentsEnrolled
    moduleInserted = False

    #print(f"{module_info.modName} {type}") 

    while not moduleInserted:
        correctRoomType = False

        while not correctRoomType:
            randPotentialRoom = random.randint(0, len(roomsList) - 1)

            #checks that the room is the correct type for the sessions being assigned to
            if roomsList[randPotentialRoom] [3] == type:
                room = roomsList[randPotentialRoom]
                correctRoomType = True 

        #inserts the requirements of the module into the timetable
        moduleInserted = checkConstraints(module_info, type, randPotentialRoom, studentsUnassigned, room)

    print("Module insertion completed")

    #time.sleep(10)

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
            
        #adds to this array to ensure the same module does not get added to the timetable again.
        modulesCompleted.append(randMod) 

    #test print
    displayTimetable()
