def check_quadrant(a, b):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y >0:
        return 2
    elif x < 0 and y <0:
        return 3
    else:
        return 4
        
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    
    print(check_quadrant(x, y))