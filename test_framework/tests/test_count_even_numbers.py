from test_framework import assert_equals
from count_even_numbers import count_even_numbers

# Arrange
print("count_even_numbers returns 3 for list containing 1-6")
input = [1, 2, 3, 4, 5, 6]
expected_output = 3

# Act
actual_output = count_even_numbers(input)

# Assert
result = assert_equals(actual_output, expected_output)
# Print test passes for True and test fails for False
if result:
    print("Test passes")
else:
    print("Test fails")
print("======")

# Test 2
# Arrange
print("count_even_numbers returns 0 for list containing 1, 3 and 5")
input = [1, 3, 5]
expected_output = 0

# Act
actual_output = count_even_numbers(input)

# Assert
result = assert_equals(actual_output, expected_output)
# Print test passes for True and test fails for False
if result:
    print("Test passes")
else:
    print("Test fails")
print("======")

# Test 3
# Arrange
print("count_even_numbers returns 2 for list containing 0, 1, 2, 3")
input = [0, 1, 2, 3]
expected_output = 2

# Act
actual_output = count_even_numbers(input)

# Assert
result = assert_equals(actual_output, expected_output)
# Print test
if result:
    print("Test passes")
else:
    print("Test fails")
print("======")

# Test 4
# Arrange
print("count_even_numbers returns 0 for empty list")
input = []
expected_output = 0

# Act
actual_output = count_even_numbers(input)

# Assert
result = assert_equals(actual_output, expected_output)
# Print test
if result:
    print("Test passes")
else:
    print("Test fails")
print("======")