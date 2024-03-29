import psycopg2
from psycopg2 import sql
from typing import Any

from databaseBuilder import buildDatabaseSchema, insertDataToDb


class dbManger:
    """
    Class is used to mangage inputs and outputs from the database

    Attributes 
    ==========

    dbConnection (variable / type: any) : holds the database connection variables
    dbCursor (variable / type: any) : is the cussor which is used to access the database
    lineNo (Int) : holds the line number in a given file
    
    """
    def __init__(self) -> None:

        self.dbConnection = psycopg2.connect(
            host = "localhost",
            dbname = "postgres",
            user = "postgres",
            password = "Lebihan01!", #change this to your password if testing etc...
            port = 5432
        )

        self.dbCursor = self.dbConnection.cursor()

        self.lineNo = 0


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
    
    def selectOnCondition(self, tbl_fields: list[str], tbl_name: str, target: str, value: Any):
        """
        Selects entires from a table based of a given condition

        Parameters
        ----------
        tbl_feilds : List[str]
            The selected fields from a table
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
        self.dbCursor.execute(
            sql.SQL("select {fields} from {table} where {conditon} = %s").format(
                fields = sql.SQL(',').join(
                    sql.Identifier(n) for n in tbl_fields
                ),
                table = sql.Identifier(tbl_name),
                condition = sql.Identifier(target)),
                [value]
            )
        return self.dbCursor.fetchall()

    def insertIntoDb(self, tbl_name: str, tbl_cols: list[str], values: Any) -> None:
        """
        Inserts values into the database to a given table

        Parameters
        ----------
        tbl_name : str
            table the values are being inserted into
        tbl_cols : List[str]
            the column names where the data is being inserted into
        value : Any
            The data being inserted into the table

        Returns
        -------
        None
        """
        self.dbCursor.execute(
            sql.SQL("insert into {table} ({columns}) values %s").format(
                table = sql.Identifier(tbl_name),
                columns = sql.SQL(',').join(
                    sql.Identifier(n) for n in tbl_cols
                )),
                [values]
                
        )

        self.dbConnection.commit()
        # ? do we need to keep this ^ the above works for multiple columns with different data types to be inserted
        # self.dbCursor.execute(
        #     sql.SQL("insert into {table} ({column}) values (%s)").format(
        #         table = sql.Identifier(tbl_name),
        #         column = sql.Identifier(tbl_cols)),
        #         [value]
        #     )
        # self.dbConnection.commit()

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
    
        self.dbConnection.commit()

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
        self.dbConnection.commit()
        return 
    

    def insertFile(self, file: Any) -> None:
        #! method reads the file, need to check the input of the line before using the insert function. 
        file = open(file, "r")

        for line in file:

            self.lineNo += 1
            # needs testing to check the values are properly split
            table = line.lower().split(",")[0]
            values = line.lower().split(",")[1:]
            print(table)
            print(values)

            self.dbCursor.execute(
                sql.SQL("insert into {table} values %s").format(
                    table = sql.Identifier(table)),
                [values]
            )

            self.dbConnection.commit()
            
        return 