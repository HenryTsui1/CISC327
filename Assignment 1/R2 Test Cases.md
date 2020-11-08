# R2 /register [GET]

Test Data:
```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
test_user_register = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend'),
    password2=password
)
```
## Test Case R2.1 If the user has logged in, redirect back to the user profile page
Mocking:
 - Mock backend.get_user to return a test_user instance 

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element #email
 - enter test_user's password into element #password
 - click element input[type="submit"]
 - open /login again
 - validate / is open

## Test Case R2.2 otherwise, show the user registration page
Mocking:
 - Mock backend.get_user to return a test_user instance 

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter 'wrong email' into element #email
 - enter 'wrong password' into element #password
 - click element input[type="submit"]
 - validate /register is open

## Test Case R2.3 the registration page shows a registration form requesting: email, user name, password, password2
Mocking:
 - N/A

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /register
 - validate that current page contains #email element
 - validate that current page contains #username element
 - validate that current page contains #password element
 - validate that current page contains #password2 element

# [POST]

## Test case R2.4 - The registration form can be submitted as a POST request to the current URL (/register)
Mocking:
 - Mock backend.get_user to return a test_user_regsiter instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /register
 - validate that current page contains #submit element

## Test case R2.5.1 - Email, password, password2 all have to satisfy the same required as defined in R1 - Positive
Mocking:
 - Mock backend.get_user to return a test_user_register instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /register
 - enter test_user_register's email into element #email
 - enter test_user_register's username into element #username
 - enter test_user's password into element #password
 - enter test_user's password2 into element #password2
 - click element input[type="submit"]
 - validate that the current page shows message 'successful registration'.

## Test case R2.5.2 - Email, password, password2 all have to satisfy the same required as defined in R1 - Negative (email doesn't satisfy)
Mocking:
 - Mock backend.get_user to return a test_user_register instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /register
 - enter 'esf' into element #email
 - enter test_user_register's username into element #username
 - enter test_user's password into element #password
 - enter test_user's password2 into element #password2
 - click element input[type="submit"]
 - validate that the current page shows message 'incorrect input'.


## Test case R2.5.3 - Email, password, password2 all have to satisfy the same required as defined in R1 - Negative (username doesn't satisfy)
Mocking:
 - Mock backend.get_user to return a test_user_register instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /register
 - enter test_user_register's email into element #email
 - enter '12 ' into element #username
 - enter test_user's password into element #password
 - enter test_user's password2 into element #password2
 - click element input[type="submit"]
 - validate that the current page shows message 'incorrect input'.

## Test case R2.5.4 - Email, password, password2 all have to satisfy the same required as defined in R1 - Negative (password doesn't satisfy)
Mocking:
 - Mock backend.get_user to return a test_user_register instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /register
 - enter test_user_register's email into element #email
 - enter test_user_register's username into element #username
 - enter '23' into element #password
 - enter test_user's password2 into element #password2
 - click element input[type="submit"]
 - validate that the current page shows message 'incorrect input'.

## Test case R2.5.5 - Email, password, password2 all have to satisfy the same required as defined in R1 - Negative (password2 doesn't satisfy)
Mocking:
 - Mock backend.get_user to return a test_user_register instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /register
 - enter test_user_register's email into element #email
 - enter test_user_register's username into element #username
 - enter test_user's password into element #password
 - enter ' 32' into element #password2
 - click element input[type="submit"]
 - validate that the current page shows message 'incorrect input'.

## Test case R2.6.1 - Password and password2 have to be exactly the same - Positive
Mocking:
 - Mock backend.get_user to return a test_user_register instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /register
 - enter test_user_register's email into element #email
 - enter test_user_register's username into element #username
 - enter test_user's password into element #password
 - enter test_user's password2 into element #password2
 - click element input[type="submit"]
 - validate that the current page shows message 'successful registration'.

## Test case R2.6.2 - Password and password2 have to be exactly the same - Negative
Mocking:
 - Mock backend.get_user to return a test_user_register instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /register
 - enter test_user_register's email into element #email
 - enter test_user_register's username into element #username
 - enter 'Mn!32323232' into element #password
 - enter 'Nm!23232323' into element #password2
 - click element input[type="submit"]
 - validate that the current page shows message 'incorrect input'.

## Test case R2.7.1 - User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character. - Positive
Mocking:
 - Mock backend.get_user to return a test_user_register instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /register
 - enter test_user_register's email into element #email
 - enter test_user_register's username into element #username
 - enter test_user's password into element #password
 - enter test_user's password2 into element #password2
 - click element input[type="submit"]
 - validate that the current page shows message 'successful registration'.


## Test case R2.7.2 - User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character. - Negative (empty username)
Mocking:
 - Mock backend.get_user to return a test_user_register instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /register
 - enter test_user_register's email into element #email
 - enter '' into element #username
 - enter test_user's password into element #password
 - enter test_user's password2 into element #password2
 - click element input[type="submit"]
 - validate that the current page shows message 'incorrect input'.

