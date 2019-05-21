import src.db_func as dbf
import src.parse_xml_data as pxd
from collections import namedtuple


def main():

    # RSS Feeds from Assignment
    MyFeed = namedtuple("MyFeed", "nf_entry nf_url")

    f1 = MyFeed(nf_entry="BBC News UK", nf_url="http://feeds.bbci.co.uk/news/uk/rss.xml")
    f2 = MyFeed(nf_entry="BBC News Technology", nf_url="http://feeds.bbci.co.uk/news/technology/rss.xml")
    f3 = MyFeed(nf_entry="Reuters UK", nf_url="http://feeds.reuters.com/reuters/UKdomesticNews?format=xml")
    f4 = MyFeed(nf_entry="Reuters Technology", nf_url="http://feeds.reuters.com/reuters/technologyNews?format=xml")

    # -----------------------------------------------------------------------------------------------------------------
    # RSS Feed elements to be gathered in the Database
    # News feed entry title
    nf_title = pxd.parse_xml(f1.nf_url, 'channel', 'title')
    # News Feed entry description
    nf_description = pxd.parse_xml(f1.nf_url, 'channel', 'description')

    # News Feed entry link
    nf_link = pxd.parse_xml(f1.nf_url, 'channel', 'link')

    # News Feed entry feeds
    # Feeds titles
    feeds_titles = pxd.parse_xml(f1.nf_url, 'channel/item', 'title')

    # Feeds description
    feeds_descriptions = pxd.parse_xml(f1.nf_url, 'channel/item', 'description')

    # Feeds link
    feeds_links = pxd.parse_xml(f1.nf_url, 'channel/item', 'link')

    # Feeds publish date
    feeds_pubdate = pxd.parse_xml(f1.nf_url, 'channel/item', 'pubDate')
    # -----------------------------------------------------------------------------------------------------------------

    # create a database connection
    conn = dbf.create_connection(dbf.database)
    if conn is not None:
        with conn:
            # create nf_entries table
            dbf.create_table(conn, dbf.sql_create_nf_entries_table)
            # create feeds table
            dbf.create_table(conn, dbf.sql_create_feeds_table)

            # create a new news feed entry
            my_feed_entry_1 = (nf_title[0], nf_description[0], nf_link[0])
            nf_entry_id_1 = dbf.create_nf_entry(conn, my_feed_entry_1)
            # create feeds for our feed entry
            for i in range(len(feeds_titles)):
                my_feed = (feeds_titles[i], feeds_descriptions[i], feeds_links[i], feeds_pubdate[i], nf_entry_id_1)
                dbf.create_feed(conn, my_feed)

    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
