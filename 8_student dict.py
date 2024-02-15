student = {'name': 'Andrew', 'age': 20, 'major': 'MIS', 'hobbies': ['Basketball', 'Disc Golf', 'Fly Fishing']}
    
student['state'] = 'Texas'
student['age'] += 1
for key in student:
     u_key = f'{key.title()}'
     if u_key == 'Hobbies':
          print(f'{u_key}: {student[key][0]}, {student[key][1]}, and {student[key][2]}')
     else:          
          print(f'{u_key}: {student[key]}')
