# Task 1
Solved fairly easily with recursion over filenames and binary search on a sorted array of characters

#Usage
Run traversal.py from any directory you wish to investigate

```
>python traversal.py
```

# Task 2
Solved using flask. The USSD code works fairly simply. Could be made better if sessions behaved the way I expected them to. Needs flask and ngrok to function.

#Usage
#For conda users:

```
>conda install flask
```

#For pip users:
```
>pip install flask
```

#Simply run ussd.py and attach ngrok to the listening port
```
>python ussd.py
#Default port for ngrok is localhost:5000
>./ngrok http 5000
#Could be run from wherever ngrok is
```
#Current callback_url:
```
http://2426c52b.ngrok.io
as at 28.03.2019 21:22:00
```
