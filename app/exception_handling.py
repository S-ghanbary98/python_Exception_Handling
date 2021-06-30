

class FileReaderWriter:
    def __init__(self, filename):
        self.filename = filename
        self.file_read()




    def file_read(self):
        try:
            file = open(self.filename)
            print("File found")
            print("Contents of {}: {}".format(self.filename, file.read()))
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

