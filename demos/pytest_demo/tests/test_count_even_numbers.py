from src.list_utils import count_even_numbers

def test_count_even_numbers_returns_3_for_1_6_list():
    # Arrange
    input = [1, 2, 3, 4, 5, 6]
    expected_output = 3
    
    # Act
    actual_output = count_even_numbers(input)
    
    # Assert
    assert actual_output == expected_output
    
def test_count_even_numbers_returns_0_for_1_3_list():
    # Arrange
    input = [1, 3]
    expected_output = 0
    
    # Act
    actual_output = count_even_numbers(input)
    
    # Assert
    assert actual_output == expected_output
