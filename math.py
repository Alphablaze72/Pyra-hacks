
from tokenize import Number
from math import factorial


def main():
    userinput = input("facctoral, pascal triangle or ncr: ")
    if userinput == "factoral":
        Number = int(input("factorial of: "))
        ans = factoral(Number)
        print(ans)
        ans = str(ans)
        sum = 0
        for i in ans:
            sum += 1
        print(sum)

    elif userinput == "pascal":
        steps = int(input("Number of steps: "))
        pascal(steps)
    elif userinput == "ncr":
        N = int(input("N: "))
        R = int(input("R: "))
        ans = ncr(N,R)
        print(ans)



def pascal(n):
    for i in range(n+1):
        for b in range(n-i+1):
            print(end=" ")
        for j in range(i+1):
            print(ncr(i,j), end=" ")
        print()

def factoral(n):
    if n == 1:
        return 1
    return(n* factoral(n-1))

def ncr(a,b):
    return((factorial(a))//(factorial(b)*factorial(a-b)))
    

main()