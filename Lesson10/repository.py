import sqlite3
class Repository:
    def __init__(self, database: str, timeout: float):
        self.Database: str = database
        self.TimeOut: float = timeout
    def Query(self, sQueary: str):
        try:
            connection = sqlite3.connect(self.Database, self.TimeOut)
            cursor = connection.cursor()
            cursor.execute(sQueary)
            connection.commit()
        except:
            raise
        finally:
            connection.close()