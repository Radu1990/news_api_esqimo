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
    :return nf_entries id:
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
    :return feeds id:
    """
    sql = ''' INSERT INTO feeds(name,nf_entries_id)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, feeds)
    return cur.lastrowid
