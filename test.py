import requests

BASE = "http://127.0.0.1:5000/"

data = [{"name": "Video1", "likes": 78, "views": 100000},
        {"name": "Video2", "likes": 1050, "views": 800000},
        {"name": "Video3", "likes": 35, "views": 5000}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())


input()
response = requests.patch(BASE + "video/2", {"views":99})
print(response.json())

input()
response = requests.delete(BASE + "video/1")
print(response)