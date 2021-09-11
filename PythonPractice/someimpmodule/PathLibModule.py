from pathlib import Path

# this will return the path of the current dir
# in case we want to operate on different dir then, we need to pass the path as argument
current_dir = Path()
print(current_dir.absolute())


# Get all the files in a directory
print(current_dir.glob("*.py"))

# Loop over all the files
for file in current_dir.glob("*.py"):
    print(file)
