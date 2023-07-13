

class Creation:

    def __init__(self):
        pass

    def create_and_populate(cur):
        with open('..\\documents\\contact_creation.sql', 'r') as creation_file:
            creation_query = creation_file.read()

        with open('..\\documents\\contact_insertion.sql', 'r') as insertion_file:
            insertion_query = insertion_file.read()

        cur.execute(creation_query)
        cur.execute(insertion_query)