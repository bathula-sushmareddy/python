r=int(input())
n=65
for i in range(1,r+1):
    for j in range(1,i+1):
        print(chr(n),"",end="")
        n+=1
    print("")
