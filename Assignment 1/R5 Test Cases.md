# R5 /update [POST]
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
    quantity=20,
    price=20,
    date='20200901'
)
```

## Test Case R5.1 The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. - Positive
Mocking:
 - Mock backend.get_user to return a test_user instance 
 - Mock backend.get_ticket to return a test_ticket instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - enter `test_ticket` into element `#update_name`
 - enter `10` into element `#update_quantity`
 - enter `10` into element `#update_price`
 - enter `20201017` into element `#update_date`
 - click element `#update_submit`
 - validate that the `#update_message` element shows `Successful.`
 - open /logout (clean up)

## Test Case R5.1 The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. - Negative (Non-Aplhanumeric)
Mocking:
 - Mock backend.get_user to return a test_user instance
 - Mock backend.get_ticket to return a test_ticket instance 

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - enter `test_ticket$$` into element `#update_name`
 - enter `10` into element `#update_quantity`
 - enter `10` into element `#update_price`
 - enter `20201017` into element `#update_date`
 - click element `#update_submit`
 - validate that the `#update_message` element shows `Error. Invalid ticket name.`
 - open /logout (clean up)

## Test Case R5.1 The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. - Negative (Space in first character)
Mocking:
 - Mock backend.get_user to return a test_user instance 
 - Mock backend.get_ticket to return a test_ticket instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - enter ` test_ticket` into element `#update_name`
 - enter `10` into element `#update_quantity`
 - enter `10` into element `#update_price`
 - enter `20201017` into element `#update_date`
 - click element `#update_submit`
 - validate that the `#update_message` element shows `Error. Invalid ticket name.`
 - open /logout (clean up)

## Test Case R5.1 The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. - Negative (Space in last character)
Mocking:
 - Mock backend.get_user to return a test_user instance 
 - Mock backend.get_ticket to return a test_ticket instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - enter `test_ticket ` into element `#update_name`
 - enter `10` into element `#update_quantity`
 - enter `10` into element `#update_price`
 - enter `20201017` into element `#update_date`
 - click element `#update_submit`
 - validate that the `#update_message` element shows `Error. Invalid ticket name.`
 - open /logout (clean up)

## Test Case R5.2 The name of the ticket is no longer than 60 characters. - Positive
Mocking:
 - Mock backend.get_user to return a test_user instance 
 - Mock backend.get_ticket to return a test_ticket instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - enter `test_ticket` into element `#update_name`
 - enter `10` into element `#update_quantity`
 - enter `10` into element `#update_price`
 - enter `20201017` into element `#update_date`
 - click element `#update_submit`
 - validate that the `#update_message` element shows `Successful.`
 - open /logout (clean up)

## Test Case R5.2 The name of the ticket is no longer than 60 characters. - Negative
Mocking:
 - Mock backend.get_user to return a test_user instance 
 - Mock backend.get_ticket to return a test_ticket instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - enter `test_tickettest_tickettest_tickettest_tickettest_tickettest_ticket` into element `#update_name`
 - enter `10` into element `#update_quantity`
 - enter `10` into element `#update_price`
 - enter `20201017` into element `#update_date`
 - click element `#update_submit`
 - validate that the `#update_message` element shows `Error. Ticket name over 60 Characters.`
 - open /logout (clean up)

## Test Case R5.3 The quantity of the tickets has to be more than 0, and less than or equal to 100. - Positive
Mocking:
 - Mock backend.get_user to return a test_user instance 
 - Mock backend.get_ticket to return a test_ticket instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - enter `test_ticket` into element `#update_name`
 - enter `10` into element `#update_quantity`
 - enter `10` into element `#update_price`
 - enter `20201017` into element `#update_date`
 - click element `#update_submit`
 - validate that the `#update_message` element shows `Successful.`
 - open /logout (clean up)

## Test Case R5.3 The quantity of the tickets has to be more than 0, and less than or equal to 100. - Negative (Quantiity of 0)
Mocking:
 - Mock backend.get_user to return a test_user instance 
 - Mock backend.get_ticket to return a test_ticket instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - enter `test_ticket` into element `#update_name`
 - enter `0` into element `#update_quantity`
 - enter `10` into element `#update_price`
 - enter `20201017` into element `#update_date`
 - click element `#update_submit`
 - validate that the `#update_message` element shows `Error. Invalid ticket quantity.`
 - open /logout (clean up)

