def count(list, N):
  num_of_count = list.count(N)

  print(num_of_count)

if __name__ == '__main__':
  T = int(input())
  T_list = list(map(int, input().split()))
  N = int(input())

  count(T_list, N)
