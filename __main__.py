import src.db_func as dbf
import src.parse_xml_data as pxd
from collections import namedtuple


def main():
    # where our DB is stored
    database = "/home/cho/PYTHON/news_api_esqimo/sqlite/db/rssnews.db"

    # RSS Feeds from Assignment
    MyFeed = namedtuple("MyFeed", "nf_entry nf_url")

    f1 = MyFeed(nf_entry="BBC News UK", nf_url="http://feeds.bbci.co.uk/news/uk/rss.xml")
    f2 = MyFeed(nf_entry="BBC News Technology", nf_url="http://feeds.bbci.co.uk/news/technology/rss.xml")
    f3 = MyFeed(nf_entry="Reuters UK", nf_url="http://feeds.reuters.com/reuters/UKdomesticNews?format=xml")
    f4 = MyFeed(nf_entry="Reuters Technology", nf_url="http://feeds.reuters.com/reuters/technologyNews?format=xml")

    nf_title = pxd.nf_title(f1.nf_url)
    nf_description = pxd.nf_description(f1.nf_url)
    nf_link = pxd.nf_link(f1.nf_url)
    print(nf_title)
    print(nf_description)
    print(nf_link)

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
