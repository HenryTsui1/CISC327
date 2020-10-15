# R4 /sell [POST]
Test Data:
```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
```

## Test Case R4.1 The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. - Positive
Mocking:
 - Mock backend.get_user to return a test_user instance 

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - enter `test ticket1` into element `#sell_name`
 - enter `10` into element `#sell_quantity`
 - enter `10` into element `#sell_price`
 - enter `20201017` into element `#sell_date`
 - click element `#sell_submit`
 - validate that the `#sell_message` element shows `Successful.`
 - open /logout (clean up)

## Test Case R4.1 The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. - Negative (Non-Aplhanumeric)
Mocking:
 - Mock backend.get_user to return a test_user instance 

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - enter `test_ticket$$` into element `#sell_name`
 - enter `10` into element `#sell_quantity`
 - enter `10` into element `#sell_price`
 - enter `20201017` into element `#sell_date`
 - click element `#sell_submit`
 - validate that the `#sell_message` element shows `Error. Invalid ticket name.`
 - open /logout (clean up)

## Test Case R4.1 The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. - Negative (Space in first character)
Mocking:
 - Mock backend.get_user to return a test_user instance 

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - enter ` test_ticket` into element `#sell_name`
 - enter `10` into element `#sell_quantity`
 - enter `10` into element `#sell_price`
 - enter `20201017` into element `#sell_date`
 - click element `#sell_submit`
 - validate that the `#sell_message` element shows `Error. Invalid ticket name.`
 - open /logout (clean up)

## Test Case R4.1 The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. - Negative (Space in last character)
Mocking:
 - Mock backend.get_user to return a test_user instance 

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - enter `test_ticket ` into element `#sell_name`
 - enter `10` into element `#sell_quantity`
 - enter `10` into element `#sell_price`
 - enter `20201017` into element `#sell_date`
 - click element `#sell_submit`
 - validate that the `#sell_message` element shows `Error. Invalid ticket name.`
 - open /logout (clean up)

## Test Case R4.2 The name of the ticket is no longer than 60 characters. - Positive
Mocking:
 - Mock backend.get_user to return a test_user instance 

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - enter `test_ticket` into element `#sell_name`
 - enter `10` into element `#sell_quantity`
 - enter `10` into element `#sell_price`
 - enter `20201017` into element `#sell_date`
 - click element `#sell_submit`
 - validate that the `#sell_message` element shows `Successful.`
 - open /logout (clean up)

## Test Case R4.2 The name of the ticket is no longer than 60 characters. - Negative
Mocking:
 - Mock backend.get_user to return a test_user instance 

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - enter `test_tickettest_tickettest_tickettest_tickettest_tickettest_ticket` into element `#sell_name`
 - enter `10` into element `#sell_quantity`
 - enter `10` into element `#sell_price`
 - enter `20201017` into element `#sell_date`
 - click element `#sell_submit`
 - validate that the `#sell_message` element shows `Error. Ticket name over 60 Characters.`
 - open /logout (clean up)

## Test Case R4.3 The quantity of the tickets has to be more than 0, and less than or equal to 100. - Positive
Mocking:
 - Mock backend.get_user to return a test_user instance 

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - enter `test_ticket` into element `#sell_name`
 - enter `10` into element `#sell_quantity`
 - enter `10` into element `#sell_price`
 - enter `20201017` into element `#sell_date`
 - click element `#sell_submit`
 - validate that the `#sell_message` element shows `Successful.`
 - open /logout (clean up)

## Test Case R4.3 The quantity of the tickets has to be more than 0, and less than or equal to 100. - Negative (Quantiity of 0)
Mocking:
 - Mock backend.get_user to return a test_user instance 

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - enter `test_ticket` into element `#sell_name`
 - enter `0` into element `#sell_quantity`
 - enter `10` into element `#sell_price`
 - enter `20201017` into element `#sell_date`
 - click element `#sell_submit`
 - validate that the `#sell_message` element shows `Error. Invalid ticket quantity.`
 - open /logout (clean up)

