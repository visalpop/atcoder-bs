#ABC087B Coins

a = int(input())
b = int(input())
c = int(input())
x = int(input())

num_combination = 0

for n_500 in range(0,a+1):          #num of 500yen coins
    for n_100 in range(0, b+1):     #num of 100yen coins
        for n_50 in range(0,c+1):   #num of 50yen coins
            if n_500*500+n_100*100+n_50*50 == x:
                num_combination += 1
print(num_combination)
