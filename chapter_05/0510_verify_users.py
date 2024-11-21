# Lista de usuários atuais
current_users = [
    "sussy explorer",
    "code endemic",
    "bicycle nomad",
    "vector hunter",
    "pixel pathfinder"
]

# Lista de novos usuários
new_users = [
    "Sussy Explorer",  # Um nome repetido da lista current_users
    "Urban Scout",
    "Helio Rider",    
    "Daily Questor",
    "Code Endemic"   # Um nome repetido da lista current_users
]

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"O nome '{new_user}' já está em uso. Por favor, forneça um novo nome.")
    else:
        print(f"O nome '{new_user}' está disponível.")
