# feed_generator.py
from random import choice


def generate_feed():
    title = choice(['BBC', 'BBC Technology', 'Reuters', 'Reuters Technology'])
    description = choice(['BBC News UK', 'BBC News Technology', 'Reuters - UK', 'Reuters Technology'])
    url = choice(['http://feeds.bbci.co.uk/news/uk/rss.xml',
                  'http://feeds.bbci.co.uk/news/technology/rss.xml',
                  'http://feeds.reuters.com/reuters/UKdomesticNews?format=xml',
                  'http://feeds.reuters.com/reuters/technologyNews?format=xml'])
    category = choice(['News', 'Technology', 'News', 'Technology'])

    return (
        {
            "title": title,
            "description": description,
            "url": url,
            "category": category
        }
    )
