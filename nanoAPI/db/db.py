import sqlite3
from nano.utils import err


class DB:
    def __init__(self, models):
        self.server = sqlite3.connect('database.db')
        self.admin = self.server.cursor()
        self.models = models
        for model in self.models:
            model.table_name = model.__name__.lower()

    def is_booted(self):
        is_booted = False
        for model in self.models:
            self.admin.execute(
                f"SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{model.__name__.lower()}'")
            if self.admin.fetchone()[0]:
                is_booted = True
        return is_booted

    def boot(self):
        fields = "id INT PRIMARY KEY NOT NULL"
        for model in self.models:
            for field in model.get_fields():
                fields = fields + ", " + field
            try:
                self.admin.execute(
                    f"CREATE TABLE {model.__name__.lower()} ({fields})")
            except sqlite3.OperationalError:
                print(err("MODEL", f"Model {model.__name__} already booted"))
            fields = "id INT PRIMARY KEY NOT NULL"
        self.server.commit()

    def __del__(self):
        self.admin.close()
        self.server.close()
