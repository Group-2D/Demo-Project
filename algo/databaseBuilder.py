### File is used to build the Postgres SQL ###
from typing import Any

def buildDatabaseSchema(dbCursor: Any) -> None:     
        """
        Used to build the database

        Parameters
        ----------
        dbCursor: any
            a function used to make changes to the database
        dbCommit: any
            a function used to commit data to the database

        Returns 
        -------
        None
        """
        dbCursor.execute(
            """
            CREATE TABLE IF NOT EXISTS modules(
                mod_id SERIAL PRIMARY KEY,
                mod_name VARCHAR(40) NOT NULL, 
                mod_enrolled INT NOT NULL,
                mod_lectures INT NOT NULL,
                mod_practicals INT NOT NULL,
                mod_tutorials INT NOT NULL,
                mod_prof_req INT NOT NULL
            );
            
            CREATE TABLE IF NOT EXISTS lecturer(
                lecturer_id SERIAL PRIMARY KEY,
                lecturer_title VARCHAR(4) NOT NULL,
                lecturer_fname VARCHAR(20) NOT NULL,
                lecturer_lname VARCHAR(20) NOT NULL,
                lecturer_modules VARCHAR(200) NOT NULL,
                lecturer_availability VARCHAR(100) NOT NULL
            );

            CREATE TABLE IF NOT EXISTS building(
                building_id SERIAL PRIMARY KEY,
                building_name VARCHAR(50)
            );

            CREATE TABLE IF NOT EXISTS room(
                room_id SERIAL PRIMARY KEY,
                room_name VARCHAR(30),
                room_capacity INT NOT NULL,
                building_id INT NOT NULL REFERENCES building(building_id)
            );

            CREATE TABLE IF NOT EXISTS lecture(
                lecuture_id SERIAL PRIMARY KEY,
                mod_id INT NOT NULL REFERENCES modules(mod_id),
                room_id INT NOT NULL REFERENCES room(room_id),
                lecturer_id INT NOT NULL REFERENCES lecturer(lecturer_id),
                lecturer_start DECIMAL, 
                lecturer_end DECIMAL
            );
            """
        )

        return 

def insertDataToDb(dbCursor: Any):
    """
    Used to build the database

    Parameters
    ----------
    dbCursor: any
        a function used to make changes to the database
    dbCommit: any
        a function used to commit data to the database

    Returns 
    -------
    None
    """
    dbCursor.execute(
          """
            INSERT INTO modules (mod_name, mod_enrolled, mod_lectures, mod_practicals, mod_tutorials, mod_prof_req)
            VALUES
                ('Architecture & Operating Systems', 200, 1, 2, 0, 1),
                ('Comp Tutorial 4', 200, 0, 0, 1, 1),
                ('Core Computing Concepts', 200, 1, 1, 0, 1),
                ('Database Systems Development', 200, 1, 2, 0, 1),
                ('Networks', 200, 1, 1, 0, 1),
                ('Programming', 150, 1, 2, 0, 1);

            INSERT INTO building (building_name) VALUES
            ('Anglesea'),
            ('Liongate'),
            ('Park'),
            ('Richmond'),
            ('Future Technology Centre') ;

            
            INSERT INTO lecturer (lecturer_title, lecturer_fname, lecturer_lname, lecturer_modules, lecturer_availability) VALUES
            ('Miss', 'Taylor', 'Swift', 'Architecture & Operating Systems', '000000000000000001000000001000000001000000001'),
            ('Mr','Adam', 'Levine', 'Networks', '000010010010000100001000001100000000000010000'),
            ('Mr', 'Lewis', 'Capaldi', 'Programming', '000000000000000000000000000000000000000000000'),
            ('Miss', 'Katy', 'Perry', 'Programming', '000000000000000000000000000000000000000000000'),
            ('Dr', 'John', 'Smith', 'Architecture & Operating Systems, Programming, Comp Tutorial 4', '000000100000000100000000100000000100000000100'),
            ('Dr', 'Lisa', 'Franklin', 'Core Computing Concepts', '000000000000000000000000000000000000000000000'),
            ('Dr', 'Herbert', 'Jones', 'Core Computing Concepts', '000000000000000000000000000000000000000000000'),
            ('Dr', 'Richard', 'Johnson', 'Database Systems Development', '000010000000000010000000000000010000000000000'),
            ('Dr', 'Hugh', 'Piper', 'Programming', '000000000000000000000000000000000000000000000'),
            ('Dr', 'Javier', 'Rodriguez', 'Networks', '000000000000000000000000000000000000000000000'),
            ('Dr', 'Kathlyn', 'Ferguson', 'Networks', '000000000000001000000000000100000000000000001');
			 
			INSERT INTO room (room_name, room_capacity, building_id) VALUES
            ('A2.03', 40, 1),
            ('FTC_Floor1', 80, 5), 
            ('FTC_Floor2', 80, 5), 
            ('FTC_Floor1', 50, 5),
            ('L0.14a', 67, 2),
            ('RLT1', 330, 4), 
            ('RLT2', 160, 4), 
            ('R1.03', 24, 4) ;
        """)
    return

# modules_list = []
# modName = ["Architecture & Operating Systems", 
#            "Comp Tutorial 4", 
#            "Core Computing Concepts", 
#            "Database Systems Development", 
#            "Networks", 
#            "Programming"]

# lecHours = [1, 0, 1, 1, 1, 1] 
# practHours = [2, 0, 1, 2, 1, 2] 
# tutHours = [0, 1, 0, 0, 0, 0]
# studentsEnrolled = [200, 200, 200, 200, 200, 150]
# hoursRequiredForPract = [1, 1, 1, 1, 1, 1]


# roomsList = [["A2.03", "Anglesea", 40, "pract"],
#             ["FTC_Floor1", "Future Technology Centre", 80, "pract"], 
#             ["FTC_Floor2", "Future Technology Centre", 80, "pract"], 
#             ["FTC_Floor1", "Future Technology Centre", 50, "tut"],
#             ["L0.14a", "LionGate", 67, "tut"],
#             ["RLT1", "Richmond Building", 330, "lec"], 
#             ["RLT2", "Richmond Building", 160, "lec"], 
#             ["R1.03", "Richmond Building", 24, "pract"]]


# professorsList = [['Dr', 
#                   'John',
#                   'Smith', 
#                   'Architecture & Operating Systems, Comp Tutorial 4', 
#                   '000000100000000100000000100000000100000000100'],
#                 ['Dr', 
#                  'Lisa',
#                  'Franklin', 
#                  'Core Computing Concepts', 
#                  '000000000000000000000000000000000000000000000'],
#                 ['Dr', 
#                  'Herbert',
#                  'Jones', 
#                  'Core Computing Concepts', 
#                  '000000000000000000000000000000000000000000000'],
#                 ['Dr', 
#                  'Richard',
#                  'Johnson', 
#                  'Database Systems Development', 
#                  '000010000000000010000000000000010000000000000'],
#                 ['Dr', 
#                  'Hugh',
#                  'Piper',
#                  'Programming', 
#                  '000000000000000000000000000000000000000000000'],
#                 ['Dr',
#                  'Javier',
#                  'Rodriguez', 
#                  'Networks', 
#                  '000000000000000000000000000000000000000000000'],
#                 ['Dr', 
#                  'Kathlyn',
#                  'Ferguson', 
#                  'Networks', 
#                  '000000000000001000000000000100000000000000001']]