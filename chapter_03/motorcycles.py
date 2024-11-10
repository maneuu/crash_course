motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles, end="\n\n")
#modifica uma lista 
# motorcycles[0] = 'ducati'
# print(motorcycles)

# método append() em Python é utilizado para adicionar um item ao final de uma lista.
motorcycles.append('ducati') 
print("Metdodo append para adicionar elemento ao final de uma lista.")
print(motorcycles)


# RESULTA ERRO
# frutas = []
# frutas.append("maçã", "banana", "laranja")
# print(frutas)

frutas = []
frutas.append("maçã")
frutas.append("banana")
frutas.append("laranja")
print(frutas, end="\n\n")

#O método insert() em Python permite inserir um elemento em uma posição específica dentro de uma lista. Ao contrário de append(), que sempre adiciona o elemento ao final, insert() insere o item no índice desejado, deslocando os elementos subsequentes uma posição para a direita
nomes = ["Lucas", "Ana", "Gabriel", "Mariana"]
nomes.insert(2, "Beatriz")
print("Adicionando elemento em uma posição especifica")
print(nomes,end="\n\n")

# O comando del em Python é usado para remover um elemento
del nomes[0]
print("Removendo elementos de uma lista")
print(nomes)

