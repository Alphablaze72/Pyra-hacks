
from tokenize import Number
from math import cos, factorial, sin, sqrt 


def main():
    userinput = input('what would you like to scalculate: Area(a) or sides(s): ')
    side1 = int(input('GIve thee first side:'))
    side2 = int(input('give the sec side:'))
    angle1 = int(input("give the angle between those sides: "))
    if userinput == ('s'):
        return sides(side1 , side2, angle1)
    elif userinput =='a':
        return area(side1 , side2, angle1)

def sides(side1, side2, angle1):
    side3= (side1**2)+ (side2**2) - 0.5*side1*side2*cos(angle1)
    print(sqrt(side3))
def area(side1 , side2, angle1):
    area = side1*side2*0.5*sin(angle1)
    print(area)
main()