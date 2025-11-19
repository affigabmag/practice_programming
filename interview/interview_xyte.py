#implement the find methid in class Connect.
#upon providing id, it will return the whole row from database object.
#https://gist.githubusercontent.com/borisd/1e1ec1c3a536a34ea24b9096f3cd2819/raw/2db6a932eaf68c10f2ab55e967eab257c463f69b/question.py

MAX_CACHE_SIZE = 3

# TODO: Implement this
class Connect:
    def __init__(self, db):
        pass        

class DataBase:
    def __init__(self, data):
        self.__data = data

    def get(self, id):
        print(' -- DB Access for: ', id)
        return self.__data[id]
        
    def update(self, id, field, value):
        print(' -- DB Update for: ', id)
        self.__data[id][field] = value


db = DataBase(
    {
        1: { "price": 13, "age": 100 },
        2: { "price": 43, "height": 200 },
        3: { "age": 2, "name": "David", "price": 21 },
        4: { "age": 77, "name": "Haim", "price": 20 }
    }
)

def run_tests():
    orm = Connect(db)

    # Get price of #2 record
    print("Price:", orm.find(2).price)
    
    return # Move me as we progress in implementation

    # Read the height from cache
    print("Height:", orm.find(2).height)

    # Update DB
    db.update(2, "price", 100)

    # Return cached price
    print("Price:", orm.find(2).price)

    # Reload cache
    print("Price:", orm.find(2).reload().price)

    orm.clear()

    print("Check cache limitation")
    orm.find(1).price
    orm.find(2).price
    orm.find(1).price
    orm.find(3).price
    orm.find(4).price
    orm.find(3).price
    orm.find(1).price
    orm.find(2).price
    orm.find(3).price
    orm.find(4).price

run_tests()