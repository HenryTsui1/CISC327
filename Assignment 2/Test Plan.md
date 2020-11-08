# Test Plan

## How test cases of different levels (frontend, backend units, integration) are organized.
The frontend, backend and integration test cases will all be independent of each other. The frontend will be tested by spoofing the backend and ensuring the correct actions are made and displayed to the user. 
The backend will be tested by entering different inputs and checking the database for successful entries. The integration combines the two and ensures that the frontend can accurately display information retrieved from the backend.
All test cases in each level will isolate specific functions from the code and test for appropriate success and failures.

## The order of the test cases (which level first which level second).
The order of the tests should reflect the manner in which a user would progress through the website.
•	First, the UI elements for /login and for /register must be checked. This includes verifying that all elements and fields exist, and that the buttons point to the webpages they're supposed to. 
•	The second part of the testing would be for /register. For this page, the values entered in the field must all be legal (following all the requirements of the assignment) and  when the button ‘Register’ is clicked, the entered values must be sent to the database for storage and future use. 
•	The next item to test is the database itself. Once values are sent from /register, we must verify that the new values have been properly recorded in the database and can be properly pulled for future uses. 
•	Once in the database, /login can be tested properly. The values in /login have to be properly sent to the frontend, and the frontend must make a request to the backend to check the user/pass combination. If the login succeeds, the user should be redirected to “ / ”, which is our homepage. 
•	After login confirmation, the profile page ("/") can be tested. The user should be able to see their specific balance/info on the page as well as all the available tickets, which requires more backend accesses. On the page the buy, sell and update fields should be visible, and their buttons should properly point to the correct functions to complete those forms. These functions are not yet developed, but will be later on in the assignment. 

## Techniques and tools used for testing.
We will be performing white box testing methods on our code to ensure that every function works correctly and indepently of one another. This will allow us to see exactly where any potential issues could be found in our code and help quickly pinpoint smaller errors. This kind of testing will require more resources and detail, but given the size of the project, we believe it is an appropriate choice. All tests for this project will be automated using python.

## Environemnts (all the local environment and the cloud environment) for the testing.
•	All tests will be run on windows devices
•	In addition to testing on windows, Github will also be used to test the project
•	Multiple browsers will be used for testing
•	All of the code will be written in HTML or python 3

## Responsibility (who is responsible for which test case, and in case of failure, who should you contact)
•	Billy Clarke will be responsible for testing R1
•	Sebastian Dobrowolski will be responsible for testing R2 and R3
•	Michael Kalpouzos will be responsible for R7
•	Henry Tsui will be responsible for R8

## Budget Management (you have limited CI action minutes, how to monitor, keep track and minimize unncessary cost)
To keep a low budget for this project, our testing plan must be organized and capable of efficiently using the available resources. 
To minimize the use of the limited CI action minutes, all jobs will be optimized and run selectively so that they are only tested when specific changes are made. Github will be ultilized to monitor and track all the changes.