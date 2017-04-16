import math
def quadratic(a, b, c):

    if not isinstance(a, (int, float)):
        raise TypeError('Bad operand type(a)')
    if not isinstance(b, (int, float)):
        raise TypeError('Bad operand type(b)')
    if not isinstance(c, (int, float)):
        raise TypeError('Bad operand type(c)')

    if a == 0:
        if b == 0:
            print('c == 0')
        else:
            print('x = %.1f' % (-c / b))
    else:
        n = b ** 2 - (4 * a * c)
        if n >= 0:
            x1 = (-b + math.sqrt(n) / (2 * a))
            x2 = (-b - math.sqrt(n) / (2 * a))
            print('x1 is %.1f' % x1)
            print('x2 is %.1f' % x2)
        else:
            print('NO Answer!')

quadratic(89, 67, 9)