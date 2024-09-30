from flask import Flask
from flask_restful import Api
from resources.book import BookResource
from extensions import db, migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  
migrate.init_app(app, db)  

api = Api(app)

api.add_resource(BookResource, '/book', '/book/<int:book_id>')

if __name__ == '__main__':
    app.run(debug=True)