#!/usr/bin/env python3

print('The first method:')
with open('learnning_python.txt') as file_object:
    print(file_object.read())

print("\nThe second method:")
with open('learnning_python.txt') as file_object:
    for line in file_object:
        print(line.strip())

print("\nThe third method:")
with open('learnning_python.txt') as file_object:
    lines=file_object.readlines()
for line in lines:
    print(line.strip())
    
print("\nThe replace method:")
with open('learnning_python.txt') as file_object:
    lines=file_object.readlines()
for line in lines:
    message=line.replace('python','JAVA')
    print(message.strip())