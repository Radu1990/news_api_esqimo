import requests


def generate_feed(x):
    title = ['BBC', 'BBC Technology', 'Reuters', 'Reuters Technology']
    description = ['BBC News UK', 'BBC News Technology', 'Reuters - UK', 'Reuters Technology']
    url = ['http://feeds.bbci.co.uk/news/uk/rss.xml',
           'http://feeds.bbci.co.uk/news/technology/rss.xml',
           'http://feeds.reuters.com/reuters/UKdomesticNews?format=xml',
           'http://feeds.reuters.com/reuters/technologyNews?format=xml']
    category = ["News", "Technology", "News", "Technology"]

    return (
        {
            "title": title[x],
            "description": description[x],
            "url": url[x],
            "category": category[x]
        }
    )


def _url(path):
    return 'http://localhost:5000' + path


def get_feed(feed_id):
    return requests.get(_url('/feed/{:d}/'.format(feed_id)))


def get_all_feeds():
    return requests.get(_url('/feed/'))


def add_specific_feed(x):
    return add_feed(generate_feed(x))


def add_feed(feed):
    return requests.post(_url('/feed/'), json=feed)


def remove_feed(feed_id):
    return requests.delete(_url('/feed/{:d}/'.format(feed_id)))


def update_feed(feed_id, title, description,
                url, category):
    return requests.put(_url('/feed/{:d}/'.format(feed_id)), json={
        "title": title,
        "description": description,
        "url": url,
        "category": category
    })
