# Test Plan

## How test cases of different levels (frontend, backend units, integration) are organized.
The frontend, backend and integration test cases will all be independent of each other. The frontend will be tested by spoofing the backend and ensuring the correct actions are made and displayed to the user. The backend will be tested by entering different inputs and checking the database for successful entries. The integration combines the two and ensures that the frontend can accurately display information retrieved from the backend.
All test cases in each level will isolate specific functions from the code and test for appropriate success and failures.
## The order of the test cases (which level first which level second).

## Techniques and tools used for testing.
We will be performing white box testing methods on our code to ensure that every function works correctly indepently of one another. This will allow us to see exactly where any potential issues could be found in our code and help pinpoint smaller errors. This kind of testing will require more resources and detail. However, given the size of the project, we believe it is an appropriate choice. All tests will be automated using python.
## Environments (all the local environment and the cloud environment) for the testing.

## Responsibility (who is responsible for which test case, and in case of failure, who should you contact)

## Budget Management (you have limited CI action minutes, how to monitor, keep track and minimize unncessary cost)
To keep the costs low for this project, our testing plan must be organized to efficiently use the available resources. To minimize the use of the limited CI action minutes, all jobs will be optimized and run selectively so that they are only tested when specific changes are made. They will be monitored and tracked using git hub.
