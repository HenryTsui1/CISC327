#R8

##Test Data:


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






##Test Cases

##R8.1

## Of all http methods, make sure that only GET and POST work on /login
Mocking:
-none

Actions:
-GET /login 
-verify that login page is displayed
-POST /login username=temp&password=temp
-verify that /login shows values in fields

-HEAD /login
-verify that error 404 displayed
-PUT /login
-verify that error 404 displayed
-DELETE /login
-verify that error 404 displayed
-CONNECT /login
-verify that error 404 displayed
-OPTIONS /login
-verify that error 404 displayed
-TRACE /login
-verify that error 404 displayed
-PATCH /login
-verify that error 404 displayed




##R8.2
## Of all http methods, make sure that only GET and POST work on /register

Mocking:
-none

Actions:
-GET /register
-verify that /register page is displayed
-POST /register username=temp&password=temp
-verify that /register shows values in fields
-HEAD /register
-verify that error 404 displayed
-PUT /register
-verify that error 404 displayed
-DELETE /register
-verify that error 404 displayed
-CONNECT /register
-verify that error 404 displayed
-OPTIONS /register
-verify that error 404 displayed
-TRACE /register
-verify that error 404 displayed
-PATCH /register
-verify that error 404 displayed





##R8.3
## Of all http methods, make sure that only GET works on / 

Mocking:
-none

Actions:
-GET /
-verify that / page is displayed
-POST / username=temp&password=temp
-verify that error 404 displayed
-HEAD /
-verify that error 404 displayed
-PUT /
-verify that error 404 displayed
-DELETE /
-verify that error 404 displayed
-CONNECT /
-verify that error 404 displayed
-OPTIONS /
-verify that error 404 displayed
-TRACE /
-verify that error 404 displayed
-PATCH /
-verify that error 404 displayed






##R8.4
## Of all http methods, make sure that only GET and POST work on /logout

Mocking:
-none

Actions:
-GET /logout
-verify that /logout page is displayed
-POST /logout username=temp&password=temp
-verify that user is logged out
-HEAD /logout
-verify that error 404 displayed
-PUT /logout
-verify that error 404 displayed
-DELETE /logout
-verify that error 404 displayed
-CONNECT /logout
-verify that error 404 displayed
-OPTIONS /logout
-verify that error 404 displayed
-TRACE /logout
-verify that error 404 displayed
-PATCH /logout
-verify that error 404 displayed





##R8.5
## Of all http methods, make sure that only POST works on /buy

Mocking:
-none

Actions:
-GET /buy
-verify that error 404 displayed
-POST /buy price=30&quantity=12
-verify that price = 30 and quantity =12 profile page ( / ) 
-HEAD /buy
-verify that error 404 displayed
-PUT /buy
-verify that error 404 displayed
-DELETE /buy
-verify that error 404 displayed
-CONNECT /buy
-verify that error 404 displayed
-OPTIONS /buy
-verify that error 404 displayed
-TRACE /buy
-verify that error 404 displayed
-PATCH /buy
-verify that error 404 displayed






##R8.6
## Of all http methods, make sure that only POST works on /sell

Mocking:
-none

Actions:
-GET /sell
-verify that error 404 displayed
-POST /sell price=30&quantity=12
-verify that price = 30 and quantity =12 profile page ( / ) 
-HEAD /sell
-verify that error 404 displayed
-PUT /sell
-verify that error 404 displayed
-DELETE /sell
-verify that error 404 displayed
-CONNECT /sell
-verify that error 404 displayed
-OPTIONS /sell
-verify that error 404 displayed
-TRACE /sell
-verify that error 404 displayed
-PATCH /sell
-verify that error 404 displayed



