import urllib.request
import urllib.error
import xml.etree.ElementTree as elTree

"""
    This program parses an XML file from a specific URL 
    and retrieves the values from the container field
    named "xxx" and then outputs those values.
  
    Input: 
    Output:    
"""


# parsing news feed link
def parse_xml(address, items_arg, item_arg):
    """
    Parse xml data from specified URL
    :param address:
    :param items_arg:
    :param item_arg:
    :return map:
    """
    while True:
        # break if url address is too short
        if len(address) < 1:
            break

        url = address

        uh = urllib.request.urlopen(url)
        data = uh.read()
        tree = elTree.fromstring(data)

        items = tree.findall(items_arg)

        # create an empty list which will return the gathered data
        ret = []

        # loop through all xml items
        for item in items:
            # search for title
            title_string = item.find(item_arg).text
            # add it to list
            ret.append(title_string)

        return ret


# -----------------------------------------------------------------------------------------------------------------
    # RSS Feed elements to be gathered in the Database
class ParseFeed:
    def __init__(self, url):
        self.url = url

    # News feed entry title
    def nf_title(self):
        nf_title = parse_xml(self.url, 'channel', 'title')
        return nf_title

    # News Feed entry description
    def nf_description(self):
        nf_description = parse_xml(self.url, 'channel', 'description')
        return nf_description

    # News Feed entry link
    def nf_url(self):
        nf_url = parse_xml(self.url, 'channel', 'link')
        return nf_url

    # News Feed entries
    # Feeds titles
    def feed_titles(self):
        feeds_titles = parse_xml(self.url, 'channel/item', 'title')
        return feeds_titles

    # Feeds description
    def feed_description(self):
        feed_description = parse_xml(self.url, 'channel/item', 'description')
        return feed_description

    # Feeds link
    def feed_urls(self):
        feed_urls = parse_xml(self.url, 'channel/item', 'link')
        return feed_urls

    # Feeds publish date
    def feed_pubdate(self):
        feed_pubdate = parse_xml(self.url, 'channel/item', 'pubDate')
        return feed_pubdate

    # Feeds guid
    def feed_guid(self):
        feed_guid = parse_xml(self.url, 'channel/item', 'guid')
        return feed_guid
# -----------------------------------------------------------------------------------------------------------------

