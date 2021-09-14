"""Implementing the head shell command in python."""

import sys
from lib.helper import head, readfile
'''
line-3
we are importing sys library using the import keyword, using this keyword we can import the required library 
line-4
In line-4 we are importing only required files uisng the from keyword. Using from keyword we are sying that from lib.helper
we are importing head, readfile
'''
TEXT = None # Intalizing the TEXT valrable wiht null
ARG_CNT = len(sys.argv) - 1 
# we are intalizing a variable ARG_CNT with a length function in which it calucaltes the length of the of the argument whihc we will be giving in the command line
'''
--- if condition == 0---
if the ARG_CNT becomes 0 then program control flow enters the condition and executes the if condition body

---if condition body---
We are intalizing the TEXT varibale with the an input funnction using sys library. If above condition satisfies(==0)
then program control flow enters the body and start seeking the input from the user until you use the command control+z
'''
if ARG_CNT == 0:
    TEXT = sys.stdin.read()
'''
---If condition ==1---
If the ARG_CNT equals 1, then  program control flow enters the body and start executing the body.
in the body we are inatalizing a variable as filename and storing the filename for which we need to perofrom the head operation.
eg: python head abc [here abc is 1, so we are storing this file in filename]. 
in the next line we are using another variable TEXT. In TEXT we are storing a functioncall operation return value. 
'''
if ARG_CNT == 1:
    filename = sys.argv[1]
    TEXT = readfile(filename)
'''
if the ARG_CNT value is greater than 1 then it executes the print statement saying with the command name and displayes that message
eg: python head.py wc.py head.py "this conditon satifies the ARG_CNT>1 conditon then it displays written in print statement"

'''
if ARG_CNT > 1:
    print("Usage: head.py <file>")
'''
----print---
this print playes a key role, becaues it displays the overall output of the head command. In this print we are calling a function called head
with a TEXT parameter
'''
print(head(TEXT))
