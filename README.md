# Code Challenge for the June 2019 Cohort

Here's the challenge for joining the June to August Technical Internship Cohort at Africa's Talking. 
## Prerequisites
The following are required in order for the application to run efficiently
>Python 3.6+

>Flask

>AfricasTalking

## Getting Started

1. Clone this repo
```sh
$ git clone https://github.com/felixrono/TechnicalChallengeJune2019/deployments
```
2. Check out the branch felix_rono
```sh
$ git checkout felix_rono
```
3. Set up a virtual environment and activate it
```sh
$ virtualenv venv
$ source venv/bin/activate
```
4. Install the necessary requirements
```sh
$(venv) pip install requirements.txt
```

## Task 1
##### Those structures though...
##### Play around with these structures, make sure the logic and the approach are tight.

With the assumption that you are using an object oriented programming language, write a program that given hundreds of documents, can find all documents with words containing the letter "a" in them.

## Usage
1. Put your documents in a folder
2. Run command specifying the path to the directory containing your documents

```sh
$ python task_1.py dir_to_files
```
3. Files containing words with the letter 'a' are displayed

## Task 2
##### Send and validate
##### Play around with some of our products.

Create a simple USSD + SMS app that does user registration.

User journey: person dials the USSD Code and gets prompted for a username and email address. After which they get an SMS response telling them they've registered successfully

1. Under sandbox in [AfricasTalking platform](https://account.africastalking.com/), launch a simulator
2. Create a service code under USSD
3. Use a unique number for your service.
4. There is a hosted version of task_2.py on [heroku](https://africastalking-tech-challenge.herokuapp.com/), add this as your callback url.
4. Enjoy yourself registering users using USSD

## Author
> Felix Rono 
