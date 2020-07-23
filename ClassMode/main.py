from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO
import re
import models as dbHandler


# Create an instance, specify where to find the html templates
app = Flask(__name__, template_folder='template')

# secret key for the application
app.secret_key = 'qwertyuiop'

socketio = SocketIO(app)

# The welcome page
@app.route('/')
def welcome():
    return render_template('welcome.html')


# The login page code section
@app.route('/login/', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong
    msg = ''
    # Check if <username> and <password> POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        account = dbHandler.retrieveUsers(username, password)
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account[0]  # account id
            session['username'] = account[1]    # account username
            session['fullname'] = account[3]    # account user's fullname
            session['email'] = account[4]   # account email
            session['school'] = account[5]  # account school
            session['major'] = account[6]   # account major
            # Redirect to home page
            return redirect(url_for('home'))
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('index.html', msg=msg)


@app.route('/login/logout')
def logout():
    # Remove session data, this will log the user out
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    session.pop('email', None)
    session.pop('major', None)
    # Redirect to login page
    return redirect(url_for('login'))


@app.route('/login/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong
    msg = ''
    # Check if <username>, <password> and <email> POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form and 'fullname' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        fullname = request.form['fullname']
        email = request.form['email']
        # Check if account exists
        account = dbHandler.retrieveUsers(username, password)
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif len(password) < 8:
            msg = 'Password must be at least 8 letters.'
        elif re.search('[0-9]', password) is None:
            msg = 'Password must contain a number.'
        elif re.search('[A-Z]', password) is None:
            msg = 'Password must contain at least one capital letter.'
        elif re.search('[_@$]', password) is None:
            msg = 'Password must contain special characters _@$.'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            dbHandler.insertUser(username, password, fullname, email)
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty...(no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)


@app.route('/login/home')
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('home.html', fullname=session['fullname'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


@app.route('/login/profile')
def profile():
    # Check if user is loggedin
    if 'loggedin' in session:
        # We need all the account info for the user so we can display it on the profile page\
        username = session['username']
        school = session['school']
        fullname = session['fullname']
        email = session['email']
        major = session['major']
        id = session['id']
        course = dbHandler.getClass(id)
        # Show the profile page with account info
        return render_template('profile.html', username=username, school = school, fullname = fullname, email=email, major=major, course=course)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


# This will be the route for the find matches.
@app.route('/login/findmatches', methods=['GET', 'POST'])
def search():
    msg = ''
    match = []
    coursename = ''
    if request.method == 'POST' and 'coursename' in request.form:
        # Get the entered course name
        coursename = request.form['coursename']
        if coursename not in ('MA 161', 'MA 162', 'MA 265', 'CS 180', 'CS 240', 'CNIT 242', 'CNIT 270', 'ECON 252', 'MGMT 201', 'STAT 351'):
            msg = 'The course entered does not exist'
        else:
            courseid = dbHandler.getCourseid(coursename)
            match = dbHandler.matchtable(courseid)
            if match:
                msg = 'Search completed'
            else:
                msg = 'None'

    return render_template('findmatches.html', msg=msg, match=match, coursename=coursename)


@app.route('/login/sharenotes')
def sharenotes():
    # Check if user is loggedin
    if 'loggedin' in session:
        return render_template('sharenotes.html')
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


@app.route('/login/join', methods=['GET', 'POST'])
def join():
    # Output message if something goes wrong
    msg = ''
    # Check if <fullname> and <roomid> POST requests exist (user submitted form)
    if request.method == 'POST' and 'fullname' in request.form and 'roomid' in request.form:
        # Create variables for easy access
        fullname = request.form['fullname']
        roomid = request.form['roomid']
        # Check if fullname is valid
        if fullname != session['fullname']:
            msg = 'Please fill in your correct full name'
        else:
            id = dbHandler.checkRoomid(roomid)
            roomname = dbHandler.getRoomname(roomid)
            if id:
                # Create session data, we can access this data in other routes
                session['name'] = fullname
                session['roomid'] = roomid
                session['room'] = roomname
                # Redirect to chat page
                return redirect(url_for("chatroom"))
            else:
                # Room doesnt exist or room incorrect
                msg = 'Incorrect roomid/room does not exist'
    # Show the login form with message (if any)
    return render_template('join.html', msg=msg)


@app.route('/login/chat', methods=['GET', 'POST'])
def chat():
    # Output message if something goes wrong
    msg = ''
    # Check if <fullname> and <roomname> POST requests exist (user submitted form)
    if request.method == 'POST' and 'fullname' in request.form and 'roomname' in request.form:
        # Create variables for easy access
        fullname = request.form['fullname']
        roomname = request.form['roomname']
        if fullname != session['fullname']:
            msg = 'Please fill in your correct full name'
        else:
            dbHandler.insertRoom(roomname,fullname)
            session['name'] = fullname
            session['room'] = roomname
            session['roomid'] = dbHandler.getRoomid(roomname)
            return redirect(url_for('chatroom'))
    elif request.method == 'POST':
        # Form is empty...(no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('chat.html', msg=msg)


@app.route('/login/chat/chatroom', methods=['GET', 'POST'])
def chatroom():
    """Chat room. The user's name and room must be stored in
    the session."""
    name = session.get('fullname')
    room = session.get('room')
    roomid = session.get('roomid')
    if name == '' or room == '' or roomid == '':
        return redirect(url_for('chat'))
    return render_template('chatroom.html', name=name, room=room, roomid=roomid)


if __name__ == '__main__':
    socketio.run(app, debug=True)