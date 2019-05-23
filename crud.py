from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import parse_xml_data as px
import os


"""
How to use: 
1. Run $ python3.6
2. import db object and generate SQLite database
Use following code in python interactive shell
    >>> from crud import db
    >>> db.create_all()
3. Run tests
"""


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://' + os.path.join(basedir, '/db/crud.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)
guid_db = []


# Feeds
# --------------------------------------------------------
class Feed(db.Model):
    __tablename__ = 'Feed'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    url = db.Column(db.String(120), unique=True, nullable=False)
    category = db.Column(db.String(80), nullable=False)

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
feed_schemas = FeedSchema(many=True)

"""
This part defined structure of response of our endpoint.
We want that all of our endpoints will have JSON response.
Here we define that our JSON response will have two keys
(title, description, url and category). 
Also we defined feed_schema as instance of FeedSchema, 
and feed_schemas as instances of list of FeedSchema
"""


# Feed Entries
# --------------------------------------------------------
class FeedEntry(db.Model):
    __tablename__ = 'Feed_entry'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    url = db.Column(db.String(120), unique=True, nullable=False)
    pub_date = db.Column(db.String(80), nullable=False)
    feeds_id = db.Column(db.Integer, db.ForeignKey('Feed.id'), nullable=False)

    def __init__(self, title, description, url, pub_date, guid):
        self.title = title
        self.description = description
        self.url = url
        self.pub_date = pub_date
        self.guid = guid  # global unique identifier for feed entry


class FeedEntrySchema(ma.Schema):
    class Meta2:
        # Fields to expose
        fields = ('title', 'description', 'url', 'pub_date')


feed_entry_schema = FeedEntrySchema()
feeds_entries_schemas = FeedEntrySchema(many=True)


# endpoint to create new feed
@app.route("/feed/", methods=["POST"])
def add_feed():
    title = request.json['title']
    description = request.json['description']
    url = request.json['url']
    category = request.json['category']

    # we first check if url already in db
    exists = db.session.query(Feed.url).scalar()

    if exists is not None:
        # create new feed
        new_feed = Feed(title, description, url, category)

        # add it to db
        db.session.add(new_feed)
        db.session.commit()

        # create new feed entries
        nf_data = px.ParseFeed(url)
        nf_titles = nf_data.feed_titles()
        nf_descriptions = nf_data.feed_description()
        nf_urls = nf_data.feed_urls()
        nf_pubdate = nf_data.feed_pubdate()
        nf_guid = nf_data.feed_guid()

        for x in range(len(nf_titles)):
            new_feed_entry = FeedEntry(title=nf_titles[x], description=nf_descriptions[x],
                                       url=nf_urls[x], pub_date=nf_pubdate[x], guid=nf_guid[x])

            # add it to db
            db.session.add(new_feed_entry)
            db.session.commit()

        return jsonify(
            title=new_feed.title,
            description=new_feed.description,
            url=new_feed.url,
            category=new_feed.category
        )
    else:

        return jsonify(
            Error='Feed already exists in DB!'
        )


# endpoint to show all feeds
@app.route("/feed/", methods=["GET"])
def get_feed():
    all_feeds = Feed.query.all()
    result = feed_schemas.dump(all_feeds)
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


# endpoint to create new feed entry
@app.route("/feed/entry/", methods=["POST"])
def add_feed_entry():
    title = request.json['title']
    description = request.json['description']
    url = request.json['url']
    pub_date = request.json['pub_date']
    guid = request.json['guid']

    new_feed_entry = FeedEntry(title, description, url, pub_date, guid)

    # we check if guid already in db
    exists = db.session.query(
        db.session.query(guid).exists()
    ).scalar()

    if not exists:
        db.session.add(new_feed_entry)
        db.session.commit()

        return jsonify(
            title=new_feed_entry.title,
            description=new_feed_entry.description,
            url=new_feed_entry.url,
            category=new_feed_entry.category
        )
    else:

        return jsonify(
            Error='GUID already exists in DB!'
        )

# endpoint to show all feed entries
@app.route("/feed/entry/", methods=["GET"])
def get_feed_entry():
    all_feeds_entries = FeedEntry.query.all()
    result = feeds_entries_schemas.dump(all_feeds_entries)
    return jsonify(result.data)

# endpoint to get feed entry detail by id
@app.route("/feed/<id>/", methods=["GET"])
def feed_entry_detail(id):
    feed_entry = Feed.query.get(id)
    return feed_entry_schema.jsonify(feed_entry)

# endpoint to update feed entry
@app.route("/feed/entry/<id>/", methods=["PUT"])
def feed_entry_update(id):
    feed_entry = FeedEntry.query.get(id)
    title = request.json['title']
    description = request.json['description']
    url = request.json['url']
    pub_date = request.json['pub_date']
    guid = request.json['guid']

    feed_entry.title = title
    feed_entry.description = description
    feed_entry.url = url
    feed_entry.pub_date = pub_date
    feed_entry.guid = guid

    db.session.commit()
    return feed_entry_schema.jsonify(feed_entry)


# trebuie facute API rest care sa returneze feed in functie de combinatia aleasa (mai citeste o data ex)
# 1 git clone
# 2 totul intr-un readme: se instaleaza dependintele cu venv cu pip install + testing
# cum se ruleaza testele automat cu o singura linie deschis server + RULAT TESTE + inchis server

if __name__ == '__main__':
    app.run(debug=True)
