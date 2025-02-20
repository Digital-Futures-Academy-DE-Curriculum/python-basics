from unittest.mock import patch
from src.http_requests import get_url

def test_get_request():
    # Arrange
    test_url = 'https://www.somerandomname.com'
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = '<html><p>Hello World</p></html>'
        # Act
        response = get_url(test_url)
        # Assert
        assert response.text == '<html><p>Hello World</p></html>'
        assert response.status_code == mock_get.return_value.status_code
        mock_get.assert_called_once_with(test_url)
        