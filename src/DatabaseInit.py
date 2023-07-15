import sqlite3


class DatabaseInit:
    db = sqlite3.connect(':memory:')
    cur = db.cursor()

    def __init__(self):
        pass

    def get_cursor(self):
        return self.cur

    def create_and_populate(self):
        with open('..\\documents\\contact_creation.sql', 'r') as creation_file:
            creation_query = creation_file.read()

        with open('..\\documents\\contact_insertion.sql', 'r') as insertion_file:
            insertion_query = insertion_file.read()

        self.cur.execute(creation_query)
        self.cur.execute(insertion_query)