def cal_time(a, b, c):
    time = int(a)*60 + int(b)
    dtime = time + int(c) 
    h = dtime//60
    if h >= 24:
        h = h - 24
    m = dtime%60
    print(f'{h} {m}') 


if __name__ == '__main__':
    a, b = input().split()
    c = input()

    cal_time(a, b, c)