def maxmin(lista):
     return max(lista,min(lista)) # tupla 2 ele

l = [1,3,5,6,8]
# desempaqueta la tupla en 2 variables
maximo, minimo = maxmin(l)

print(maximo, minimo, sep=' ')

 