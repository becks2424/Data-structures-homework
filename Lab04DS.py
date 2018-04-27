#Lab04

import time
n=int(input("Please enter the number you would like to calculate: "))

######Without Recursion#####
start=time.clock()
x=y=1
if b<2:
    print("1")
else:
    for i in range(b-1):
        fib=x+y
        x=y
        y=fib
    print(x)
end=time.clock()
wor=end-start       
print(wor, "seconds without recursion.")

#######With Recursion#######
def fibrecursion(b):
    if b<2:
        return(1)
    else:
        return fibrecursion(b-1)+fibrecursion(b-2)
    
start2=time.clock()
print(fibrecursion(b-1))
end2=time.clock()
wr=end2-start2      #wr-with recursion
print(wr, "seconds with recursion.")

######Dynamic Programming######
key=[1,1]
for i in range(b):
    key.append(0)
def fibdynamic(b):
    if key[b]==0:
        key[b]=fibdynamic(b-1)+fibdynamic(b-2)
    return key[b]

start3=time.clock()
print(fibdynamic(b-1))
end3=time.clock()
wdp=end3-start3     
print(wdp, "seconds with dynamic programming.")



if wor<wr and wor<wdp:
    print('Without recursion is fastest.')
if wr<wor and wr<wdp:
    print('Recursion is fastest.')
else:
    print("Dynamic programming is fastest.")
