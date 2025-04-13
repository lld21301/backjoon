def small_number(list, N):
  for i in list:
    if i < N:
      print(i, end=" ")

if __name__ == '__main__':
  L, N = map(int, input().split())
  T_list = list(map(int, input().split()))

  small_number(T_list, N)