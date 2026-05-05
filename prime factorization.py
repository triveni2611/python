def karthikeya(a):
    if a==1:
       return 
    i=2
    while(a%i !=0):
        i=i+1
    print(i,end=" ")
    karthikeya(a/i)
a=int(input("enter any number:"))
karthikeya(a)
