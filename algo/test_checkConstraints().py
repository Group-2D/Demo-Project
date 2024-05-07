import unittest
from parameterized import parameterized
from unittest.mock import MagicMock

from algorithm_with_db_functionality import checkConstraints

class TestCheckConstraints(unittest.TestCase):

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
        ("valid", 
         dummy_modInfo, "lec", 6, 200, ['RLT2', 160, (4,), None], profsList),

        ("invalid modInfo (incorrect modname)", 
         dummy_invalidModInfo, "lec", 6, 200, ['RLT2', 160, (4,), None], profsList),

        ("invalid modInfo (invalid object passed)", 
         dummy_object, "lec", 6, 200, ['RLT2', 160, (4,), None], profsList),

        ("invalid studentsUnassigned (out of bounds)", 
         dummy_modInfo, "lec", 6, 23490, ['RLT2', 160, (4,), None], profsList),

        ("invalid studentsUnassigned (out of bounds)", 
         dummy_modInfo, "lec", 6, None, ['RLT2', 160, (4,), None], profsList),

        ("invalid classType (out of bounds)", 
        dummy_modInfo, "peepee", 6, 200, ['RLT2', 160, (4,), None], profsList),

        ("invalid classType (data type)", 
        dummy_modInfo, "peepee", 6, 200, ['RLT2', 160, (4,), None], profsList),

        ("invalid randPotentialRoom (out of bounds)", 
        dummy_modInfo, "lec", 1239, 200, ['RLT2', 160, (4,), None], profsList),

        ("invalid randPotentialRoom (invalid null type)", 
        dummy_modInfo, "lec", None, 200, ['RLT2', 160, (4,), None], profsList),

        ("invalid room (invalid room name, doesnt exist)", 
        dummy_modInfo, "lec", 6, 200, ['blank', 0, (82,), None], profsList),

        ("invalid room (invalid data type null)", 
        dummy_modInfo, "lec", 6, 200, None, profsList),

        ("invalid professorsList (out of bounds)", 
        dummy_modInfo, "lec", 6, 200, ['RLT2', 160, (4,), None], ["Mister","Invalid"]),

    ])

    def test_valid(self, name, modInfo, ctype, randroom, studs, room, profs):
        
        self.assertTrue(checkConstraints(module_info = modInfo,
                                         classType = ctype,
                                         randPotentialRoom = randroom,
                                         studentsUnassigned= studs,
                                         room = room,
                                         professorsList = profs))
        

if __name__ == '__main__':
    unittest.main()