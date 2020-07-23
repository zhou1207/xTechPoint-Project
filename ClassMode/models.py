import sqlite3 as sql


def insertUser(username, password, fullname, email):
    con = sql.connect("testDB.db")
    cur = con.cursor()
    cur.execute("INSERT INTO account (username,password,fullname,email) VALUES (?,?,?,?)", (username, password, fullname, email))
    con.commit()
    con.close()


def retrieveUsers(username, password):
    con = sql.connect("testDB.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM account WHERE username = ? AND password = ?", (username, password))
    users = cur.fetchone()
    con.close()
    return users


def getUsers(id):
    con = sql.connect("testDB.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM account WHERE id = ?", (id,))
    users = cur.fetchone()
    con.close()
    return users


# get the course name of one account
def getClass(id):
    con = sql.connect("testDB.db")
    cur = con.cursor()
    cur.execute("SELECT coursename FROM course INNER JOIN courselist ON course.courseid = courselist.courseid WHERE id = ?", (id,))
    courselist = cur.fetchall()
    con.close()
    return courselist


# get the course id of one account
def getClassid(id):
    con = sql.connect("testDB.db")
    cur = con.cursor()
    cur.execute("SELECT courselist.courseid FROM course INNER JOIN courselist ON course.courseid = courselist.courseid WHERE id = ?", (id,))
    courselist = cur.fetchall()
    con.close()
    return courselist


# get the course id of a course
def getCourseid(coursename):
    con = sql.connect("testDB.db")
    cur = con.cursor()
    cur.execute("SELECT courseid FROM courselist WHERE coursename = ?", (coursename,))
    courseid = cur.fetchone()
    con.close()
    return courseid


def matchtable(courseid):
    con = sql.connect("testDB.db")
    cur = con.cursor()
    cur.execute("SELECT fullname, email, school, major FROM course INNER JOIN account ON course.id = account.id WHERE courseid = ?", courseid)
    course = cur.fetchall()
    con.close()
    return course


# ============================================================================================
# Room methods section
def insertRoom(roomname, creator):
    con = sql.connect("testDB.db")
    cur = con.cursor()
    cur.execute("INSERT INTO room (roomname,creator) VALUES (?,?)", (roomname,creator))
    con.commit()
    con.close()


def checkRoomid(roomid):
    con = sql.connect("testDB.db")
    cur = con.cursor()
    cur.execute("SELECT roomid from room WHERE roomid = ?", (roomid))
    id = cur.fetchone()
    con.close()
    return id


def getRoomname(roomid):
    con = sql.connect("testDB.db")
    cur = con.cursor()
    cur.execute("SELECT roomname from room WHERE roomid = ?", (roomid))
    name = cur.fetchone()
    con.close()
    return name


def getRoomid(roomname):
    con = sql.connect("testDB.db")
    cur = con.cursor()
    cur.execute("SELECT roomid from room WHERE roomname = ?", (roomname,))
    id = cur.fetchone()
    con.close()
    return id


def checkRoomname(roomname):
    con = sql.connect("testDB.db")
    cur = con.cursor()
    cur.execute("SELECT roomname from room WHERE roomname = ?", (roomname,))
    name = cur.fetchall()
    con.close()
    return name

