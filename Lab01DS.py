#Rebecca Menda
#Lab01


#Part A FizzBuzz
for i in range(1,11):
    if i%15==0:
        print("FizzBuzz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0:
        print("Fizz")
    else:
        print(i)



#Part C Apples
prices=[14,6,9,7,8,10,3,9]

x=len(prices)
profits=[]

for i in range(x-1):
    profit=prices[i+1]-prices[i]
    profits.append(profit)

profits.sort()
y=len(profits)
print("The greatest possible profit is $",profits[y-1],".")



#Readings
text=open("FallingUp.txt","r")
line=1
for i in text.readlines():
    print(line,i)
    line=line+1
