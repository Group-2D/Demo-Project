import unittest
import random
from databaseManager import dbManager
from algorithm_with_db_functionality import *

class TestInsertIntoTimetable(unittest.TestCase):

    def setUp(self) -> None:
        self.session = dbManager()

    def tearDown(self) -> None:
        self.session.dbClose()


    def test_insertIntoTimetable_valid_classType(self):

        # Sample input values
        module_info = Module("Test Module", 200, 1, 2, 0, 1)
        invalid_classType = 'InvalidType'  # Invalid classType value
        roomsList = [('A2.03', 40, 1), ('FTC_Floor1', 80, 5), ('FTC_Floor2', 80, 5), ('FTC_Floor3', 50, 5),
                     ('L0.14a', 67, 2), ('RLT1', 330, 4), ('RLT2', 160, 4), ('R1.03', 24, 4)]
        professorsList = [('Miss', 'Taylor', 'Swift', 'Architecture & Operating Systems', '000000000000000001000000001000000001000000001'),
                          ('Mr', 'Adam', 'Levine', 'Networks', '000010010010000100001000001100000000000010000'),
                          ('Mr', 'Lewis', 'Capaldi', 'Programming', '000000000000000000000000000000000000000000000'),
                          ('Miss', 'Katy', 'Perry', 'Programming', '000000000000000000000000000000000000000000000'),
                          ('Dr', 'John', 'Smith', 'Architecture & Operating Systems, Programming, Comp Tutorial 4', '000000100000000100000000100000000100000000100'),
                          ('Dr', 'Lisa', 'Franklin', 'Core Computing Concepts', '000000000000000000000000000000000000000000000'),
                          ('Dr', 'Herbert', 'Jones', 'Core Computing Concepts', '000000000000000000000000000000000000000000000'),
                          ('Dr', 'Richard', 'Johnson', 'Database Systems Development', '000010000000000010000000000000010000000000000'),
                          ('Dr', 'Hugh', 'Piper', 'Programming', '000000000000000000000000000000000000000000000'),
                          ('Dr', 'Javier', 'Rodriguez', 'Networks', '000000000000000000')]

        # Mocking the random.randint function to return a fixed value for testing
        def mock_randint(a, b):
            return 0  # Always return 0 for testing purposes

        # Monkey patching random.randint to use the mock function
        random.randint = mock_randint

        # Call the function being tested with an invalid classType
        # with self.assertRaises(ValueError) as context:
        #     insertIntoTimetable(module_info, invalid_classType, roomsList, professorsList)
        self.assertEqual((insertIntoTimetable(module_info, invalid_classType, roomsList, professorsList)), ValueError)

if __name__ == '__main__':
    unittest.main()


# class Test_DbManager_SelectAll(unittest.TestCase):

#     #set up and tear down functions
#     def setUp(self) -> None:
#         self.session = dbManager()

#     def tearDown(self) -> None:
#         self.session.dbClose()

#     #create test functions 
    
#     #test case 1 - valid test case for 'lecturer' table
#     def test_case_1(self):
#         expected = [
#             (1, 'Taylor', 'Swift', None),
#             (2, 'Adam', 'Levine', None),
#             (3, 'Lewis', 'Capaldi', None),
#             (4, 'Katy', 'Perry', None)
#         ]
#         self.session.selectAll('lecturer')
#         result = self.session.dbCursor.fetchall()
#         self.assertEqual((result), expected)

#     #test case 2 - valid test case due to uppercase 
#     def test_case_2(self):
#         expected = [
#             (1, 'Taylor', 'Swift', None),
#             (2, 'Adam', 'Levine', None),
#             (3, 'Lewis', 'Capaldi', None),
#             (4, 'Katy', 'Perry', None)
#         ]
#         self.session.selectAll('Lecturer')
#         result = self.session.dbCursor.fetchall()
#         self.assertEqual((result), expected)
    
#     #test case 3 - invalid test case due to misspelling
#     def test_case_3(self):
#         self.assertEqual((self.session.selectAll('lecturers')), False)

#     #test case 4 - invalid test case due to incorrect data type (None type)
#     def test_case_4(self):
#         self.assertEqual((self.session.selectAll(None)), False)

#     #test case 5 - invalid test case due to incorrect data type (Int type)
#     def test_case_5(self):
#         self.assertEqual((self.session.selectAll(10)), False)

#     #test case 6- invalid test case due to incorrect data type (Bool type)
#     def test_case_6(self):
#         self.assertEqual((self.session.selectAll(True)), False)

# class Test_DbManager_SelectAllOnCondition(unittest.TestCase):

#     def setUp(self) -> None:
#         self.session = dbManager()

#     def tearDown(self) -> None:
#         self.session.dbClose()

#     def test_case_1(self):
#         self.assertEqual((self.session.selectOnCondition(["lecturer_fname", "lecturer_lname"] , "lecturer" , "lecturer_fname", "Taylor")), [("Taylor", "Swift")])

#     def test_case_2(self):
#         self.assertEqual((self.session.selectOnCondition(["lecturer_fname", "lecturer_lname"], "lecturer", "lecturer_fname", "Swift")), False)

#     def test_case_3(self):
#         self.assertEqual((self.session.selectOnCondition(["lecturer_fname", "lecturer_lname"], "lecturer", "lecturer_fname", "taylor")), [])

