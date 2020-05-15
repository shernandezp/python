import mysql.connector as mysql
import json

class DataContext:
    db = None
    cursor = None
    def __init__(self):
        self.db = mysql.connect(
            host = "localhost",
            user = "root",
            passwd = "root",
            database = "security"
        )
        self.cursor = self.db.cursor()

    def Get(self, sql):
        self.cursor.execute(sql)
        
        data_json = []
        header = [i[0] for i in self.cursor.description]     #names of the query columns
        records = self.cursor.fetchall()
        for i in records:
            data_json.append(dict(zip(header, i)))

        return data_json

    def GetById(self, sql, val):        
        self.cursor.execute(sql, val)
        
        data_json = None
        header = [i[0] for i in self.cursor.description]
        records = self.cursor.fetchall()
        data_json = dict(zip(header, records[0]))

        return data_json

    def Execute(self, sql, val):
        self.cursor.execute(sql, val)
        self.db.commit()
        return self.cursor.rowcount