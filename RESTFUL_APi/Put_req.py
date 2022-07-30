from urllib import response
import requests
api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
print(response.json())

todo = {"userId": 1, "title": "Wash car", "completed": True}

response = requests.put(api_url,json =todo)
print(response.json())

print(response.status_code)



# Here, you first call requests.get() 
# to view the contents of the existing todo.
# Next, you call requests.put() with new JSON 
# data to replace the existing to-do’s values. 
# You can see the new values when you call response.json(). 
# Successful PUT requests will always return 200 instead of 201 
# because you aren’t creating a new resource but just updating an existing one.