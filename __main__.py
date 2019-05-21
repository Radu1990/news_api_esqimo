import src.db_func as dbf
import src.parse_xml_data as pxd
from collections import namedtuple


def main():
    # where our DB is stored
    database = "/home/cho/PYTHON/news_api_esqimo/db/rssnews.db"

    # RSS Feeds from Assignment
    MyFeed = namedtuple("MyFeed", "nf_entry nf_url")

    f1 = MyFeed(nf_entry="BBC News UK", nf_url="http://feeds.bbci.co.uk/news/uk/rss.xml")
    f2 = MyFeed(nf_entry="BBC News Technology", nf_url="http://feeds.bbci.co.uk/news/technology/rss.xml")
    f3 = MyFeed(nf_entry="Reuters UK", nf_url="http://feeds.reuters.com/reuters/UKdomesticNews?format=xml")
    f4 = MyFeed(nf_entry="Reuters Technology", nf_url="http://feeds.reuters.com/reuters/technologyNews?format=xml")

    # RSS Feed elements to be gathered in the Database

    # News feed entry title
    nf_title = pxd.parse_xml(f1.nf_url, 'channel', 'title')
    print(nf_title)

    # News Feed entry description
    nf_description = pxd.parse_xml(f1.nf_url, 'channel', 'description')
    print(nf_description)

    # News Feed entry link
    nf_link = pxd.parse_xml(f1.nf_url, 'channel', 'link')
    print(nf_link)

    # News Feed entry feeds
    # Feeds titles
    feeds_titles = pxd.parse_xml(f1.nf_url, 'channel/item', 'title')
    for x in feeds_titles:
        print('t')
        print(x)
    # Feeds description
    feeds_descriptions = pxd.parse_xml(f1.nf_url, 'channel/item', 'description')
    for x in feeds_descriptions:
        print('d')
        print(x)
    # Feeds link
    feeds_links = pxd.parse_xml(f1.nf_url, 'channel/item', 'link')
    for x in feeds_links:
        print('l')
        print(x)
    # Feeds publish date
    feeds_pubdate = pxd.parse_xml(f1.nf_url, 'channel/item', 'pubDate')
    for x in feeds_pubdate:
        print('p')
        print(x)


    # HINT!
    # nf_entries = news feed entries
    sql_create_nf_entries_table = """CREATE TABLE IF NOT EXISTS nf_entries ( 
                                        id INTEGER PRIMARY KEY,
                                        title TEXT NOT NULL,
                                        description TEXT NOT NULL,
                                        link TEXT NOT NULL
                                    );"""

    sql_create_feeds_table = """CREATE TABLE IF NOT EXISTS feeds (
                                    id INTEGER PRIMARY KEY,
                                    title TEXT NOT NULL,
                                    description TEXT NOT NULL,
                                    link TEXT NOT NULL,
                                    pub_date TEXT NOT NULL,
                                    nf_entries_id INTEGER NOT NULL, 
                                    FOREIGN KEY (nf_entries_id) REFERENCES nf_entries (id)
                                );"""

    # create a database connection
    conn = dbf.create_connection(database)
    if conn is not None:
        # create news feed entries table
        dbf.create_table(conn, sql_create_nf_entries_table)
        # create feeds table
        dbf.create_table(conn, sql_create_feeds_table)
        # create some new news feed entries
        nf_entry = (f1.nf_entry, f1.nf_url)
        nf_entry_id_1 = dbf.create_nf_entry(conn, nf_entry)

        # feeds
        feed_1 = ('BBC News UK', nf_entry_id_1)

    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
