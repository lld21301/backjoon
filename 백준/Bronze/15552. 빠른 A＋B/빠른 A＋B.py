import sys

def sys_add(T):
    for _ in range(T):
        a, b = map(int, sys.stdin.readline().split())
        print(a + b)


if __name__ == '__main__':
    T = int(sys.stdin.readline())

    sys_add(T)