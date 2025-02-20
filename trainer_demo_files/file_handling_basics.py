# Working with the file system in Python
import os

# Get the current working directory
print("Current Working Directory: ", os.getcwd())

# Constructing a file path

# Concatenate Paths Manually
file_path = os.getcwd() + "/data.txt"


# Using os.path.join - correctly formats dependent on OS (Windows, Linux, macOS)
file_path = os.path.join(os.getcwd(), "data.txt")
# BETTER!

# Check if a file exists
if os.path.exists(file_path):
    print("File Exists")

# Make a new directory
os.mkdir("new_directory", exist_ok=True)  # exist_ok=True prevents error if directory already exists

# Open a file
opened_file = open(file_path).read()
print(opened_file)

with open(file_path) as file:
    # Do stuff with the file
    print(file.read())

print(file)
# What is the `with` thing all about? Its a context manager
# It automatically closes the file when the block is exited
print(opened_file)

# Close the open file
opened_file.close()