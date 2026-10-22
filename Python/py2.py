#// Métodos de string

S = "Alô mundo"
L = list(S)
print(L)

S = "-".join(L)
print(S)

# Verificando início e fim

nome = "Paulo Sérgio"
print(nome.startswith("Paulo")) # -> True
print(nome.endswith("Paulo")) # -> False

s = "Essa é minha frase de teste"
print(s.lower())
print(s.upper())
print("frase" in s) # -> Verificando se existe "frase" na variável frase

t = "Este é o teste do teste"
print(t.count("teste"))
print(t.find("tes"))
print(t.find("e", 11))


# No python, o método list pode ser usado com string, fazendo uma lista com cada letra existente na string

# O método join() faz o inverso, juntando cada elemento da lista e transformando em um array. É possível colocar um separador antes dele como no exemplo usado. Que é o que vai separa os elementos deposi de juntados

# O método startswith verifica se existe aquele determinado assunto no início de uma string, retornando um valor booleano
# E também existe o método endswith, que verifica se a string termina com o determinado elemento

# lower() -> Transforma todas as letras de um array em letras minúsculas
# upper() -> Transforma todas as letras de um array em letras maiúsculas

# O método count conta quantas vezes aparece um determinado elemento em um array

# find() -> Retorna a primeira aparição de uma string determinada dentro de outra string com o seu índex. E o rfind faz a mesma coisa do lado contrário. E dentro dos dois métodos é possível especificar quando vai iniciar a pesquisa dentro do array. Do memso jeito eciste o método