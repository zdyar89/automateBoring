##chapter 7 from auto the boring stuff

import re

##regex objs exist as their own soft type
##with class functions and behaviors

##we give a reg obj behavior or a pattern wih compile

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
match = phoneNumRegex.search('My number is 865-963-5475')
print('Found phone number: ' + match.group())

##match object is returned if a pattern match is found
##this obj has a group function used to return a str result

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('my number is 415-222-3244')

mo.group(1) ##returns the first grouping with commas
mo.group(1) ##returns the second grouping with commas

mo.group(0) ##returns the entire match
mo.group() ## returns the entire match
mo.groups() ## returns all groups and separates with comma

##assign variables to the list items
areaCode, mainNum = mo.groups()
print("Area Code: " , areaCode, " Main: ", mainNum )

##using the pipe function
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())
##pipe function returns first match found
##in this case batman

##using parantheses to only match with a key phrase
batRegex = re.compile(r'Bat(man|mobile|copter|dad)')
mo = batRegex.search('Batmobile lost a wheel and Batdad got away from the Batcopter')
print(mo.group())
print(mo.group(1))
print(mo.groups())



