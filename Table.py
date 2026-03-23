from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from Entities import *

#region Database Widgets



# The Table class takes list of IEntity objects and a list of headers and populates a table.
# The table also incluedes a search function that is not case sensitive hides all data that does not match.
class Table(QTableWidget):  
    def __init__(self, records : list[IEntity], headers):
        super().__init__()
        lenHeader = len(headers)
        lenRecords = len(records)
        self.setColumnCount(lenHeader)
        self.setRowCount(lenRecords)
        self.verticalHeader().setVisible(False)
        for header in range(0,lenHeader):
            self.setHorizontalHeaderItem(header,QTableWidgetItem(str(headers[header][0])))
        
        # Converts the database format of the records into table
        for x in range(len(records)):
            record = records[x].GetDataBaseFormat()
            for y in range(0,len(record)):
                self.setItem(x,y,QTableWidgetItem(str(record[y])))
    
    def search(self, string : str):
        if string is not "":
            matches = self.findItems(string,Qt.MatchFlag.MatchContains)
            for rows in range(0,self.rowCount()):
                self.hideRow(rows)
            for match in matches:
                self.showRow(match.row())


    def UpdateTable(self, records : list[IEntity], headers):
        self.clear()
        lenHeader = len(headers)
        lenRecords = len(records)
        self.setColumnCount(lenHeader)
        self.setRowCount(lenRecords)
        self.verticalHeader().setVisible(False)
        for header in range(0,lenHeader):
            self.setHorizontalHeaderItem(header,QTableWidgetItem(str(headers[header][0])))
        
        # Converts the database format of the records into table
        for x in range(len(records)):
            record = records[x].GetDataBaseFormat()
            for y in range(0,len(record)):
                self.setItem(x,y,QTableWidgetItem(str(record[y])))
        

        

        

#endregion 
