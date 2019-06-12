from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import parse_xml_data as px
import config as cfg

"""
prerequisites:
1. Flask to create an instance of a web application
2. Request to get request data
3. Jsonify to turn the JSON output into a Response object
4. SQAlchemy from flask_sqlalchemy for accessing the database
5. Marshmallow from flask_marshmallow to serialize object
"""

# This part create an instances of our web application
# and sets path of our SQLite uri.
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = cfg.DATABASE_URI
# On this part we are binding SQLAlchemy
# and Marshmallow into our Flask application.
db = SQLAlchemy(app)
ma = Marshmallow(app)


# Here we declare model called Feed and define
# its field with it’s properties.
class Feed(db.Model):
    __tablename__ = 'feed'
    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    url = db.Column(db.String(), nullable=False)
    category = db.Column(db.String(), nullable=False)

    def __init__(self, title, description, url, category):

        self.title = title
        self.description = description
        self.url = url
        self.category = category


# This part defined structure of response of our endpoint.
# We want that all of our endpoint will have JSON response.
# Here we define that our JSON response will have 5 keys
# ('id', 'title', 'description', 'url', 'category').
# Also we defined user_schema as instance of UserSchema,
# and user_schemas as instances of list of UserSchema.
class FeedSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'title', 'description', 'url', 'category')


feed_schema = FeedSchema()
feed_schemas = FeedSchema(many=True)


# We do the same for Feed Entry
class FeedEntry(db.Model):
    __tablename__ = 'feed_entry'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    url = db.Column(db.String(), nullable=False)
    pub_date = db.Column(db.String(), nullable=False)
    feed_fk = db.Column(db.ForeignKey("feed.id"))
    guid = db.Column(db.String(), nullable=False)

    def __init__(self, title, description, url, pub_date, guid):
        self.title = title
        self.description = description
        self.url = url
        self.pub_date = pub_date
        self.guid = guid  # global unique identifier for feed entry
        # TODO check guid in DB when a feed entry is added


class FeedEntrySchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('title', 'description', 'url', 'pub_date', 'guid')


feed_entry_schema = FeedEntrySchema()
feeds_entries_schemas = FeedEntrySchema(many=True)

# endpoint to create new feed.
# set the route to “/feed/” and set HTTP methods to POST.
# After we set the route and methods we define function that will executed if we access this endpoint.
# On this function first we get 'title', 'description', 'url' and 'category' from request data.
# After that we create new news feed using data from request data.
# Then we create all the corresponding feed entries as-well.
# Last we add new feed along with the feed entries
# to data base and show new feed in JSON form as response.
@app.route("/feed/", methods=["POST"])
def add_feed():
    title = request.json['title']
    description = request.json['description']
    url = request.json['url']
    category = request.json['category']

    # create new feed
    new_feed = Feed(title=title, description=description, url=url, category=category)

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

        guid = nf_guid[x]

        # Todo check if guid is unique in DB
        # if already in DB skip news feed entry

        new_feed_entry = FeedEntry(title=nf_titles[x], description=nf_descriptions[x],
                                   url=nf_urls[x],
                                   pub_date=nf_pubdate[x], guid=guid)
        # add them to db
        db.session.add(new_feed_entry)

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
    result = feed_schemas.dump(all_feeds)
    return jsonify(result.data)


# We define endpoint to get user data based on id.
# Pattern like “<id>” is parameter
@app.route("/feed/<id>/", methods=["GET"])
def feed_detail(id):
    feed = Feed.query.get(id)
    return feed_schema.jsonify(feed)


# endpoint to update feed based on id
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

    db.session.add(new_feed_entry)
    db.session.commit()

    return jsonify(
        title=new_feed_entry.title,
        description=new_feed_entry.description,
        url=new_feed_entry.url,
        category=new_feed_entry.category
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


def recreate_database():
    # drop all tables
    db.drop_all()
    # create all tables
    db.create_all()


recreate_database()

# Run
if __name__ == '__main__':
    app.run(debug=True)
