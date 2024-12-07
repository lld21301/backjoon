def set_alarm(a, b):
    time = int(a)*60 + int(b)
    dtime = time - 45
    h = dtime//60
    if h < 0:
        h = 24 + h
    m = dtime%60
    print(f'{h} {m}') 


if __name__ == '__main__':
    a, b = input().split()

    set_alarm(a, b)