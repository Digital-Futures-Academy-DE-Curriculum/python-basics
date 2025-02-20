# Handling a CSV file (.csv) - use the in-built csv module
import csv

data_file_path = "demo_files/data.csv"
separator = "-" * 50

# Open and print an entire CSV file
with open(data_file_path, "r") as file:
    data = csv.reader(file)
    for row in data:
        print(row)

print(separator)

print(data)

# Open and read in a CSV file line by line to a list
csv_data = []
with open(data_file_path, "r") as file:
    data = csv.reader(file)
    for row in data:
        csv_data.append(row)

print(csv_data)
print(separator)

for(row) in csv_data:
    print(row)

print(separator)

new_row = ["Newbie", 24, "Data", "London", 80000]

# Add a new row to the CSV file

with open(data_file_path, "a", newline="") as file:
    data = csv.writer(file)
    data.writerow(new_row)

with open(data_file_path, "r") as file:
    data = csv.reader(file)
    for row in data:
        print(row)

print(separator)

# Delete a row from the CSV file
# Read in the file contents
# Remove the row to be deleted
# Write the updated contents back to the file
with open(data_file_path, "r") as file:
    data = csv.reader(file)
    csv_data = [row for row in data]

print(csv_data)
print(separator)

row_to_delete = 6

csv_data.pop(row_to_delete)

print(csv_data)
print(separator)

with open(data_file_path, "w", newline="") as file:
    data = csv.writer(file)
    data.writerows(csv_data)

with open(data_file_path, "r") as file:
    data = csv.reader(file)
    for row in data:
        print(row)

print(separator)

# Isn't this messy!  There must be better ways to work with CSV files!
# We need to find a bear-like solution - Pandas to the rescue (at a later date)!