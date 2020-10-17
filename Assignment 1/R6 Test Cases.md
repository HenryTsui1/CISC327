# R6 /buy [POST]
Test Data:
```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
```
test_ticket = Ticket(
    owner='test_frontend@test.com',
    name='test_ticket_yo',
    quantity=10,
    price=10,
    date='20200901'
)
```

## Test Case R6.1 The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. - Positive
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
 - enter `test ticket1` into element `#buy_name`
 - enter `10` into element `#buy_quantity`
 - enter `10` into element `#buy_price`
 - enter `20200901` into element `#buy_date`
 - click element `#buy_submit`
 - validate that the `#buy_message` element shows "Successful."
 - open /logout (clean up)

## Test Case R6.1 The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. - Negative (Non-Aplhanumeric)
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
 - enter `test_ticket$$` into element `#buy_name`
 - enter `10` into element `#buy_quantity`
 - enter `10` into element `#buy_price`
 - enter `20200901` into element `#buy_date`
 - click element `#buy_submit`
 - validate that the `#buy_message` element shows "Successful."
 - open /logout (clean up)

## Test Case R6.1 The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. - Negative (Space in first character)
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
 - enter ` test ticket1` into element `#buy_name`
 - enter `10` into element `#buy_quantity`
 - enter `10` into element `#buy_price`
 - enter `20200901` into element `#buy_date`
 - click element `#buy_submit`
 - validate that the `#buy_message` element shows "Successful."
 - open /logout (clean up)

## Test Case R6.1 The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. - Negative (Space in last character)
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
 - enter `test ticket ` into element `#buy_name`
 - enter `10` into element `#buy_quantity`
 - enter `10` into element `#buy_price`
 - enter `20200901` into element `#buy_date`
 - click element `#buy_submit`
 - validate that the `#buy_message` element shows "Successful."
 - open /logout (clean up)

## Test Case R6.2 The name of the ticket is no longer than 60 characters. - Positive
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
 - enter `testticket1` into element `#buy_name`
 - enter `10` into element `#buy_quantity`
 - enter `10` into element `#buy_price`
 - enter `20200901` into element `#buy_date`
 - click element `#buy_submit`
 - validate that the `#buy_message` element shows "Successful."
 - open /logout (clean up)

## Test Case R6.2 The name of the ticket is no longer than 60 characters. - Negative
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
 - enter `ticketticketticketticketticketticketticketticketticketticket1` into element `#buy_name`
 - enter `10` into element `#buy_quantity`
 - enter `10` into element `#buy_price`
 - enter `20200901` into element `#buy_date`
 - click element `#buy_submit`
 - validate that the `#buy_message` element shows "Error. Ticket name over 60 Characters."
 - open /logout (clean up)

## Test Case R6.3 The quantity of the tickets has to be more than 0, and less than or equal to 100. - Positive
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
 - enter `testticket1` into element `#buy_name`
 - enter `10` into element `#buy_quantity`
 - enter `10` into element `#buy_price`
 - enter `20200901` into element `#buy_date`
 - click element `#buy_submit`
 - validate that the `#buy_message` element shows "Successful."
 - open /logout (clean up)

## Test Case R6.3 The quantity of the tickets has to be more than 0, and less than or equal to 100. - Negative (Quantity of 0)
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
 - enter `testticket1` into element `#buy_name`
 - enter `0` into element `#buy_quantity`
 - enter `10` into element `#buy_price`
 - enter `20200901` into element `#buy_date`
 - click element `#buy_submit`
 - validate that the `#buy_message` element shows "Error. Invalid ticket quantity."
 - open /logout (clean up)

## Test Case R6.3 The quantity of the tickets has to be more than 0, and less than or equal to 100. - Negative (Quantity of 101)
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
 - enter `testticket1` into element `#buy_name`
 - enter `101` into element `#buy_quantity`
 - enter `10` into element `#buy_price`
 - enter `20200901` into element `#buy_date`
 - click element `#buy_submit`
 - validate that the `#buy_message` element shows "Error. Invalid ticket quantity."
 - open /logout (clean up)

## Test Case R6.4 The ticket name exists in the database and the quantity is more than the quantity requested to buy. - Positive
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
 - enter `testticket1` into element `#buy_name`
 - enter `10` into element `#buy_quantity`
 - enter `10` into element `#buy_price`
 - enter `20200901` into element `#buy_date`
 - click element `#buy_submit`
 - validate that the `#buy_message` element shows "Successful"
 - open /logout (clean up)

## Test Case R6.4 The ticket name exists in the database and the quantity is more than the quantity requested to buy. - Negative (Ticket name does not exist in the database)
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
 - enter `wrong_ticket` into element `#buy_name`
 - enter `10` into element `#buy_quantity`
 - enter `10` into element `#buy_price`
 - enter `20200901` into element `#buy_date`
 - click element `#buy_submit`
 - validate that the `#buy_message` element shows "Error. Ticket name does not exist in the database"
 - open /logout (clean up)

## Test Case R6.4 The ticket name exists in the database and the quantity is more than the quantity requested to buy. - Negative (Quantity is less than quantity requested to buy)
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
 - enter `ticketname1` into element `#buy_name`
 - enter `101` into element `#buy_quantity`
 - enter `10` into element `#buy_price`
 - enter `20200901` into element `#buy_date`
 - click element `#buy_submit`
 - validate that the `#buy_message` element shows "Error. Ticket name does not exist in the database"`
 - open /logout (clean up)

## Test Case R6.4 The ticket name exists in the database and the quantity is more than the quantity requested to buy. - Negative (Ticket name does not exist in database, Quantity is less than quantity requested to buy)
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
 - enter `wrong_ticket` into element `#buy_name`
 - enter `101` into element `#buy_quantity`
 - enter `10` into element `#buy_price`
 - enter `20200901` into element `#buy_date`
 - click element `#buy_submit`
 - validate that the `#buy_message` element shows "Error. Ticket name does not exist in the database"`
 - open /logout (clean up)


## Test Case R6.5 The user has more balance than the ticket price * quantity + service fee(35%) + tax(5%) - Positive
 - Mock backend.get_user to return a test_user instance
 - Mock backend.get_ticket to return a test_ticket instance  

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - enter `testticket1` into element `#buy_name`
 - enter `10` into element `#buy_quantity`
 - enter `10` into element `#buy_price`
 - enter `20200901` into element `#buy_date`
 - click element `#buy_submit`
 - validate that the `#buy_message` element shows "Successful"`
 - open /logout (clean up)


## Test Case R6.5 The user has more balance than the ticket price * quantity + service fee(35%) + tax(5%) - Negative (Balance less than ticket price * quantity + service fee(35%) + tax(5%)
 - Mock backend.get_user to return a test_user instance
 - Mock backend.get_ticket to return a test_ticket instance  

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - enter `testticket1` into element `#buy_name`
 - enter `10` into element `#buy_quantity`
 - enter `10` into element `#buy_price`
 - enter `20200901` into element `#buy_date`
 - click element `#buy_submit`
 - validate that the `#buy_message` element shows "Error: Invalid balance"`
 - open /logout (clean up)


## Test Case R6.6 For any errors, redirect back to / and show an error message
 - Mock backend.get_user to return a test_user instance
 - Mock backend.get_ticket to return a test_ticket instance  

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - enter `testticket1` into element `#buy_name`
 - enter `10` into element `#buy_quantity`
 - enter `10` into element `#buy_price`
 - enter `20200901` into element `#buy_date`
 - click element `#buy_submit`
 - validate that the / is open and shows "Error: Invalid entry"`
 - open /logout (clean up)



