## Test Case R5.3 The quantity of the tickets has to be more than 0, and less than or equal to 100. - Negative (Quantiity of 101)
Mocking:
 - Mock backend.get_user to return a test_user instance 
 - Mock backend.get_ticket to return a test_ticket instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - enter `test_ticket` into element `#update_name`
 - enter `101` into element `#update_quantity`
 - enter `10` into element `#update_price`
 - enter `20201017` into element `#update_date`
 - click element `#update_submit`
 - validate that the `#update_message` element shows `Error. Invalid ticket quantity.`
 - open /logout (clean up)

## Test Case R5.4 Price has to be of range [10, 100]. - Positive
Mocking:
 - Mock backend.get_user to return a test_user instance 
 - Mock backend.get_ticket to return a test_ticket instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - enter `test_ticket` into element `#update_name`
 - enter `10` into element `#update_quantity`
 - enter `10` into element `#update_price`
 - enter `20201017` into element `#update_date`
 - click element `#update_submit`
 - validate that the `#update_message` element shows `Successful.`
 - open /logout (clean up)

## Test Case R5.4 Price has to be of range [10, 100]. - Negative (Price of 9)
Mocking:
 - Mock backend.get_user to return a test_user instance 
 - Mock backend.get_ticket to return a test_ticket instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - enter `test_ticket` into element `#update_name`
 - enter `10` into element `#update_quantity`
 - enter `9` into element `#update_price`
 - enter `20201017` into element `#update_date`
 - click element `#update_submit`
 - validate that the `#update_message` element shows `Error. Invalid price.`
 - open /logout (clean up)

## Test Case R5.4 Price has to be of range [10, 100]. - Negative (Price of 101)
Mocking:
 - Mock backend.get_user to return a test_user instance 
 - Mock backend.get_ticket to return a test_ticket instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - enter `test_ticket` into element `#update_name`
 - enter `10` into element `#update_quantity`
 - enter `101` into element `#update_price`
 - enter `20201017` into element `#update_date`
 - click element `#update_submit`
 - validate that the `#update_message` element shows `Error. Invalid price.`
 - open /logout (clean up)
 
## Test Case R5.5 Date must be given in the format YYYYMMDD (e.g. 20200901). - Positive
Mocking:
 - Mock backend.get_user to return a test_user instance 
 - Mock backend.get_ticket to return a test_ticket instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - enter `test_ticket` into element `#update_name`
 - enter `10` into element `#update_quantity`
 - enter `10` into element `#update_price`
 - enter `20201017` into element `#update_date`
 - click element `#update_submit`
 - validate that the `#update_message` element shows `Successful.`
 - open /logout (clean up)

## Test Case R5.5 Date must be given in the format YYYYMMDD (e.g. 20200901). - Negative
Mocking:
 - Mock backend.get_user to return a test_user instance 
 - Mock backend.get_ticket to return a test_ticket instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - enter `test_ticket` into element `#update_name`
 - enter `10` into element `#update_quantity`
 - enter `10` into element `#update_price`
 - enter `October 17, 2020` into element `#update_date`
 - click element `#update_submit`
 - validate that the `#update_message` element shows `Error. Invalid date.`
 - open /logout (clean up)

## Test Case R5.6 The ticket of the given name must exist.
Mocking:
 - Mock backend.get_user to return a test_user instance 
 - Mock backend.get_ticket to return a test_ticket instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - enter `wrong_ticket` into element `#update_name`
 - enter `10` into element `#update_quantity`
 - enter `10` into element `#update_price`
 - enter `20201017` into element `#update_date`
 - click element `#update_submit`
 - validate that the `#update_message` element shows `Error. Ticket does not exist.`
 - open /logout (clean up)

## Test Case R5.7 For any errors, redirect back to / and show an error message.
Mocking:
 - Mock backend.get_user to return a test_user instance 
 - Mock backend.get_ticket to return a test_ticket instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - enter `test_ticket$$` into element `#update_name`
 - enter `10` into element `#update_quantity`
 - enter `10` into element `#update_price`
 - enter `20201017` into element `#update_date`
 - click element `#update_submit`
 - validate that / is open and `Error. Invalid ticket name.` message is displayed
 - open /logout (clean up)

