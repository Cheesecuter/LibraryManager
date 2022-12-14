import sqlite3
import _FrozenDir


class Database():
    def __init__(self):
        self.srcPath = _FrozenDir.app_path()+r'\\src'
        dbPath = self.srcPath+r'\\database.db'
        self.conn = sqlite3.connect(dbPath)
        self.cursor = self.conn.cursor()
        self._RowIT = 0
        self._Bno = []
        self._Bname = []
        self._Author = []
        self._Publisher = []
        self._Date = []
        self._Price = []
        self._ROWdata = []
        pass

    def _InitTB_Books(self):
        try:
            self.cursor.execute('''drop table Books''')
        except Exception as e:
            pass
        try:
            self.cursor.execute(
                '''CREATE TABLE "Books" (
	                "Bno"	    TEXT    NOT NULL UNIQUE,
	                "Bname"	    TEXT    NOT NULL,
	                "Author"	TEXT    NOT NULL,
	                "Publisher"	TEXT    NOT NULL,
	                "Date"	    TEXT    NOT NULL,
	                "Price"	    REAL    NOT NULL,
	                PRIMARY KEY("Bno")
                )''')
        except Exception as e:
            pass
        pass

    def _SQL(self, sql, default):
        if(default == True):
            try:
                self.cursor.execute('''''')
                self.conn.commit()
                pass
            except Exception as e:
                pass
            pass
        else:
            try:
                result = self.cursor.execute(sql)
                self.conn.commit()
                return result
            except Exception as e:
                pass
            pass

    def _InitBooksData(self, bno, bname, author, publisher, date, price):
        self._Bno.append(bno)
        self._Bname.append(bname)
        self._Author.append(author)
        self._Publisher.append(publisher)
        self._Date.append(date)
        self._Price.append(price)
        self._ROWdata.append((self._Bno[self._RowIT],
                              self._Bname[self._RowIT],
                              self._Author[self._RowIT],
                              self._Publisher[self._RowIT],
                              self._Date[self._RowIT],
                              self._Price[self._RowIT]))
        print(self._ROWdata[self._RowIT])
        sql = '''insert into Books values'''+str(self._ROWdata[self._RowIT])
        self.cursor.execute(sql)
        self._RowIT = self._RowIT+1
        self.conn.commit()
        pass
