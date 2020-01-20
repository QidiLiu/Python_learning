import math

def phi(x):
    if abs(x) < math.pi/3:
        return abs(math.sin(x))
    else:
        return 0

if __name__ == "__main__":
    while(1):
        x = float(input('x=?'))
        print(f'phi(x) = {phi(x)}')
