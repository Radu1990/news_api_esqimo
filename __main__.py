import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_nf_entry(conn, nf_entry):
    """
    Create a new project into the projects table
    :param conn:
    :param nf_entry:
    :return: nf_entries_id
    """
    sql = ''' INSERT INTO nf_entries(name,url)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, nf_entry)
    return cur.lastrowid


def create_feed(conn, feeds):
    """
    Create a new task
    :param conn:
    :param feeds:
    :return:
    """
    sql = ''' INSERT INTO feeds(name,nf_entries_id)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, feeds)
    return cur.lastrowid


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
    conn = create_connection(database)
    if conn is not None:
        # create news feed entries table
        create_table(conn, sql_create_nf_entries_table)
        # create feeds table
        create_table(conn, sql_create_feeds_table)
        # create some new news feed entries
        nf_entry = ('BBC News UK', 'http://feeds.bbci.co.uk/news/uk/rss.xml')
        nf_entry_id_1 = create_nf_entry(conn, nf_entry)
        nf_entry = ('BBC News Technology', 'http://feeds.bbci.co.uk/news/technology/rss.xml')
        nf_entry_id_2 = create_nf_entry(conn, nf_entry)
        nf_entry = ('Reuters UK', 'http://feeds.reuters.com/reuters/UKdomesticNews?format=xml')
        nf_entry_id_3 = create_nf_entry(conn, nf_entry)
        nf_entry = ('Reuters Technology', 'http://feeds.reuters.com/reuters/technologyNews?format=xml')
        nf_entry_id_4 = create_nf_entry(conn, nf_entry)

    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
