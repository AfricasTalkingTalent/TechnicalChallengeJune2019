# Code Challenge for the June 2019 Cohort

Here's the challenge for anyone hoping to join the June to August Technical Internship Cohort at Africa's Talking. 

## This challenge is due at 0900hrs EAT on 29th March 2019

## Simple Unchanging Rules
The code challenge is and will always be judged using the following criteria:
  - A Correct fork, branch and pull request
  - Using the GitHub Pull Request Time Stamp and correct code quality & structure, we unfortunately won't be able to consider any code challenge that goes over the timeline stated above.
  - Code quality and structure will be evaluated by the team
  - Do not share any code that you cannot opensource on the Git Repository as its open source and Africa's Talking will not be liable for any breach of intellectual property (if any) once shared on the platform.
  - Complete both challenges below

## Terms and Conditions
You can participate on as many challenges as you wish:
  - Do not share any code that you cannot opensource on the Git Repository as its open source and Africa's Talking will not be liable for any breach of intellectual property (if any) once shared on the platform.
  - Code Challenges are time bound - the time restriction is specified on the challenge
  - Additional rules MAY be provided on the code challenge and will vary for each challenge
  - You are free to use your tools of choice as long as they fall under the rules of the challenge as below
  - Only successful interviewies will be contacted for the next round of interviews

## Code Challenge Bounty:
  - A chance to work with some of the most brilliant minds in the world!
  
## Task 1
##### Those structures though...
##### Play around with these structures, make sure the logic and the approach are tight.

With the assumption that you are using an object oriented programming language, write a program that given hundreds of documents, can find all documents with words containing the letter "a" in them.

## Tips
###### Map then reduce
###### Comment your code to show your thought process
###### You can submit this as a file in your pull request named "task 1"


## Task 2
##### Send and validate
##### Play around with some of our products.

Create a simple USSD + SMS app that does user registration.

User journey: person dials the USSD Code and gets prompted for a username and email address. After which they get an SMS response telling them they've registered successfully

## Resources: 
- AT SDKs: https://github.com/AfricasTalkingLtd
- Sandbox + Simulator: Which you access when you open your AT account
- AT docs: http://docs.africastalking.com/

## Tips
###### Include run and dependency instructions in your README.md file or push a runnable file
###### Comment your code to show your thought process
###### Make sure your project is runnable for this task

# Working on the Code Challenge
1.Fork the code challenge repository provided.

2.Make a topic branch. In your github form, keep the master branch clean. When you create a branch, it essentially will be a copy of the master.

>Pull all changes, make sure your repository is up to date

```sh
$ cd June_2019_Challenge
$ git pull origin master
```

>Create a new branch as follows-> git checkout -b [your name], e.g.

```sh
$ git checkout -b roina_ochieng master
```

>See all branches created

```sh
$ git branch
* roina_ochieng
  master
```

>Push the new branch to github

```sh
$ git push origin -u roina_ochieng
```

3.Make changes to the fork following the Code Challenge provided.

4.Commit the changes to your fork.

5.Make a pull request to the January_2019_UiUx_Challenge Repo.

## Get Support from Africa's Talking
In case you have any questions, reach out [the team](mailto:talent@africastalking.com) or the #internship_challenge Slack channel

## Submissions later than 0900hrs EAT on 29th March 2019 will not be considered

# Solution

## Task 1: Find documents containing the character "a"
In this challenge I am making the following assumptions:
* The program will be offline and all the doucments to be searched are in a single directory.
* The documents are plain text files. Binary documents (e.g with extension .docx) will be ignored.
* No processing is required a part from find documents with words containing the letter "a".

The approach I used was from the thinking that if the files can be read one at a time then there would be no need to create data structures that would unnecessarily use more memory by opening all the files at once and iterating through each.

The program requires the library [BinaryOrNont](https://binaryornot.readthedocs.io/en/latest/) installed.
To run execute:
```bash
python3 check_documents.py <doucuments path>
```
If the documents are in the same directory as the program file:
```bash
python3 check_documents.py
```

At the end the program will just list the files found containing the letter "a".

## Task 2: USSD + SMS APP
In this challenge I am assuming that the USSD does not have to be live. I used sandbox for USSD but SMS is live. Therefore, use your actual phone number on the emulator so you can receive the confirmation SMS on your phone.

The live callback URL is: `http://projects.shemkiptoo.com/at/api/ussdsession`
On the source code the actual logic can be found in the file `task2/app/Http/Controllers/USSDController.php`.

I used laravel framework for the challenge. To run the application:
1. Clone the project.
2. cd into the project root directory.
3. Rename `.env.example` file to `.env` inside your project root and fill the database information. 
4. Run `composer install`
5. Navigate to config/AfricastalkingGateway.php and fill in your username and api_key
6. Run `php artisan migrate`












