# R7.1 /logout [GET, POST]
Test Data:
```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
```
```
test_ticket = Ticket(
    owner='test_frontend@test.com',
    name='test_ticket',
    quantity=10,
    price=10,
    date='20200901'
)
```

## Test Case R7.1 Logout will invalid the current session and redirect to the login page. After logout, the user shouldn't be able to access restricted pages. - Positive
Mocking:
 - Mock backend.get_user to return a test_user instance 
 - Mock backend.get_ticket to return a test_ticket instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - validate that the `#update_message` element shows `Successful.`
 - click element `#logout_submit`
 - open /logout
 - validate that /login doesn't redirect to /







