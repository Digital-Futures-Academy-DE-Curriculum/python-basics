import requests

def get_url(url: str) -> requests.models.Response | str:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        return f'HTTP error occurred: {http_err}'
    return response

# Old demo

# response = requests.get('https://jsonplaceholder.typicode.com/posts/11')

# # Loop through keys in response object and print
# print(response.text)
# print(response.headers.get('content-type'))
# print(response.status_code)

# response.raise_for_status()
