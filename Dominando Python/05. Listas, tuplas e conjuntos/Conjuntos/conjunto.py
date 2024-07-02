# Não possui objetos repetidos

print(set([1,1,2,3,4,3])) # Remove duplicados

print(set("Abacaxi"))

# Acessando dados
cores = {"Verde", "Vermelho", "Azul"}
# Transformar em lista
cores = list(cores)
print(cores[1])

for cor in cores:
    print(cor, end=" ")


# Métodos

a = {1,2,4}
b = {3,4}
print("\n",a.union(b)) # Une e exclui duplicados
print(a.intersection(b)) # Dois valores iguais 
print(a.difference(b)) # Somente no conjunto 
print(a.symmetric_difference(b)) # Remove a intersecção 

c = {1,2,3}
d = {1,44,5,2,5}
print(c.issubset(d)) # "C" está contido em "D"?
print(c.issuperset(d)) # "C" abrange "D"?
print(b.isdisjoint(d)) # "B" e "D" são diferentes?

exemplo = {1,2,5,6}
exemplo.add(3)
exemplo.discard(1)
print(exemplo)


