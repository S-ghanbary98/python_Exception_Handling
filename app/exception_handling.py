



class FileLocation:
    def __init__(self, filename):
        self.checker(filename)



    def checker(self, filename):
        try:

            file = open(filename)
            print("File found")
            print(file.read())
        except FileNotFoundError as errmsg:

            print(f"File not Found {errmsg}")  # prints the error message.
            f = open("order.txt", "x")
            fruits = input("name 3 fruits:: ")
            f.write(fruits)

        finally:  ## finally will execute regardless of try/except block
            print("Thanks for trying, See you again!!!")

