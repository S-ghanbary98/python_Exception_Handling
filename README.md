# Working with Files

## Exception Handling

#### Example of errors
-  `value error`
- `syntax error`
- `out of bounds`
- `key error`
- `attribute error`
- `ZeroDivisionError`

#### File Permissions
- `r` This is the default mode. It opens a file for reading.
- `w` This mode opens file for writing. If file doesn't exist it creates a new file for us. If file exists it deletes the data for us.
- `x` Creates a new file, if it already exists the operation fails.
- `a` Opens file in Append Mode, if file doesn't exist it creates a new one.
- `t` Default mode to open in text mode.
- `b` This is for binary mode.
- `+` This will open file for reading and writing(updating).


**We have `try` `except` and `finally`**
- `try` works as `if condition`
- `except` works as `elif`
- `finally` works as else, finally will execute regardless of `try` or `except` conditions

```python
try:
    file = open("app/order.txt")
    print("file found")
except FileNotFoundError as errmsg:
    print(f"File not Found {errmsg}")  # prints the error message.
finally:            ## finally will execute regardless of try/except block
    print("Thanks for trying, See you again")
```

### Exception Handling Package

- FileReaderWriter class takes in `filename` as an arguments.
- Upon creation of an object the file is checked to see if it exists. If not an error message will be displayed.
- Contents of file displayed.

- `file_Write` function allows user to add extra information to file.

```python
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

```
##### Running the file (program.py)
```python
from app.exception_handling import FileReaderWriter

test = FileReaderWriter("order.txt") # initialises object and looks for order.txt file. If it exists the contents will be printed.
test.file_write()   # allows user to add extra info to order.txt

print(test)
```