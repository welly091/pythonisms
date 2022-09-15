# Lab 42 - Pythonisms
## Author: Yu-Wei Hsieh

## My findings:
I noticed that dunder methods are very useful and convenient. 
They allow a class to have multiple useful features like comparison, iteration, get length and so on.
Decorators are also useful too. 
It wraps methods and provides additional functions for those methods so that they can have extra functionality.

## Iterator.py
### Dunder methods:
- \_\_iter\_\_: customized the class to become an iterable object.
- \_\_len\_\_: return the length of specific part of data structure inside the class as default.
- \_\_eq\_\_: make the class comparable.
- \_\_getitem\_\_: customized the class for a user to get specific item they want.

## Decorators.py:
- @delay_questions : delay the wrapped function and give it the input value
- @time_spend: calculate the time spent for executing a function
- @alter_output: add more strings into the wrapped function

## Sources:
https://github.com/codefellows/seattle-code-python-401d19/tree/main/class-42