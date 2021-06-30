



class FileReaderWriter:
    def __init__(self, filename):
        self.file_read(filename)
        self.filename = filename



    def file_read(self, filename):
        try:
            file = open(filename)
            print("File found")
            print("Contents of {}: {}".format(filename, file.read()))
            content = file.read()

        except FileNotFoundError as errmsg:
            print(f"File not Found {errmsg}")  # prints the error message.

        finally:  ## finally will execute regardless of try/except block
            print("Thanks for trying, See you again!!!")


    def file_write(self):
        file = open(self.filename)
        content = file.read()
        extra = input("What do you want to add to order.txt? :")
        file = open('order.txt', 'w')
        file.write(extra + " " + content)

