#  Alterando a lista de convidados: Você acabou de saber que um de seus
# convidados não poderá comparecer ao jantar, portanto será necessário enviar
# um novo conjunto de convites. Você deverá pensar em outra pessoa para
# convidar.

# • Comece com seu programa do Exercício 3.4. Acrescente uma instrução print
# no final de seu programa, especificando o nome do convidado que não
# poderá comparecer.

# • Modifique sua lista, substituindo o nome do convidado que não poderá
# comparecer pelo nome da nova pessoa que você está convidando.

# • Exiba um segundo conjunto de mensagens com o convite, uma para cada
# pessoa que continua presente em sua lista.

guest_list = ["Napoléon Bonaparte", "Isaac Newton", "Julio Cesar"]
print(f"Dear {guest_list[0]}, you’re invited to join our special party!")
print(f"Dear {guest_list[1]}, you’re invited to join our special party!")
print(f"Dear {guest_list[2]}, you’re invited to join our special party!", end="\n\n")
print(f"{guest_list[1]}, unfortunately, he won’t be able to attend the party.", end="\n\n")

guest_list[1] = "Alan Turing"

print(f"Dear {guest_list[0]}, you’re invited to join our special party!")
print(f"Dear {guest_list[1]}, you’re invited to join our special party!")
print(f"Dear {guest_list[2]}, you’re invited to join our special party!")