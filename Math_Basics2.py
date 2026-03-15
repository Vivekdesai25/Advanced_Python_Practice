# n=list(map(int, input("Enter No ").split()))
# print(n)

"""
s=0
for i in range (len(n)):
    # s+=n[i]
    s=sum(n[i],0)
print(s)
"""

# x=len(n)
# e,o=0,0
# for i in range (x):
#     if n[i]&1 == 0:
#         e+=1
#     else:
#         o+=1
# print(e,o)

"""
c=0
for i in range (len(n)):
    for j in range (len(n)):
        if n[i]==n[j]:
            c += 1
    print(n[i], ":", c)
"""

# x=int(input("Enter no to search "))
# for i in n:
#     if i==x:
#         c+=1
# print(c)

'''
c=0
for i in n:
    for j in n:
        if j==i:
            c+=1
    print(i,c)
    c=0
'''

# x=int(input("Enter no to search "))
# f=-1
# for i in n:
#     if i == x:
#         f=i
#         break
# print(f)

# x=[-1,2,4,0,3,-3,-4,-6,-7,0]
# z=p=n=0
# for  i in x:
#     if i == 0:
#         z+=1
#     elif i>0:
#         p+=1
#     else:
#         n+=1
# print(n, z, p)

# n=[1,2,3,4,2,4,2,4,5,6,6,6,7,7]
# a=[]
# for i in n:
#     if i in a:
#         pass
#     else:
#         a.append(i)
# print(a)

# n=11
# s=0
# for i in range (1,n):
#     if n%i == 0:
#         s +=i
# print(True if n == s else False)

# x=18
# y=180
# s = x if x<y else y
# i=1
# while i<s:
#     if x%i==0 and y%i==0:
#         k=i
#     i+=1
# print(k)

# x=10
# y=18
# m=max(x,y)
# while 1:
#     if m%x==0 and m%y==0:
#         print(m)
#         break
#     m+=1

# def gcd(x,y):
#     if y==0:
#         return x
#     else:
#         return gcd(y,x%y)
# print(gcd(12,15))

# n=list(map(int,input("Enter No ").split()))
# print(n)
# n=[0, -9, -33, 85, 47, 6, 888,888, 21, 4, 10, -3, -455,20, -300, 222]
# ss=s=float("inf")
# ll=l=float("-inf")
# for i in n:
#     if i<s:
#         s=ss
#         ss=i 
#     if i>l:
#         ll=l
#         l=i      
# print(s,ss)
# print(l,ll)

"""
n=[4,1,2,3,4,5,6]
f=True
for i in range (len(n)-1):
    if n[i]>n[i+1]:
        flag=False
        break
print(f)
"""

# a=[1,3,4,5]
# n=5
# for i in range(1,n+1):
#     f=False
#     for j in a:
#         if i==j:
#             f=True
#             break
#     if f==False:
#         print(i)


# a=[2,1,3,5,6]
# n=6
# t=s=0
# for i in range(1,n+1):
#     t+=i
#     if i in a:
#         s+=i
# # for j in a:
# #     s+=j
# print(t-s)

# m="Hi Python !"
# r=""
# for i in m:
#     if i != " ":
#         r+=i
# print(r) 

# n=24
# for i in range (1,n):
#     if n%i == 0:
#         print(i,end=" ")

# a="raju"
# b="raij"
# if len(a)!=len(b):
#     print("not anagram")
# else:
#     anaa = True
#     for i in a:
#         if a.count(i)!= b.count(i):
#             anaa = False
#             break
#     if anaa:
#         print("anagram")
#     else:
#         print("not anagram")

# n=2025 
# if (n%4==0 and n%100!=0) or n%400==0:
#     print("leaf year")
# else:
#     print("Not leap year")

# n=[1,2,3,2,1,4,5]
# for i in range(0,len(n)):
#     for j in range(i+1,len(n)):
#         if n[i]==n[j]:
#             print(n[i])

# n=40585 # strong number ( 1! + 4! + 5! = 145 )
# # def f(n):
# #     if n==0:
# #         return 1
# #     else:
# #         return n*f(n-1)
# t=0
# x=n
# while n>0:
#     r=n%10
#     # a=f(r)
#     a=1
#     for i in range(1,r+1):
#         a*=i
#     t+=a
#     n//=10
# print(True if t==x else False)