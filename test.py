from requests import get, post, delete
import datetime

# print(get('http://localhost:5000/api/jobs').json())
# print(get('http://localhost:5000/api/jobs/4').json())
# print(get('http://localhost:5000/api/jobs/q').json())
# print(post('http://localhost:5000/api/jobs', json={}).json())
#
# print(post('http://localhost:5000/api/jobs',
#            json={'job': 'zxccvxvc'}).json())

print(post('http://localhost:5000/api/jobs/3',
           json={'team_leader': 2,
                 'work_size': 10,
                 'is_finished': True}).json())
print(get('http://localhost:5000/api/jobs/3').json())

# print(delete('http://localhost:5000/api/jobs/999').json())
# # новости с id = 999 нет в базе
#
# print(delete('http://localhost:5000/api/jobs/4').json())
