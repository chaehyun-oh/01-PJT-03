import sys

sys.stdin = open("_문자열의거울상.txt")

# test_word = 'bdppq'
T = int(input())

for t in range(T):
        
    word = input()
    reword = ''

    for i in range(len(word)):
        if word[i] == 'b':
            reword += 'd'
        elif word[i] == 'd':
            reword += 'b'
        elif word[i] == 'p':
            reword += 'q'
        elif word[i] == 'q':
            reword += 'p'

    print(f'#{t+1} {reword[::-1]}')

#런타임 에러...
