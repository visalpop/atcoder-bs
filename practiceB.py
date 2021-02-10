#AtCoder Beginner's Selection Practice B

'''
s =input()
tokens = s.split()
a = int(tokens[0])
b = int(tokens[1])
'''
a,b = map(int, input().split())

if a*b%2 ==0:
    print('Even')
else:
    print('Odd')