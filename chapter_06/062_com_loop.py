# Criando o dicionário vazio
numeros_favoritos = {}

# Fazendo a enquete com amigos
for _ in range(5):  # Perguntar para 5 pessoas
    nome = input("Qual é o seu nome? ")
    numero = int(input(f"{nome}, qual é o seu número favorito? "))
    numeros_favoritos[nome] = numero

# Mostrando os resultados
print("\nResultados da enquete:")
for nome, numero in numeros_favoritos.items():
    print(f"O número favorito de {nome} é {numero}.")
