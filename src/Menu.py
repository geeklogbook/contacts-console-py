from CRUD import *


class Menu:
    crud_instance = CRUD()

    def __init__(self):
        option = ""
        while option != 'F':
            self.render_menu()
            option = self.get_option()
            self.call_function(option)

    def render_menu(self):
        self._print_box()

    def get_option(self) -> str: 
        option = input("What is your option [Select a valid letter]: ")
        option = option.upper()
        while option not in ("A", "B", "C", "D", "E", "F"):
                option = input("What is your option [Select a valid letter]: ")
                option = option.upper()
        return option

    def call_function(self ,option):
        if option == "A":
             first_name = input("Enter First name: ")
             last_name = input("Enter Last Name: ")
             email = input("Enter Email: ")
             phone = input("Enter Phone Number: ")
             self.crud_instance.create(first_name, last_name, email, phone)
        elif option == "B":
             self.crud_instance.read()            
        elif option == "C":
             last_name = input("Enter the last Name: ")
             self.crud_instance.read(last_name)
        elif option == "D":
            field_to_change = input("Field to Change: ")
            old_value = input("old Value: ")
            new_value = input("New Value: ")
            self.crud_instance.update(field_to_change, old_value, new_value)
        elif option == "E":
            last_name = input("Enter the last Name: ")
            self.crud_instance.delete(last_name)
            
    
    def _print_box(self):
        print("**********************************")
        print("*        MENU                    *")
        print("* A - CREATE contact             *")
        print("* B - READ all data in contacts  *")
        print("* C - READ contact by Last Name  *")
        print("* D - UPDATE contact             *")
        print("* E - DELETE contact             *")
        print("* F - EXIT                       *")
        print("**********************************")
