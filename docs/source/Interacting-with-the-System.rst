==================
Interacting with the System .. _Interacting with the System
==================

Interactions between the Database, GUI, and backend algorthirm use the dbManager class stored in the databaseManger.py file

Section 1 - Getting data 
-------------
**Selecting All data from a table**

To select all data from the table, you need to use the selectAll method

As the user, this is done through the GUI, you will need to navigate the GUI screens 
:ref: 'gui-navigation'

The GUI will run the users input and select the corresponding table as long as the table is spelt correctly and in the database, otherwise, an error will be returned along with no table data.

If the input is correct, all the data in the table will be returned as outputted through the GUI. 

**Selecting data based on a condition**

To select data stored in a table that is equal to a value, you need to use the selectOnCondition method.

As the user, this is done through the GUI, you will nedd to navigate the GUI screens
:ref: 'gui_navigation'

The user needs to input serveral values:
  1. The table name
  2. The column names from the table
  3. The column name containing the values being checked
  4. The value used as the conditon

This query will output the data from the selected column names that match the value in the column being checked, this will be outputted to the GUI. 

If the tables or column names are incorrect, an error is returned. If no values in the table column match the conditional value, no values will be outputted to the GUI. 

**Issues / Limitations** 
A current limiation is the selectOnMethod can only fetch data values that are equal to the inputted condition value. Further developement of this method ir adding more functions to the dbManager class will rectify this limitation.

Ohter issues in the selectOnCondition is that the error and exception handling is not fully complete and needs more testing. This issue is highlighted by the column validation within the function. 

Section 2 - Inserting Data 
------------
**Inserting data into a table**

To insert data into a table in the database, you need to run the insertIntoDb method.

The user will insert data through the GUI, which is located in the GUI.

The user needs to input multiple values:
  1. The table name
  2. The column names data is being inserted into
  3. The data values being inserted into the table

If the inputted values are all correct and valid, the data will be inserted into the table. This will not give the user any feedback. If an error occurs, the transaction will fail and not complete to comply with ACID. This will also provide an error message to the user. 

**Issues** 
The mehtod will insert repeated data, even if the data already exsists in the table. Also, the database uses SERIAL values for each id. However, when data is deleted, this value is not reset. This can lead to data being inserted at the end of the table increasing its overall memmory consumption.

**Inserting data via files**

Inserting data into the database via a file is done using the insertFile method. 

This method currently only works on csv or txt files. The method splits values assuming the table is the first value in a line and values being the remaining values in the file line. 
These values are then inserted into the corresponding table. 

The user can use this method through the GUI. 

**Issues**
However, proper funcationality for the user to insert a file is currently not built into the system. 

Section 3: Removing / Deleting Data
---------------------
**Remove data from tables**

The user is able to delete / remove data from the database. 

The user needs to enter several values to remove data:
  1. The table name
  2. The tables column values being compared 
  3. The value being removed 

All the data will be removed from the table that is equal to the inputted value as long as its in the selected column. 

**Issues** 
Similar to the selectOnCondition method, this method can only remove data equal to the given value.

**Removing tables**

The user is able to remove data from the database using the removeTable method. However, the function uses Cascase method to remove tables. This means all connected tables to a removed table are also removed. A major issue this can cause is the deletion of the whole database.

While the user can not access this method through the GUI, it can be run inside the databaseMangement file. 

Section 4: Miscellaneous
-------------------
This section is used to provide infomation about the various methods / functions in the dbManager file, this is to mainly help in solving potential errors.

The dbManger is a class. It has 4 attributes with varying importance.
  1. dbConnection: this is used to connect the file to the database. This is **important** and is likely needed to be edited to run the system as intended. 
  2. dbCursor: this variable stores the connection of the database and enables the methods/functions in the file to interact with the database **Do not touch this variable**
  3. tblSet: this vairable local stores the database table names in the databaseManagement file, it is used to speed up tables searches and error handling.
  4. lineNo: this is used by the insertFile function to keep track which line in the file the function reached to prevent repeated data being entered into the database.

The class also contains methods not accessed by the user. This methods are:
  - dbClose: closes the current session to the database
  - setTblSet: this sets the tblSet variable 
  - getTables: this gets all the tables in the database
  - getColumns: gets all the columns from a specified table, this is used for validation wihtin methods like selectOnConditon
  - count_db_enteries: this counts the number of rows of data inside a table, utilised by the backend algorthirm to generate the timetable

===============
Editing the dbConnection .. _editing-dbConnection
===============

This will explain how to properly edit the dbConnection to get the system running. 

Requirements
-----------
As the user, you will to have these requirements before you can run this part of system. 
(see :ref: 'requirements')
  - pdAdmin locally installed
  - python 

Method
-----------
Once you have the following requiremnts you can follow the instructions below. The code is as follows::

      self.dbConnection = psycopg2.connect(
          host = "localhost",
          dbname = "timetable_gen",
          user = "postgres",
          password = "password",
          port = 5432
      )

The 3 main changes you as the user will need to make are:
  1. host, this needs to match the name the server is stored on.
  2. dbname, this needs to match the name of the database where all the timetable data is being stored on, in your connected server
  3. password, this password is the same password you used to setup pgAdmin, or on the server the database is stored on. 

Both the user and port values should not be changed. However, if you use a different port, the value in the file needs to match the port you use to run the database through. 
