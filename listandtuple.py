
# 1 List comprehension
x = int(input("num: "))
y = int(input("num: "))
z =int(input("num: "))
n =int(input("num: "))

check = [[ix,iy,iz] for ix in range(x+1) for iy in range(y+1) for iz in range(z+1) if ix+iy+iz != n ]


print(check)

# for i in range(x+1):
#     print(i,'x')
#     for j in range(y+1):
#         print(j,'y')
#         for k in range(z+1):
#             print(k,'z')
            

# [0,0,0],[]