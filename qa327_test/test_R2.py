# import pytest
# from seleniumbase import BaseCase

# from qa327_test.conftest import base_url
# from unittest.mock import patch
# from qa327.models import db, User
# from werkzeug.security import generate_password_hash, check_password_hash

# # Moch a sample user
# test_user = User(
#     email='test@test.com',
#     name='test_user',
#     password=generate_password_hash('Test!!'),
#     balance=5000
# )



# class R2Test(BaseCase):
#     # R2.1 If the user has logged in, redirect back to the user profile page
#     @patch('qa327.backend.get_user', return_value=test_user)
#     def test_R2_1(self, *_):
#         self.open(base_url + '/logout')
#         self.open(base_url + '/login')
#         self.type("#email", "test1@test.com")
#         self.type("#password", "Test!!")  
#         self.click('input[type="submit"]')
#         self.open(base_url + '/register')
#         self.assert_element("#welcome-header")
#         self.assert_text("Hi", "#welcome-header") 



#     # Test Case R2.2 otherwise, show the user registration page
#     def test_R2_2(self, *_):
#         self.open(base_url + '/logout')
#         self.open(base_url + '/register')
#         self.assert_element("#btn-register")
      

    
#     # R2.3 the registration page shows a registration form requesting: email, user name, password, password2
#     def test_R2_3(self, *_):
#         self.open(base_url + '/logout')
#         self.open(base_url + '/register')
#         self.assert_element("#email")
#         self.assert_element("#name")
#         self.assert_element("#password")
#         self.assert_element("#password2")



# # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#     # # R2.4 The registration form can be submitted as a POST request to the current URL (/register)
#     def test_R2_4(self, *_):
#         self.open(base_url + '/logout')
#         self.open(base_url + '/register')
#         self.type("#email", "test2@test.com")
#         self.type("#name", "test_user")
#         self.type("#password", "Test!!")
#         self.type("#password2", "Test!!")
#         self.assert_element("#btn-register") 
#         self.click('input[id="btn-register"]')

# # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        
    

#     # R2.5.1 Email, password, password2 all have to satisfy the same required as defined in R1 - Positive
#     def test_R2_5_1(self, *_):
#         self.open(base_url + '/logout')
#         self.open(base_url + '/register')
#         self.type("#email", "test3@test.com")
#         self.type("#name", "test_user")
#         self.type("#password", "Test!!")
#         self.type("#password2", "Test!!")
#         self.assert_element("#btn-register") 
#         self.click('input[id="btn-register"]')


#     #R2.5.2 Email, password, password2 all have to satisfy the same required as defined in R1 - Negative (email doesn't satisfy)
#     def test_R2_5_2(self, *_):
#         self.open(base_url + '/logout')
#         self.open(base_url + '/register')
#         self.type("#email", "test")
#         self.type("#name", "test_user")
#         self.type("#password", "Test!!")
#         self.type("#password2", "Test!!")
#         self.assert_element("#btn-register") 
#         self.click('input[id="btn-register"]')
#         self.assert_text("Email format error", "#message") 


#     # R2.5.3 Email, password, password2 all have to satisfy the same required as defined in R1 - Negative (username doesn't satisfy)   
#     def test_R2_5_3(self, *_):
#         self.open(base_url + '/logout')
#         self.open(base_url + '/register')
#         self.type("#email", "test4@test.com")
#         self.type("#name", "12")
#         self.type("#password", "Test!!")
#         self.type("#password2", "Test!!")
#         self.assert_element("#btn-register") 
#         self.click('input[id="btn-register"]')
#         self.assert_text("Name format error", "#message") 







#     # # R2.5.4 Email, password, password2 all have to satisfy the same required as defined in R1 - Negative (password doesn't satisfy)
#     def test_R2_5_4(self, *_):
#         self.open(base_url + '/logout')
#         self.open(base_url + '/register')
#         self.type("#email", "test5@test.com")
#         self.type("#name", "test")
#         self.type("#password", "asdf")
#         self.type("#password2", "asdf")
#         self.assert_element("#btn-register") 
#         self.click('input[id="btn-register"]')
#         self.assert_text("Password not strong enough", "#message") 

# # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# # SKIPPED 2.5.5 - Verifying if password2 matches complexity requirements

# # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    
#     # Testcase R2.6.1 - Password and password2 have to be exactly the same - Positive
#     def test_R2_6_1(self, *_):
#         self.open(base_url + '/logout')
#         self.open(base_url + '/register')
#         self.type("#email", "test6@test.com")
#         self.type("#name", "test")
#         self.type("#password", "Test!!")
#         self.type("#password2", "Test!!")
#         self.assert_element("#btn-register") 
#         self.click('input[id="btn-register"]')
#         self.assert_text("Please Login", "#message") 


# # Testcase R2.6.2 - Password and password2 have to be exactly the same - Negative
#     def test_R2_6_2(self, *_):
#         self.open(base_url + '/logout')
#         self.open(base_url + '/register')
#         self.type("#email", "test7@test.com")
#         self.type("#name", "test")
#         self.type("#password", "wrongPass")
#         self.type("#password2", "Test!!")
#         self.assert_element("#btn-register") 
#         self.click('input[id="btn-register"]')
#         self.assert_text("The passwords do not match", "#message") 




# # Testcase R2.7.1 - ser name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character. - Positive
#     def test_R2_7_1(self, *_):
#         self.open(base_url + '/logout')
#         self.open(base_url + '/register')
#         self.type("#email", "test8@test.com")
#         self.type("#name", "test")
#         self.type("#password", "Test!!")
#         self.type("#password2", "Test!!")
#         self.assert_element("#btn-register") 
#         self.click('input[id="btn-register"]')
#         self.assert_text("Please Login", "#message") #this is a success



# # Test case R2.7.2 - User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character. - Negative (empty username)
# # The library implemented in this program does not allow user to make a submission while one of 
# # the fields is empty 

#     def test_R2_7_2(self, *_):
#         self.open(base_url + '/logout')
#         self.open(base_url + '/register')
#         self.type("#email", "test8@test.com")
#         self.type("#name", "")
#         self.type("#password", "Test!!")
#         self.type("#password2", "Test!!")
#         self.assert_element("#btn-register") 
#         self.click('input[id="btn-register"]')
#         self.assert_element_absent("#login-header")




# # Test case R2.7.3 - User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character. - Negative (not only alphanumeric username)
#     def test_R2_7_3(self, *_):
#         self.open(base_url + '/logout')
#         self.open(base_url + '/register')
#         self.type("#email", "test9@test.com")
#         self.type("#name", "test!@#$@")
#         self.type("#password", "Test!!")
#         self.type("#password2", "Test!!")
#         self.assert_element("#btn-register") 
#         self.click('input[id="btn-register"]')
#         self.assert_text("Name format error", "#message") #this is a success, since this is only visible on login




# # Test case R2.7.4 - User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character. - Negative (space in front of username)
#     def test_R2_7_4(self, *_):
#         self.open(base_url + '/logout')
#         self.open(base_url + '/register')
#         self.type("#email", "test10@test.com")
#         self.type("#name", " frontSpace")
#         self.type("#password", "Test!!")
#         self.type("#password2", "Test!!")
#         self.assert_element("#btn-register") 
#         self.click('input[id="btn-register"]')
#         self.assert_text("Name format error", "#message")

# # Test case R2.7.5 - User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character. - Negative (space behind the username)
#     def test_R2_7_5(self, *_):
#         self.open(base_url + '/logout')
#         self.open(base_url + '/register')
#         self.type("#email", "test11@test.com")
#         self.type("#name", "endSpace ")
#         self.type("#password", "Test!!")
#         self.type("#password2", "Test!!")
#         self.assert_element("#btn-register") 
#         self.click('input[id="btn-register"]')
#         self.assert_text("Name format error", "#message")


# # Test case R2.8.1 - User name has to be longer than 2 characters and less than 20 characters. - Positive
#     def test_R2_8_1(self, *_):
#         self.open(base_url + '/logout')
#         self.open(base_url + '/register')
#         self.type("#email", "test12@test.com")
#         self.type("#name", "testUser")
#         self.type("#password", "Test!!")
#         self.type("#password2", "Test!!")
#         self.assert_element("#btn-register") 
#         self.click('input[id="btn-register"]')
#         self.assert_text("Please Login", "#message") #this is a success


