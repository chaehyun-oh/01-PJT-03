import sys

sys.stdin = open("_신용카드만들기1.txt")


# testCase = [4,5,2,0,0,2,0,0,1,9,0,0,4,1,6]
# testCase = [4, 5, 2, 0, 0, 2, 0, 0, 1, 9, 0, 0, 4, 0, 6]


# total = 0

# for idx in range(1, len(testCase)+1):
#     if idx % 2 == 0:
#         total += testCase[idx-1]
#     else:
#         total += testCase[idx-1] * 2

# n = 10 - (total % 10)
# print(f'# {n}')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    nums = list(map(int, input().split()))
    total = 0

    for idx in range(1, len(nums)+1):
        if idx % 2 == 0:
            total += nums[idx-1]
        else:
            total += nums[idx-1] * 2

#인덱스 문제는 아님..

    if total == 0:
        n = 10
    else:
        n = 10 - int(total % 10)
        
    print(f'#{test_case} {n}')