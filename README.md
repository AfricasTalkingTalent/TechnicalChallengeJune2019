# TechnicalChallengeJune2019

A Simple USSD + SMS App that does user registration using AfricasTalking SDK.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

 * Git
 * Python 3.6.5
 * Virtualenv
 * ngrok live server


### Quick Start

A step by step series of examples that tell you how to get a development venv running

1. Git clone the repository

```
$ git clone https://github.com/Harrison-Gitau/TechnicalChallengeJune2019.git
```

2. Change directory to TechnicalChallengeJune2019

```
$ cd TechnicalChallengeJune2019
```

3. Initialize and activate a Virtualenv

```
$ virtualenv venv
$ source venv/bin/activate
```

4. Open the folder with your favourite text editor. For example: Sublime, Visual Code or Atom

```
$ subl .
$ code .
$ atom .
```

5. Install Project Dependencies

```
$ pip3 install -r requirements.txt
```

6. Start your ngrok live server
   Head over to where you have installed ngrok.

```
$ ./ngrok http 5000
```

7. Access ussd.py and sms.py files and run in your terminal

```
$ python3 ussd.py
```

## Deployment

Add additional notes about how to deploy this on a live system
To test the USSD, The moment your ngrok live server runs, copy the first likn and paste
it as your callback url. Ensure that your local development server is running too. Head over
to the Simulator and try it out.

## Built With

* Flask


## Authors

* **Harrison Gitau** - *Initial work* - [Harrison-Gitau](https://github.com/Harrison-Gitau)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to documentation at https://build.at-labs.io/discover
* Inspiration
