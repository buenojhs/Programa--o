#função filter()
#sintaxe:
# filter(função, sequência)

def numeros_pares(n):
    return n % 2 == 0
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13]

num_par = list(filter(numeros_pares, numeros))
print(num_par)


numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13]
num_impar = list(filter(lambda x: x%2 != 0, numeros))
print(num_impar)