
from flask import Flask, request

app = Flask(__name__)

books = []

@app.route('/')

def hello() :
    q = request.args.get ('q')
    print(q)
    return {"message":"Hello!"}

@app.route('/book',methods=['POST','GET','PUT','DELETE'])
def book():
    if request.method == 'POST' :
        #แปลงเป็น dictionary
        body = request.get_json()
        books.append(body)
        return{"message":"Book already add to database","body":body},201
    elif request.method == 'GET':
        return {"book":books},200
    elif request.method == 'PUT':
        body = request.get_json()
        for i,book in enumerate(books):
            if book['id'] == body['id']:
                book[i] = body
            return {"message":"Book has been replace","body": body},200
    ''' elif request.method == 'DELETE':
        deleteID = request.args.get('ID')
        for i, book in enumerate(books):
            if book['id']'''
if __name__ == '__main__' :
    app.run(debug = True)
