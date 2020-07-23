import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


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


def main():
    database = r"C:\temp\testDB.db"

    sql_create_account_table = """ CREATE TABLE IF NOT EXISTS account (
                                        id integer PRIMARY KEY autoincrement,
                                        username text NOT NULL,
                                        password text NOT NULL,
                                        fullname text NOT NULL,
                                        email text NOT NULL,
                                        school text,
                                        major text
                                    ); """

    sql_create_course_table = """ CREATE TABLE IF NOT EXISTS COURSE (
                                        courseid integer NOT NULL,
                                        id integer NOT NULL,
                                        PRIMARY KEY (courseid, id),
                                        FOREIGN KEY (id)
                                            REFERENCES account_id (id),
                                        FOREIGN KEY (courseid)
                                            REFERENCES courselist_courseid (courseid)
                                    ); """

    sql_create_courselist_table = """ CREATE TABLE IF NOT EXISTS COURSELIST (
                                        courseid integer PRIMARY KEY autoincrement,
                                        coursename text NOT NULL
                                    ); """

    sql_create_room_table = """ CREATE TABLE IF NOT EXISTS room (
                                        roomid integer PRIMARY KEY autoincrement,
                                        roomname text NOT NULL,
                                        creator text NOT NULL
                                    ); """

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_account_table)
        create_table(conn, sql_create_course_table)
        create_table(conn, sql_create_courselist_table)
        create_table(conn, sql_create_room_table)

    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()