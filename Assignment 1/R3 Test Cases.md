# R3

## Test Data:



test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)

temp_tickets = Tickets(
	name = 'Billy Joel',
	quantity = '7',
	price = '30',
	expiration-date = '20201212')




## Test Cases

## R3.1

## User is not logged in. Check that / redirects to login, 
Mocking:
-backend.get_user 

Actions:
-open /logout (to invalidate any logged-in sessions that may exist)
open /
-check that /login opens automatically when accessing / 
-open /logout



## R3.2

## User is logged in. Check that / displays proper info is displayed and /logout works
Mocking:
-backend.get_user ## returns user info

Actions:
-open /logout (to invalidate any logged-in sessions that may exist)
open /
-check that /login opens automatically when accessing / 
-open /login
-enter test_user's email into element `#email`
-enter test_user's password into element `#password`
-click element `input[type="submit"]`
-open /
-validate that this page contains #welcome-header element
-validate #welcome-header includes " 'Hi {}'.format(user.name) "
-validate that element #user.balance is displayed
-validate that #logout button is displayed
-click element input[type="logout"]
-check that clicking #logout triggers open/logout 
-open /logout (clean up)




## R3.3
## This verifies that ticket info is available after login

Mocking:
-backend.get_user ## returns user info

Actions:
-open /logout (to invalidate any logged-in sessions that may exist)
-open /login
-enter test_user's email into element `#email`
-enter test_user's password into element `#password`
-click element `input[type="submit"]`
-open /
-validate that tickets are visible on /
-validate that #quantity element displays '7'
-validate that #owners-email displays 'test_frontend@test.com'
-validate that #price displays '30'
-validate that #quantity, #owners-email and #price elements are not visible on expired tickets
-open /logout



## R3.4.1
## Verify that sell fields exist

Mocking:
-backend.get_user

Actions:
-open /logout (to invalidate any logged-in sessions that may exist)
-open /login
-enter test_user's email into element `#email`
-enter test_user's password into element `#password`
-click element `input[type="submit"]`
-open /
-validate that #sell-name element is present in selling form
-validate that #sell-quantity element is present in selling form
-validate that #sell-price element is present in selling form
-validate that #sell-expiration-date element is present in selling form

open /logout



## R3.4.2
## Verify that sell fields can have data entered

Mocking:
-backend.get_user

Actions:
-open /logout (to invalidate any logged-in sessions that may exist)
-open /login
-enter test_user's email into element `#email`
-enter test_user's password into element `#password`
-click element `input[type="submit"]`
-open /
-enter "temp-name" into #sell-name element
-enter "4" into #sell-quantity element
-enter "30" into #sell-price element
-enter "20200904" into #esell-xpiration-date element
open /logout


## R3.5.1
## Verify that buy fields exist 

Mocking:
-backend.get_user ## to get specific user instance
-backend.get_temp_tickets

Actions:
-open /logout (to invalidate any logged-in sessions that may exist)
-open /login
-enter test_user's email into element `#email`
-enter test_user's password into element `#password`
-click element `input[type="submit"]`
-open /
-validate that #buy-name element is present in buying form
-validate that #buy-quantity element is present in buying form
- open /logout



## R3.5.2
## Verify that buy fields can have info entered

Mocking:
-backend.get_user ## to get specific user instance
-backend.get_temp_tickets

Actions:
-open /logout (to invalidate any logged-in sessions that may exist)
-open /login
-enter test_user's email into element `#email`
-enter test_user's password into element `#password`
-click element `input[type="submit"]`
-open /
-enter 'Billy Joel' as #buy-name
-enter "4" as #buy-quantity
- open /logout


## R3.6
## Verify that sell operation can be completed

Mocking:
-backend.get_user 
-backend.set-temp-tickets## update tickets available for user

