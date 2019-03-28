
## HOW TO RUN

## method 1 (online app)

The app is online - deployed on heroku. 
The callback url is: https://at-ussdapp.herokuapp.com/callback/
The registered ussd code is: \*384\*6854\#

Open the Africa's Talking phone simulator and call the ussd code *384*6854#



## method 2 (ofline app / running locally)
##### Goal
Set up the app locally and expose the callback uri `callback/` to the web and start accepting USSD POST data.
##### prerequisites:
1. python 3.4+
2. Ngrok



##### Set up a virtual environment:

>install pipenv tool

```sh
$ pip install pipenv
```

>create a virtual environment using python three

```sh
$ pipenv --three
```

>activate virtual environment

```sh
$ pipenv shell
```

>install app dependencies listed in the Pipfile

```sh
$ pipenv install
```

>Start django development server

```sh
$ python manage.py runserver
```

>start up a secure tunnel that is connected to your local HTTP port

```sh
$ ngrok http 8000
```


Now, a callback url can be accessed at `'host'/callback/`. 
Note: host value is the one ngrok will assign you.


# App Documentation

## The django app structure

There are two main folders;
1. `ussd_app` - the main application folder.
2. `ussd_project` - django project-wide settings

##### **callback/**
This is the callback url path. It is defined inside `ussd_project/urls.py`. The path maps to the `ussd_callback()` function described below.



The ussd_app/views.py file contains the application logic.
Inside the file, two functions are defined:
1. `ussd_callback()` : the callback url for the ussd application
2. `send_sms()` : a function that implements sending sms using the AT SMS service.


##### **1. ussd_callback(request)**

##### short description
This is the callback url defined inside ussd_app/views.py. It's mapped to the uri: 'callback/'

##### verbose description
The ussd_callback funtion takes a request as an argument. This is following the django convention for a function view.

First, The function is decorated with `@csrf_exempt` to exempt the view from CSRF protection. Failure to do this will result to any requests to this callback being denied as it won't contain the CSRF token. 

```
@csrf_exempt
def ussd_callback(request):
  ...    
```

We define global variables that we will use later to store the user data we obtain from the user input i.e `username` and `email.` 

``` 
global user_name
global email
```

From the POST data, we extract the user's phone number and store it in a variable. This will later be used to send the user an sms if registration is successfull.

``` 
phone_number = request.POST.get("phoneNumber", None)
```

The `text` parameter from the POST data is set to a text variable inside the function. This will be used to obtain user input and carry out tests that process the input.

``` 
text = request.POST.get("text", "default")
```

**Registration**
*The registration process relies upon checking for the astericks in the `text` variable value. To ensure there are no false positives, the user is prohibited from using the asterick '\*' when providing data.* 

Registration process is implemented as follows:
1. check first if it's the first session. An indicator for this is an empty string. If indeed it is the first session, the user is expected to `reply with '1'` to proceed with registration.

2. After starting the session, we start checking for the number of astericks in subsequent user reply inputs to tell what data to prompt the user to provide next.

3. On the last prompt, we extract user details i.e `username` and `email` which we store in the respective global variables we defined earlier. We then send a response to the user telling them that registration is done. The user is also notified that they should expect an SMS confirmation.

4. finally, we call the `send_sms` function which implements sending the success SMS.



##### **2. send_sms(phone_number)**

##### short description
Sends user an sms confirming that their registration was successful

##### verbose description
The function simply;

1. Initializes the AT sdk using the sandbox environment.
2. Uses the phone_number passed in as an argument to send and SMS. The phone number is obtained from the  user session by the callback function.











