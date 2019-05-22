import requests
import _unittests.feed_generator as fg


def _url(path):
    return 'http://localhost:5000/' + path


def get_feeds(title="", description="", url="", category=""):
    payload = {}
    if title:
        payload['title'] = title
    if description:
        payload['description'] = description
    if url:
        payload['url'] = url
    if category:
        payload['category'] = category

    if payload:
        return requests.get(_url('/feed/'), params=payload)
    else:
        return requests.get(_url('/feed/'))


def describe_feed(feed_id):
    return requests.get('http://localhost:5000/feed/{:d}'.format(feed_id))


def add_random_feed():
    return add_feed(fg.generate_feed())


def add_feed(feed):
    return requests.post(_url('/feed/'), json=feed)


def remove_feed(feed_id):
    return requests.delete(_url('/booking/{:d}'.format(feed_id)))


def update_feed(feed_id, title='Realitatea', description='Stiri online',
                url='http://rss.realitatea.net/stiri.xml', category='News'):
    return requests.put(_url('/booking/{:d}'.format(feed_id)), json={
        "title": title,
        "description": description,
        "url": url,
        "category": category
    })


def main():

    print(describe_feed(1))


if __name__ == '__main__':
    main()

