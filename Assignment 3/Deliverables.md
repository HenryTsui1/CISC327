# Assignment 3

## Template
The template for testing was changed slightly to keep things in line with the requirements laid out in the project description. There are 5 test case files that test the requirement R1, R2, R3, R7 and R8. As these are mainly front end tests, an additional test case was made to ensure the backend was functioning properly.

## Failure Report
| Testcase   number | What is being tested                                                                                                                                      | Why it failed                                                                                                                                                                                                                                             | How you fixed it                                                                                                                                                                                                                              |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  R2.4             | The registration form can be submitted as a POST request to  the current URL (/register)                                                                  | Register Button did not have any id in html, so we couldn’t  reference it                                                                                                                                                                                 | Added an 'id' for the register button                                                                                                                                                                                                         |
| R2.5.1            | Email, password, password2 all have to satisfy the same  required as defined in R1 - Positive                                                             | Test failed because the current email used to register a new  used (2.5.1) was the same as the user made in the previous test  (2.4). This threw the "user email been ALREADY used" error.                                                                | Changed all emails for consecutive test functions in the file.                                                                                                                                                                                |
| R2.5.1            | Email, password, password2 all have to satisfy the same  required as defined in R1 - Positive                                                             | Test failed again during second execution of pytest. This is because the  'db.sqlite' was storing logged in users, meaning two consecutive pytest's  would fail, since all the users already exist.                                                       | Testing twice in a row causes issues, but deleting the  'db.sqlite' before each new pytest solved this issue                                                                                                                                  |
| R2.7.2            |  User name has to be   non-empty, alphanumeric-only, and space  allowed only if it is not the first   or the last character. -  Negative (empty username) | This failed because the library implemented in the CISC327  course for this project does not allow the user to make a  submission if a   field is empty. This stopped "Name format  error" from appearing because testing never left the /register page.  | This was solved by checking for the negative of a condition,  instead of the positive. The condition was "Log In" text is not  visible after clicking the register button, and that the text for all the  other errors was also not visible.  |
| R2.11             | If no error regarding the inputs following the rules above,  create a new user, set the balance to 5000, and go back to the  /login page                  | This failed because the backend file 'models.py' was missing a  balance attribute for the object "User". This did not allow us to  assign a balance to each user.                                                                                         | 'models.py' was edited   and a "balance" column was added to the User object.                                                                                                                                                                 |
| R2.11             | If no error regarding the inputs following the rules above,  create a new user, set the balance to 5000, and go back to the  /login page                  | This failed because again because the mock user at the beginning of the  file had no balance initialized for them.                                                                                                                                        | A balance of 5000 was initialized for the mock user at the beginning of the file.                                                                                                                                                             |
| R3.9 - 11         | Testing if the forms on '/' can be posted to '/sell', '/buy'  and '/update' respectively                                                                  | Code for the POST methods of '/sell', '/buy' and '/update' has not been  written yet.                                                                                                                                                                     | Post methods were made in forntend.py to navigate to temporary  pages used as a placeholder for '/sell', '/buy' and '/update'.                                                                                                                |
| R7.1.2            | After logout, the user shouldn't be able to access restricted  pages                                                                                      | Test code was looking for restricted pages that did not exist yet.                                                                                                                                                                                        | Tested the authentication of '/' and made sure it redirected  to '/login' instead.                                                                                                                                                            |

## Backend Test
The backend test uses the black-box technique for testing in three steps. Step 1: Create a new user, and give them a balance of 5000.  This is all recorded in the database.
Step 2:Login as the newly created user. Step 3: Verify that the profile page displays 5000 as the current user balance.
The html page pulls its information to populate name and balance based on that user's login info, so the database must have 5000 entered for that specific user. 