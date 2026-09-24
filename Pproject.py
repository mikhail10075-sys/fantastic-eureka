student_data = {'id1' : {'name' : 'John', 'class': 'X', 'sub':'Economics'} ,
'id2':{'name' : 'Jake','class':'IX','sub':'Mathematics'},
'id3':{'name' : 'Amy', 'class': 'X', 'sub':'Computer Science'},
'id4':{'name' : 'Janet','class':'VII', 'sub' : 'English'}}

print(student_data)

print(" ")
print('id3 details: ')
print(student_data.get('id3','Not found'))

print(" ")
print('id5 details:')
print(student_data.get('id5', 'Not found'))


student_data['id5'] = {'name' : 'Mary', 'class' : 'X', 'sub':'Computer Applications'}

print(" ")
print('After adding id5')
print(student_data.get('id5', 'Not Found'))

student_data['id2']['subject'] = {'Commerce'}

print(" ")
print("After updating id2's subject")
print(student_data.get('id2', 'subject'))

cleaned_data = {}
seen_records = []

for student_id, details in student_data.items():
    unique_key = (details['name'], details['class'], details['sub'])

    if unique_key not in seen_records:
        seen_records.append(unique_key)
        cleaned_data[student_id] = details
student_data = cleaned_data

print(" ")
print("After removal of duplicates:")
print(student_data)

print(" ")
removed_student = (student_data.pop('id1', 'Student not found'))
print("Removed Student:")
print(removed_student)

print(" ")
print("Total students left", len(student_data))

print(" ")
print('======FINAL STUDENT COUNT======')
for student_id, details in student_data.items():
    print(student_id ,":", details)

print('=================================================================================')