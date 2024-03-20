from requests import get, post, delete
import datetime

# print(get('http://localhost:5000/api/users').json())
# print(get('http://localhost:5000/api/users/1').json())
# print(get('http://localhost:5000/api/users/q').json())
# print(post('http://localhost:5000/api/users', json={}).json())
#
# print(post('http://localhost:5000/api/users',
#            json={'job': 'zxccvxvc'}).json())
# print(post('http://localhost:5000/api/users',
#            json={'surname': 'lox',
#                  'name': 'zxc',
#                  'age': 21,
#                  'position': 'cap',
#                  'speciality': 'engineer',
#                  'address': 'module_2',
#                  'email': 'engineer@mars.org',
#                  'hashed_password': ''
#                  }).json())
#
# print(get('http://localhost:5000/api/users/1').json())

print(post('http://localhost:5000/api/users/2',
           json={'surname': 'norm'}).json())

print(get('http://localhost:5000/api/users/2').json())
