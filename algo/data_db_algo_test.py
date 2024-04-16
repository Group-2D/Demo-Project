

from databaseManager import dbManager

def get_modules_tbl(session):

    session.setTblSet()

    for table in session.tblSet:
        session.selectAll(table)
        priint(session.fetchall())






def main():

    session = dbManager()

    get_modules_tbl(session)