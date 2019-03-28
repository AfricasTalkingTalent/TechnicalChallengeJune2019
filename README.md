# Code Challenge for the June 2019 Cohort

This pull request contains the solution to both Task 1 and Task 2. 

## Task 1

Task one has been done using a python script found in python/task1.py

To run the file, copy it to any location on your PC, preferrably one with lots of text documents

 - Open terminal and change directory into the directory with the script
```
        cd /path/to /your/python/script
```
 - run the script using the command 
```
        python3 test1.py
```
- Thats it! You should see your results

You can edit the values of `self.search_term` and `self.file_type` to select search query and the type of document to be searched respectively. 

##### Have fun!
#
#
## Task 2

Task two has been implemented in a single php file for ease of deployment.

This script receives a USSD sandbox request and sends a confirmation SMS after confirmation of entry of the specified fields.

Africa's talking requires developers to register a callback url for all USSD requests. This can be found in the script between line 27 and 60.

The send SMS function is found in the script too. This and other functions are documented in the code.

#
To run the file, copy it to any location on your PC, preferrably one with lots of text documents

 - Create an account on cloud9.io
 - Select a php project to run your project.
 - Copy the contents of this repository there, most importantly,`composer.json` and `composer-lock.json` and `index.php`
 - Open the bash terminal and type `composer install`
 - Then `run` the project
 - Go to africastalking's sandbox and register your callback url to reference `index.php` https://account.africastalking.com/apps/sandbox/ussd/channel/create
 - Go to https://account.africastalking.com/apps/sandbox/settings/key and get an api key. 
 - Replace `YOUR_API_KEY` in index .php with your new API key.
 - Log into your sandbox application and after registering a phone number,dial the ussd code you had specified in the prevoious stel
 
##### Have fun!
