from DatabaseInit import *


class CRUD():
    cur = DatabaseInit().get_cursor()

    def __init__(self):
        pass

    def create(self,first_name, last_name, email, phone):
        self.cur.execute(f'''INSERT INTO contact(first_name,last_name,email,phone) VALUES("{first_name}","{last_name}","{email}","{phone}")''')
        self.cur.execute('''SELECT * FROM contact''')
        data = self.cur.fetchall()
        for e in data:
            print(e)

    def read(self, last_name=""):
        if last_name == "":
            self.cur.execute('''SELECT * FROM contact''')
        else:
            self.cur.execute(f'''SELECT * FROM contact WHERE last_name ="{last_name}"''')
        data = self.cur.fetchall()
        for e in data:
            print(e)
        
    def update(self):
        pass
    def delete(self):
        pass