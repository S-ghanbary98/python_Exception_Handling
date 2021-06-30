# print(1/0) # ZeroDivisionError


# We will create a file with required Permissions and see what errors/exception are possible

# First iterations
#file = open("order.txt")  # open() takes string argument of file name.
#print(file)  # Produces an FileNotFoundError


# Second Iteration
try:
    file = open("app/order.txt")
    print("file found")
except FileNotFoundError as errmsg:
    print(f"File not Found {errmsg}")  # prints the error message.
finally:            ## finally will execute regardless of try/except block
    print("Thanks for trying, See you again")



# Let's Create a file called order.txt - naming is essential


# Let's apply DRY - OOP - Python Packaging
            #  1     2            3

