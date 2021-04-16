    
books = [{
    'id': 0,
    'title': 'A Fire Upon the Deep',
    'author': 'Vernor Vinge',
    'first_sentence': 'The coldsleep itself was dreamless.',
    'year_published': '1992'
  },
  {
    'id': 1,
    'title': 'The Ones Who Walk Away From Omelas',
    'author': 'Ursula K. Le Guin',
    'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
    'published': '1973'
  },
  {
    'id': 2,
    'title': 'Dhalgren',
    'author': 'Samuel R. Delany',
    'first_sentence': 'to wound the autumnal city.',
    'published': '1975'
  } 
]

from flask import Flask, render_template, abort, redirect, request, flash, url_for
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/books', methods=['GET'])
def listBooks():
  return jsonify(books)



@app.route('/book/<id>', methods=['GET'])
def listBook(id):

  return jsonify(books[int(id)]) if int(id) < len(books) else  abort(404, description="Page not found.")

@app.route('/add', methods=('GET', 'POST'))
def addBook():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        fSent = request.form['fSent']
        published = request.form['published']

        if not title:
            flash('Title is required!')
        else:
            book = {
                'id': len(books),
                'title': title,
                'author': author,
                'first_sentence': fSent,
                'year_published': published
                }
            books.append(book)
            return redirect(url_for('listBooks'))

    return render_template('addBook.html')


@app.errorhandler(404)
def page_not_found(e):
    return '<h1>404</h1><p>Page could not be found.</p>'