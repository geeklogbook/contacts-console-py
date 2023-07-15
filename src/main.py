from Menu import *
from CRUD import *

if __name__ == "__main__":
    DatabaseInit().create_and_populate()
    Menu()