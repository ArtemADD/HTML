from requests import get, post, delete

# print(get('http://localhost:5000/api/v2/jobs').json())
# print(get('http://localhost:5000/api/v2/jobs/1').json())
# print(get('http://localhost:5000/api/v2/jobs/q').json())
# print(post('http://localhost:5000/api/v2/jobs', json={}).json())
#
# print(post('http://localhost:5000/api/v2/jobs',
#            json={'job': 'zxccvxvc'}).json())
# print(post('http://localhost:5000/api/v2/jobs',
#            json={'job': 'zxczxczxc',
#                  'team_leader': 2,
#                  'work_size': 2,
#                  'collaborators': '1, 3',
#                  'is_finished': True
#                  }).json())
# print(delete('http://localhost:5000/api/v2/jobs/'))

print(get('http://localhost:5000/api/v2/users').json())
print(get('http://localhost:5000/api/v2/users/1').json())
# print(get('http://localhost:5000/api/v2/users/q').json())
print(post('http://localhost:5000/api/v2/users', json={}).json())

print(post('http://localhost:5000/api/v2/users',
           json={'surname': 'zxccvxvc'}).json())
print(post('http://localhost:5000/api/v2/users',
           json={'surname': 'zxczxczxc',
                 'name': 'asd',
                 'age': 23,
                 'position': 'dhll',
                 'speciality': 'qwerty',
                 'address': 'address',
                 'email': 'emai@g.com',
                 'hashed_password': '123'
                 }).json())
# print(delete('http://localhost:5000/api/v2/users/5'))
