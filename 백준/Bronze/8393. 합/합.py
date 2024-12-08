def sum(N):
    sum = 0
    for i in range(N):
        sum += i+1

    print(sum)

if __name__ == '__main__':
    N = int(input())

    sum(N)