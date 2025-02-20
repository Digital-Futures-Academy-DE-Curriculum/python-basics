import os

# Get the current working directory
cwd = os.getcwd()
print(cwd)

# Construct a path to a file in the current directory
# file_path = os.path.join(cwd, 'file_handling_basics2.py')
# print(file_path)

# Check a file exists
# if os.path.exists(file_path):
#     print("File exists!")
# else:
#     print("404: File Not Found")

# Create a new directory
# os.mkdir('demo_dir')

# Opening a file
demo_file_path = os.path.join(cwd, '..', 'trainer_demo_files', 'demo_files', 'data.txt')
print(demo_file_path)

# if os.path.exists(demo_file_path):
#     print("File exists!")
# else:
#     print("404: File Not Found")
    
file = open(demo_file_path)
# print(file.read())

# Context manager
demo_file_path_2 = os.path.join(cwd, '..', 'trainer_demo_files', 'demo_files', 'data_2.txt')
with open(demo_file_path_2) as file_from_context:
    # print(file_from_context.read()) # Read in the whole file at once
    for line in file_from_context:
    # for i in range(len(file_from_context.readlines())):
        print(file_from_context.readline())
        # print(file_from_context.readline())
        print(line)     # \n
        print("=====")

# print(file.read())
# print(file_from_context.read()) # Context manager closes the file automatically so not available
