from requests import get, post

# print(get('http://localhost:5000/api/v2/jobs').json())
# print(get('http://localhost:5000/api/v2/jobs/1').json())
# print(get('http://localhost:5000/api/v2/jobs/100').json())

# print(get('http://localhost:5000/api/v2/users').json())
# print(get('http://localhost:5000/api/v2/users/1').json())
# print(get('http://localhost:5000/api/v2/users/100').json())

# print(post('http://localhost:5000/api/v2/users', json={}).json())  # нет словаря
# print(post('http://localhost:5000/api/v2/users', json={'name': 'Sonya'}).json())  # не все поля
print(post('http://localhost:5000/api/v2/users', json={'name': 'Sonya', 'position': 'junior programmer',
                                                       'surname': 'Wolf', 'age': '17', 'address': 'module_3',
                                                       'speciality': 'computer sciences',
                                                       'hashed_password': 'wolf', 'email': 'wolf10@mars.org'}).json())
