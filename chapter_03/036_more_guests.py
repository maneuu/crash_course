
guest_list = ["Napoléon Bonaparte", "Isaac Newton", "Julio Cesar"]
print(f"Dear {guest_list[0]}, you’re invited to join our special party!")
print(f"Dear {guest_list[1]}, you’re invited to join our special party!")
print(f"Dear {guest_list[2]}, you’re invited to join our special party!", end="\n\n")
print(f"{guest_list[1]}, unfortunately, he won’t be able to attend the party.", end="\n\n")

guest_list[1] = "Alan Turing"

print(f"Dear {guest_list[0]}, you’re invited to join our special party!")
print(f"Dear {guest_list[1]}, you’re invited to join our special party!")
print(f"Dear {guest_list[2]}, you’re invited to join our special party!",end="\n\n")

# 3.6 – Mais convidados: Você acabou de encontrar uma mesa de jantar maior,
# portanto agora tem mais espaço disponível. Pense em mais três convidados para o jantar.

# • Comece com seu programa do Exercício 3.4 ou do Exercício 3.5. Acrescente
# uma instrução print no final de seu programa informando às pessoas que
# você encontrou uma mesa de jantar maior.

# • Utilize insert() para adicionar um novo convidado no início de sua lista.

# • Utilize insert() para adicionar um novo convidado no meio de sua lista.

# • Utilize append() para adicionar um novo convidado no final de sua lista.

# • Exiba um novo conjunto de mensagens de convite, uma para cada pessoa
# que está em sua lista.

print("Dear guests, we are happy to inform you that we've found a larger table with 3 extra chairs available for more guests.",end="\n\n")
# adicionando novos convidados
guest_list.insert(0,"Santa Claus")
guest_list.insert(2,"Sherlock Holmes") 
guest_list.append("Harry Potter")

print(f"Dear {guest_list[0]}, you’re invited to join our special party!")
print(f"Dear {guest_list[1]}, you’re invited to join our special party!")
print(f"Dear {guest_list[2]}, you’re invited to join our special party!")
print(f"Dear {guest_list[3]}, you’re invited to join our special party!")
print(f"Dear {guest_list[4]}, you’re invited to join our special party!")
print(f"Dear {guest_list[5]}, you’re invited to join our special party!")



