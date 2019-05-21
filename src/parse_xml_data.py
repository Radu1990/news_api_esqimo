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


def parse_xml_titles(address):
    """
    Parse xml data from specified URL
    :param address:
    :return map:
    """
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

        # create an empty list for our titles
        titles = []

        # loop through all xml items
        for item in items:
            # search for title
            title_string = item.find("title").text
            # add it to list
            titles.append(title_string)

        return titles
