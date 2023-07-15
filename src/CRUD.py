from DatabaseInit import *


class CRUD():
    cur = DatabaseInit().get_cursor()

    def __init__(self):
        pass

    def create(self,first_name, last_name, email, phone):
        self.cur.execute(f'''INSERT INTO contact(first_name,last_name,email,phone) VALUES("{first_name}","{last_name}","{email}","{phone}")''')
        return 0

    def read(self, last_name=""):
        if last_name == "":
            self.cur.execute('''SELECT * FROM contact''')
        else:
            self.cur.execute(f'''SELECT * FROM contact WHERE last_name ="{last_name}"''')
        data = self.cur.fetchall()
        for e in data:
            print(e)
        
    def update(self, field_to_change, old_value, new_value):
        if field_to_change == 'first_name':
            self.cur.execute(f'''UPDATE contact SET first_name="{new_value}" WHERE first_name ="{old_value}"''')
        elif field_to_change == 'last_name':
            print("update last name")
        elif field_to_change == 'email':
            print("update email")
        elif field_to_change == 'phone':
            print("update phone")

    def delete(self, last_name):
        self.cur.execute(f'''DELETE FROM contact WHERE last_name ="{last_name}"''')