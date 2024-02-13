student = {'name': 'Andrew', 'age': 20, 'major': 'MIS', 'hobbies': ['Basketball', 'Disc Golf', 'Fly Fishing']}
    
student['state'] = 'Texas'
student['age'] += 1
for key in student:
     ukey = f'{key.title()}'
     if ukey == 'Hobbies':
          print(f'{ukey}: {student[key][0]}, {student[key][1]}, and {student[key][2]}')
     else:          
          print(f'{ukey}: {student[key]}')
