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


def parse_xml_data():
    """
    Parse xml data from specified URL
    :param address:
    :return -:
    """
    address = 'http://feeds.bbci.co.uk/news/uk/rss.xml'
    while True:
        # break if url address is too short
        if len(address) < 1:
            break

        url = address
        print('Retrieving', url)

        uh = urllib.request.urlopen(url)
        data = uh.read()
        tree = elTree.fromstring(data)

        items = tree.findall('channel/item')

        for item in items:
            title_string = item.find("title").text
            print("Title value is ", title_string)
