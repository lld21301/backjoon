def reward(a, b, c):
    list = [int(a), int(b), int(c)]
    cnt = list.count(list[0])
    cnt2 = list.count(list[1])
    if cnt == 3:
        print(10000 + list[0]*1000)
    elif cnt == 2:
        print(1000 + list[0]*100)
    elif cnt2 == 2:
        print(1000 + list[1]*100)
    else:
        print(max(list)*100)

if __name__ == '__main__':
    a, b, c = input().split()

    reward(a, b, c)