import unittest
from databaseManager import dbManager


class TestDbManager(unittest.TestCase):

    #set up and tear down functions
    def setUp(self) -> None:
        self.session = dbManager()

    def tearDown(self) -> None:
        self.session.dbClose()

    #create test functions 
    def test_selectAll(self):

        #test case 1 - valid test case for 'lecturer' table
        expected = [
            (1, 'Taylor', 'Swift', None),
            (2, 'Adam', 'Levine', None),
            (3, 'Lewis', 'Capaldi', None),
            (4, 'Katy', 'Perry', None)
        ]
        
        self.session.selectAll('lecturer')
        result = self.session.dbCursor.fetchall()
        self.assertEqual((result), expected)

        #test case 2 - invalid test case due to misspelling
        expected = False
        self.assertEqual((self.session.selectAll('lecturers')), expected)
        
        #test case 3 - invalid test case due to type error (None type)
        expected = False
        self.assertEqual((self.session.selectAll(2)), expected)

        #test case 4 - valid test case for 'building' table
        expected = [
            ('Angelesea'),
            ('Liongate'),
            ('Park'),
            ('Richmond')
        ]
        self.session.selectAll('building')
        result = self.session.dbCursor.fetchall()
        self.assertEqual((result), expected)

        #test case 5 - valid test case for 'Building' - handles uppercase misspelling correctly
        self.session.selectAll('Building')
        result = self.session.dbCursor.fetchall()
        self.assertEqual((result), expected)

        #test case 6 - invalid test case due to type error (Int type)
        expected = False
        self.assertEqual((self.session.selectAll(10)), expected)
        #test case 7 - invalid test case due to type erro (Bool type)
        self.assertEqual((self.session.selectAll(True)), expected)
    def test_selectOnConditon(self):
        pass




if __name__ == '__main__':
    unittest.main()