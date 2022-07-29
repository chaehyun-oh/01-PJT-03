import sys

sys.stdin = open("_직사각형길이찾기.txt")

# a, b, c = 5, 5, 5

# if a == b:
#     print(c)
# elif a == c:
#     print(b)
# else:
#     print(a)

T = int(input())

for test_case in range(1, T + 1):
    a, b, c = map(int, input().split())

    if a == b:
        print(f'#{test_case} {c}')
    elif a == c:
        print(f'#{test_case} {b}')
    else:
        print(f'#{test_case} {a}')