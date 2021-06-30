from app.exception_handling import FileReaderWriter



test = FileReaderWriter("order.txt")
test.file_write()

print(test)