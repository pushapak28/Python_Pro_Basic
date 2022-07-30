import  requests
api_url = "https://jsonplaceholder.typicode.com/todos/21"
response = requests.get(api_url)
print(response.json())
print(response.status_code)
print( response.headers["Content-Type"])

