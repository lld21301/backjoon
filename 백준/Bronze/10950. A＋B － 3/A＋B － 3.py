def add(T):
    add_list = []
    for _ in range(T):
        a, b = map(int, input().split())
        add_list.append(a+b)

    for i in add_list:
        print(i)

if __name__ == '__main__':
    T = int(input())

    add(T)