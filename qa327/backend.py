from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all backend logic that interacts with database and other services
"""


def get_user(email):
    """
    Get a user by a given email
    :param email: the email of the user
    :return: a user that has the matched email address
    """
    user = User.query.filter_by(email=email).first()
    return user


def login_user(email, password):
    """
    Check user authentication by comparing the password
    :param email: the email of the user
    :param password: the password input
    :return: the user if login succeeds
    """
    # if this returns a user, then the name already exists in database
    user = get_user(email)
    if not user or not check_password_hash(user.password, password):
        return None
    return user


def register_user(email, name, password, password2, balance):
    """
    Register the user to the database
    :param email: the email of the user
    :param name: the name of the user
    :param password: the password of user
    :param password2: another password input to make sure the input is correct
    :return: an error message if there is any, or None if register succeeds
    """

    hashed_pw = generate_password_hash(password, method='sha256')
    # store the encrypted password rather than the plain password
    new_user = User(email=email, name=name, password=hashed_pw, balance=balance)
    db.session.add(new_user)
    db.session.commit()
    return None

def create_ticket(title, quantity, price, expDate):
    new_ticket = Ticket(title=title, quantity=quantity, price=price, expDate=expDate)
    db.session.add(new_ticket)
    db.session.commit()
    return None

def get_ticket(title):
    ticket = Ticket.query.filter_by(title=title).first()
    return ticket

def update_ticket(title, quantity, price, expDate):
    t = get_ticket(title)
    t.quantity = quantity
    t.price = price
    t.expDate = expDate
    db.session.commit()
    return None

def buy_ticket(title, quantity, cost, user):
    t = get_ticket(title)
    user.balance = user.balance - cost
    t.quantity = t.quantity - quantity
    if t.quantity < 1:
        db.session.delete(t)
    db.session.commit()
    return None


def get_all_tickets():
    tickets = Ticket.query.all()
    return tickets