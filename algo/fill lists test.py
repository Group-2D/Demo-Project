import unittest
from parameterized import parameterized
import psycopg2
from databaseManager import dbManager

from algorithm_with_db_functionality import fillModuleLists, fillProfessorsLists, fillRoomLists

class TestFillLists(unittest.TestCase):

    def test_functionality(self):
        
        self.assertIsNot()






    pass


class TestDBConnection(unittest.TestCase):

    def test_connection(self):

        self.assertRaises(psycopg2.OperationalError, dbManager())

    pass


if __name__ == "__main__":
    unittest.main()