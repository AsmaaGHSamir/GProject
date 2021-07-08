import sqlite3
import json
import os
#this class reads from DatabaseConf.json file that must be in the same path as this file
class DatabaseLog:
    def __init__(self):
        self._conn=None
        self._cur=None
        self._table_name=None
        try:    #try to read the conf file
            file_dir_path = os.path.dirname(os.path.realpath(__file__)) #the current directory
            f = open('{0}/DatabaseConf.json'.format(file_dir_path),mode="r")
            data = json.load(f) #put what inside json file in data as dictionary
            path = r'{0}'.format(data['db_filename'])
            self._conn = sqlite3.connect(path,check_same_thread=False)
            self._cur = self._conn.cursor()
            self._table_name = data['tabel_name']
        except Exception as e: #if there is any errors will create with the  default values
            self._conn = sqlite3.connect("data.db",check_same_thread=False)
            self._cur = self._conn.cursor()
            self._table_name = "skills"
        self.create_table()


    def create_table(self):
        self._cur.execute("create table if not exists {0} (url text, ip , mac , time)".format(self._table_name))

    def insert_many(self,list_of_tuples):
        self._cur.executemany("insert into {0} values(?, ?, ?, ?)".format(self._table_name), list_of_tuples)
        self._conn.commit()

    def insert_one(self,row_tuple):
        self._cur.execute("insert into {0} values(?, ?, ?, ?)".format(self._table_name), row_tuple)
        self._conn.commit()

    def close(self):
       self._conn.close()

