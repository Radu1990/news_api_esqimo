from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

"""
How to use: 
1. $ python3.6
2. import db object and generate SQLite database
Use following code in python interactive shell
    >>> from crud import db
    >>> db.create_all()
"""

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Feed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(120), unique=True)
    url = db.Column(db.String(120), unique=True)
    category = db.Column(db.String(80), unique=False)

    def __init__(self, title, description, url, category):
        self.title = title
        self.description = description
        self.url = url
        self.category = category


class FeedSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('title', 'description', 'url', 'category')


feed_schema = FeedSchema()
feeds_schema = FeedSchema(many=True)
"""
This part defined structure of response of our endpoint.
We want that all of our endpoint will have JSON response.
Here we define that our JSON response will have two keys
(title, description, url and category). 
Also we defined user_schema as instance of UserSchema, 
and user_schemas as instances of list of UserSchema
"""

# endpoint to create new feed
@app.route("/feed/", methods=["POST"])
def add_feed():
    title = request.json['title']
    description = request.json['description']
    url = request.json['url']
    category = request.json['category']

    new_feed = Feed(title, description, url, category)

    db.session.add(new_feed)
    db.session.commit()

    return jsonify(
        title=new_feed.title,
        description=new_feed.description,
        url=new_feed.url,
        category=new_feed.category
    )


# endpoint to show all feeds
@app.route("/feed/", methods=["GET"])
def get_feed():
    all_feeds = Feed.query.all()
    result = feeds_schema.dump(all_feeds)
    return jsonify(result.data)


# endpoint to get feed detail by id
@app.route("/feed/<id>/", methods=["GET"])
def feed_detail(id):
    feed = Feed.query.get(id)
    return feed_schema.jsonify(feed)


# endpoint to update feed
@app.route("/feed/<id>/", methods=["PUT"])
def feed_update(id):
    feed = Feed.query.get(id)
    title = request.json['title']
    description = request.json['description']
    url = request.json['url']
    category = request.json['category']

    feed.title = title
    feed.description = description
    feed.url = url
    feed.category = category

    db.session.commit()
    return feed_schema.jsonify(feed)


# endpoint to delete feed
@app.route("/feed/<id>/", methods=["DELETE"])
def feed_delete(id):
    feed = Feed.query.get(id)
    db.session.delete(feed)
    db.session.commit()

    return feed_schema.jsonify(feed)


if __name__ == '__main__':
    app.run(debug=True)