# # Test case R2.8.2 - User name has to be longer than 2 characters and less than 20 characters. - Negative (less than 2 characters)
#     def test_R2_8_2(self, *_):
#         self.open(base_url + '/logout')
#         self.open(base_url + '/register')
#         self.type("#email", "test13@test.com")
#         self.type("#name", "a")
#         self.type("#password", "Test!!")
#         self.type("#password2", "Test!!")
#         self.assert_element("#btn-register") 
#         self.click('input[id="btn-register"]')
#         self.assert_text("Name format error", "#message")





# #Test case R2.8.3 - User name has to be longer than 2 characters and less than 20 characters. - Negative (more than 20 characters)
#     def test_R2_8_3(self, *_):
#         self.open(base_url + '/logout')
#         self.open(base_url + '/register')
#         self.type("#email", "test14@test.com")
#         self.type("#name", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
#         self.type("#password", "Test!!")
#         self.type("#password2", "Test!!")
#         self.assert_element("#btn-register") 
#         self.click('input[id="btn-register"]')
#         self.assert_text("Name format error", "#message")


# # Test case R2.9 - For any formatting errors, redirect back to /login and show message '{} format is incorrect.'.format(the_corresponding_attribute)

#     def test_R2_9(self, *_):
#        #email
#         self.open(base_url + '/logout')
#         self.open(base_url + '/register')
#         self.type("#email", "test15")
#         self.type("#name", "testing")
#         self.type("#password", "Test!!")
#         self.type("#password2", "Test!!")
#         self.assert_element("#btn-register") 
#         self.click('input[id="btn-register"]')
#         self.assert_text("Email format error", "#message") 

#     #name
#         self.open(base_url + '/logout')
#         self.open(base_url + '/register')
#         self.type("#email", "test16@test.com")
#         self.type("#name", "a")
#         self.type("#password", "Test!!")
#         self.type("#password2", "Test!!")
#         self.assert_element("#btn-register") 
#         self.click('input[id="btn-register"]')
#         self.assert_text("Name format error", "#message")

#     #password
#         self.open(base_url + '/logout')
#         self.open(base_url + '/register')
#         self.type("#email", "test17@test.com")
#         self.type("#name", "testUser")
#         self.type("#password", "asdasd")
#         self.type("#password2", "asdasd")
#         self.assert_element("#btn-register") 
#         self.click('input[id="btn-register"]')
#         self.assert_text("Password not strong enough", "#message") 



# # Test case R2.10 - If the email already exists, show message 'this email has been ALREADY used'
#     # @patch('qa327.backend.get_user', return_value=test_user)
#     def test_R2_10(self, *_):
#         self.open(base_url + '/logout')
#         self.open(base_url + '/register')
#         self.type("#email", "test999@test.com")
#         self.type("#name", "testing")
#         self.type("#password", "Test!!")
#         self.type("#password2", "Test!!")
#         self.assert_element("#btn-register") 
#         self.click('input[id="btn-register"]')

#         self.open(base_url + '/logout')
#         self.open(base_url + '/register')
#         self.type("#email", "test999@test.com")
#         self.type("#name", "testing")
#         self.type("#password", "Test!!")
#         self.type("#password2", "Test!!")
#         self.assert_element("#btn-register") 
#         self.click('input[id="btn-register"]')
#         self.assert_text("This email has been ALREADY used.", "#message") 



# # Test case R2.11 - If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page
    
#     def test_R2_11(self, *_):
#         #register
#         self.open(base_url + '/logout')
#         self.open(base_url + '/register')
#         self.type("#email", "test30@test.com")
#         self.type("#name", "testing")
#         self.type("#password", "Test!!")
#         self.type("#password2", "Test!!")
#         self.assert_element("#btn-register") 
#         self.click('input[id="btn-register"]')
#         #login
#         self.open(base_url + '/login')
#         self.type("#email", "test30@test.com")
#         self.type("#password", "Test!!")  
#         self.click('input[type="submit"]')
#         #profile
#         self.assert_element("#balance-elem") 
#         self.assert_text("Balance: 5000", "#balance-elem") 
