#ABC081B shift only

'''
s=input()
token= s.split() # list of string
numbers = list(map(int, token))
'''

size = int(input())
numbers = list(map(int, input().split()))
num_div = 0
all_even = True

while all_even:
    for i in range(size):
        if numbers[i]%2 == 1:
            all_even = False
            break
        else:
            numbers[i]//=2
    if all_even:
        num_div +=1

print(num_div)