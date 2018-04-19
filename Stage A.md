# Feature - Arithmatic operation

* Programmer: Deokate Sayali
* Date: 04/18/2018

# Problem Definition

simple arimthatic opeartions can be done on given numbers. 

## User stories

As a user, I want to perform simple arithmatic opeartion on given integers like addition, subtraction, multiplication division and module. These opeartion commands can ve taken from user as argument parsing

# Design 

* API name: we define `argparse` RESTFul API
* Input: operation command
* Action: Arithmatic opeartion done.
* Output: result is shown on command line.

### Detailed design

* Import necessary APIs
* By argparse command take the operation command from user.
* Do arithmatic operation.
* Show the result.

# Test 

* By taking opeartion command from user and do correct opeartion. 

# limitation of tests

1. Not able to take numbers from users.

# User documentation

User can perform any operation on given numbers.