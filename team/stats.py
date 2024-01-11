### Imports ###
# Global #
import sqlite3
from datetime import datetime
# Local #
from basics import Basics
### Code ###
class Manager:
    def __init__(self, dbPath:str) -> None:
        self.connection = sqlite3.connect(dbPath)
        self.cursor = self.connection.cursor()

    def insertRecord(self, table:str, values:list[int|float]) -> bool:
        """Insert a records into the database
        
        Params:
            table:str = the name of the table to insert into
            value:list = a list of values (int|float) to insert into the row

        Returns:
            True = sucessful
            False = falure
        """
        tab_values:str = ",".join(str(item) for item in values)
        statement:str = f"INSERT INTO {table} VALUES ({tab_values})"
        print(statement)
        self.cursor.execute(statement)
        self.connection.commit()

### Main ###
if __name__ == "__main__":
    arguments = Basics.Terminal.Arguments()
    manager = Manager("stats.db")
    if arguments.find("--add") != None:
        arguments.run("--add", print)
        now = datetime.now(); year = now.year; month = now.month; day = now.day
        date = [int(f"{year:04d}{month:02d}{day:02d}")]
        points:list[float] = [float(val) for val in arguments.find("--add").split(',')]
        to_insert:list[int|float] = date+points
        manager.insertRecord('main', to_insert)
    elif arguments.find("--date") != None:
        now = datetime.now(); year = now.year; month = now.month; day = now.day
        date = f"{year:04d}{month:02d}{day:02d}"
        print(date)
    else:
        # ask using input
        pass