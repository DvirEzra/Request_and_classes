import json
import requests

url = 'https://jsonplaceholder.typicode.com/users'
res = requests.get(url)

class MyUser:
    def __init__(self, id, email, username, name):
        self.id = id
        self.email = email
        self.username = username
        self.name = name

    def __str__(self):
        return f"The ID {self.id}\nThe Name is: {self.name}\nThe UserName is {self.username}\nThe Email: {self.email}\n"

users_dict = res.json()

while True:
    name = input('Enter Your Full Name : ').title()

    found_user = False
    for user_dict in users_dict:
        if name == user_dict['name']:
            my_user = MyUser(user_dict['id'], user_dict['email'], user_dict['username'], user_dict['name'])
            print(my_user)
            found_user = True
            break

    if not found_user:
        print('User not found')
