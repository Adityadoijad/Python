import requests

'''To get the data in the server'''
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code) #200 for success
print(response.url)
# print(response.json())        # JSON response content
print(response.text)
print("\n")



'''to send data to the server, typically for creating or updating resources.'''
redata = {'title': 'foo', 'body': 'bar', 'userId': 1}
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=redata)
print(response.status_code)   # Status code (e.g., 201 for created)
print(response.url)
# print(response.json())        # JSON response content
print(response.text)





print("\n")
'''to update an existing resource on the server.'''
data = {'title': 'Title Changed', 'body': 'Body Changed'}
response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=data)
print(response.status_code)   # Status code 
print(response.url)
# print(response.json())
print(response.text)


'''to delete a resource from the server.'''
print("\n")
response=requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)


'''to download binary data like images or PDFs.'''
print("\n")
response = requests.get('https://via.placeholder.com/150', stream=True)

with open('image.jpg', 'wb') as f:
    for chunk in response.iter_content(chunk_size=1024):
        f.write(chunk)

print('File downloaded successfully')
