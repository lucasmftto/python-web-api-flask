from flask import Flask, url_for, request
from flask_pymongo import PyMongo
from blog.config import configure

# app = Flask(__name__)
#
# app.config["APP_NAME"] = "My Blog"
# app.config["MONGO_URI"] = "mongodb+srv://mongo:SJjtxZ2MdybhP5no@study.emtthmt.mongodb.net/blog?retryWrites=true&w=majority"
#
# mongo = app.mongo = PyMongo(app)
# # mongo
# # SJjtxZ2MdybhP5no
#
#
# @app.errorhandler(404)
# def page_not_found(error):
#     return f"Page not found on {app.config['APP_NAME']}"
#
#
# @app.route('/')
# def hello():
#     # mongo.db.posts.insert_one({"title": "Hello World!"})
#     posts = mongo.db.posts.find()
#     print(list(posts))
#     # print(url_for("hello"))
#     return "<strong>Hello World!</strong>"
#
#
# if __name__ == '__main__':
#     app.run(debug=True)


def create_app():
    app = Flask(__name__)
    # app.config["APP_NAME"] = "My Blog"
    # app.config["MONGO_URI"] = "mongodb+srv://mongo:SJjtxZ2MdybhP5no@study.emtthmt.mongodb.net/blog?retryWrites=true&w=majority"
    #
    # mongo = app.mongo = PyMongo(app)

    configure(app)

    return app