#     def test_case_4(self):
#         self.assertEqual((self.session.selectOnCondition(["lecturer_fname", "lecturer_lname"], "lecturer", "lecturer_fname", True)), False)

#     def test_case_5(self):
#         self.assertEqual((self.session.selectOnCondition(["lecturer_fname", "lecturer_lname"], "lecturer", "lecturer_fname", None)), [])

#     def test_case_6(self):
#         self.assertEqual((self.session.selectOnCondition(["lecturer_fname", "lecturer_lname"], "lecturer", "lecturer_fname", 2)), False)


#     def test_case_7(self):
#         self.assertEqual((self.session.selectOnCondition(["lecturer_fname", "lecturer_lname"], "lecturer", lecturer_fname, "Taylor")), False)

#     def test_case_8(self):
#         self.assertEqual((self.session.selectOnCondition(["lecturer_fname", "lecturer_lname"], "lecturer", 2, "Taylor")), False)

#     def test_case_9(self):
#         self.assertEqual((self.session.selectOnCondition(["lecturer_fname", "lecturer_lname"], "lecturer", True, "Taylor")), False)

#     def test_case_10(self):
#         self.assertEqual((self.session.selectOnCondition(["lecturer_fname", "lecturer_lname"], "lecturer", None, "Taylor")), False)

#     def test_case_11(self):
#         self.assertEqual((self.session.selectOnCondition(["lecturer_fname", "lecturer_lname"], "lecturer", "Lecturer_Fname", "Taylor")), False)


#     def test_case_12(self):
#         self.assertEqual((self.session.selectOnCondition(["lecturer_fname", "lecturer_lname"] , "Lecturer" , "lecturer_fname", "Taylor")), [("Taylor", "Swift")])

#     def test_case_13(self):
#         self.assertEqual((self.session.selectOnCondition(["lecturer_fname", "lecturer_lname"] , "lecturers" , "lecturer_fname", "Taylor")), False)

#     def test_case_14(self):
#         self.assertEqual((self.session.selectOnCondition(["lecturer_fname", "lecturer_lname"] , 6 , "lecturer_fname", "Taylor")), False)

#     def test_case_15(self):
#         self.assertEqual((self.session.selectOnCondition(["lecturer_fname", "lecturer_lname"] , None , "lecturer_fname", "Taylor")), False)

#     def test_case_16(self):
#         self.assertEqual((self.session.selectOnCondition(["lecturer_fname", "lecturer_lname"] , False , "lecturer_fname", "Taylor")), False)

#     def test_case_17(self):
#         self.assertEqual((self.session.selectOnCondition(["lecturer_fname", "lecturer_lname"] , "$%IJINSIBUI" , "lecturer_fname", "Taylor")), False)


#     def test_case_18(self):
#         self.assertEqual((self.session.selectOnCondition(("lecturer_fname", "lecturer_lname") , "lecturer" , "lecturer_fname", "Taylor")), False)

#     def test_case_19(self):
#         self.assertEqual((self.session.selectOnCondition(["", ""], "lecturer" , "lecturer_fname", "Taylor")), [])
    
#     def test_case_20(self):
#         self.assertEqual((self.session.selectOnCondition([], "lecturer", "lecturer_fname", "Taylor")), [])
    
#     def test_case_21(self):
#         self.assertEqual((self.session.selectOnCondition(["kdfjadsf", "True"], "lecturer", "lecturer_fname", "Taylor")), False)

#     def test_case_22(self):
#         self.assertEqual((self.session.selectOnCondition(["Lecture_fname", "lecturer_lName"], "lecturer", "lecturer_fname", "Taylor")), [("Taylor", "Swift")])
    
#     def test_case_23(self):
#         self.assertEqual((self.session.selectOnCondition([4, -1], "lecturer", "lecturer_fname", "Taylor")), False)

#     def test_case_24(self):
#         self.assertEqual((self.session.selectOnCondition([True, False], "lecturer", "lecturer_fname", "Taylor")), False)

#     def test_case_25(self):
#         self.assertEqual((self.session.selectOnCondition([None, "lecturer_lname"], "lecturer", "lecturer_fname", "Taylor")), False)

# class Test_DbManager_InsertIntoDb(unittest.TestCase):
#     #set up and tear down functions
#     def setUp(self) -> None:
#         self.session = dbManager()

#     def tearDown(self) -> None:
#         self.session.dbClose()

#     def test_case_1(self):
#         self.assertEqual((self.session.insertIntoDb("lecturer", ["lecturer_fname", "lecturer_lname"], ("Bruno", "Mars"))), self.session.dbCursor.fetchall())
   
# class Test_DbManager_RemoveDataEqual(unittest.TestCase):
#     #set up and tear down functions
#     def setUp(self) -> None:
#         self.session = dbManager()

#     def tearDown(self) -> None:
#         self.session.dbClose()

# class Test_DbManager_RemoveTable(unittest.TestCase):
#     #set up and tear down functions
#     def setUp(self) -> None:
#         self.session = dbManager()

#     def tearDown(self) -> None:
#         self.session.dbClose()

# class Test_DbManager_InsertFile(unittest.TestCase):
#     #set up and tear down functions
#     def setUp(self) -> None:
#         self.session = dbManager()

#     def tearDown(self) -> None:
#         self.session.dbClose()


# if __name__ == '__main__':
#     unittest.main()