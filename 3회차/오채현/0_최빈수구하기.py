
import sys

sys.stdin = open("_최빈수구하기.txt")

#최빈수 = 가장 자주 나온 값
# test_scores = [10, 8, 7, 2, 2, 4, 8, 8, 8, 9, 5, 5, 3]

T = int(input())

for t in range(T):
    case_num = int(input())
    scores = list(map(int, input().split()))
    cnt = {}

    for score in scores:
        score = str(score)
        cnt[score] = cnt.get(score, 0) + 1
    
    idx = max(cnt.values())

    for k, v in cnt.items():
        if v == idx:
            print(f'#{case_num} {k}')
