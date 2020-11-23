from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid



# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'Atlas Shrugged',
        'author': 'Ayn Rand',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        data = request.json
        print(request.json)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': data['title'],
            'author': data['author'],
            'read': data['read']
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)

@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        data = request.json
        remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': data['title'],
            'author': data['author'],
            'read': data['read']
        })
        response_object['message'] = 'Book updated!'
    if request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)

def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False

if __name__ == '__main__':
    app.run()

# curl -X POST http://localhost:5000/books -d "{\"title\": \"1Q84\", \"author\": \"Haruki Murakami\", \"read\": true}" -H 'Content-Type:application/json'