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
    except Error as e:
        print(e)

    return conn


def create_account(conn, account):

    sql = ''' INSERT INTO account(id,username,password,fullname,email,school,major)
              VALUES(?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, account)
    conn.commit()
    print(cur.lastrowid)


def create_course(conn, course):

    sql = ''' INSERT INTO course(id,courseid)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, course)
    conn.commit()
    print(cur.lastrowid)


def create_courselist(conn, courselist):

    sql = ''' INSERT INTO courselist(courseid,coursename)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, courselist)
    conn.commit()
    print(cur.lastrowid)


def create_room(conn, room):
    sql = ''' INSERT INTO room(roomid,roomname,creator)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, room)
    conn.commit()
    print(cur.lastrowid)


def main():
    database = r"C:\temp\testDB.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        account1 = (1, 'test', 'test', 'Test test', 'test@test.com', 'Purdue University', 'Math');
        account2 = (2, 'James', 'test', 'James Zhou', 'james@test.com', 'Purdue University', 'Cybersecurity');
        account3 = (3, 'Dylan', 'test', 'Dylan Harker', 'dylan@test.com', 'Purdue University', 'Data Science');
        account4 = (4, 'Syed', 'test', 'Syed Oeshic', 'syed@test.com', 'Purdue University', 'Computer Science');
        account5 = (5, 'Logan', 'test', 'Logan Vinson', 'logan@test.com', 'Purdue University', 'Business');
        account6 = (6, 'Maya', 'test', 'Maya Goldheim', 'maya@test.com', 'Purdue University', 'Management');
        account7 = (7, 'AnLT', 'test', 'An Le Thuy Nguyen', 'anlt@test.com', 'Purdue University', 'Accounting');

        courselist1 = (1, 'MA 161');
        courselist2 = (2, 'MA 162');
        courselist3 = (3, 'MA 265');
        courselist4 = (4, 'CS 180');
        courselist5 = (5, 'CS 240');
        courselist6 = (6, 'CNIT 242');
        courselist7 = (7, 'CNIT 270');
        courselist8 = (8, 'ECON 252');
        courselist9 = (9, 'MGMT 201');
        courselist10 = (10, 'STAT 351');

        courseJ01 = (2, 3)
        courseJ02 = (2, 7)
        courseD01 = (3, 3)
        courseD02 = (3, 6)
        courseS01 = (4, 4)
        courseS02 = (4, 1)
        courseL01 = (5, 1)
        courseL02 = (5, 8)
        courseM01 = (6, 9)
        courseM02 = (6, 10)
        courseA01 = (7, 9)
        courseA02 = (7, 10)

        room01 = (1, 'Test Room', 'test')

    create_account(conn, account1)
    create_account(conn, account2)
    create_account(conn, account3)
    create_account(conn, account4)
    create_account(conn, account5)
    create_account(conn, account6)
    create_account(conn, account7)

    create_courselist(conn, courselist1)
    create_courselist(conn, courselist2)
    create_courselist(conn, courselist3)
    create_courselist(conn, courselist4)
    create_courselist(conn, courselist5)
    create_courselist(conn, courselist6)
    create_courselist(conn, courselist7)
    create_courselist(conn, courselist8)
    create_courselist(conn, courselist9)
    create_courselist(conn, courselist10)

    create_course(conn, courseJ01)
    create_course(conn, courseJ02)
    create_course(conn, courseD01)
    create_course(conn, courseD02)
    create_course(conn, courseS01)
    create_course(conn, courseS02)
    create_course(conn, courseL01)
    create_course(conn, courseL02)
    create_course(conn, courseM01)
    create_course(conn, courseM02)
    create_course(conn, courseA01)
    create_course(conn, courseA02)

    create_room(conn, room01)


if __name__ == '__main__':
    main()