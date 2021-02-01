import sqlite3
from .prop_types import IntegerType, StringType, BooleanType

class Model:

    table_name = str()
    fields = list()
    db_server = sqlite3.connect('database.db')
    db_admin = db_server.cursor()
    id = str()

    def db_handler(self, command):
        self.db_admin.execute(command)
        self.db_admin.commit()
        return self.db_admin.fetchone()

    def save(self):
        return self.db_handler(f"UPDATE {self.table_name} SET {self} WHERE id={self.id}")

    @classmethod
    def create(self, data):
        return self.db_handler(f"INSERT INTO {self.table_name} VALUES ({data})")

    @classmethod
    def find(self, id):
        return self.db_handler(f"SELECT * FROM {self.table_name} WHERE id={id}")

    @classmethod
    def update(self, id, data):
        return self.db_handler(f"UPDATE {self.table_name} SET {data} WHERE id={id}")

    @classmethod
    def delete(self, id):
        self.db_handler(f"DELETE FROM {self.table_name} WHERE id={id}")

    def test(self):
        print(self.table_name)

    @classmethod
    def get_fields(self):
        for field in self.__dict__:
            if ((field.startswith("__") and field.endswith("__"))
                or str(self.__dict__[field]).startswith("<classmethod")
                    or str(self.__dict__[field]).startswith("<function")):
                pass
            else:
                self.fields.append(self.__dict__[field].command)
        print(self.fields)