## Test case R2.7.3 - User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character. - Negative (not only alphanumeric username)
Mocking:
 - Mock backend.get_user to return a test_user_register instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /register
 - enter test_user_register's email into element #email
 - enter '!#$@' into element #username
 - enter test_user's password into element #password
 - enter test_user's password2 into element #password2
 - click element input[type="submit"]
 - validate that the current page shows message 'incorrect input'.

## Test case R2.7.4 - User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character. - Negative (space in front of username)
Mocking:
 - Mock backend.get_user to return a test_user_register instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /register
 - enter test_user_register's email into element #email
 - enter ' anderson123' into element #username
 - enter test_user's password into element #password
 - enter test_user's password2 into element #password2
 - click element input[type="submit"]
 - validate that the current page shows message 'incorrect input'.

## Test case R2.7.5 - User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character. - Negative (space behind the username)
Mocking:
 - Mock backend.get_user to return a test_user_register instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /register
 - enter test_user_register's email into element #email
 - enter 'anderson123 ' into element #username
 - enter test_user's password into element #password
 - enter test_user's password2 into element #password2
 - click element input[type="submit"]
 - validate that the current page shows message 'incorrect input'.

## Test case R2.8.1 - User name has to be longer than 2 characters and less than 20 characters. - Positive
Mocking:
 - Mock backend.get_user to return a test_user_register instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /register
 - enter test_user_register's email into element #email
 - enter test_user_register's username into element #username
 - enter test_user's password into element #password
 - enter test_user's password2 into element #password2
 - click element input[type="submit"]
 - validate that the current page shows message 'successful registration'.

## Test case R2.8.2 - User name has to be longer than 2 characters and less than 20 characters. - Negative (less than 2 characters)
Mocking:
 - Mock backend.get_user to return a test_user_register instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /register
 - enter test_user_register's email into element #email
 - enter 'ty' into element #username
 - enter test_user's password into element #password
 - enter test_user's password2 into element #password2
 - click element input[type="submit"]
 - validate that the current page shows message 'incorrect input'.

## Test case R2.8.3 - User name has to be longer than 2 characters and less than 20 characters. - Negative (more than 20 characters)
Mocking:
 - Mock backend.get_user to return a test_user_register instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /register
 - enter test_user_register's email into element #email
 - enter 'ty12345678ty12345678ty1234' into element #username
 - enter test_user's password into element #password
 - enter test_user's password2 into element #password2
 - click element input[type="submit"]
 - validate that the current page shows message 'incorrect input'.

## Test case R2.9 - For any formatting errors, redirect back to /login and show message '{} format is incorrect.'.format(the_corresponding_attribute)
Mocking:
 - Mock backend.get_user to return a test_user_register instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /register
 - run Test case R2.5.2
 - validate that the current page shows message '{} format is incorrect.'.format(the_corresponding_attribute)
 - validate that /login is open
 - open /register again
 - run Test case R2.5.3
 - validate that the current page shows message '{} format is incorrect.'.format(the_corresponding_attribute)
 - validate that /login is open
 - open /register again
 - run Test case R2.5.4
 - validate that the current page shows message '{} format is incorrect.'.format(the_corresponding_attribute)
 - validate that /login is open
 - open /register again
 - run Test case R2.5.5
 - validate that the current page shows message '{} format is incorrect.'.format(the_corresponding_attribute)
 - validate that /login is open
 - open /register again
 - run Test case R2.6.2
 - validate that the current page shows message '{} format is incorrect.'.format(the_corresponding_attribute)
 - validate that /login is open
 - open /register again
 - run Test case R2.7.2
 - validate that the current page shows message '{} format is incorrect.'.format(the_corresponding_attribute)
 - validate that /login is open
 - open /register again
 - run Test case R2.7.3
 - validate that the current page shows message '{} format is incorrect.'.format(the_corresponding_attribute)
 - validate that /login is open
 - open /register again
 - run Test case R1.7.4
 - validate that the current page shows message '{} format is incorrect.'.format(the_corresponding_attribute)
 - validate that /login is open
 - open /register again
 - run Test case R1.7.5
 - validate that the current page shows message '{} format is incorrect.'.format(the_corresponding_attribute)
 - validate that /login is open
 - open /register again
 - run Test case R1.8.2
 - validate that the current page shows message '{} format is incorrect.'.format(the_corresponding_attribute)
 - validate that /login is open
 - open /register again
 - run Test case R1.8.3
 - validate that the current page shows message '{} format is incorrect.'.format(the_corresponding_attribute)
 - validate that /login is open

## Test case R2.10 - If the email already exists, show message 'this email has been ALREADY used'
Mocking:
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - enter 'alreadyusedemail@gmail.com' into element #email
 - enter test_user_register's username into element #username
 - enter test_user's password into element #password
 - enter test_user's password2 into element #password2
 - click element input[type="submit"]
 - validate that the current page shows message 'this email has been ALREADY used'

## Test case R2.11 - If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page
Mocking:
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - enter test_user_register's email into element #email
 - enter test_user_register's username into element #username
 - enter test_user's password into element #password
 - enter test_user's password2 into element #password2
 - click element input[type="submit"]
 - validate that the current page shows message 'successful registration'.
 - validate that a new user was created and balance is equal to 5000
 - validate /login page is open
