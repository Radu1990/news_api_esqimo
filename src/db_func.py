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
    :return nf_entries id:
    """
    sql = ''' INSERT INTO nf_entries(title, description, link)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, nf_entry)
    return cur.lastrowid


def create_feed(conn, feeds):
    """
    Create a new task
    :param conn:
    :param feeds:
    :return feeds id:
    """
    sql = ''' INSERT INTO feeds(title, description, link, pub_date, nf_entries_id)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, feeds)
    return cur.lastrowid
