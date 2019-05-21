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


def nf_title(address):
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

        uh = urllib.request.urlopen(url)
        data = uh.read()
        tree = elTree.fromstring(data)

        items = tree.findall('channel')

        # create an empty list which will return the gathered data
        ret = []

        # loop through all xml items
        for item in items:
            # search for title
            title_string = item.find("title").text
            # add it to list
            ret.append(title_string)

        return ret


def nf_description(address):
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

        uh = urllib.request.urlopen(url)
        data = uh.read()
        tree = elTree.fromstring(data)

        items = tree.findall('channel')

        # create an empty list which will return the gathered data
        ret = []

        # loop through all xml items
        for item in items:
            # search for title
            title_string = item.find("description").text
            # add it to list
            ret.append(title_string)

        return ret


def nf_link(address):
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

        uh = urllib.request.urlopen(url)
        data = uh.read()
        tree = elTree.fromstring(data)

        items = tree.findall('channel')

        # create an empty list which will return the gathered data
        ret = []

        # loop through all xml items
        for item in items:
            # search for title
            title_string = item.find("link").text
            # add it to list
            ret.append(title_string)

        return ret
