
# 1. Extend the rectangular_basic.py from above to print both the area and the circumference of
# the rectangle.

def main():    
    width = 23
    height = 17
    area = width * height
    circumference = 2 * (width + height)
    print(f'area: {area}') # 391
    print(f'circumference: {circumference}') #80
main()


# 2. Write a script that has a variable holding the radius of a circle and prints out the area of the
# circle and the circumference of the circle.
import math

def main():
    radius = 7
    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius
    print('area: %.2f' % area) # 153.94
    print('circumference: %.2f' % circumference) # 43.98
main()

# 3. Write a script that has two numbers a and b and prints out the results of a+b, a-b, a*b, a/b
def main():
    a = 20
    b = 5
    
    print(a+b) #25
    print(a-b) #15
    print(a*b) #100
    print(a/b) #4.0
main()

# 4. Write a script that will ask for the sides of a rectangular and print out the area.
# Provide error messages if either of the sides is negative.
def main():
    a = int(input('side a:'))
    b = int(input('side b:'))
    
    if a <= 0 or b <= 0:
        print('please enter positive number')
        return
            
    area = a * b
    print('area: %.2f' % area)

main()

# 5. Create a script that accepts 2 numbers and an operator (+, -, *, /), and prints the result of the
# operation.
def main():
    a = int(input('Enter first number : '))
    b = int(input('Enter second number : '))
    operator = input('Enter Operator +,-,/,* :')
    
    if operator=='+':
        res = a+b
    elif operator == '-':
        res = a-b
    elif operator == '*':
        res = a*b
    elif operator == '/':
        res = a/b
    else:
        return print('Invalid Choice')
    return res
main()

# 6. Create a script to calculate area of rectangle that will accept the arguments 
# on the command line like this: python rect.py 2 4

import sys
def main():
    if len(sys.argv) != 3:
        print('need 2 arguments - length and width')
    
    width = int(sys.argv[1])
    length = int(sys.argv[2])
    
    if width <= 0 or length <=0:
        print('Enter positive value')
    area = length * width
    print(area)
main()