import unittest
from unittest.mock import MagicMock 
from parameterized import parameterized

from databaseManager import dbManager
from algorithm_with_db_functionality import *


class TestInsertIntoTimetable(unittest.TestCase):

    def setUp(self) -> None:
        self.session = dbManager()

    def tearDown(self) -> None:
        self.session.dbClose()

    # module_name Test case 1: Check valid "This test will check that the value in module_info [0] (module_name) is a string."
    dummy_modInfoValid = MagicMock()
    dummy_modInfoValid.modName = 'Architecture & Operating Systems'

    # module_name Test case 2: Check invalid "This test will check that the value in module_info [0] (module_name) is a string (invalid)"
    dummy_modInfoInvalid = MagicMock()
    dummy_modInfoInvalid.modName = 124

    # # module_name Test case 3: Check if in DB "This test will check that the value in modName [0] (module_name) is an actual module name."
    # dummy_modInfoInDB = MagicMock()
    # dummy_modInfoInDB.modName = 'Programming'



    # mod_enrolled TEST CASES

    # mod_enrolled Test Case 1: Check valid "Tests that integer values will be accepted in module_info [1] (mod_enrolled)"
    dummy_modInfoValid.modEnrolled = 2

    # mod_enrolled Test Case 2: Check invalid "Tests that non-integer values will not be accepted in module_info [1] (mod_enrolled)"
    dummy_modInfoInvalid.modEnrolled = '2'


    # mod_lectures TEST CASES

    # mod_enrolled Test Case 1: Check valid "Tests that integer values will be accepted in module_info [1] (mod_enrolled)"
    dummy_modInfoValid.modLectures = 2

    # mod_enrolled Test Case 2: Check invalid "Tests that non-integer values will not be accepted in module_info [1] (mod_enrolled)"
    dummy_modInfoInvalid.modLectures = '2'


    # mod_practicals TEST CASES

    # mod_enrolled Test Case 1: Check valid "Tests that integer values will be accepted in module_info [1] (mod_enrolled)"
    dummy_modInfoValid.modPracticals = 2

    # mod_enrolled Test Case 2: Check invalid "Tests that non-integer values will not be accepted in module_info [1] (mod_enrolled)"
    dummy_modInfoInvalid.modPracticals = '2'


    # mod_tutorials TEST CASES

    # mod_enrolled Test Case 1: Check valid "Tests that integer values will be accepted in module_info [1] (mod_enrolled)"
    dummy_modInfoValid.modTutorials = 2

    # mod_enrolled Test Case 2: Check invalid "Tests that non-integer values will not be accepted in module_info [1] (mod_enrolled)"
    dummy_modInfoInvalid.modTutorials = '2'


    # mod_prof_required TEST CASES

    # mod_enrolled Test Case 1: Check valid "Tests that integer values will be accepted in module_info [1] (mod_enrolled)"
    dummy_modInfoValid.modProfRequired = 2

    # mod_enrolled Test Case 2: Check invalid "Tests that non-integer values will not be accepted in module_info [1] (mod_enrolled)"
    dummy_modInfoInvalid.modProfRequired = '2'


    
    profsList = [
			('Miss', 'Taylor', 'Swift', 'Architecture & Operating Systems', 
             '000000000000000001000000001000000001000000001'),
            ('Mr','Adam', 'Levine', 'Networks',
             '000010010010000100001000001100000000000010000'),
            ('Mr', 'Lewis', 'Capaldi', 'Programming', 
             '000000000000000000000000000000000000000000000'),
            ('Miss', 'Katy', 'Perry', 'Programming', 
             '000000000000000000000000000000000000000000000'),
            ('Dr', 'John', 'Smith', 
             'Architecture & Operating Systems, Programming, Comp Tutorial 4', 
             '000000100000000100000000100000000100000000100'),
            ('Dr', 'Lisa', 'Franklin', 'Core Computing Concepts', 
             '000000000000000000000000000000000000000000000'),
            ('Dr', 'Herbert', 'Jones', 'Core Computing Concepts', 
             '000000000000000000000000000000000000000000000'),
            ('Dr', 'Richard', 'Johnson', 'Database Systems Development', 
             '000010000000000010000000000000010000000000000'),
            ('Dr', 'Hugh', 'Piper', 'Programming', 
             '000000000000000000000000000000000000000000000'),
            ('Dr', 'Javier', 'Rodriguez', 'Networks', 
             '000000000000000000000000000000000000000000000'),
            ('Dr', 'Kathlyn', 'Ferguson', 'Networks', 
             '000000000000001000000000000100000000000000001')]
    
    roomsList = [('A2.03', 40, 1),
                ('FTC_Floor1', 80, 5), 
                ('FTC_Floor2', 80, 5), 
                ('FTC_Floor3', 50, 5),
                ('L0.14a', 67, 2),
                ('RLT1', 330, 4), 
                ('RLT2', 160, 4), 
                ('R1.03', 24, 4)]
    
    @parameterized.expand([
        # Test Cases for module name
        ("valid", dummy_modInfoValid, "lec", roomsList , profsList), #Test Case 1 for moduleInfo
        ("invalid", dummy_modInfoInvalid, "lec", roomsList, profsList), # Test Case 2

        # Test Cases for moduleType
        ("valid", dummy_modInfoValid, "lec", roomsList , profsList), #Test Case 1 for classType
        ("valid", dummy_modInfoValid, "tut", roomsList , profsList), #Test Case 1 for classType
        ("valid", dummy_modInfoValid, "pract", roomsList , profsList), #Test Case 1 for classType
        ("invalid", dummy_modInfoValid, 4, roomsList , profsList), #Test Case 1 for classType
        ("invalid", dummy_modInfoValid, "null", roomsList , profsList), #Test Case 1 for classType
    ])

    def test_valid(self, modinfo, ctype, roomlists, profs):
        
        self.assertTrue(insertIntoTimetable(module_info = modinfo,
                                            class_type = ctype,
                                            roomLists = roomlists,
                                            professorsList = profs))



