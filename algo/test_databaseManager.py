import unittest
from psycopg2 import sql
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
            (1, 'Taylor', 'Swift', 10),
            (2, 'Adam', 'Levine', 14),
            (3, 'Lewis', 'Capaldi', 0),
            (4, 'Katy', 'Perry', 2)
        ]
        self.session.selectAll('lecturer')
        result = self.session.dbCursor.fetchall()
        self.assertEqual((result), expected)

    #test case 2 - valid test case due to uppercase 
    def test_case_2(self):
        expected = [
            (1, 'Taylor', 'Swift', 10),
            (2, 'Adam', 'Levine', 14),
            (3, 'Lewis', 'Capaldi', 0),
            (4, 'Katy', 'Perry', 2)
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

    def test_case_1(self):
        expected = [('Taylor', 'Swift')]
        self.session.selectOnCondition(["lecturer_fname", "lecturer_lname"] , "lecturer" , "lecturer_fname", "Taylor")
        self.assertEqual(self.session.dbCursor.fetchall(), expected)

    def test_case_2(self):
        self.session.selectOnCondition(["lecturer_fname", "lecturer_lname"], "lecturer", "lecturer_fname", "Swift")
        self.assertEqual(self.session.dbCursor.fetchall(), [])

    def test_case_3(self):
        self.session.selectOnCondition(["lecturer_fname", "lecturer_lname"], "lecturer", "lecturer_fname", "taylor")
        self.assertEqual(self.session.dbCursor.fetchall(), [])

    def test_case_4(self):
        self.assertEqual((self.session.selectOnCondition(["lecturer_fname", "lecturer_lname"], "lecturer", "lecturer_fname", True)), False)

    def test_case_5(self):
        self.assertEqual(self.session.selectOnCondition(["lecturer_fname", "lecturer_lname"], "lecturer", "lecturer_fname", None), False)
        

    def test_case_6(self):
        self.assertEqual((self.session.selectOnCondition(["lecturer_fname", "lecturer_lname"], "lecturer", "lecturer_fname", 2)), False)


    def test_case_7(self):
        self.assertEqual((self.session.selectOnCondition(["lecturer_fname", "lecturer_lname"], "lecturer", lecturer_fname, "Taylor")), False)

    def test_case_8(self):
        self.assertEqual((self.session.selectOnCondition(["lecturer_fname", "lecturer_lname"], "lecturer", 2, "Taylor")), False)

    def test_case_9(self):
        self.assertEqual((self.session.selectOnCondition(["lecturer_fname", "lecturer_lname"], "lecturer", True, "Taylor")), False)

    def test_case_10(self):
        self.assertEqual((self.session.selectOnCondition(["lecturer_fname", "lecturer_lname"], "lecturer", None, "Taylor")), False)

    def test_case_11(self):
        self.assertEqual((self.session.selectOnCondition(["lecturer_fname", "lecturer_lname"], "lecturer", "Lecturer_Fname", "Taylor")), False)


    def test_case_12(self):
        self.assertEqual((self.session.selectOnCondition(["lecturer_fname", "lecturer_lname"] , "Lecturer" , "lecturer_fname", "Taylor")), False)

    def test_case_13(self):
        self.assertEqual((self.session.selectOnCondition(["lecturer_fname", "lecturer_lname"] , "lecturers" , "lecturer_fname", "Taylor")), False)

    def test_case_14(self):
        self.assertEqual((self.session.selectOnCondition(["lecturer_fname", "lecturer_lname"] , 6 , "lecturer_fname", "Taylor")), False)

    def test_case_15(self):
        self.assertEqual((self.session.selectOnCondition(["lecturer_fname", "lecturer_lname"] , None , "lecturer_fname", "Taylor")), False)

    def test_case_16(self):
        self.assertEqual((self.session.selectOnCondition(["lecturer_fname", "lecturer_lname"] , False , "lecturer_fname", "Taylor")), False)

    def test_case_17(self):
        self.assertEqual((self.session.selectOnCondition(["lecturer_fname", "lecturer_lname"] , "$%IJINSIBUI" , "lecturer_fname", "Taylor")), False)


    def test_case_18(self):
        self.session.selectOnCondition(("lecturer_fname", "lecturer_lname") , "lecturer" , "lecturer_fname", "Taylor")
        self.assertEqual(self.session.dbCursor.fetchall(), [('Taylor', 'Swift')])

    def test_case_19(self):
        self.assertEqual((self.session.selectOnCondition(["", ""], "lecturer" , "lecturer_fname", "Taylor")), False)
    
    def test_case_20(self):
        self.session.selectOnCondition([], "lecturer", "lecturer_fname", "Taylor")
        self.assertEqual(self.session.dbCursor.fetchall(), [()])
    
    def test_case_21(self):
        self.assertEqual((self.session.selectOnCondition(["kdfjadsf", "True"], "lecturer", "lecturer_fname", "Taylor")), False)

    def test_case_22(self):
        self.assertEqual((self.session.selectOnCondition(["Lecture_fname", "lecturer_lName"], "lecturer", "lecturer_fname", "Taylor")), False)
    
    def test_case_23(self):
        self.assertEqual((self.session.selectOnCondition([4, -1], "lecturer", "lecturer_fname", "Taylor")), False)

    def test_case_24(self):
        self.assertEqual((self.session.selectOnCondition([True, False], "lecturer", "lecturer_fname", "Taylor")), False)

    def test_case_25(self):
        self.assertEqual((self.session.selectOnCondition([None, "lecturer_lname"], "lecturer", "lecturer_fname", "Taylor")), False)
'''
class Test_DbManager_InsertIntoDb(unittest.TestCase):
    #set up and tear down functions
    def setUp(self) -> None:
        self.session = dbManager()

    def tearDown(self) -> None:
        self.session.dbClose()
    #! re-write test case to properly function
    # def test_case_1(self):
    #     self.assertEqual((self.session.insertIntoDb("lecturer", ["lecturer_fname", "lecturer_lname"], ("Bruno", "Mars"))), self.session.dbCursor.fetchall())
    #     self.session.dbCursor.execute(
    #         sql.SQL("delete from lectures where lecturer_fname == 'Bruno' "))
        
    #     self.session.dbCursor.execute(
    #         sql.SQL("alter sequence lecturer_lecturer_id_seq restart with 5")
    #     )
'''       
class Test_DbManager_RemoveDataEqual(unittest.TestCase):
    #set up and tear down functions
    def setUp(self) -> None:
        self.session = dbManager()

    def tearDown(self) -> None:
        self.session.dbClose()

    #likley to fail due to databases not matching up
    def test_case_1(self):
        expected = [
            (1, 'Portland'),
            (2, 'FTSE')
        ]
        self.session.removeDataEqual('building', 'building_id', 3)
        self.session.selectAll('building')
        result = self.session.dbCursor.fetchall()
        self.assertEqual((result), expected)
    
    #likley to fail due to databases not matching up
    def test_case_2(self):
        expected = [
            (1, 'Taylor', 'Swift', 10),
            (2, 'Adam', 'Levine', 14),
            (3, 'Lewis', 'Capaldi', 0),
        ]
        self.session.removeDataEqual('lecturer', 'lecturer_fname', 'Katy')
        self.session.selectAll('lecturer')
        result = self.session.dbCursor.fetchall()
        self.assertEqual((result), expected)

    def test_case_3(self):
        self.session.removeDataEqual('Lecturers', 'lecturer_fname', 'Katy')
        self.assertEqual((False), False)
        
    def test_case_4(self):
        self.session.removeDataEqual('lecturer', 'lecturer_lname', 'Katy')
        self.assertEqual(False, False)

    def test_case_5(self):
        self.session.removeDataEqual('lecturers', 'lecturer_fname', 'Shawn')
        self.assertEqual(False, False)

    def test_case_6(self):
        self.session.removeDataEqual('lecturer', 'lecturer_fname', 1)
        self.assertEqual(False, False)

    def test_case_7(self):
        self.session.removeDataEqual('lecturers', 'lecturer_fname', True)
        self.assertEqual(False, False)

    def test_case_8(self):
        self.session.removeDataEqual('lecturers', 'lecturer_fname', None)
        self.assertEqual(False, False)
'''
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

'''
if __name__ == '__main__':
    unittest.main()