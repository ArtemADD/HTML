from requests import get, post, delete

# print(get('http://localhost:5000/api/users').json())
# print(get('http://localhost:5000/api/users/1').json())
# print(get('http://localhost:5000/api/users/q').json())
# print(post('http://localhost:5000/api/users', json={}).json())
#
# print(post('http://localhost:5000/api/users',
#            json={'job': 'zxccvxvc'}).json())
# print(post('http://localhost:5000/api/users',
#            json={'surname': '123',
#                  'name': '123',
#                  'age': 1,
#                  'position': '123',
#                  'speciality': '123',
#                  'address': '123',
#                  'email': '123@mars.org',
#                  'hashed_password': '123'
#                  }).json())
#
# print(get('http://localhost:5000/api/users/5').json())
#
# print(post('http://localhost:5000/api/users/5',
           # json={'surname': 'norm'}).json())

# print(get('http://localhost:5000/api/users/5').json())
print(delete('http://localhost:5000/api/users/5').json())
