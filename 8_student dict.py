student = {'name': 'Andrew', 'age': 20, 'major': 'MIS', 'hobbies': ['Basketball', 'Disc Golf', 'Fly Fishing']}
    


student['state'] = 'Texas'
student['age'] += 1
for key in student:
     ukey = f'{key.title()}'
     print(f'{ukey}:', student[key])
 