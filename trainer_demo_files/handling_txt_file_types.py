# Handling a text file (.txt)

data_file_path = "demo_files/data.txt"
separator = "-" * 50

# Open and read in an entire text file
print("READ AN ENTIRE TEXT FILE")
with open(data_file_path, "r") as file:
    data = file.read()
    print(data)

print(separator)
    
# Open and read in a text file line by line
print("READ A TEXT FILE LINE BY LINE")
text_in_file = []
with open(data_file_path, "r") as file:
    for line in file:
        print(line)
        text_in_file.append(line)

print(separator)

print("ACCESS TEXT FILE CONTENTS FROM THE STORED LIST")

for line in text_in_file:
    print(line)

print(separator)

# Write to the end of a text file
print("WRITE TO THE END OF A TEXT FILE")
with open(data_file_path, "a") as file:
    file.write("Line 6: A new line written to the file\n")
    file.write("Line 7: Another new line written to the file\n")
    # file.read()  # This will throw an error because the file is open for writing, not reading
    
with(open(data_file_path, "r")) as file:
    print(file.read())

print(separator)

# Overwrite a text file
print("OVERWRITE A TEXT FILE")
with open(data_file_path, "w") as file:
    file.write("Line 1: This is the first line of the file.\n")
    file.write("Line 2: Python makes file handling easy.\n")
    file.write("Line 3: Understanding file paths is crucial.\n")
    file.write("Line 4: Context managers ensure resource safety.\n")
    file.write("Line 5: End of the demo text file.")

with(open(data_file_path, "r")) as file:
    print(file.read())

print(separator)