from urllib import response
import requests
api_url = "https://jsonplaceholder.typicode.com/todos/10"

#  {"userId": 1, "title": "Wash car", "completed": True}

todo = {"title":"Mow Lawn"}
response = requests.patch(api_url,json=todo)
print(response.json())


# you’ll use requests.patch()  to modify the value of a specific
#  field on an existing todo. PATCH differs from PUT in that it
# doesn’t completely replace the existing resource.
# It only modifies the values set in the JSON sent 
# with the request



