import json

from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


@app.route('/')
def hello_world():
    return 'hello test'


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)


@app.route('/api/v1/hello_world')
def h_world():
    return 'Hello!'


@app.route('/api/v1/resources/books/<int:book_id>', methods=['GET', 'POST'])
def bookss(book_id):
    if request.method == "GET":
        for x in books:
            if x['id'] == book_id:
                return jsonify(x)
        return "Not found"
    if request.method == "PUT":
        return "Book is added"


if __name__ == '__main__':
    app.run()
