inp1 = 2000 
inp2 = 2013



# agar soni ohirgi ikkitasi 00 bilan tugamagan bolsa 
# u 4 ga bo'linadi va 100 ga bolinganda 0 teng bomasligi kerak 
# agar 00 bilan tugagan bo'sa u 400 ga bolinadi va 0 teng bolishi kerak 

def is_leap(year):
    leap = False
    if (year % 4 == 0 and  year % 100 != 0) or year % 400 == 0 :
        return True
    else: 
        return False


print(is_leap(inp1))
print(is_leap(inp2))


n = int(input())
collector = []
for i in range(n):
    collector.append(i+1)
res = ''.join(collector)