from app import multiplo

soma=0
var1=int(input())
var2=int(input())

if (var2>var1):
    for n in range(var1,(var2+1)):
        if multiplo(n) == True:
            soma = soma + n

if (var1>var2):
    for n in range(var2,(var1+1)):
        if multiplo(n) == True:
            soma = soma + n

print(soma)