if __name__ == '__main__':
    unittest.main()





# def test_insertIntoTimetable_valid_classType(self):

    #     # Sample input values
    #     module_info = Module("Test Module", 200, 1, 2, 0, 1)
    #     invalid_classType = 'InvalidType'  # Invalid classType value
    #     roomsList = [('A2.03', 40, 1), ('FTC_Floor1', 80, 5), ('FTC_Floor2', 80, 5), ('FTC_Floor3', 50, 5),
    #                  ('L0.14a', 67, 2), ('RLT1', 330, 4), ('RLT2', 160, 4), ('R1.03', 24, 4)]
    #     professorsList = [('Miss', 'Taylor', 'Swift', 'Architecture & Operating Systems', '000000000000000001000000001000000001000000001'),
    #                       ('Mr', 'Adam', 'Levine', 'Networks', '000010010010000100001000001100000000000010000'),
    #                       ('Mr', 'Lewis', 'Capaldi', 'Programming', '000000000000000000000000000000000000000000000'),
    #                       ('Miss', 'Katy', 'Perry', 'Programming', '000000000000000000000000000000000000000000000'),
    #                       ('Dr', 'John', 'Smith', 'Architecture & Operating Systems, Programming, Comp Tutorial 4', '000000100000000100000000100000000100000000100'),
    #                       ('Dr', 'Lisa', 'Franklin', 'Core Computing Concepts', '000000000000000000000000000000000000000000000'),
    #                       ('Dr', 'Herbert', 'Jones', 'Core Computing Concepts', '000000000000000000000000000000000000000000000'),
    #                       ('Dr', 'Richard', 'Johnson', 'Database Systems Development', '000010000000000010000000000000010000000000000'),
    #                       ('Dr', 'Hugh', 'Piper', 'Programming', '000000000000000000000000000000000000000000000'),
    #                       ('Dr', 'Javier', 'Rodriguez', 'Networks', '000000000000000000')]

    #     # Mocking the random.randint function to return a fixed value for testing
    #     def mock_randint(a, b):
    #         return 0  # Always return 0 for testing purposes

    #     # Monkey patching random.randint to use the mock function
    #     random.randint = mock_randint

    #     # Call the function being tested with an invalid classType
    #     # with self.assertRaises(ValueError) as context:
    #     #     insertIntoTimetable(module_info, invalid_classType, roomsList, professorsList)
    #     self.assertEqual((insertIntoTimetable(module_info, invalid_classType, roomsList, professorsList)), ValueError)


    # def test_roomList(self):
    #     print()


    # def test_professorsList(self) :
    #     print()