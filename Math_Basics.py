# print("Hello DSA")

# --------Palindrome Number & Reverse a Number -----

# n=int(input("en text or no "))
# def p(x):
#     s=0
#     while x>0:
#         s=x%10 + s*10
#         x//=10 
#     return s
# print(p(n))
# print("t" if  p(n)==n else "f")

# def rev(n, r=0):
#     if n==0:
#         return r
#     else:
#         return rev(n//10, n%10 + r*10)
# print (rev(1241))

# false -- n<o or (n%10 == 0 and n!= 0)
# while n > rev :
#     .......
#     return n == rev or n == rev // 10


# def p(n):
#     div=1
#     while n//div >= 10:
#         div *= 10
#     while n>0:
#         f=n//div
#         l=n%10
#         if f!=l:
#             return False
#         n = (n%div) // 10

#         # //  → cuts right side
#         # %   → cuts left side

#         div //=100
#     return True
# print(p(123421))

# ------------------ Armstrong approaches  --------


# n = (input("en no "))
# p = len(str(n))
# a=sum(map(lambda x : int (x) ** p, n))
# print(a)

# for i in n:
#     s += int(i)**p
# print(s)

# def arm(d):
#     a=0
#     while(d>0):
#         a = pow(d%10,p)+(a)
#         d//=10
#     return a

# def rev(n, a):
#     if n == 0:
#         return 0
#     else:
#         return pow(n%10,p)+rev(n//10,p)
        
# ---- factorial ------

# def f(n):
#     if n==0:
#         return 1
#     else:
#         return (n)*f(n-1) 
# print(f(5))

# # n=5
# f=1
# for i in range(2,n+1):  #(n,1,-1):
#     f *= i
# print(f)

#=====Fibonacci Series--
def f(n):
    a,b=0,1 
    for i in range(n):
        if i==n-1:
            print(a)
        else:    
            print(a,end=",")
            a,b=b,a+b
f(6)

# def f(n,a=0,b=1):
#     if n==0:
#         return
#     print(a,end="," if n>1 else "")
#     f(n-1,b,a+b)
# f(6)

# j=6
# def f(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return f(n-1)+f(n-2)
  
# print(f(j))


#-----------Largest Element in an Array-----------
# n=list(map(lambda x:int(x),input(" en ").split()))

# # print (max(n),min(n))
# maxi = n[0] #float("inf")
# for i in range (len(n)):
#     if maxi > n[i]:
#         maxi = n[i]
# print(maxi)

n=[24, 10, 20 ,5, -6, 85,56]
# l=0
# r=len(n)-1
# def mm(l,r):
#     mid=(l+r)//2
#     if l==r:
#         return n[l]
#     else:
#         a=mm(l,mid)
#         b=mm(mid+1,r)
#     return a if a>b else b
# print(mm(l,r))

# def pp(n):
#     if len(n)==1:
#         return n[0]
#     a=[]
#     for i in range (0,len(n),2):
#         if i+1 >=  len(n):
#             a.append(n[i])
#         else:
#             if n[i]>n[i+1]:
#                 a.append(n[i])
#             else:
#                 a.append(n[i+1])
#     return pp(a)
# print(pp(n))
