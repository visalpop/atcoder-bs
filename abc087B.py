#ABC087B Coins

a = int(input())
b = int(input())
c = int(input())
x = int(input())

num_combination = 0

for n_500 in range(0,a+1):          #num of 500yen coins
    for n_100 in range(0, b+1):
        n_50 = (x - n_500*500 - n_100*100)//50
        if n_50<=c and n_50>=0:
            num_combination += 1
print(num_combination)
