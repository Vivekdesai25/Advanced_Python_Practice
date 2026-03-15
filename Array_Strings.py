# n="hi bharat"
# c=0
# for i in n:
#     c+=1

# print(c

# def toh(n,s,a,d):
#     if n==1:
#         print(f"move disk 1 from {s} to {d}")
#         return
#     toh(n-1,s,d,a)
#     print(f"move disk {n} form {s} to {d}")
#     toh(n-1,a,s,d)

#n=[1,2,0,-2,8,1,-2,6]
# n=[3,5,8,10]
# s=ss=float("inf")
# ll=l=float("-inf")
# for i in n:
#     if i<s:
#       ss=s
#       s=i
#     elif i<ss and i!=s:
#         ss=i
# print(ss)

# n=[1,2,0,4,5,0,3]
# k=[]
# for i in n:
#     if i!=0:
#         k.append(i)
# for i in n:
#     if i==0:
#         k.append(i)
# print(k)

# n=[1,3,4,5,6,2]
# m=[7,8,5,4,3,9,3,22]
# for i in n:
#     for j in m:
#         if i==j:
#             print(i)

# n="hahavivek" # non repeating charecter
# for i in n:
#     c=0
#     for j in n:
#         if i==j:
#             c+=1
#     if c==1:
#         print(i)

# Rotate array left by 1
# n=[1,2,3,4,5,6,7]
# k=[]
# for i in range (1,len(n)):
#     k.append(n[i])
# k.append(n[0])
# print(k)

# f=n[0]
# for i in range (len(n)-1):
#     n[i]=n[i+1]
# n[len(n)-1]=f
# print(n)

# sort half array only
# m=[5,4,7,6,55,3,44,2]
# n=len(m)//2

# ------- Selection sort -------
# for i in range(n):
#     for j in range(i+1,n):
#         if m[i]>m[j]:
#             m[i],m[j]=m[j],m[i]

# -------- Bubble sort ---------
# for i in range(n):
#     for j in range(n-i-1):
#         if m[j]>m[j+1]:
#             m[j],m[j+1]=m[j+1],m[j]          
# print(m)