Actions:
-open /logout (to invalidate any logged-in sessions that may exist)
-open /login
-enter test_user's email into element `#email`
-enter test_user's password into element `#password`
-click element `input[type="submit"]`
-open /
-enter "sell-temp-name" into #name element
-enter "4" into #sell-quantity element
-enter "30" into #sell-price element
-enter "20210904" into #sell-expiration-date element
-open /sell
-verify that /sell POST has been sent, recorded and shows success



## R3.7
## Verify that sell operation now visible to user 

Mocking:
-backend.get_user 
-backend.set-temp-tickets## update tickets available for user

Actions:
-open /logout (to invalidate any logged-in sessions that may exist)
-open /login
-enter test_user's email into element `#email`
-enter test_user's password into element `#password`
-click element `input[type="submit"]`
-open /
-validate "sell-temp-name" as #name element
-validate "4" as #sell-quantity element
-validate "30" as #sell-price element
-validate "20210904" as #sell-expiration-date element
- open /logout



## R3.8.1
## Verify that buy can be completed 

Mocking:
-backend.get_user to get specific user instance ## returns user info
-backend.get_temp_tickets

Actions:
-open /logout (to invalidate any logged-in sessions that may exist)
-open /login
-enter test_user's email into element `#email`
-enter test_user's password into element `#password`
-click element `input[type="submit"]`
-open /
-enter 'Billy Joel' as buy-name
-enter "4" as #buy-quantity
-click element #buy-submit
-validate that /buy POST has been completed, recorded and shows success
- open /logout




## R3.8.2
## Verify that bought tickets are visible to user

Mocking:
-backend.get_user to get specific user instance ## returns user info
-backend.get_temp_tickets

Actions:
-open /logout (to invalidate any logged-in sessions that may exist)
-open /login
-enter test_user's email into element `#email`
-enter test_user's password into element `#password`
-click element `input[type="submit"]`
-open /
-validate that new tickets are visible in /
-validate element #name = 'Billy Joel' 
-validate element #quanitity = "4"
-validate element #expiration-date = "20201212"
-validate element #price = "30"
- open /logout





## R3.9.1
## Verify that update elements exist

Mocking:
-backend.get_user to get specific user instance ## returns user info
-backend.get_temp_tickets

Actions:
-open /logout (to invalidate any logged-in sessions that may exist)
-open /login
-enter test_user's email into element `#email`
-enter test_user's password into element `#password`
-click element `input[type="submit"]`
-open /
-validate element #update-price is displayed
-validate element #update-name is displayed
-validate element #update-quantity is displayed
-validate element #update-expiry-date is displayed
-open /logout


## R3.9.2
## Verify that update elements can have info entered

Mocking:
-backend.get_user to get specific user instance ## returns user info
-backend.get_temp_tickets

Actions:
-open /logout (to invalidate any logged-in sessions that may exist)
-open /login
-enter test_user's email into element `#email`
-enter test_user's password into element `#password`
-click element `input[type="submit"]`
-open /
-click element #update-price
-enter "5"
-click element #update-name
-enter "BILLY-JOEL"
-click element #update-quantity
-enter "4"
-click element #update-expiry-date
-enter "20211212"
-open /logout

## R3.9.3
## Verify that updated tickets now visible to user

Mocking:
-backend.get_user to get specific user instance ## returns user info
-backend.get_temp_tickets

Actions:
-open /logout (to invalidate any logged-in sessions that may exist)
-open /login
-enter test_user's email into element `#email`
-enter test_user's password into element `#password`
-click element `input[type="submit"]`
-open /
-click element #update-price
-enter "5"
-click element #update-name
-enter "BILLY-JOEL"
-click element #update-quantity
-enter "4"
-click element #update-expiry-date
-enter "20211212"
-click element #save-changes
-POST /update
-open / (refresh)
-validate element #update-price = "5"
-validate element #update-name = "BILLY-JOEL"
-validate element #update-quantity = "4"
-validate element #update-expiry-date = "20211212"
-open /logout





