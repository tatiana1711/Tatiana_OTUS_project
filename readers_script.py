
import os
from csv import DictReader
import json


def get_path(file_name)

    work_folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(work_folder, file_name)


CSV_FILE = get_path('books.csv')
JSON_FILE = get_path('users.json')
JSON_FILE_W = get_path('result.json')


with open(JSON_FILE, r) as f
    users = json.load(f)

books = []
with open(CSV_FILE, newline='') as f
    readers = DictReader(f)
    for row in readers
        books.append(row)

data = []

for p in users
    data.append({
        'name' p['name'],
        'gender' p['gender'],
        'address'  p['address'],
        'age' p['age'],
        'books' []
    })


for i in range(0, len(books))
    data[i % len(users)]['books'].append({
        title books[i][Title],
        author books[i][Author],
        pages books[i][Pages],
        genre books[i][Genre]
    })

with open(JSON_FILE_W, w) as f
    s = json.dumps(data, indent=4)
    f.write(s)