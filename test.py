from requests import get, post, delete

# print(get('http://localhost:5000/api/v2/jobs').json())
# print(get('http://localhost:5000/api/v2/jobs/1').json())
# print(get('http://localhost:5000/api/v2/jobs/q').json())
# print(post('http://localhost:5000/api/users', json={}).json())
#
# print(post('http://localhost:5000/api/users',
#            json={'job': 'zxccvxvc'}).json())
print(post('http://localhost:5000/api/v2/jobs',
           json={'job': 'zxczxczxc',
                 'team_leader': 2,
                 'work_size': 2,
                 'collaborators': '1, 3',
                 'is_finished': True
                 }).json())
#
# print(get('http://localhost:5000/api/users/5').json())
#
# print(post('http://localhost:5000/api/users/5',
           # json={'surname': 'norm'}).json())

# print(get('http://localhost:5000/api/users/5').json())
# print(delete('http://localhost:5000/api/users/5').json())
