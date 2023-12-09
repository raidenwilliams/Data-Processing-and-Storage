import os

class InMemoryDB:
    def __init__(self):
        self.db = {}
        self.transaction = None

    def get(self, key):
        if key in self.db:
            print("-> Get message: " + str(key) + " " + str(self.db.get(key, None)))
            return self.db.get(key, None)
        if self.transaction is not None and key in self.transaction:
            print("-> Null, transaction in progress")
            return None
        elif key is not self.db and key is not self.transaction:
            print("-> Key " + str(key) + " does not exist in db")
            return None            

    def put(self, key, val):
        if self.transaction is None:
            print("-> No transaction in progress")
        else:
            self.transaction[key] = val
            print("-> Put message: " + key + " " + val)


    def begin_transaction(self):
        if self.transaction is not None:
            print("-> Transaction already in progress")
        else:
            self.transaction = {}
            print("-> Transaction started")

    def commit(self):
        if self.transaction is None:
            print("-> No transaction in progress")
        else:
            print("-> Transaction committed")
            self.db.update(self.transaction)
            self.transaction = None

    def rollback(self):
        if self.transaction is None:
            print("-> No transaction in progress")
        else:
            self.transaction = None
            print("-> Transaction rolled back")


import sys

class Main:
    def __init__(self, db):
        self.db = db

    def transfer(self, account_a, account_b, amount):
        self.db.begin_transaction()
        try:
            balance_a = self.db.get(account_a)
            balance_b = self.db.get(account_b)
            if balance_a is None or balance_b is None:
                print("Account does not exist")
            if balance_a < amount:
                print("Insufficient funds")
            self.db.put(account_a, balance_a - amount)
            self.db.put(account_b, balance_b + amount)
            self.db.commit()
            print("-> Transfer successful" + "from" + account_a + " to " + account_b + 
                        " for $" + amount + " dollars 💵")

        except Exception as e:
            print(f"Error: {e}")
            self.db.rollback()

if __name__ == "__main__":

    # run a script to clear users command line 
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # print welcome message
    print(" ___________________________________")
    print("|                                   |")
    print("|   Welcome to Python World Bank!   |")
    print("|___________________________________|")
    print("")

    # initilize db
    db = InMemoryDB()

    # initilize main
    main = Main(db)

    # print commands
    print(" ___________________________________ ")
    print("|                                   |")
    print("|      Commands are as follows      |")
    print("|___________________________________|")
    print("|                                   |")
    print("| Begin: b                          |")
    print("| Put: p                            |")
    print("| Get: g                            |")
    print("| Commit: c                         |")
    print("| Rollback: r                       |")
    print("| Transfer: t                       |")
    print("| Exit: e                           |")
    print("|___________________________________|")

    while (True):
        command = input("\nInput command:\n")

        if (command == "b"):
            db.begin_transaction()

        elif (command == "p"):
            key = input("Input key: ")
            val = input("Input val: ")
            db.put(key, val)

        elif (command == "g"):
            key = input("Input key: ")
            val = db.get(key)
            
        elif (command == "c"):
            db.commit()

        elif (command == "r"):
            db.rollback()

        elif (command == "t"):
            account_a = input("Input account a: ")
            account_b = input("Input account b: ")
            amount = input("Input amount: ")
            main.transfer(account_a, account_b, amount)

        elif (command == "e"):
            os.system('cls' if os.name == 'nt' else 'clear')
            sys.exit()

        else:
            print("-> Invalid command type")

