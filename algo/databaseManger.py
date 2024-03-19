import psycopg2
from psycopg2 import sql
from typing import Any

from .databaseBuilder import buildDatabaseSchema, insertDataToDb


class dbManger:
    """
    Class is used to mangage inputs and outputs from the database

    Attributes 
    ==========

    dbConnection (variable / type: any) : holds the database connection variables
    dbCursor (variable / type: any) : is the cussor which is used to access the database
    dbCommit (variable / type: any) : holds a function used to commit any changes made to the database

    """
    def __init__(self) -> None:

        self.dbConnection = psycopg2.connect(
            host = "localhost",
            dbname = "postgres",
            user = "postgres",
            password = "Lebihan01!",
            port = 5432
        )

        self.dbCursor = self.dbConnection.cursor()

        self.dbCommit = self.dbConnection.commit()

    def dbClose(self):
        """
        closes the connection to the database 

        Prameters
        ---------
        None 

        Returns
        -------
        None
        """
        self.dbCursor.close()
        self.dbConnection.close()
    
    def selectAll(self, table: str):
        """
        Gets all the data from a given table
        
        Parameters
        ---------
        table (str) : the table selected 

        Returns
        -------
        None
        """
        self.dbCursor.execute(
            """SELECT * FROM %s """ % table
        )

        for row in self.dbCursor.fetchall():
            print(row)
        
        return
    
    def selectOnCondition(self, tbl_feild: str, tbl_name: str, target: str, value: Any):
        """
        Selects entires from a table based of a given condition

        Parameters
        ----------
        tbl_feild : str
            The selected field from a table
        tbl_name : str
            The selected table 
        target : str
            The field selected for the conditional statement
        value : Any
            The value the condition has to meet 

        Returns
        -------
        All values that match the statement and returns a list of tuples
            
        """
        # ! Error occurs: 'Composed' object is not subscriptable
        self.dbCursor.mogrify( 
            query = sql.SQL("select {field} from {table} where {condition} = %s").format(
                field = sql.Identifier(tbl_feild),
                table = sql.Identifier(tbl_name),
                condition = sql.Identifier(target))
                [value]
        )
        return self.dbCursor.fetchall()

    def insertIntoDb(self, tbl_name: str, tbl_cols: str, value: Any) -> None:
        """
        Inserts values into the database to a given table

        Parameters
        ----------
        tbl_name : str
            table the values are being inserted into
        tbl_cols : str
            the column name where data is being inserted into
        value : Any
            The data being inserted into the table

        Returns
        -------
        None
        """
        
        self.dbCursor.execute(
            sql.SQL("insert into {table} ({column}) values (%s)").format(
                table = sql.Identifier(tbl_name),
                column = sql.Identifier(tbl_cols)),
                [value]
            )
        return 
    
    def removeDataEqual(self, tbl_name: str, tbl_column: str, value: Any) -> None:
        """
        removes data from a given table

        Parameters
        ----------
        tbl_name : str
            table the values are being removed from
        tbl_column : str
            the coloumn name where values are being removed from
        value : Any
            the value being removed
        """
        self.dbCursor.execute(
            sql.SQL("DELETE FROM {table} WHERE {column} = %s").format(
                table = sql.Identifier(tbl_name),
                column = sql.Identifier(tbl_column)),
                [value]
            )

        return

    def removeTable(self, tbl_name: str) -> None:
        """
        removes a given table and all referenced tables from the database

        Parameters
        --------
        tble_name : str
            name of the table being dropped
        """
        self.dbCursor.execute(
            """DROP TABLE IF EXISTS %s CASCADE;""" % tbl_name
        )

        return 

'''
session = dbManger()

print(type(session.dbConnection))
print(type(session.dbCursor))

buildDatabaseSchema(session.dbCursor)
insertDataToDb(session.dbCursor)

session.selectAll('building')

session.insertIntoDb('building', 'building_name','Libiary')
print()
session.selectAll('building')
print()

session.removeDataEqual('building', 'building_name', 'Park')

session.selectAll('building')

session.removeTable('building')

session.dbCommit

session.dbClose()A
'''