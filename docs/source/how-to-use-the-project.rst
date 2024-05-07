=======================
How to use the Project
=======================
.. _how-to-use-the-project

This area is used to provide various guides on how to use the timetable generator program as intended and avoid various issues.

Getting Data from the Database
===============================

Firstly, you need to navigate though the GUI. 
--> Navigate the GUI

After navigating through the GUI. The user will need to select what data they want to pull from the database.

Selecting All Data
==================

To select all data from a table in the database, the user will need to input the name of the disired table.
To prevent errors, check the Database ERD for the correct spelling of the table name. This will then call the dbManager class and run
the selectAll method.

This will return all the data stored in the queried table.


Selecting Specific Data
========================

