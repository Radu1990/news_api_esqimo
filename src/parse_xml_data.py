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
