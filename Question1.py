# method 1

ans = 0

for i in range(2, 100001, 2):
    ans = ans+i

print (ans)




#method 2

ans = 0

for i in range(100001):
    if i%2 == 0:
        ans += i

print (ans)


ans = 0

for i in range(1000):
    if i%3 == 0:
        ans += i
    elif i%5 == 0:
        ans += i

print (ans)

#question2
ans=0
a, b = 0, 1
for x in range(4000000):

 a, b = b, a + b
if i%2 == 0:
     ans += x

print (ans)




  
