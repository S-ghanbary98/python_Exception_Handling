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


** We have `try` `except` and `finally` **
- `try` works as `if condition`
- `except` works as `elif`
- `finally` works as else, finally will execute regardless of `try` or `except` conditions