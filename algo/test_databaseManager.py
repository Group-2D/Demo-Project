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
        expected = [
            (1, 'Taylor', 'Swift', None),
            (2, 'Adam', 'Levine', None),
            (3, 'Lewis', 'Capaldi', None),
            (4, 'Katy', 'Perry', None)
        ]
        
        
        self.session.selectAll('lecturer')
        result = self.session.dbCursor.fetchall()
        print(expected, '\n', result)
        self.assertEqual((result), expected)

    def test_selectOnConditon(self):
        pass




if __name__ == '__main__':
    unittest.main()