from requests import get, post, delete
import datetime

# print(get('http://localhost:5000/api/jobs').json())
# print(get('http://localhost:5000/api/jobs/1').json())
# print(get('http://localhost:5000/api/jobs/q').json())
# print(post('http://localhost:5000/api/jobs', json={}).json())
#
# print(post('http://localhost:5000/api/jobs',
#            json={'job': 'zxccvxvc'}).json())

# print(post('http://localhost:5000/api/jobs',
#            json={'job': 'ouidoufgiofgioi',
#                  'team_leader': 1,
#                  'work_size': 12,
#                  'collaborators': '1, 2',
#                  'start_date': '2023-03-11 12:37:40',
#                  'end_date': '2024-01-10 14:07:05',
#                  'is_finished': False}).json())

print(delete('http://localhost:5000/api/jobs/999').json())
# новости с id = 999 нет в базе

print(delete('http://localhost:5000/api/jobs/1').json())
