
from tokenize import Number
from math import factorial
import flask
import time
collat = {}
def build(num):
    stepsdict = {}
    for number in range(num):
        steps = equation(number)
        stepsdict[str(number)]= str(steps)
f


def main():
    number = int(input("ENTER NUMBER:"))          
    collat = build(number)
    print(collat)
    
def equation(number):
    count = 0
    while True:
        if(number == 1):
            break
        elif (number%2==0):
            number = number/2
        else:
            number = (3*number)+1
        count += 1
    return count


build(3)

