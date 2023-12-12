from pydantic import BaseModel
import requests

url = 'https://randomuser.me/api/'
response = requests.get(url)
print(response)
data = response.json()
print(data)

class Name(BaseModel):
    title: str
    first: str
    last: str

class Picture(BaseModel):
    large: str

class UserInfo(BaseModel):
    name: Name
    email: str
    picture: Picture

print("---------------------------------")
print(data['results'][0]['email'])
print("---------------------------------")
print(data['results'][0]['picture'])
photo_url = data['results'][0]['picture']['large']
response_photo = requests.get(photo_url)
with open("user_photo.jpg", 'wb') as f:
    f.write((response_photo.content))

user = data['results'][0]
user_info = UserInfo(**user)
print(user_info)
print(type(user_info))
response_photo_pydantic = requests.get((user_info.picture.large))
with open('user_photo_pydantic.jpg', 'wb') as f:
    f.write(response_photo_pydantic.content)
