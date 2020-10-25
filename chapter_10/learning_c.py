# 10-2. Learning C:
filename = 'chapter_10/learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.rstrip()
    print(line.replace('Python', 'C'))