# WebLogAnalysis
Performs data analysis on web logs

## Objective
To identify most visited pages of a website using web logs.

## Dependencies
1. Python
2. Pandas

## Dataset
A sample weblog file is taken in this example which has around 14k lines of access logs. It can be replaced with access logs of any of your 
website perferably in the same format as the one attached here.

## Method
The python script reads the log file and the log information is then matched against a pattern which is the standard format for Apache log files.
It gives the top visited pages for the sample log file. 
This script shows the importance of data cleaning and how it can be used efficiently to perform data analysis.

## Future Work
Web Analysis can be done not only to identify top visited pages but also understand the users’ behavior based on the sequences of the requests.
We can technically get location information from where the requests are referred or originated from. There are many other ways in which web analytics can be useful.

