# a = [1, 2, 3, 4, 5, 6]
# l = 0
# r = len(a) - 1
# # for _ in range(len(a) // 2):
# while l<=r:
#     a[l], a[r] = a[r], a[l]
#     l += 1
#     r -= 1
# print(a)

# # ============ shortest word ============
# s = "python is very powecvcvrful language !"
# w=""
# sw=""
# for i in s:
#     if i != " ":
#         w+=i
#     else:
#         if sw=="" or len(w)<len(sw):
#             sw=w
#         w=""
# print(sw if len(sw)<len(w) else w)

# # ============ longest word ============
# s = "python is very powerfull language !"
# w=""
# lw=""
# for i in s:
#     if i!=" ":
#         w+=i
#     else:
#         if len(w)>len(lw):
#             lw=w
#         w=""
# print(lw if len(lw)>len(w) else w)       

# # No of Words
# s = "python is easy to learn vivek.."
# c=1
# for i in s:
#     if i == " ":
#         c+=1
# print(c)

# arr = [1,2,3,2,4,5,3]
# a=[]
# for i in arr:
#     if i not in a:
#         a.append(i)
#     else:
#         print(i,end=" ")

# print(chr(ord("z")-32))

# # ----- count latters in the word -----
# s="vanilla"
# a=[]
# for i in s:
#     if i in a:
#         continue
#     c=1
#     for j in s:
#         if i==j :
#             a.append(j)
#             c+=1
#     print(i,c)


# # ----- count latters in the word -----
# s="vanilla"
# a=[]
# c=0
# for i in s:
#     if i in a:
#         continue
#     c=0
#     for j in s:
#         if i==j :
#             a.append(j)
#             c+=1
#     print(i,c)
# 

# # Toggle Case of String
# s = "PyThOn"
# r=""
# for i in s:
#     if "a"<= i <="z": # if i>="a" and i<="z":
#         r+=chr((ord(i)-32))
#     elif "A"<= i <= "Z":
#         r+=chr((ord(i)+32))
# print(r) 

# arr = [2,7,11,15]
# target = 9
# for i in arr:
#     for j in arr:
#         if i+j == target:
#             print(i,j)
#             break

# s = "learn python coding"
# result = ""
# ## print(s.replace(" ","_"))
# # for i in s:
# #     if i == " ":
# #         result+="_"
# #     else:
# #         result+=i
# # print(result)


# a = [1,2,3]
# b = [4,5,6]
# n=[]
# for i in a:
#     n.append(i)
# for i in b:
#     n.append(i)
# print(n)

# s1 = "python"
# s2 = "python1"
# flag=True
# if len(s1)!=len(s2):
#     flag=False
# for i in range (len(s1)):
#     if s1[i]!=s2[i]:
#         flag=False
#         break
# print("equal" if flag else "not equal")

# #------ ratate array by 2----
# a = [10,20,30,40,50,60]
# f=a[0]
# s=a[1]
# for i in range (len(a)-2):
#     a[i]=a[i+2]
# a[len(a)-1],a[len(a)-2]=s,f
# print(a)

# # --- non repeating charecters ----
# s = "aabbcddeez"
# r=""
# for i in s:
#     c=0
#     for j in s:
#         if i==j:
#             c+=1
#     if c==1:
#         print(i)
