def assert_equals(value1, value2) -> bool:
    return value1 == value2

def assert_true(value) -> bool:
    return value == True

def assert_greater_than(value1: int, value2: int) -> bool:
    if type(value1) != int or type(value2) != int:
        return TypeError("At least one value was not an integer")
    return value1 > value2

# print(assert_equals(2, 2))
# print(assert_equals(True, False))
# print(assert_equals("Hello", "Hello"))
# print(assert_equals(10, 20))
# print(assert_true((10 < 20)))