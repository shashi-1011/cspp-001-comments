"""Implementing the wc shell command in python."""

import sys
from lib.helper import wc, readfile
# line-3
# we are importing sys library using the import keyword, using this keyword we can import the required library 
# line-4
# In line-4 we are importing only required files uisng the from keyword. Using from keyword we are sying that from lib.helper
# we are importing wc and readfile functions

TEXT = None # initalzing a variable with null value and naming it as TEXT
ARG_CNT = len(sys.argv) - 1 #storing the argument length in the ARG_CNT
'''
--- if condition == 0---
if the ARG_CNT becomes 0 then program control flow enters the condition and executes the if condition body

---if condition body---
We are intalizing TEXT varibale with the an input funnction using sys library. If above condition satisfies(==0)
then program control flow enters the body and start seeking the input from the user until you use the command control+z
'''
if ARG_CNT == 0:
    TEXT = sys.stdin.read()
'''
---If condition ==1---
If the ARG_CNT equals to 1, then program control flow enters the body and start executing the body.
in the body we are initalizing a variable as filename and storing the file given by user for which we need to perofrom the WC operation.
eg: python cat abc [here abc is 1, so we are storing this file in filename]. 
in the next line we are using another variable TEXT. In TEXT we are storing a functioncall operation return value. 
In this we are calling a function readfile and passing a argument as filename
'''
if ARG_CNT == 1:
    filename = sys.argv[1]
    TEXT = readfile(filename)
'''
we are creating a response variable and in that we are calling a function wc which has a argument TEXT which holds the readfile fucntion call return value
'''
response = wc(TEXT)
print(" " + str(response[0]) + "  " + str(response[1]) + " " + str(response[2]))
'''
all the strings are concatenated in the print
'''