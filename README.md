; These scripts were only tested with python 3.7

; ```africastalking``` package is required. It is only available on PyPI.

```
#Requires python3-pip installed
>pip install africastalking
```

# Task 1
Solved in a fairly straightforward manner with recursion over filenames and binary search on a sorted array of characters

#Usage

Run traversal.py from any directory you wish to investigate

```
>python traversal.py
```

# Task 2
Solved using flask. The USSD code works fairly simply. Could be made better if sessions behaved the way I expected them to. Needs flask and ngrok to function.

#Usage

# For pip users:
```
>pip install flask
```

# For conda users:

```
>conda install flask
```

#Simply run ussd.py and attach ngrok to the listening port
``` 
>python ussd.py
 #Default port for flask is localhost:5000
 #Could be run from wherever ngrok is
>./ngrok http 5000
 
```
#Current callback_url:
```
http://2426c52b.ngrok.io
as at 28.03.2019 21:22:00
USSD Channel: *384*741852# (Sandbox)
```
