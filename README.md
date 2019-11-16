# jumpcloudrepository

This project is made with python and pytest-bdd to create the scenarios. In order to test the application, I just started to validate the services with postman and write some scenarios for each service, validationg the parameters, type of this parameters, kind of response (JSON, text) and type of request (GET and POST in this case).

The following sections shows the cases and the bugs that were found for each service:

Post to the /hash endpoint: For this endpoint, the target validations were addressed to check if the service response as expected for each request, sending string, alphanumeric (short and long ones), numeric and null entrances. Assumpsion for this endpoint-> it just accept alphanumeric values. Bugs:

The service accept null as a value, and generate a hash for an empty value.
The requirement describe this service should responds immediately, but it takes at least 5 second to response the job indicator
Get hash service: Validate that the service only accept numeric values as parameter, if it is numeric, the validation expect a 200 status code and a valid enconde response (SHA512 in Base 64). Contains two vlaidation for a short and long vlaue to encode. For me, this service is working as expected.

Get stats service: Validates if the service response 200 and a valid json body. Calculate the number of request and compare it with the response, also for the average time. And valdiate that the service only accept Get request. Bugs:

The average time is wrong, should be between 5 and 5.3 (maximum that you can modify) since the hash service take arround 5 second to generate the hash.
As a user, you can call POST and PUT request to generate a response.
Post shutdown: Validates if the service response 200

How to run it

Just use the command pytest

It also contains a report generator with allure, toy can generate it writing the following commands:

pytest --alluredir=/tmp/my_allure_results
allure serve /tmp/my_allure_results
