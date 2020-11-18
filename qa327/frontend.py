from flask import render_template, request, session, redirect
from qa327 import app
import qa327.backend as bn
import re

regex_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
regex_password = '^(?=.*[a-z])(?=.*[A-Z])(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{6,}$'
regex_name = '(?=^[0-9a-zA-Z])(?=.*[0-9a-zA-Z]$)^[0-9a-zA-Z ]{3,19}$'

"""
This file defines the front-end part of the service.
It elaborates how the services should handle different
http requests from the client (browser) through templating.
The html templates are stored in the 'templates' folder. 
"""


@app.route('/register', methods=['GET'])
# This function checks to see if user is logged in, then directs them to the register page.
def register_get():
    # templates are stored in the templates folder


    if 'logged_in' in session:
        return redirect('/')
    
    # This directs the user to the /register page.

    if 'logged_in' in session:
        return redirect('/')

    return render_template('register.html', message='')


@app.route('/register', methods=['POST'])
# This function takes inputs from user and makes sure they follow the requirements for new registrants.
def register_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    error_message = None


    if password != password2:
        error_message = "The passwords do not match"
        return redirect('/login?message=The passwords do not match')

    elif not re.search(regex_email,email):
        error_message = "Email format error"
        return redirect('/login?message=Email format error')

    elif not re.search(regex_name,name):
        error_message = "Name format error"
        return redirect('/login?message=Name format error')

    elif not re.search(regex_password,password):
        error_message = "Password not strong enough"

        return redirect('/login?message=Password not strong enough')


        return redirect('/login?message=Password not strong enough')

    else:
        user = bn.get_user(email)
        if user:
            error_message = "This email has been ALREADY used."
        elif bn.register_user(email, name, password, password2, 5000):
            error_message = "Failed to store user info loser."
    # if there is any error messages when registering new user
    # at the backend, directs back to the /register.
    if error_message:
        return render_template('register.html', message=error_message)
    else:
        return redirect('/login')


@app.route('/login', methods=['GET'])
# This function checks to see if user is logged in, if they aren't it directs them to the login page.
def login_get():
    if 'logged_in' in session:
        return redirect('/')
    
    m = request.args.get('message')
    if m == None:
        m = 'Please Login'

    return render_template('login.html', message=m)


@app.route('/login', methods=['POST'])
# This function takes inputs from user and makes sure they are in the database.
# If they are it directs them to '/', if not they are redirected back to the /login page.
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    user = bn.login_user(email, password)
    
    if not re.search(regex_email,email):
        return render_template('login.html', message='Email/password format is incorrect.')

    if not re.search(regex_password,password):
        return render_template('login.html', message='Email/password format is incorrect.')

    if user:
        session['logged_in'] = user.email
        """
        Session is an object that contains sharing information 
        between browser and the end server. Typically it is encrypted 
        and stored in the browser cookies. They will be past 
        along between every request the browser made to this services.

        Here we store the user object into the session, so we can tell
        if the client has already login in the following sessions.

        """
        # success! go back to the home page
        # code 303 is to force a 'GET' request
        return redirect('/', code=303)
    else:
        return render_template('login.html', message='Email/password combination incorrect.')


@app.route('/logout')
# This function logs out a user if they are logged in.
def logout():
    if 'logged_in' in session:
        session.pop('logged_in', None)
    return redirect('/')

# This function is called to authenticate the user info for login.
def authenticate(inner_function):
    """
    :param inner_function: any python function that accepts a user object

    Wrap any python function and check the current session to see if 
    the user has logged in. If login, it will call the inner_function
    with the logged in user object.

    To wrap a function, we can put a decoration on that function.
    Example:

    @authenticate
    def home_page(user):
        pass
    """

    def wrapped_inner():

        # check did we store the key in the session
        if 'logged_in' in session:
            email = session['logged_in']
            user = bn.get_user(email)
            if user:
                # if the user exists, call the inner_function
                # with user as parameter
                return inner_function(user)
        else:
            # else, redirect to the login page
            return redirect('/login')

    # return the wrapped version of the inner_function:
    return wrapped_inner


@app.route('/')
@authenticate
def profile(user):
    # authentication is done in the wrapper function
    # see above.
    # by using @authenticate, we don't need to re-write
    # the login checking code all the time for other
    # front-end portals
    tickets = bn.get_all_tickets()
    return render_template('index.html', user=user, tickets=tickets)

@app.errorhandler(404)
def page_not_found(e):
    # If the url does not met any of the existing
    # urls it redirects to 404.html.
    return render_template('404.html'), 404


# The following code was added to test form submissions, will be updated in next assignment.

@app.route('/sell', methods=['GET'])
def sell_get():
    return render_template('temp.html', message='Sold')

@app.route('/buy', methods=['GET'])
def buy_get():
    return render_template('temp.html', message='Bought')

@app.route('/update', methods=['GET'])
def update_get():
    return render_template('temp.html', message='Updated')