## Test Case R4.3 The quantity of the tickets has to be more than 0, and less than or equal to 100. - Negative (Quantiity of 101)
Mocking:
 - Mock backend.get_user to return a test_user instance 

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - enter `test_ticket` into element `#sell_name`
 - enter `101` into element `#sell_quantity`
 - enter `10` into element `#sell_price`
 - enter `20201017` into element `#sell_date`
 - click element `#sell_submit`
 - validate that the `#sell_message` element shows `Error. Invalid ticket quantity.`
 - open /logout (clean up)

## Test Case R4.4 Price has to be of range [10, 100]. - Positive
Mocking:
 - Mock backend.get_user to return a test_user instance 

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - enter `test_ticket` into element `#sell_name`
 - enter `10` into element `#sell_quantity`
 - enter `10` into element `#sell_price`
 - enter `20201017` into element `#sell_date`
 - click element `#sell_submit`
 - validate that the `#sell_message` element shows `Successful.`
 - open /logout (clean up)

## Test Case R4.4 Price has to be of range [10, 100]. - Negative (Price of 9)
Mocking:
 - Mock backend.get_user to return a test_user instance 

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - enter `test_ticket` into element `#sell_name`
 - enter `10` into element `#sell_quantity`
 - enter `9` into element `#sell_price`
 - enter `20201017` into element `#sell_date`
 - click element `#sell_submit`
 - validate that the `#sell_message` element shows `Error. Invalid price.`
 - open /logout (clean up)

## Test Case R4.4 Price has to be of range [10, 100]. - Negative (Price of 101)
Mocking:
 - Mock backend.get_user to return a test_user instance 

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - enter `test_ticket` into element `#sell_name`
 - enter `10` into element `#sell_quantity`
 - enter `101` into element `#sell_price`
 - enter `20201017` into element `#sell_date`
 - click element `#sell_submit`
 - validate that the `#sell_message` element shows `Error. Invalid price.`
 - open /logout (clean up)
 
## Test Case R4.5 Date must be given in the format YYYYMMDD (e.g. 20200901). - Positive
Mocking:
 - Mock backend.get_user to return a test_user instance 

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - enter `test_ticket` into element `#sell_name`
 - enter `10` into element `#sell_quantity`
 - enter `10` into element `#sell_price`
 - enter `20201017` into element `#sell_date`
 - click element `#sell_submit`
 - validate that the `#sell_message` element shows `Successful.`
 - open /logout (clean up)

## Test Case R4.5 Date must be given in the format YYYYMMDD (e.g. 20200901). - Negative
Mocking:
 - Mock backend.get_user to return a test_user instance 

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - enter `test_ticket` into element `#sell_name`
 - enter `10` into element `#sell_quantity`
 - enter `10` into element `#sell_price`
 - enter `October 17, 2020` into element `#sell_date`
 - click element `#sell_submit`
 - validate that the `#sell_message` element shows `Error. Invalid date.`
 - open /logout (clean up)

## Test Case R4.6 For any errors, redirect back to / and show an error message.
Mocking:
 - Mock backend.get_user to return a test_user instance 

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - enter `test_ticket$$` into element `#sell_name`
 - enter `10` into element `#sell_quantity`
 - enter `10` into element `#sell_price`
 - enter `20201017` into element `#sell_date`
 - click element `#sell_submit`
 - validate that / is open and `Error. Invalid ticket name.` message is displayed
 - open /logout (clean up)

## Test Case R4.7 The added new ticket information will be posted on the user profile page.
Mocking:
 - Mock backend.get_user to return a test_user instance 

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - enter `test_ticket` into element `#sell_name`
 - enter `10` into element `#sell_quantity`
 - enter `10` into element `#sell_price`
 - enter `20201017` into element `#sell_date`
 - click element `#sell_submit`
 - validate that / is open and `test_ticket` is in list of tickets
 - open /logout (clean up)
