
# x=2
# y=1
# print(x%y>=x/y)

# x=0
# y=5
# x+=y
# y-=x
# Y=y+x
# print(2*x/y)

def maxTwo(a,b):
    if a>b:
        return a
    else:
        return b

def maxThree(a,b,c):
    return (maxTwo(maxTwo(a,b),c))

print(maxThree(1,3,1))



