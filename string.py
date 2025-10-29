
# abracadabra mutate string find index 5 change character

# task 1
string = 'abracadabra'
# mutate string
string = string[:4] + "k" + string[5:]
print(string)

# task 2
string = input("string:")
sub_string = input("sub_string:")

total = 0
for i in range(len(string)):
    if (string[i:len(string)].startswith(sub_string)):
        total += 1
print(total)

# task 3 if in the word any alpha,digit,lower,upper,alpha
s = input(":") # qA2
print(any(i.isalnum() for i in s))
print(any(i.isalpha() for i in s))
print(any(i.isdigit() for i in s))
print(any(i.islower() for i in s))
print(any(i.isupper() for i in s))

# output:
# True
# True
# True
# True
# True

# task 4 text wrap
import textwrap
text = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
width = 3
wrap = textwrap.wrap(text, width) # wrap function listga bolib beradi
wrapfill = textwrap.fill(text, 10) # qator tashab bolib beradi
print(wrap)
print(wrapfill)

# task 5 capitalize

cap = "hello world"
words = cap.split(" ")
res = [i.capitalize() for i in words]

print(" ".join(res))

# print(cap.title())\

# task 6 
string = "BANANA"

vowels = 'AEIOU'
kevin_score = 0
stuart_score = 0
n = len(string)

for i in range(n):
    if string[i] in vowels:
        print(n,i)
        kevin_score += n - i

    else:
        print(n,i)
        stuart_score += n - i