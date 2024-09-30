from flask import request
from flask_restful import Resource
from models import Book 
from extensions import db
from flask import abort

class BookResource(Resource):
    def get(self, book_id=None):
        if book_id is None:
            # Получаем все книги
            books = Book.query.all()
            return [{"id": book.id, "title": book.title, "author": book.author} for book in books]
        else:
            # Получаем книгу по ID
            book = Book.query.get(book_id)
            if book is None:
                abort(404, description="Book not found")
            return {
                "message": "book found",
                "book": {
                    "id": book.id,
                    "title": book.title,
                    "author": book.author
                }
            }, 200
            
    def post(self):
        data = request.get_json()
        new_book = Book(title=data['title'], author=data['author'])
        db.session.add(new_book)
        db.session.commit()
        
        return {
            "message": "Book created",
            "book": {
                "id": new_book.id,
                "title": new_book.title,
                "author": new_book.author
            }
        }, 201
        
    def put(self, book_id):
        data = request.get_json()
        book = Book.query.get(book_id)

        if not book:
            return {"message": "Book not found"}, 404

        book.title = data.get('title', book.title)
        book.author = data.get('author', book.author)
        db.session.commit()

        return {"message": "Book updated", "book": {"id": book.id, "title": book.title, "author": book.author}}, 200

    def delete(self, book_id):
        book = Book.query.get(book_id)

        if not book:
            return {"message": "Book not found"}, 404

        db.session.delete(book)
        db.session.commit()

        return {"message": "Book deleted"}, 200
