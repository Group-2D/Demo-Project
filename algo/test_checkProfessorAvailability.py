import unittest
from unittest.mock import MagicMock
from parameterized import parameterized

from algorithm_with_db_functionality import checkProfessorAvailability

class TestProfessorAvailability(unittest.TestCase):

    dummy_modInfo = MagicMock()
    dummy_modInfo.modName = 'Architecture & Operating Systems'
    dummy_invalidModInfo = MagicMock()
    dummy_invalidModInfo.modName = 'Forensic Science'
    dummy_object = MagicMock()

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

    @parameterized.expand([
        ("valid data",
         5, "THU", dummy_modInfo, profsList),
        
        ("invalid checkTime (out of range)",
         3657, "THU", dummy_modInfo, profsList),

        ("invalid checkTime (incorrect data type)",
         "Hey", "THU", dummy_modInfo, profsList),

        ("invalid checkDay (string out of range)",
         5, "Error", dummy_modInfo, profsList),
        
        ("invalid checkDay (incorrect data type)",
         5, None, dummy_modInfo, profsList),
        
        ("invalid modinfo (incorrect modname)",
         5, "THU", dummy_invalidModInfo, profsList),
        
        ("invalid modinfo (invalid object type)",
         5, "THU", dummy_object, profsList),
        
        ("invalid proflist (invalid list data)",
         5, "THU", dummy_modInfo, ["This", "Is", "A", "Test"]),
        
        ("invalid proflist (invalid data type)",
         5, "THU", dummy_modInfo, None)
    ])

    def test_valid(self, name, pTime, pDay, pModInfo, pProfList):
        
        self.assertIsInstance(checkProfessorAvailability(
            checkTime= pTime,
            checkDay= pDay,
            module_info= pModInfo,
            professorsList= pProfList
        ), list)


if __name__ == '__main__':
    unittest.main()