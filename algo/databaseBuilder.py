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
                mod_tutorials INT NOT NULL
            );
            
            CREATE TABLE IF NOT EXISTS lecturer(
                lecturer_id SERIAL PRIMARY KEY,
                lecturer_fname VARCHAR(20) NOT NULL,
                lecturer_lname VARCHAR(20) NOT NUll,
                lecturer_availability VARCHAR(100)
            );

            CREATE TABLE IF NOT EXISTS building(
                building_id SERIAL PRIMARY KEY,
                building_name VARCHAR(20)
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
          """INSERT INTO building (building_name) VALUES
            ('Angelesea'),
            ('Liongate'),
            ('Park'),
            ('Richmond');
            
            INSERT INTO lecturer (lecturer_fname, lecturer_lname, lecturer_availability) VALUES
            ('Taylor', 'Swift', 'EX001'),
            ('Adam', 'Levine', 'EX003'),
            ('Lewis', 'Capaldi', 'EX009'),
            ('Katy', 'Perry', 'EX001');
        """)
    return