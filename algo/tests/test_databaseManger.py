import unittest
# ! anyone know how to solve import issues from files in a differnt folder
from algo.databaseManger import dbManger

class TestDatabasseManger(unittest.TestCase):

    #used to setup repeated values in testing
    @classmethod
    def setUpClass(cls) -> None:
        #creates a singular session to test each method in the class 
        session = dbManger()
        
        # Creating test data to run automated tests on the class and methods
        session.dbCursor.execute(
            """
            INSERT INTO IF NOT EXSISTS lecturers (lecturer_fname, lecturer_lname, lecturer_availability) VALUES
            ('Taylor', 'Swift', 'EX001'),
            ('Adam', 'Levine', 'EX003'),
            ('Lewis', 'Capaldi', 'EX009'),
            ('Katy', 'Perry', 'EX001'); 
            
            INSERT INTO IF NOT EXSISTS building (building_name) VALUES
            ('Angelesea'),
            ('Liongate'),
            ('Park'),
            ('Richmond');
            """
        )

        session.dbConnection.commit()

        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()
    
    #used to setup and tear down tests once completed 

    def setUp(self) -> None:
        self.session = dbManger()
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()
    

    def test_selectAll(self):
        """
        tests all the primmitive cases for the method
        """

        result = self.session.selectAll('lecturer')
        expected = [
            ('Taylor', 'Swift', 'EX001'),
            ('Adam', 'Levine', 'EX003'),
            ('Lewis', 'Capaldi', 'EX009'),
            ('Katy', 'Perry', 'EX001')
            ]
        
        #runs the test
        self.assertEquals(result, expected)