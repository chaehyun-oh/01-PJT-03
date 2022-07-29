import sys

sys.stdin = open("_소득불균형.txt")

# testnum = 7
# test = [15, 15, 15, 15, 15, 15, 15]
T = int(input())

for t in range(T):
    n = int(input())
    incomes = list(map(int, input().split()))

    # total = sum(incomes)
    total = 0

    avrg = int(total // n)
    cnt = 0
    for i in incomes:
        if i <= avrg:
            cnt += 1

    print(f'#{t+1} {cnt}')

#런타임 에러...