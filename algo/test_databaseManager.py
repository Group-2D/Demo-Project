import unittest
from databaseManager import dbManger

class TestDatabaseManger(unittest.TestCase):

    #used to setup repeated values in testing
    @classmethod
    def setUpClass(cls) -> None:
        #creates a singular session to test each method in the class 
        session = dbManger()
        # Creating test data to run automated tests on the class and methods
        session.dbCursor.execute(
            """
            INSERT INTO lecturer (lecturer_fname, lecturer_lname, lecturer_availability) VALUES
            ('Taylor', 'Swift', 'EX001'),
            ('Adam', 'Levine', 'EX003'),
            ('Lewis', 'Capaldi', 'EX009'),
            ('Katy', 'Perry', 'EX001'); 
            
            INSERT INTO building (building_name) VALUES
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


#driver function to run the unittests

if __name__ == '__main__':
    unittest.main()