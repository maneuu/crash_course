bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
#Se você pedir a Python que exiba uma lista, ela devolverá a representação da lista, incluindo os colchetes: ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
print(bicycles[0].title())

print(bicycles[1]) 
print(bicycles[3]) 
# python tem uma sintaxe especial para acessar o último elemento de uma lista. Ao solicitar o item no índice -1, Python sempre devolve o último item da lista
print(bicycles[-1])
print(bicycles[-2])

message = "My first bicycle was a " + bicycles[0].title() + "."
message = f"My first bicycle was a {bicycles[-1].title()}."
print(message) 