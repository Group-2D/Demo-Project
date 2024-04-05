import unittest
from databaseManager import dbManager


class Test_DbManager_SelectAll(unittest.TestCase):

    #set up and tear down functions
    def setUp(self) -> None:
        self.session = dbManager()

    def tearDown(self) -> None:
        self.session.dbClose()

    #create test functions 
    
    #test case 1 - valid test case for 'lecturer' table
    def test_case_1(self):
        expected = [
            (1, 'Taylor', 'Swift', None),
            (2, 'Adam', 'Levine', None),
            (3, 'Lewis', 'Capaldi', None),
            (4, 'Katy', 'Perry', None)
        ]
        self.session.selectAll('lecturer')
        result = self.session.dbCursor.fetchall()
        self.assertEqual((result), expected)

    #test case 2 - valid test case due to uppercase 
    def test_case_2(self):
        expected = [
            (1, 'Taylor', 'Swift', None),
            (2, 'Adam', 'Levine', None),
            (3, 'Lewis', 'Capaldi', None),
            (4, 'Katy', 'Perry', None)
        ]
        self.session.selectAll('Lecturer')
        result = self.session.dbCursor.fetchall()
        self.assertEqual((result), expected)
    
    #test case 3 - invalid test case due to misspelling
    def test_case_3(self):
        self.assertEqual((self.session.selectAll('lecturers')), False)

    #test case 4 - invalid test case due to incorrect data type (None type)
    def test_case_4(self):
        self.assertEqual((self.session.selectAll(None)), False)

    #test case 5 - invalid test case due to incorrect data type (Int type)
    def test_case_5(self):
        self.assertEqual((self.session.selectAll(10)), False)

    #test case 6- invalid test case due to incorrect data type (Bool type)
    def test_case_6(self):
        self.assertEqual((self.session.selectAll(True)), False)

class Test_DbManager_SelectAllOnCondition(unittest.TestCase):

    def setUp(self) -> None:
        self.session = dbManager()

    def tearDown(self) -> None:
        self.session.dbClose()

    #test case 1 
    def test_case_1(self):
        self.assertEqual((self.session.selectOnCondition(["lecturer_fname", "lecturer_lname"] , "lecturer" , "lecturer_fname", "Taylor")), [("Taylor", "Swift")])

    #test case 2
    def test_case_2(self):
        pass

    #test case 3
    def test_case_3(self):
        pass

    #test case 4
    def test_case_4(self):
        pass

    #test case 5
    def test_case_5(self):
        pass

    #test case 6
    def test_case_6(self):
        pass

    #test case 7
    def test_case_7(self):
        pass

class Test_DbManager_InsertIntoDb(unittest.TestCase):
    #set up and tear down functions
    def setUp(self) -> None:
        self.session = dbManager()

    def tearDown(self) -> None:
        self.session.dbClose()

class Test_DbManager_RemoveDataEqual(unittest.TestCase):
    #set up and tear down functions
    def setUp(self) -> None:
        self.session = dbManager()

    def tearDown(self) -> None:
        self.session.dbClose()

class Test_DbManager_RemoveTable(unittest.TestCase):
    #set up and tear down functions
    def setUp(self) -> None:
        self.session = dbManager()

    def tearDown(self) -> None:
        self.session.dbClose()

class Test_DbManager_InsertFile(unittest.TestCase):
    #set up and tear down functions
    def setUp(self) -> None:
        self.session = dbManager()

    def tearDown(self) -> None:
        self.session.dbClose()


if __name__ == '__main__':
    unittest.main()