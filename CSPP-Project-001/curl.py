"""The python code helps to read the command line input for curl method."""

import sys
from lib.helper import curl
# line-3
# we are importing sys library using the import keyword, using this keyword we can import the required library 
# line-4
# In line-4 we are importing only required files uisng the from keyword. Using from keyword we are sying that from lib.helper
# we are importing curl
URL = None # Intalizing the a empty variable with null value and naming it as URL
ARG_CNT = len(sys.argv) - 1
# we are intalizing a variable ARG_CNT with a length function in which it calucaltes the length of the of the argument whihc we will be giving in the command line
#here the argument is url(for which we need to download the data)
'''
-- if condition !=1--
this if conditon checks weather thier is an url or not in gernreal terms

if the ARG_CNT is not equal to one then the condtion satisfies and program control flow enters the condition body and executes the print
statement. if the condition is not satisfied then it skips the print statement and goes to the other if statement
'''
if ARG_CNT != 1:
    print('Usage: curl [URL]...')
'''
--- if statement ==1---
if ARG_CNT==1 then program cotrol flow enters the if condition and saves the user specified URL in the "URL" variable and using another
if statement we are checking weather the URL is valid URL or not. if it is a invalid url then the if statemnt gets executed.
otherwise the printstatement gets executed. In the print statement we calling a curl function and passing a URL(in which we stored the user specified url) parameter 
'''
if ARG_CNT == 1:
    URL = sys.argv[1]
    if 'http' not in URL[:5]:
        URL = "http://"+URL
    print(curl(URL))
