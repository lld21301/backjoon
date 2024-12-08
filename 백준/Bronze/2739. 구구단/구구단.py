def multiplication_table(a):
    for i in range(1,10):
        print(f'{a} * {i} = {a*i}')

if __name__ == '__main__':
    a = int(input())

    multiplication_table(a)