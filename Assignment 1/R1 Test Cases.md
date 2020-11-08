# R1 /login [GET]

Test Data:
```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
```

## Test Case R1.1.1 If the user hasn't logged in, show the login page.
Mocking:
 - Mock backend.get_user to return a test_user instance 

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - validate /login is open.

## Test Case R1.2 The login page has a message that by default says 'please login'.
Mocking:
 - Mock backend.get_user to return a test_user instance 

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - validate that current page contains #please_login-header element

## Test case R1.3 - If the user has logged in, redirect to the user profile page.
Mocking:
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element #email
 - enter test_user's password into element #password
 - click element input[type="submit"]
 - open /login again
 - validate that current page contains #welcome-header element

## Test case R1.4 - The login page provides a login form which requests two fields: email and password.
Mocking:
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - validate that current page has #email element
 - validate that current page has #password element

# [POST]

## Test case R1.5 - The login form can be submitted as a POST request to the current URL (/login).
Mocking:
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element #email
 - enter test_user's password into element #password
 - click element input[type="submit"]
 - open /login again
 - validate that current page contains #welcome-header element

## Test case R1.6.1 - Email and password both cannot be empty. - Positive
Mocking:
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element #email
 - enter test_user's password into element #password
 - click element input[type="submit"]
 - open /login again
 - validate that current page contains #welcome-header element

## Test case R1.6.2 - Email and password both cannot be empty. - Negative (password is empty)
Mocking:
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element #email
 - enter '' into element #password
 - click element input[type="submit"]
 - validate that the current page shows message 'email/password combination incorrect'.

## Test case R1.6.3 - Email and password both cannot be empty. - Negative (username is empty)
Mocking:
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter '' into element #email
 - enter test_user's password into element #password
 - click element input[type="submit"]
 - validate that the current page is /login

## Test case R1.7.1 - Email has to follow addr-spec defined in RFC 5322. -Postive
Mocking:
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter 'asjdh' email into element #email
 - enter test_user's password into element #password
 - click element input[type="submit"]
 - open /login again
 - validate that current page contains #welcome-header element

## Test case R1.7.2 - Email has to follow addr-spec defined in RFC 5322. -Negative (doesn't follow addr-spec defined)
Mocking:
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element #email
 - enter test_user's password into element #password
 - click element input[type="submit"]
 - validate that the current page is /login

## Test case R1.8.1 - Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character. - Postive
Mocking:
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element #email
 - enter test_user's password into element #password
 - click element input[type="submit"]
 - open /login again
 - validate that current page contains #welcome-header element

## Test case R1.8.2 - Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character. - Negative (less than 6 characters)
Mocking:
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element #email
 - enter 'Lel!' into element #password
 - click element input[type="submit"]
 - validate that the current page is /login

## Test case R1.8.3 - Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character. - Negative (no upper case letter)
Mocking:
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element #email
 - enter 'ewe!ewes' into element #password
 - click element input[type="submit"]
 - validate that the current page is /login

## Test case R1.8.4 - Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character. - Negative (no lower case letter)
Mocking:
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element #email
 - enter 'JAJDH!ER' into element #password
 - click element input[type="submit"]
 - validate that the current page is /login

## Test case R1.8.5 - Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character. - Negative (no special character)
Mocking:
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element #email
 - enter 'Hrjsieow' into element #password
 - click element input[type="submit"]
 - validate that the current page is /login

## Test case R1.9 - For any formatting errors, render the login page and show the message 'email/password format is incorrect.'.
Mocking:
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - run Test case R1.6.2
 - validate that the current page shows message 'email/password combination incorrect'.
 - open /logout
 - open /login again
 - run Test case R1.6.3
 - validate that the current page shows message 'email/password combination incorrect'.
 - open /logout
 - open /login again
 - run Test case R1.7.2
 - validate that the current page shows message 'email/password combination incorrect'.
 - open /logout
 - open /login again
 - run Test case R1.8.2
 - validate that the current page shows message 'email/password combination incorrect'.
 - open /logout
 - open /login again
 - run Test case R1.8.3
 - validate that the current page shows message 'email/password combination incorrect'.
 - open /logout
 - open /login again
 - run Test case R1.8.4
 - validate that the current page shows message 'email/password combination incorrect'.
 - open /logout
 - open /login again
 - run Test case R1.8.5
 - validate that the current page shows message 'email/password combination incorrect'.

## Test case R1.10 - If email/password are correct, redirect to /.
Mocking:
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element #email
 - enter test_user's password into element #password
 - click element input[type="submit"]
 - validate that / page is open

## Test case R1.11 - Otherwise, redict to /login and show message 'email/password combination incorrect'.
Mocking:
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter 'random' into element #email
 - enter 'stuff' into element #password
 - click element input[type="submit"]
 - validate that the current page shows message 'email/password combination incorrect'.




