n = int(input("Zadaj n: "))
faktorial = 1
for i in range(n):
    faktorial = faktorial * (i+1)
# print(n, "!=", faktorial)
print(f"{n}! = {faktorial}") # {} napíšeme pravý pravý alt+b, pravý alt+n