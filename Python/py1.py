a = set()
a.add(1)
a.add(2)
a.add(3)
print(a)

a.add(1) # Como já faz parte de a, ele não adiciona.
print(a)

a.add(0)
a.add(-1)
print(a)

print(1 in a)
print(-2 in a)
print(len(a))

b = {2,3}
c = set({4, 5, 6})

print(a | b)
print(a | c)
print(a.union(c)) # Faz a mesma coisa que a | b

print (a & b)
print(a.intersection(b))

print (a - b)
print(a.difference(b))

print (a ^ b)
print(a.symmetric_difference(b))

print(a > b) # Todos os elementos de a estão em b

# O Set é uma estrutura de dados que implementa operações de união, interseção e diferença, entre outras. A principal característica dessa estrutura é não admitir repetição de elementos. Outra característica é que eles não matém a ordem dos seus elementos.

# É possível comparar as conjuções (set) com outras conjunções, como na matemática.
# a | b --> Junta os elementos que estã em a e em b
# a & b --> Mostra os elementos que são comuns entre os dois
# a - b --> Mostra a diferença enrtre os dois. Os elementos presentes em a que não estão em b
# a ^ b --> Mostra a diferença simétrica entre eles. Elementos que não comun entre os dois