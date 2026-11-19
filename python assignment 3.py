def is_right_triangle(a, b, c):
    
    sides = [a, b, c]
    sides.sort()
    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        return True
    else:
        return False


a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))


if a <= 0 or b <= 0 or c <= 0:
    print("Sides must be positive numbers.")
elif a + b <= c or b + c <= a or a + c <= b:
    print("These sides cannot form a triangle.")
elif is_right_triangle(a, b, c):
    print("It is a right-angled triangle.")
else:
    print("It is not a right-angled triangle.")
