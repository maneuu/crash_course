my_pizzas = ["queijo", "chocolate","pepperoni"]
# copia da minha lista de pizzas
friend_pizzas = my_pizzas[:]
# adicionando valores diferentes nas duas listas
my_pizzas.append("churrasco")
friend_pizzas.append("catupiry")
for pizza in my_pizzas:
  print(f"Eu amo pizza de {pizza}")

print("\n\n")

for pizza in friend_pizzas:
  print(f"Meus amigos gostam de pizza de {pizza}")