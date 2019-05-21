import src.db_func as dbf
import src.parse_xml_data as pxd


def main():
    database = "/home/cho/PYTHON/news_api_esqimo/sqlite/db/rssnews.db"

    # nf_entries = news feed entries
    sql_create_nf_entries_table = """ CREATE TABLE IF NOT EXISTS nf_entries ( 
                                        id INTEGER PRIMARY KEY,
                                        name TEXT NOT NULL,
                                        url TEXT NOT NULL
                                    );"""

    sql_create_feeds_table = """CREATE TABLE IF NOT EXISTS feeds (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL,
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
        nf_entry = ('BBC News UK', 'http://feeds.bbci.co.uk/news/uk/rss.xml')
        nf_entry_id_1 = dbf.create_nf_entry(conn, nf_entry)
        nf_entry = ('BBC News Technology', 'http://feeds.bbci.co.uk/news/technology/rss.xml')
        nf_entry_id_2 = dbf.create_nf_entry(conn, nf_entry)
        nf_entry = ('Reuters UK', 'http://feeds.reuters.com/reuters/UKdomesticNews?format=xml')
        nf_entry_id_3 = dbf.create_nf_entry(conn, nf_entry)
        nf_entry = ('Reuters Technology', 'http://feeds.reuters.com/reuters/technologyNews?format=xml')
        nf_entry_id_4 = dbf.create_nf_entry(conn, nf_entry)
        # feeds
        feed_1 = ('BBC News UK', nf_entry_id_1)
        feed_2 = ('BBC News Technology', nf_entry_id_2)
        feed_3 = ('Reuters UK', nf_entry_id_3)
        feed_4 = ('Reuters Technology', nf_entry_id_4)

    else:
        print("Error! cannot create the database connection.")

    pxd.parse_xml_data()


if __name__ == '__main__':
    main()
