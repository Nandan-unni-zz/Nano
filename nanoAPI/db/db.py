import sqlite3
from nanoAPI.utils import err, msg
from .model import Model


class DB:
    def __init__(self):
        self.server = sqlite3.connect('database.db')
        self.admin = self.server.cursor()
        self.models = []

    def set_models(self, *args):
        self.models.extend(args)
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
            print("\n", msg("BOOT", f"Model {model.__name__}"))
            if issubclass(model, Model):
                for field in model.get_fields():
                    fields = fields + ", " + field.command
                    print(f"\t  - {field.name}")
                try:
                    self.admin.execute(
                        f"CREATE TABLE IF NOT EXISTS {model.table_name} ({fields})")
                except sqlite3.OperationalError:
                    print(
                        err("MODEL", f"Error in booting {model.__name__} model"))
                fields = "id INT PRIMARY KEY NOT NULL"
            else:
                print(
                    err(model.__name__, f"Models must be an instance of *nanoAPI.db.model.Model*"))
        self.server.commit()

    def __del__(self):
        self.admin.close()
        self.server.close()
