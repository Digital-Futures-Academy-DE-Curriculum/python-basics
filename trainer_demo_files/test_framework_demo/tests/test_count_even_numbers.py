from trainer_demo_files.test_framework_demo.testing_framework import assert_equals

print("Testing that [1,2,3,4,5,6] => 3")
# 1. Arrange
input = [1,2,3,4,5,6]
expected_output = 3

# 2. Act
actual_output = count_even_numbers(input)

# 3. Assert
result = assert_equals(actual_output, expected_output)
print(result)

