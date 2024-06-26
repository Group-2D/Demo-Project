import psycopg2
from psycopg2 import sql
from typing import Any

class dbManager:
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
            dbname = "timetable_gen",
            user = "postgres",
            password = "Lebihan01!", #change this to your password if testing etc...
            port = 5432
        )

        self.dbCursor = self.dbConnection.cursor()
        #? add a list of tables stored in the database?
        self.tblSet: set[str] = self.setTblSet()
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
    
    def setTblSet(self):
        """
        creates a set of all tables in the database for easier searching

        Returns
        -------
        self.tblSet
            a set of all tables stored in the database
        """
        self.dbCursor.execute(
            sql.SQL("select tablename from pg_catalog.pg_tables where schemaname != 'information_schema' and schemaname != 'pg_catalog'")
        ) 

        tblSet: set[str] = set()
        for tbl in self.dbCursor.fetchall():
            tblSet.add(tbl[0])

        return tblSet
        
    def selectAll(self, table: str) -> Any:
        """
        Gets all the data from a given table
        
        Parameters
        ---------
        table (str) : the table selected 

        Returns
        -------
        None
        """

        if type(table) != str:
            return False

        try:
            self.dbCursor.execute(
                """SELECT * FROM %s """ % table.lower()
            )
        
        except psycopg2.ProgrammingError:
            return False
    
        else:
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
        if type(tbl_name) != str:
            return False
        
        if tbl_name not in self.tblSet:
            return False
               
        columns = self.getColumns(tbl_name)
                
        for field in tbl_fields:
            if type(field) != str or field not in columns:
                return False
            

        if type(target) != str:
            return False
        
        # self.dbCursor.execute(
        #     sql.SQL("select pg_typeof({column}) from {table}").format(
        #         column = sql.Identifier(target),
        #         table = sql.Identifier(tbl_name)
        #     )
        # )

        # columnDataType = self.dbCursor.fetchone()

        # if columnDataType[0] == 'character varying':
        #     columnDataType = str
        # elif columnDataType[0] == 'integer':
        #     columnDataType = int

        # if type(value) != columnDataType:
        #     return False
        
        try:    
            self.dbCursor.execute(
                sql.SQL("select {fields} from {table} where {condition} = %s").format(
                    fields = sql.SQL(',').join(
                        sql.Identifier(n.lower()) for n in tbl_fields
                    ),
                    table = sql.Identifier(tbl_name),
                    condition = sql.Identifier(target)),
                    [value]
                )
        
        except psycopg2.ProgrammingError and psycopg2.OperationalError and psycopg2.errors.UndefinedColumn:
            return False
        
        return
    
    def getTables(self):
        """
        gets all the table names in the database

        Returns
        -------
        List[Str]
            A list of strings that reference the names of all the tables in the database
        """
        self.dbCursor.execute(
            sql.SQL("select tablename from pg_catalog.pg_tables where schemaname != 'information_schema' and schemaname != 'pg_catalog'")
        ) 
        return self.dbCursor.fetchall()

    def getColumns(self, tbl_name: str):
        """
        _summary_

        Parameters
        ----------
        tbl_name : _type_
            _description_
        """
        tbl_cols: set[str] = set()

        self.dbCursor.execute(
            sql.SQL("select column_name from information_schema.columns where table_name = %s"),
            [tbl_name]
        )
    
        for col in self.dbCursor.fetchall():
            tbl_cols.add(col[0])
        return tbl_cols


    def count_db_enteries(self, tbl_name: str, col_name: str):
        """
        returns the number of enteries in a database table

        Parameters
        ----------
        tbl_name : str
            the table being quirried 
        col_name : str
            the column being counted
        """
        self.dbCursor.execute(
            sql.SQL("select count({column_name}) from {table}").format(
                table = sql.Identifier(tbl_name.lower()),
                column_name = sql.Identifier(col_name.lower())

            )
        )

        return
        
    
    def insertIntoDb(self, tbl_name: str, tbl_cols: list[str], values: Any):
        #! this function needs to check for duplicate inputs
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
        if type(tbl_name) != str and tbl_name not in self.tblSet:
            print(TypeError)
            return False
        
        for tbl in tbl_cols:
            if type(tbl) != str:
                return False
        
        try:
            self.dbCursor.execute(
                sql.SQL("insert into {table} ({columns}) values %s").format(
                    table = sql.Identifier(tbl_name.lower()),
                    columns = sql.SQL(',').join(
                        sql.Identifier(n.lower()) for n in tbl_cols
                    )),
                    [values]
                    
            )
            self.dbConnection.commit()

        except psycopg2.ProgrammingError and psycopg2.OperationalError as error:
            print(error)
            return False
    
        return
        # ? do we need to keep this ^ the above works for multiple columns with different data types to be inserted
        # self.dbCursor.execute(
        #     sql.SQL("insert into {table} ({column}) values (%s)").format(
        #         table = sql.Identifier(tbl_name),
        #         column = sql.Identifier(tbl_cols)),
        #         [value]
        #     )
        # self.dbConnection.commit()

        return 
    
    def removeDataEqual(self, tbl_name: str, tbl_column: str, value: Any):
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
        if type(tbl_name) != str and tbl_name not in self.tblSet:
            print(TypeError, "check the table is in the database")
            return False
    
        self.setTblSet()

        if tbl_name not in self.tblSet:
            return False
        
        if type(tbl_column) != str:
            print(TypeError, "check the column is in ")
            return False
        
        columns = self.getColumns(tbl_name)

        if tbl_column not in columns:
            return False

        try:
            self.dbCursor.execute(
                sql.SQL("DELETE FROM {table} WHERE {column} = %s").format(
                    table = sql.Identifier(tbl_name),
                    column = sql.Identifier(tbl_column)),
                    [value]
                )
    
            self.dbConnection.commit()

        except psycopg2.ProgrammingError and psycopg2.OperationalError and psycopg2.errors.UndefinedColumn and psycopg2.errors.UndefinedFunction:
            return False

        return

    def removeTable(self, tbl_name: str):
        """
        removes a given table and all referenced tables from the database

        Parameters
        --------
        tble_name : str
            name of the table being dropped
        """
        if type(tbl_name) != str and tbl_name not in self.tblSet:
            return False
        try:
            self.dbCursor.execute(
                """DROP TABLE IF EXISTS %s CASCADE;""" % tbl_name
            )
            self.dbConnection.commit()

            self.tblSet.remove(tbl_name)

        except psycopg2.ProgrammingError and psycopg2.OperationalError as error:
            print(error)
            return False

        return 
    

    def insertFile(self, file: Any) -> None:
        """
        Inserts values from a file into the correct table in the database

        Parameters
        ----------
        file : Any
            a file containing data that is to be inserted into the database
        """
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

def main():

    session = dbManager()
    print(session.selectOnCondition(["lecturer_fname", "lecturer_lname"], "lecturer", "lecturer_fname", None))
    session.dbClose()


if __name__ == '__main__':
    main()