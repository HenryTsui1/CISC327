##Integration Testing Scenario - Postings

- Tester visits the webpage.
- The tester puts in the email = test@test.com
- The testers puts in the password = Test!!
- Pressing the login button
- On the homepage the tester would click sell-form
- On this page the user would input the values 5 for quantity, 'TestTest' for name, 10 for price, and 12122020 for expiration date.
- Can exit session after finishing, /logout

##Integration Testing Scenario - Purchasing

- User login
- If new user, direct to /register
- If login info does not exist in database, direct to /register
- Direct to '/' if user login is successful
- User can make transactions (/buy, /sell)
- Updates (/update) data when user buys or sells tickets
- Once user is done with transcation, they can logout (/logout) and exit the session
