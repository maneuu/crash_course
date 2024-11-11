
guest_list = ["Napoléon Bonaparte", "Isaac Newton", "Julio Cesar"]
print(f"Dear {guest_list[0]}, you’re invited to join our special party!")
print(f"Dear {guest_list[1]}, you’re invited to join our special party!")
print(f"Dear {guest_list[2]}, you’re invited to join our special party!", end="\n\n")
print("-" * 40, f"\n{guest_list[1]}, unfortunately, he won’t be able to attend the party.", end="\n\n")

guest_list[1] = "Alan Turing"

print(f"Dear {guest_list[0]}, you’re invited to join our special party!")
print(f"Dear {guest_list[1]}, you’re invited to join our special party!")
print(f"Dear {guest_list[2]}, you’re invited to join our special party!",end="\n\n")

print("-" * 40, "\nDear guests, we are happy to inform you that we've found a larger table with 3 extra chairs available for more guests.",end="\n\n")
# adicionando novos convidados
guest_list.insert(0,"Santa Claus")
guest_list.insert(2,"Sherlock Holmes") 
guest_list.append("Harry Potter")

print(f"Dear {guest_list[0]}, you’re invited to join our special party!")
print(f"Dear {guest_list[1]}, you’re invited to join our special party!")
print(f"Dear {guest_list[2]}, you’re invited to join our special party!")
print(f"Dear {guest_list[3]}, you’re invited to join our special party!")
print(f"Dear {guest_list[4]}, you’re invited to join our special party!")
print(f"Dear {guest_list[5]}, you’re invited to join our special party!", end ="\n\n")
#3.7 – Reduzindo a lista de convidados
# Você acabou de descobrir que sua nova
# mesa de jantar não chegará a tempo para o jantar e tem espaço para somente dois convidados.

# • Comece com seu programa do Exercício 3.6. Acrescente uma nova linha que
# mostre uma mensagem informando que você pode convidar apenas duas pessoas para o jantar.

# • Utilize pop() para remover os convidados de sua lista, um de cada vez, até
# que apenas dois nomes permaneçam em sua lista. Sempre que remover um
# nome de sua lista, mostre uma mensagem a essa pessoa, permitindo que ela
# saiba que você sente muito por não poder convidá-la para o jantar.

# • Apresente uma mensagem para cada uma das duas pessoas que continuam
# na lista, permitindo que elas saibam que ainda estão convidadas.

# • Utilize del para remover os dois últimos nomes de sua lista, de modo que você
# tenha uma lista vazia. Mostre sua lista para garantir que você realmente tem
# uma lista vazia no final de seu programa.

print("-" * 40, "\nUnfortunately, I’m only able to invite two people to the party.", end="\n\n")

print(f"I'm sorry {guest_list.pop()}, but the party won't be happening as planned. I only have two chairs available, so you are uninvited.")
print(f"I'm sorry {guest_list.pop()}, but the party won't be happening as planned. I only have two chairs available, so you are uninvited.")
print(f"I'm sorry {guest_list.pop()}, but the party won't be happening as planned. I only have two chairs available, so you are uninvited.")
print(f"I'm sorry {guest_list.pop()}, but the party won't be happening as planned. I only have two chairs available, so you are uninvited.", end="\n\n")

print(f"Just letting you know, {guest_list[0]}, that you’re still invited to the party!")
print(f"Just letting you know, {guest_list[1]}, that you’re still invited to the party!", end="\n\n")

del guest_list[-1]
del guest_list[-1]

print(guest_list, end="\n\n\n")