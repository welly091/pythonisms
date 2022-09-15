from functools import wraps
from time import sleep
from datetime import datetime

#################
### Decorators ##
#################

def delay_questions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        name = input("What is your name?")
        sleep(2)
        age = input("Age?")
        sleep(2)
        happy = input("Where you live?")
        return func([name, age, happy])
    return wrapper()

def time_spend(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        begin = datetime.now()
        f = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time spent for createData function is: " + str((end-begin).microseconds) + " ms")
        return f
    return wrapper()

def alter_output(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sentence = func(*args, **kwargs)
        return "Wow!!!" + sentence
    return wrapper()

#################
### Functions ###
#################

@delay_questions
def input_info(info=None):
    print("You are " + info[0] + " and your age is " + info[1] + " and you live in " + info[2])

@time_spend
def createData():
    n = [i for i in range(1000000)]

@alter_output
def cal():
    return "Today's is a sunny day!"


if __name__ == '__main__':
    input_info
    createData
    print(cal)