import sqlite3
from ..utils import err
from .types import IntegerType, StringType, BooleanType

def sqlcommand(method):
    def wrapper(self, *args, **kwargs):
        try:
            return method(self, *args, **kwargs)
        except sqlite3.OperationalError as sql_err:
            if str(sql_err).startswith("no such table:"):
                print(err("MODEL", "No such table. Please boot your models."))
            else:
                print(err("MODEL", str(sql_err)))
            return None
    return wrapper

class Model:

    table_name = str()
    fields = list()
    __db_server__ = sqlite3.connect('database.db')
    __db_admin__ = __db_server__.cursor()
    id = str()

    @classmethod
    @sqlcommand
    def save(self):
        return self.__db_admin__.execute(f"UPDATE {self.table_name} SET {self} WHERE id={self.id}")

    @classmethod
    @sqlcommand
    def create(self, data):
        return self.__db_admin__.execute(f"INSERT INTO {self.table_name}{self.__data_dictor__(data)}")

    @classmethod
    @sqlcommand
    def find(self, id: str):
        self.__db_admin__.execute(f"SELECT * FROM {self.table_name} WHERE id={id}")
        return self.__data_undictor__(self.__db_admin__.fetchone())


    @classmethod
    def get_fields(self):
        self.fields.clear()
        for field in self.__dict__:
            if ((field.startswith("__") and field.endswith("__"))
                or str(self.__dict__[field]).startswith("<classmethod")
                or str(self.__dict__[field]).startswith("<function")
                    or field == "table_name"):
                pass
            else:
                self.fields.append(self.__dict__[field])
        return self.fields
    
    @classmethod
    def __data_dictor__(self, data: dict) -> str:
        field_names = [field.name for field in self.get_fields()]
        fields = "("
        values = "("
        for data_item_name in data:
            if data_item_name in field_names:
                fields += data_item_name + ", "
                if type(data[data_item_name]) == str:
                    values += "'" + data[data_item_name] + "', "
                elif type(data[data_item_name]) == int:
                    values += str(data[data_item_name]) + ", "
                elif type(data[data_item_name]) == bool:
                    values += "1, " if data[data_item_name] else "0, "
        if fields.endswith(", "): fields = fields[:-2]
        if values.endswith(", "): values = values[:-2]
        return fields + ") VALUES " + values + ")"
    
    @classmethod
    def __data_undictor__(self, data) -> dict:
        field_names = [field.name for field in self.get_fields()]
        dict_data = {}
        for item in data:
            if not data.index(item) == 0:
                dict_data[field_names[data.index(item) - 1]] = item
        return dict_data
