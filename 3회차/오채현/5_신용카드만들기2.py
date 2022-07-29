# import sys

# sys.stdin = open("_신용카드만들기2.txt")

test_nums = '5388-9075-9509-8708'

test_nums = test_nums.replace('-', '')

if test_nums[0] in '34569':
    if len(test_nums) == 16:
        print(True)
    else:
        print(False)
else:
    print(False)

